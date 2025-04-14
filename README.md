# .eml De-Duper (dee-DOOP-er)

A Python script that removes duplicate .eml files output by Barracuda Message Archiver.

## Install

Clone the repository:
```
git clone https://github.com/john-bieren/eml-de-duper.git
```
For ease of use, a desktop shortcut to `eml_de_duper.ps1` can be created. This allows the script to be run without using the terminal, and includes a pause statement so that the output can be read before closing the window. For this to work, make sure that the shortcut starts in the project directory, or change the first line of `eml_de_duper.ps1` to use the full path to `main.py` on your machine.

## Usage

Run `main.py` or `eml_de_duper.ps1` and input the full path to the folder which includes the .eml files from which you want to remove duplicates.
