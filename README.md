# tassk4

## Getting Started

The instructions down below will help you to create/retrieve/delete courses from database using API.
We will be using Django framework on Linux Ubuntu OS.
### Prerequisites

First of all, it is needed to download Python 3.6 or newer on your computer. 
  
You need to open Terminal and write these commands:

```
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6
```
After it download Postman from Ubuntu Software

### Installing

The next step is to download all needed packages (Django framework, pip and virtualenv.): 

To install Django, we first need to install pip and virtualenv:

```
sudo apt install python3-pip
pip3 install virtualenv
```

Then we need to clone git repository :

```
git clone https://github.com/Dongolok/tassk4.git

```

And install Django in our new virtual environment:
 
```
cd tassk4
virtualenv NameOfYourVenv
source NameOfYourVenv/bin/activate 
pip3 install django 
```
And since we use Rest Framework, we need to add it as well:

```
pip install djangorestframework
```
Now we can run our server:

```
(NameOfYourVenv)$ cd tutorial
(NameOfYourVenv)$ python manage.py runserver
```
Open Postman and make your first GET method!

https://dongolok.docs.apiary.io/#reference
