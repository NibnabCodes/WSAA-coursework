# Web Services & Applications ~ 2026

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Bitcount+Ink&size=35&duration=2000&pause=2000&color=B842BD&background=FF86E800&width=435&lines=Assignments)](https://git.io/typing-svg)

This repository contains three weekly task submissions completed as part of the assessment requirements for the *Web Services &amp; Applications* module at Atlantic Technological University ~ Galway.

Author: Niamh Hogan

## About this Repository

This repository is comprised of the following files and folders:

* **WSAA-assignments** Folder containing the three assignments displayed in Jupyter Notebooks
  - Each .ipynb file contains a brief description of the program, code with short explanations & references.  
* **WSAA-labs** file containing the labwork for this module
* A **.gitignore** file which contains all the files/folders to be ignored by Git in this repository.
* A **README** file that contains the utility of each program, list of dependencies, how to: set up environment, download the repository & run the code.
* A **requirements.txt** file containing all packages that the assignment programs depend on & their versions.

## Features  

### Assignment 2 – Card Draw (`assignment2-carddraw.ipynb`)
Interacts with a deck of cards API to simulate a card hand. The program shuffles a deck, draws 5 cards, and evaluates the hand - checking for a pair, triple, straight, or same suit and congratulating the user on any winning combination.

### Assignment 3 – CSO Data Retrieval (`assignment03-cso.ipynb`)
Fetches the *Exchequer Account (Historical Series)* dataset from the Central Statistics Office (CSO) open data API and stores the retrieved data locally as `cso.json`.

### Assignment 4 – GitHub File Editor (`assignment04-github.ipynb`)
Uses the GitHub API to read a `.txt` file from a repository, replace all instances of the name "Andrew" with "Niamh", and push the updated file back to the repository. GitHub authorisation is handled via a Personal Access Token stored in a `config.py` file, which is excluded from version control via `.gitignore`.

## Dependencies

The following libraries are required to run the programs in this repository:

- **Python** 3.13.9
- **requests** 2.32.5 - Used to make HTTP requests to external APIs (CSO, card draw)
- **PyGithub** 2.8.1 - Python library for interacting with the GitHub API
- **sys** - Python standard library module, used to manage the system path for importing `config.py`

All dependencies (excluding `sys`, which is built into Python) are listed in `requirements.txt` and can be installed by running:
```bash
pip install -r requirements.txt
``` 

## Environment Setup

- **Git** – Download the latest version of Git at: https://git-scm.com/downloads
- **GitHub** – Create a free GitHub account at: https://github.com/signup
- **Anaconda** – I would recommend using Anaconda as it comes bundled with Python 3.13.9 & the Python libraries necessary to run the code in this repository. Install Anaconda using the following steps:
  1. Download Anaconda from: https://www.anaconda.com/download
  2. Open the downloaded file & press next, next
  3. When the advanced options appear check the following boxes:
     * Add to PATH environment variable
     * Make this version your default Python
- **Visual Studio Code** – Download Visual Studio Code at: https://code.visualstudio.com/Download

Once the above are installed, open the repository in VS Code and run the following command in the terminal to install the remaining dependencies:
```bash
pip install -r requirements.txt
```

Create a `config.py` file in the parent directory of the repository with the following structure:
```python
config = {
    "githubkey": "your_personal_access_token_here"
}
```

⚠️ Never share or commit your `config.py` file. It is excluded from this repository via `.gitignore`.


## How to Download Repository  

You can clone this repository to VS Code using the following steps:

1. Copy the repository URL: https://github.com/NibnabCodes/WSAA-coursework.git
2. Create a folder in VS Code where you want to store the cloned repository
3. Open a new terminal in VS Code and input the following commands:
```bash
git clone https://github.com/NibnabCodes/WSAA-coursework.git
git config pull.rebase false
git pull
```
The repository should now be accessible in VS Code & ready to execute.

## How to Run the Code  

Once the repository has been cloned and dependencies installed, follow these steps to run each notebook:

1. Open the repository folder in VS Code
2. Ensure your `config.py` file is in place with your GitHub Personal Access Token (required for `assignment04-github.ipynb` only)
3. Navigate to the `WSAA-assignments` folder and open the desired `.ipynb` file
4. Select the **base (Python 3.13.9)** kernel by clicking the kernel picker in the top right of the notebook
5. Run the notebook by clicking **Run All** at the top of the notebook

⚠️ Ensure `config.py` is set up before running `assignment04-github.ipynb`, otherwise the GitHub authorisation will fail.

## References  
Please see .ipynb files for references used