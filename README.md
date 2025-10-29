# .eml De-Duper (dee-DOOP-er)

A Python script that moves potential duplicate .eml files output by Barracuda Message Archiver from a given folder into a separate subfolder.

## Methodology

Files that are identified as potential duplicates will be moved into a "Potential Duplicates" subfolder. Potential duplicates are identified by comparing file names, which include the time when the email was sent, specified to the second. Files with identical timestamps are marked as potential duplicates, and only one copy will be left in the original folder.

**Be advised: it is possible that unique emails could have been sent at the same second, in which case this script would identify one as a potential duplicate. Make sure to verify whether potential duplicates are, in fact, duplicates.**

## Install

Clone the repository and install dependencies:
```
git clone https://github.com/john-bieren/eml-de-duper.git
cd eml-de-duper
& ./update.ps1
```
**Note**: The tags in this repository do not correspond to releases, they simply indicate breaking changes.

For ease of use, desktop shortcuts to `eml_de_duper.ps1` and `update.ps1` can be created. `eml_de_duper.ps1` allows the script to be run in a virtual environment without using the terminal, and includes a pause statement so that the output can be read before the window closes. `update.ps1` automates the process of setting up the virtual environment and keeping the repository and its dependencies up to date. Make sure that the shortcuts start in the project directory.

## Usage

To move potential duplicate .eml files:
1. Run `main.py` or `eml_de_duper.ps1`.
2. Input the full path to the folder which includes the potential duplicate .eml files.
