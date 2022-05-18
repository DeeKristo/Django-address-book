steps to set up the addressbook application
--------------------------------------------
The application is tested with Python version 3.8.3

1: Install Python 3.8.3 in computer.
2: Open the project Dover-assignment in any IDE for python.
3: Run "virtualenv Dover" to create a virtaul environment.
   Note : here "Dover" is the name of virtual environment. You can put any name you wish.
4: Activate the virtual environment with the following command.
   for Windows :  Dover\Scripts\activate
   for Linux : source Dover/bin/activate  
5: Install all the dependencies inside the virtual environment to run the application using the below command.
   pip install -r requirements.txt 
6: Start the python server using below command.
   python manage.py runserver
7: Open the address in browser that shows in the terminal after step 6.      

Note : It supports all CRUD functionality and a SEARCH where user can search by any by anything.Only signed in users 
       can perform all the crud and search operations. If a unauthenticated user tries
       to access a specific URL, they will be asked to login.
       A sql.log file will be generated in the project. This will log the sql queries everytime
       a django ORM sql query runs.