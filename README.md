images/Railway1.jpg
images/Railway2.jpg
images/Railway3.jpg

# G-Code Generator for Railway Sleepers

This Python application provides a graphical user interface (GUI) for generating G-code to mill railway sleepers and rails using a CNC machine. Built with Tkinter, it allows users to customize cutting parameters and export the generated G-code to a file.

## Features
- Simple and intuitive Tkinter GUI
- Input fields for track length, sleeper spacing, overhang, cutting depth, feed rates, and spindle speed
- Axis selection for X or Y direction milling
- Clickable status bar linking to [Anton CNC on YouTube](https://www.youtube.com/@boessi)
- Input validation and error handling

## Installation
1. Make sure you have Python 3 installed.
2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/gcode-generator
   cd gcode-generator
   ```
3. Run the application:
   ```bash
   python gcode_generator.py
   ```

## Usage
1. Enter the desired parameters in the input fields.
2. Select the cutting axis (X or Y).
3. Click "Generate and Save G-Code" to export the G-code to a `.nc` or `.txt` file.
4. Click the "Anton CNC" status bar to visit the author's YouTube channel.

## Author
Anton CNC — [YouTube Channel](https://www.youtube.com/@boessi)

## Disclaimer
This software is provided "as is", without warranty of any kind, express or implied. The author assumes no responsibility for any damage or loss resulting from the use of this script. Use at your own risk.