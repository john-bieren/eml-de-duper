# pull recent changes
git pull

# activate virtual environment and upgrade pip
if (-not (Test-Path .venv)) { python -m venv .venv }
./.venv/Scripts/Activate.ps1
python -m pip install --upgrade pip

# install dependencies
$Dependencies = @(
    "tqdm>=4.67.1,<5.0.0"
)
foreach ($item in $Dependencies) {
    python -m pip install $item
}

# deactivate virtual environment
deactivate
