# Gold1

## The Project
The purpose of the Gold1 project is to create a B2C platform that buys and sells precious materials, in particular: gold, silver, metal, palladium, platinum and rhodium.
The platform can be accessed by both users and employees, which have different functionalities available. For instance, users are able to register and to buy the desired type of metal. The employees can register into the platform, but they are also able to consult the register of historical orders and the inventory, and to repay the loan asked in case money is sufficient. The process of buying and selling is performed automatically: whenever the customer wants to buy a particular metal, the price is immediately calculated (using API) and the transaction is stored in the register. In case there is a shortage of metal, an amount will be automatically purchased and if there is not enough money in the wallet, a bank loan will be asked.
For the purposes of this project, we organized the Python code into multiple modules, each one performing a specific task. Then, the repository contains the main, the license that we chose, the README file and  three different sections:

- *packages*: a folder containing the modules;
- *csv_files*: a folder storing all the csv files;
- *tests*: a folder containing the unit tests performed on the code.

## CSV Files
- *db_users*: Database storing the users’ email and hashed password, each entry corresponding to a user. This csv is accessed by the log_in function, when the user wants to log-in into the platform and whenever a new user wants to register into the platform.
- *db_employees*: Database containing the registered employees and their information accessed during the log-in: their email addresses and their hashed password. This csv is accessed also when a new employee wants to register into the platform.
- *employees*: This csv file lists all the employees of the Gold1 company, even the ones which are not registered in the platform yet. This database was created with the purpose of checking whether an employee exists before giving the chance to someone to register him/herself as an employee.
- *info_users*: This database stores the registered users’ credit card information, in particular: the user’s ID, the number, the expiration date and the cvc. The purpose of this csv file is to check whether the cvc inserted during the purchasing phase corresponds to the one provided during the registration process. In case the two correspond, the user is able to buy the desired precious metal.
- *inventory_csv*: Database storing the quantity and price of each precious metal in the inventory of the Gold1 platform.
- *register_csv*: This csv file represents the register of historical orders made by users. In fact, it contains the customer email, the date of the purchase, the metal bought, its quantity and price.
- *wallet_csv*: Database containing the current balance of the Gold1 platform. It stores all the inflows and outflows deriving from each transaction and amount corresponding to the bank loan (if any).

## Installation
Use the command *git clone https://github.com/Rithoshi/Gold1.git* in the bash of your computer to locally download the git repository containing all the packages and modules. The libraries required to properly run the programs are:

- pandas
- os
- argparse
- sys
- hashlib
- email_validator
- time
- datetime
- requests
- unittest
- random

# Modules

## *Add Employees*
The function add_employee takes into account two unique csv files: the first, *employees.csv*, which contains all the employees' names, surnames, and emails, and the second one, namely *db_employees.csv*, which is a database storing the emails and passwords of the employees registered on the platform
Its main duty is to check whether the mail inserted corresponds to either one of those found in the *employees.csv* file, and if it is, it registers the employee in the *db_employees.csv* file. More specifically, the first control performed on the email is to check whether it is in the correct format, for instance: if it has the *@* sign, if it displays a valid domain name and whether it is inserted as a string.
Then, the function ensures that the employee's email address is valid by checking that the domain is equal to *‘@gold1.com’* and that the password is of the proper length and type (string).
The function will return 'This account is already registered' if the email is already in our database; otherwise, it will check whether the email inserted is authorized to register as an employee.
If access is granted, we will generate a digest of the password inserted for inclusion in the following csv file and register the employee in *db_employees.csv*.

## *Check Password*
The function *check_password* gets called in both the registering functions (add_user and add_employee), everytime the user wants to register, either as a client or as an employee. The purpose of this function is to ask the user to insert again the password that has been inserted previously in the registration phase, in order to check that the two passwords are the same.
At the end, the function will return “True” if the two passwords match and “False” if the two are different. Going a little more into detail, the function initially checks that the length of the password inserted is at least 6 characters and if this condition is satisfied, the user will have three attempts to enter the correct password. If the user is not able to insert the correct password within the three allowed attempts, the program will return an error message.

## *Verify User*
This function checks whether a person is eligible to register as a new user in the Gold1 platform. In particular, it controls  whether the email is inserted in the right format, that is, a string, and whether the email is already present in the *db_users.csv* database. Additionally, it checks that the domain is not equal to *'@gold1.com'*, which is the one of employees. Other controls on the email inserted are also done thanks to the library *email_validator*, which more generally controls the validity of the domain and whether all the characteristics that an email has are satisfied. If the email provided passes all the controls, the user is allowed to register and the function will return True, otherwise, it will return False.
