# Fusion 360 STEP Component and Body Batch Exporter

Author: Dominik Kowalczyk

## Description

This Fusion 360 script exports all components and bodies in your design to separate STEP files. It is useful for breaking down complex designs into individual STEP files, making it easier to collaborate in software agnostic work environment or share specific components.

## Installation

1. **Download the Script**: Download the script file provided. Unzip.

2. **Import the Script into Fusion 360**:
   - Open Fusion 360.
   - Click on the "Scripts and Add-Ins" button located in the "Tools" dropdown on the toolbar or press the shortcut `Shift+S`.
   - In the "Scripts and Add-Ins" dialog, click the "Scripts" tab (it usually opens by default).
   - Next to "My Scripts", hit the green plus icon
   - Select the folder where you unzipped it
   - "ComponentsToSTEP" should now appear under "My Scripts"

## Usage

1. **Run the Script**:
   - After importing the script, select it from the "Scripts" section in Fusion 360.
   - Click the "Run" button to execute the script.

2. **Export Location**:
   - The script will create a folder on your desktop with a sanitized name based on your design's name.

3. **Export Process**:
   - The script moves each body in the root component to separate components, creating a one-to-one correspondence between bodies and components.

4. **Exported Files**:
   - Each component, including the original root component, is exported as a separate STEP file in the designated folder.

5. **File Naming**:
   - The script automatically sanitizes folder name, removing diacritics and replacing certain characters with underscores to ensure compatibility with filename Fusion 360 Python environment and characters allowed by OS naming convention.

6. **Message Box**:
   - A message box will display a purely informational message if there are no bodies to move to components. A message box will display a confirmation message after the folder is created and export finished.

## Requirements

- Fusion 360 installed on your system.

## Limitations and Considerations

- The script may take a while to finish - so please be patient.
- The script currently supports exporting to STEP files only.
- It works by creating a separate component for each body in the root component. This may result in a large number of components if your design contains many bodies.
- The script may not handle extremely complex designs or components with very large numbers of bodies gracefully.
- There is no way to export bodies without moving them to components because ExportManager.createSATExportOptions method takes only a Component object as a valid geometry argument.

## License

This script is provided under slightly modified [UIUC Licence](LICENSE). You are free to use, modify, and distribute it as needed.

## TODO

- Add UI 
- Add export options for all others file extentions 
- Let users choose the export directory
- Let users choose naming convention for exported files 

## Support and Contribution

For issues or contributions, please visit the script's [GitHub repository](https://github.com/DominikKowalczyk/ComponentsToSTEP).

Feel free to contribute to and improve this script to meet your specific needs. Happy exporting!
