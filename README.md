# Automate The Boring Stuff
Web scraping and Automation project build to automate the process of creating alx projects file structure and their readme files
This is a CLI application build with python

## Requirments
> Make sure to have Python3.8 and above in order to use this project

## How to use Building Projects Files:
After cloning this repo

```
$ git clone https://github.com/mojtabababiker/ALX-AutomatingStuff.git
``` 
Run the following commands
```
$ pip3 install -r requirements.txt  
$ cd <your_project_dir>
$ python3 <ALX_AUTOMATINGSTUFF_PATH>/Building_Project_Files/main.py "[Project Name]"
```
### Explainations:
At the first time you run the script, you will be premited for your alx interanet user name and password. *ex:*
>$ python3 /ALX-AutomatingStuff/Building_Project_Files/main.py "alx project X"

The application will ask for my interanet credintial
> Enter Email: jahndoe@foo.bar<br>
Enter Password:

After providing email and password the script will start building the file structure for the project your provide on as command line arguments *(the `alx project X` in our case)*.<br>
If no project name provided the the application will prompt you for the project name as following:
> Enter the required project name: 

After finshing the file structures and the README file building, or an Exception accured the script will provide a message indicates the statuse of the process, and the time consumed for building will be displayed on the seccuss.

> ========Done Creating README.md=======<br>
Time consumed Buillding README.md:  98.779261 seconds

---
<br>

## How to use Github Token Replace:
Follow the instructions provided *[here](Github-token_replace/README.md)*

---
<br>

## The project is open for contributions:

Clone the repo add your updates, features, bugs fixes, etc.., and create a pull request after adding yourself into the contributions section on this README file.


## contributers:
*[mojtabababiker](https://github.com/mojtabababiker)*

*[MohdMuslim92](https://github.com/MohdMuslim92)*

*[mmubarak0](https://github.com/mmubarak0)*
