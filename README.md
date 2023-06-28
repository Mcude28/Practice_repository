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

    The YAML files should be located in the root directory follwoing with the two directories .github-> workflows
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

`pip freeze > requiremnts.txt`

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

## Pytest - testing functions for development

    We want to use pytest to test functions going into the Development Branch when working on new features from an indiviual branch. Making these features requires the user to create test cases for them that ensure that they work correctly for every scenario

    For pytest to work it's best practice to make a directory within the webApp directory labeled test and for the test file, label as test_<file name> or <file name>_test and pytest will automatically find this file for the searching for tests. However, for the specific functions, those need to be labeled as test_<function name> otherwise pytest will not test the functions

    Pytest will then go and activate any function with the test_ label and check the values of the assertions to see if they are all true. If any comes out false, the test will output as failed


### YAML file for a pytest on all OS

    name: Python application

    on:
    push:
        branches: [ "Development" ]
    pull_request:
        branches: [ "Development" ]

    permissions:
    contents: read

    jobs:
    build:

        runs-on: ${{ matrix.os }}
        strategy:
        matrix:
            os: [windows-latest, ubuntu-latest, macOS-latest]

        steps:
        - uses: actions/checkout@v3
        - name: Set up Python 3.10
        uses: actions/setup-python@v3
        with:
            python-version: "3.10"
        - name: Install dependencies
        run: |
            make install
        - name: Lint with flake8
        run: |
            # stop the build if there are Python syntax errors or undefined names
            flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
            flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
        - name: Test with pytest
        run: |
            pytest
## Example test

    import time

    def time_consuming_function():
        # Simulate a time-consuming task
        time.sleep(2)

    def test_performance():
        start_time = time.time()
        time_consuming_function()
        execution_time = time.time() - start_time

        # Assert that the execution time is within the expected range
        assert execution_time < 3  # Assuming the expected execution time is less than 3 seconds
        
        start_time = time.time()
        long_time_function()
        execution_time = time.time() - start_time

        # Assert that the execution time is within the expected range
        assert execution_time < 3  # Assuming the expected execution time is less than 3 seconds

    def long_time_function():
        # Simulate a time-consuming task
        time.sleep(1)


## Unittest - testing functions for UAT

    We use Unittest for UAT testing because this type of test allows you to create test cases that can replicate the users actions. It's best used for testing filters, ensuring urls go where we want them to go, and other encounters a user may experience

    For unittest python files you'd typically encounter imports similar to the one's shown below. More may be needed in the future or you may not end up using all of them

.

    import unittest
    from webapp.views import login_view
    from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
    from django.test import TestCase
    import boto3
    from django.urls import reverse

.

    In the actual program, we'd want a class that takes in a TestCase with functions that preform the assertions needed to check if the values pass. outside of the classes, we need to use the if__name__=="__main__" and call unittest.main() for these tests to be ran with the command if the tests are located in a test file within the webApp directory 

`python manage.py test webApp.test.test_views` 
or gernerally
`python manage.py test path.to.test.from.root`

    A small example of a simple test code is as follows:

.

    import unittest
    from webapp.views import login_view
    from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
    from django.test import TestCase
    import boto3
    from django.urls import reverse


    class HomePageTest(TestCase):
        def test_homepage_rendering(self):
            print('running homepage test')
            # checks if the reverse -> homepage actuctually goes to the home page
            response = self.client.get(reverse("homePage"))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "homepage.html")


    if __name__ == "__main__":
        unittest.main()
### Example YAML file to run unittest on all OS
        
    name: Python application

    on:
    push:
        branches: [ "UAT" ]
    pull_request:
        branches: [ "UAT" ]

    permissions:
    contents: read

    jobs:
    build:

        runs-on: ${{ matrix.os }}
        strategy:
        matrix:
            os: [windows-latest, ubuntu-latest, macOS-latest]

        steps:
        - uses: actions/checkout@v3
        - name: Set up Python 3.10
        uses: actions/setup-python@v3
        with:
            python-version: "3.10"
        - name: Install dependencies
        run: |
            make install
        - name: Lint with flake8
        run: |
            # stop the build if there are Python syntax errors or undefined names
            flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
            # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
            flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
        - name: Django test
        run: |
            python manage.py test webApp.test.test_views
# Making a django project server

    Using the steps shown above, create a Conda env for this new server for a reminder they are also shown below. Make sure you are using Anaconda as an Admin

`conda create --name server_env`
`conda activate server_env`

    To remove any installed packages if this isn't empty, first check the installed packages with 

`pip freeze`

    If there are still installed packages, do the steps within the server below 

`pip freeze > requiremnets.txt`
`pip uninstall -r requirements.txt -y`

    Now after confirming all the packages, the server alone should be empty. From here make sure Node.js is installed
### Windows 
- `choco install nodejs`
### MacOs 
- `brew install node`
### Ubuntu 
- `sudo apt-get update`
- `sudo apt-get install nodejs`

    Otherwise use the Node.js installer via the website https://nodejs.org and after it is intalled, you can verify with the command

`node --version`

## Installing django with Anaconda

- Current directory

`python -m django startproject <Project_Name>`

- Path to directory

`python -m django startproject /path/to/<Project_Name>`

## Creating project

    Making sure you are working on the location of the project directory, to create a new Django app name myApp, use the following command

`python manage.py startapp myApp`

    From within the project directory, files should be made the help run the app. To say "Hello, World!", go into the views.py file and implement the following code
.

    from django.http import HttpResponse

    def hello(request):
        return HttpResponse("Hello, World!")

.

    Now in the urls.py file, configure it so that it has the content of the code shown below

.

    from django.urls import path
    from myapp.views import hello

    urlpatterns = [
        path('hello/', hello, name='hello'),
    ]

.

    To run the server use the command

`python manage.py runserver`
    and clicke the server link displayed on the terminal, or use this link -> http://localhost:8000/ . To see Hellow World, at the end of the url, add hello/ or use this link -> http://localhost:8000/hello/

## Adding Javascript and html

    In the Anaconda terminal, use the command:

`mkdir static`

    Change the working directory to static and do the command:

`mkdir js`
    This is where the scripts would go. Now change the working directory to the path of the myApps and do the follwoing command:

`mkdir templates`

    This is where the html files would go. In the js directory, add the file scripts.js and type in the following code

.

    alert('Hello, JavaScript!');

.

    In the templates directory, add a index.html file and type the follwoing code

.

    {% load static %}
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Project</title>
        <script src="{% static 'js/script.js' %}"></script>
    </head>
    <body>
        <h1>Hello, Django!</h1>
    </body>
    </html>

. 

    Update the urls.py to have the following code

.   

    from django.urls import path
    from myapp.views import hello, index

    urlpatterns = [
        path('hello/', hello, name='hello'),
        path('', index, name='index'),
    ]

. 

    *Note* make sure that in the settings.py, the STATIC_URL should look like this 

    STATIC_URL = '/static/'

    and the INSTALLED_APPS should look like this

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'myApp',  # Add your app name here
    ]   


