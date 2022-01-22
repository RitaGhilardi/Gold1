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

## *Get number*
This function is called by the main during the registration of a new user and has the role of getting from the user the number of its credit card. The function does not have any input and returns the credit card number in the string format. The function asks the user an input and makes some checks on it: it verifies that each character of the string is one of the ten numbers, it verifies that the length of the string is 16 and it verifies that the int number of the string is in between the accepted interval. All these checks are inside a while loop that asks the user to insert again the credit card number if some errors occur. The loop cycle allows the user to insert the number at most three times, then, if the number is still not correct, it returns *“None”*, so the main knows that the number is not  valid.

## *Get date*
The *main* calls this function during the registration process of a new user, and its major duty is to obtain the credit card expiration date. The function simply returns the month and year the credit card will expire (expressed in a string format).
We exploit the command *input()* which allows the user to insert the card's expiration date directly from the bash. Then, a few conditions are verified on that entry: first, it confirms that the characters in the input are numerical (equivalent to one of the 10 integer values), then it ensures that the numbers inputted are in the correct format, and finally it verifies the date’s validity.
Furthermore, the user may enter the card's details up to three times; otherwise, if the expiration date is still invalid, the program will return *'None'*, informing the *main* that the number is invalid and it will show an error message to the user.

## *Get cvc*
This is another function called by the *main* throughout the registration process of a new user, and it is used to get the CVC number of the user's credit card. As a result, the method will simply return the three-digit CVC of each new user's credit card. The function allows us to check that each string character is an integer value, that the string's length is 3, and that it fits within the acceptable range. 
The procedures are carried out within an if/else loop which prompts the user to re-enter the CVC if anything goes wrong. The user has up to three attempts; if the CVC is still incorrect, the loop will return *'None'*, informing the main that the number is invalid.

## *Add user*
The registration of a new user is allowed by the *add_user* function, which adds a entry to the csv *db_users.csv*, that is necessary for a user to log in, and to register the information of the new user's credit card on the database *info_users.csv*.
It starts by assigning the new user a random ID number, it computes the digest of the password created by the user, then it appends the user credentials to the existing *db_users.csv* database and, last, it appends the credit card data to the other csv file *info_users.csv*.
At the beginning of our development, we were associating credit card data directly to the  email of the client in a single database. This wasn’t good from the security point of view because, in cases of data leakage, hackers had the credit cards data associated with the username of the user. For this reason, we improved security by having two distinct databases, one for user credentials and one for credit card information, and we anonymized the *info_users* database by associating to every user a random ID number, and then identifying the credit card associated with the user account by its ID.

## *Log in*
The *log-in* function requests in input two variables, *email* and *password*, for anyone (already registered) that is willing to access the platform. This module accesses two different databases: *db_employees.csv*, which stores the information of registered users, and *db_employees.csv*, which accounts for registered employees. The function returns a boolean variable that states if the log-in process was successful or not.
In order to verify the emails’ format, we use a library called *email validator*; once we make sure that an email is valid, this one is stored in the variable ‘email’.
After that, we analyze and check the email suffix to see whether the person is trying to log-in as an employee or user: if the suffix corresponds to *“gold1.com”*, then we understand that it’s trying to log in as an employee, therefore we make sure that the email, given as an input, is exactly equal to one of those found in the database (*db_employees.csv*). 
- If there’s a match, you can proceed by checking which one is the row in which the email is stored, so that it can be possible to see its corresponding password in the csv file. As a result, we calculate the password's digest: if the password located in the row (of the csv file) corresponding to the email inserted matches the calculated digest, access is granted.
- else: in this case, the for loop found an email correspondence, meaning that the mail is indeed in the database but the corresponding password is different (possibly, the password given as an input is wrong). This will return: *“Please check password”*.
- If the for loop does not find correspondence with any email addresses in the database, then it will simply return: *“We're sorry but your employee account does not exist, please register to our website before log in”*.

In terms of users, if the email suffix is not *@gold1.com*, that person is automatically identified as a user. We then check whether the inserted e-mail address is already in the database, as we've seen before. The row in which the email is saved, as well as the password's digest, are then calculated. When the password does not match the ones in the database, it will respond *'Please check password’*. Furthermore, anyone registering with an incorrect email address (i.e., one with an invalid suffix) will automatically turn out to be an error.

## *Read register*
The function *read_register* can be called only by employees and its main purpose is to print all the information inside the *register.csv*, which contains the history of all the transactions done by the company. For every transaction, the function will show the  email of the customer, the date of the transaction, the metal that has been bought, the quantity and the final price. 

## *Get balance*
*Get_balance* is one of the three functions that only the employee can call (*read_register*, *get_balance*, and *pay_loan*). The function has three main purposes: Initially, it will read the *inventory.csv* and then print the amount of all the metals available in the inventory. 
Secondly, the function will analyze the *wallet.csv* and then show the value associated with the balance column, which corresponds to the cash available to buy materials. Finally, the function will print the bank loan that the company asked to buy new materials if money is not enough.

## *Pay loan*
Employees are the only ones who can call the *pay loan* function. Its major purpose is to determine whether there is enough money to repay the bank, thereby verifying the availability of funds and repaying the bank loan in part or in full utilizing all of the company's accessible funds. Here, we consider the *wallet.csv* file, which contains any hypothetical amount to be returned to the bank, our balance, and then any cash inflow and outflow.

As a result, the function's initial task is to determine whether any bank loan must be repaid. If our company's balance is equal to 0, the function will return *'You have no money to repay your bank loan.'* If the bank loan is equal to 0, the function will return *'There are no debts to be repaid.'*
However, if our balance exceeds the loan, we will be able to repay the entire bank loan; otherwise, we will repay only a portion of the bank loan.
