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
    git checkout -b <branch_name>
    This creates the branch
    git push -u origin <branch_name>
    This pushes the branch to the reopository
    

### Making changes
    Open the file you want to make changes to.
    Make changes.
    Save the file.
    

### Committing changes
    git add  -A
    This adds all the files for specific files use 
    git add <file_name1> <file_name2> ...
    git commit -m "message"
    This sends the  changes to the repo with a message
### Pushing changes to remote repository
    git push origin <branch_name>
   
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