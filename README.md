# Govee Display

## Overview
This Python script is designed to display and graph data from Govee Smart Thermometers

## Prerequisites
- Python 3.x
- pandas library
- matplotlib

## Installation
To install the required libraries, run the following command in your terminal:

```bash
pip install pandas matplotlib
```

## Usage
1. Place your `.csv` data file in the same directory as the script, or modify the `file_path` in the `main()` function to point to the location of your data file.
2. Run the script using Python:

```bash
GoveeDisplay.py
```

The script will open the graph gui window, where can you view it, edit display attributes, or save it as an image

## Localisation
The graph reads "Celsius" but with all calculations that are done, the unit does not matter. So you can freely find and replace all instances of Celsius with Fahrenheit.

## License
This project is licensed under the GNU GPL V3.0 License - see the LICENSE file for details.