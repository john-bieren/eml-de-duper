# .eml De-Duper (dee-DOOP-er)

A Python script that removes duplicate .eml files output by Barracuda Message Archiver.

## Install

Clone the repository:
```
git clone https://github.com/john-bieren/eml-de-duper.git
```
For ease of use, desktop shortcuts to `eml_de_duper.ps1` and `update.ps1` can be created. `eml_de_duper.ps1` allows the script to be run without using the terminal, and includes a pause statement so that the output can be read before closing the window. `update.ps1` automates the process of keeping the repository and its dependencies up to date. For these to work, make sure that the shortcuts start in the project directory.

## Usage

Run `main.py` or `eml_de_duper.ps1` and input the full path to the folder which includes the .eml files from which you want to remove duplicates.
