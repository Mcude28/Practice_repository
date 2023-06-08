# Practice_repository

    This is a test repository to set up an infrastructure for git hub.

## Setup 
    - Clone the repository
    - Create a new branch
    - Make changes
    - Commit changes
    - Push changes to remote repository
    - Create a pull request
    - Merge changes to development branch (with approval)
    - Delete the branch

## License

### Cloning the repository
    Using git bash on the location where you want the clone repo, use the command:
    git clone https://github.com/username_0/Practice_repository.git
    otherwise you can use SSH


### Creating a new branch
    To creates the branch and change the branch you are on to the new brance use
`git checkout -b <branch_name>`
    
    To pushes the branch to the reopository
`git push -u origin <branch_name>`
    
    

### Making changes
    Open the file you want to make changes to.
    Make changes.
    Save the file.
    

### Committing changes
    To add All the files from your laptop to the repo
`git add  -A`

    To adds all the files for specific files use 
`git add <file_name1> <file_name2> ...`

    This sends the  changes to the repo with a message
`git commit -m "message"`
    
### Pushing changes to remote repository
`git push origin <branch_name>`
   
### Creating a pull request
    Go to the repository on github.
    Click on the pull request tab.
    Click on the New pull request button.
    Select the branch you want to merge into.
    Click on Create pull request.
    Add a title and description to your pull request.
    Add a correspodning label to the request
    Select a reviewer
    Click on Create pull request.
**At this point the automated test will show if passed or failed**
**If the test fails, you can go back and make changes and commit them**

    Click on Merge pull request.
    Click on Confirm merge.
    Click on Delete branch.

    
## Setting up Branch Protection
    From the practice repository go settings -> Branches -> Add Rule 
    label the branch name youd like to add the rules to

    Select 
        -Require a pull request before merging
        -Require approvals
        -Require review from Code Owners
        -Require status checks to pass before merging
        -Require branches to be up to date before merging
            *scroll*
        -Do not allow bypassing the above settings

## Git Hub Action
    -Go to the repository on github.
    -Click on the Actions tab.
    -Click on the New workflow button
    -Check out some of the prebuilt actions
    -Select the action you want to use
    -Click on Set up this workflow
    -Click on Start commit
    -Click on Create new file
    -Configure the Yaml file template such that it works on all OS

## Setting up YAML
    The reccomeneded templates should have already premade the YAML files, it's a matter of if it works on our oerationg system and has all the correct downloads and sysntax

    For working on multiple OS it is important to create a requirements.txt and a makefile that includes all the downloads

## Making requiremnts.txt
    With pip installed, use the command in a window's powershell. make sure the path of the directory is where you are running your repositroy
`pip freeze > requiremnts.txt`

    This should create a file requitrments.txt that contains all the downloads needed to run the programs within the repository

    Otherwise, you can install conda (a method of using a virtual enviormnet that can be designated to the ) using the link https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html and following the instuctions on the site. After installation, run Anaconda Prompt and to check if the installation worked use the command

`conda list`

    and a List of all packages and versions installed in active environment should show up on the terminal after some time. This shows that it is running properly.

    To create a venv named Hynts use the command:

`conda create --name Hynts`

    To activate the venv, use the command

`conda activate Hynts`

    and to deactivate

`conda deactivate Hynts`

    To install python version 3.8 and to check the version of python the following commands should work

`conda install python=3.8`
`python --version`
    
    To install numpy

`conda install numpy`

    To remove numpy

`conda remove numpy`

    To upate numpy

`conda update numpy`

    To freeze the packages in a path and put into a requiremnts.txt file use the commands

`conda list > requiremnts.txt`

    To install the requirements onto a new environment use the command

`conda create --name newenv --file requirments.txt`

## Makefile
    In the YAML file, use the  run command follwed with make "make name" and this command serches for a makefile and installs the dependencies inuded. an example of this is shown below:
`-name: Install dependecies `

`run: |`

 ` make install`

    The following Makefile would now include instructions for what we want to install like:
`install:`

`python -m pip install --upgrade pip && \`

`pip install flake8 pytest && \`

`pip install -r requirements.txt`
