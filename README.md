# .eml De-Duper (dee-DOOP-er)

A Python script that removes duplicate .eml files output by Barracuda Message Archiver.

## Methodology

Files that are identified as duplicates can either be deleted or moved into a "Duplicates" subfolder. Duplicates are identified by comparing file names, which include the time when the email was sent, specified to the second. Files with the same time in their names are considered duplicates, and only one copy will be left in the original folder. This is not a perfect method, but it works correctly in the vast majority of cases, and opting to move duplicates instead of deleting them can mitigate the risk of false positives.

## Install

Clone the repository:
```
git clone https://github.com/john-bieren/eml-de-duper.git
```
**Note**: The tags in this repository do not correspond to releases, they simply indicate breaking changes.

For ease of use, desktop shortcuts to `eml_de_duper.ps1` and `update.ps1` can be created. `eml_de_duper.ps1` allows the script to be run without using the terminal, and includes a pause statement so that the output can be read before closing the window. `update.ps1` automates the process of keeping the repository and its dependencies up to date. For these to work, make sure that the shortcuts start in the project directory.

## Usage

To remove duplicate .eml files:
1. Run `main.py` or `eml_de_duper.ps1`.
2. Input the full path to the folder which includes the .eml files from which you want to remove duplicates.
3. Indicate whether you want duplicates to be deleted or moved into a "Duplicates" subfolder.
