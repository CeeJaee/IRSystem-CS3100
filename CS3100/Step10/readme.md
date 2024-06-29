UPDATES FOR STEP 10:
- Added randomfiles.py
    - creates a csv file called "temp_rand" that adds in a specified number of entries and shuffles the lines of the csv
- Added analysis.py
    - based on number of entries and search queries, finds the amount of time it takes to search through the data for each data structure
        - for list, binary search tree, linked list, sorted list, and hash table
- in main.py
    - includes country_analysis() function to run the country analysis
    - includes two command-line interfaces for the list and bst implementation
    - includes the external gui using tkinter

UPDATES FOR STEP 9:
- in dict folder, created htdict.py
  - HTDict class
  - implementation for dictionary using a hash table (data strucuture)
    - Use of open hashing collision resolution (linked lists)
- Created HTCountryIRSystem.py, functionalities of IRSystem using the hash table
-----------------------------------------------------------
UPDATES FOR STEP 8:
- in dict folder, created sldict.py
  - SLDict class
  - implementation for dictionary using a sorted list
    - use of bubble sort and binary search
- Created SLCountryIRSystem.py, implements functionalities of IRSystem using the sorted list
-----------------------------------------------------------
UPDATES FOR STEP 7:
- in dict folder, created lldict.py
  - lldict.py contains _Node class and LLDict class
  - contains implemenation for dictionary using a linked list.
    - magic methods adapted from Step 6 to work with a linked list rather than a binary search tree
- Created LLCountryIRSystem.py which implements the functionalities of the IRSystem using a linked list implementation of a dictionary
- Rather than using an interface, the main function tests each functionality of the IR sytem using print stmts
-----------------------------------------------------------
UPDATES FOR STEP 6:
- added dict folder
  - abstract.py contains declarations of abstract functions
  - bstdict.py contains implementation for dictionary using a binary search tree
  - added BSTCountryIRSystem.py which implements the functionalities of the IRSystem using the binary search tree dictionary instead of a list
  - In Interface.py
    - added bst_country_menu function to implement the console/commandline GUI that uses the dictionary implementation of CountryIRSystem
-----------------------------------------------------------
UPDATES FOR STEP 5:
- Interface.py creates an interface for the IRSystem on the console
  - to use must have Interface.country_menu() uncommented in main.py
- GUI.py uses tkinter, a GUI toolkit to create a GUI for IRSystem
  - to use must have GUI.extraGUI() uncommented
  - as of 3/27 9:14 PM, still a work in progress
  - The only functionalities implemented are load_data, countries_list, country_search, remove_country
    - still need to implement country_compare, min_and_max, add_country and developing_or_developed
-----------------------------------------------------------
Problem to solve: We need to implement the methods for our country IR System which are searching for a country, comparing values of 2 country's indicators (which has higher value), which country has the highest and lowest values out of all countries in the given data, finding if a country is developed or developing, list all the countries currently in the data list, adding a country, and removing a country

To be able to implement these functions, we need a function that can load data from a csv file into a list which is the load_data function

Once each function is implemented, we need to make sure they work by calling them and using print statements in the main function, making sure they return and print the right values.
------------------------------------------------------
File information:
- main_data.csv is the csv file that contains 20 countries and 6 indicators used in main.py
- data(not in use).csv is the original csv file in an old format - not being used currently
- meeting_log.md contains a Google Doc link to the group's weekly meetings
- main.py
  - creates irsystem object and loads the csv file data into a list
  - calls list_of_countries, remove_country, and add_country
  - calls country_compare
  - calls min_and_max
  - calls country search
  - calls developed_or_developing
  - calls main()
  - input parameters are currently hard-coded for ease of testing, but can be switched to user input
- Country.py
  - contains variables for country information: name and indicator values
  - getters and setters for each variable
- CountryIRSystem.py
  - Two attributes: countries and indicators
  - defines load_data, country_search, country_compare, min_and_max, and developed_or_developing
  - defines list_of_countries, add_country, remove_country