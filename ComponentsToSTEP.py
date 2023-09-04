#Author- Dominik Kowalczyk
#Description- Exports all compoonents and bodies to separate STEP files 

import adsk.core, adsk.fusion, adsk.cam
import traceback, platform, os, re, unicodedata
from pathlib import Path


# Define a function to create directory for export location if it does not exist already 
def init_directory(name):
        directory = Path(name)
        directory.mkdir(exist_ok=True)
        return directory

# Define a function to remove diacritics 
def remove_diacritics(input_str: str) -> str:
    # Normalize the string using Unicode normalization (NFD) and remove diacritics
    normalized_str = unicodedata.normalize('NFD', input_str)
    diacritic_removed_str = ''.join([char for char in normalized_str if not unicodedata.combining(char)])
    return diacritic_removed_str

# Define a function to sanitize a string to use as a part of an export path name
def sanitize(name: str) -> str:
    # Remove diacritics using unidecode
    name = remove_diacritics(name)
    with_replacement = re.sub(r'[:\\/*?<>|]', '_', name)
    return with_replacement

def run(context):
    ui = None
    try:
        
        app = adsk.core.Application.get()
        ui  = app.userInterface
        
         # get active design        
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        
        # get root component in this design
        rootComp = design.rootComponent
        
        # create a single exportManager instance
        exportMgr = design.exportManager

        # get and sanitize the design name
        designName = sanitize(design.parentDocument.name)
        
        # set the export location
        if platform.system() == 'Windows':
            desktopPath = os.path.join(os.getenv('USERPROFILE'), 'Desktop', designName)
        else:
            desktopPath = os.path.join(os.path.expanduser('~'), 'Desktop', designName)
        
        init_directory(desktopPath)
        

        # move each body stored in root one by one to a separate component
        sourceBodies = rootComp.bRepBodies
        transform = adsk.core.Matrix3D.create()
         
        if len(sourceBodies) != 0:
            for i in range(0,sourceBodies.count):
                currentBody = sourceBodies.item(0)
                occurence = rootComp.occurrences.addNewComponent(transform)
                occurence.component.name = currentBody.name
                occurence.isLightBulbOn = True
                currentBody.moveToComponent(occurence)
        else:
             ui.messageBox('No bodies to move to components')
        
        # get all components in this design
        allComps = design.allComponents

        # Create a string to hold the exported components names list 
        expComps = ""
        # export the component one by one with a specified format
        for comp in allComps:
            compName = sanitize(comp.name)
            filePath = os.path.join(desktopPath, compName)
            # Create an STEPExportOptions object and do the export.
            stepOptions = exportMgr.createSTEPExportOptions(filePath, comp)
            exportMgr.execute(stepOptions)
            expComps += compName + '\n'
        
        # If everething ran smoothly let the user know!
        ui.messageBox('Created folder:\n' + desktopPath + ' and exported following components:\n' + expComps)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
