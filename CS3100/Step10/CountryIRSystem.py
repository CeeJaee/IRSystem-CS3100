# List Implementation of IR System
from Country import Country
from dict.abstract import CountryIRSystemAbstract 
import csv 

class CountryIRSystem(CountryIRSystemAbstract):
  def __init__(self):
    self.__countries = []  # creating a list of countries
    self.__indicators = ["agricultural_land", "access_to_electricity", "life_expectancy","total_population", "labor_force", "GNI_per_capita"]  # list for indicators -- they are static

  # Jude - for each line in csv, create country object
  # assign country attribute values based on index
  # push country object into countries list
  def load_data(self, file_name):
    with open(file_name, "r") as csvfile:
      csvreader = csv.reader(csvfile)
      for lines in csvreader:
        country = Country()
        country.country_name = str(lines[0])
        country.country_code = lines[1]
        country.agricultural_land = float(lines[2])
        country.access_to_electricity = float(lines[3])
        country.life_expectancy = float(lines[4])
        country.total_population = int(lines[5])
        country.labor_force = int(lines[6])
        country.GNI_per_capita = float(lines[7])
        
        self.__countries.append(country)
       
        

        
    return 0
      
  # Jude - display one country's data
  # iterate through countries list, if countryname is found
  # return the country object
  def country_search(self, countryname):
    for country in self.__countries:
      if country.country_name == countryname:
        return country
    return None
    
  # Jude - find the higher of two country's values
  # return an list of higher and lower values and their country names
  def country_compare(self, country1, country2, indicator):
    # values = [country1_name, val1, country2_name, val2]
    values = []
    # find the objects of the given countries by searching
    c1 = self.country_search(country1)
    c2 = self.country_search(country2)
    val1 = None     # data value of the first country's indicator
    val2 = None     # data value of the second country's indicator
    # check if indicator parameter exists, if it does, then access the indicator value
    for x in self.__indicators:
      if x == indicator:
        attribute = self.__indicators[self.__indicators.index(indicator)]
        val1 = getattr(c1, attribute)
        values.append(getattr(c1, "country_name"))
        values.append(val1)
        val2 = getattr(c2, attribute)
        values.append(getattr(c2, "country_name"))
        values.append(val2)
    return values
    
  # Jude - find the max and min values of an indicator out of entire country list, returns values and respective country names
  def min_and_max(self, indicator): 
    # values = [country1_name, max value, country2_name, min value]
    values = []
    # loop through indicator list, if an element in the list matches indicator parameter, set attribute to that element
    for x in self.__indicators:
      if x == indicator:
        attribute = self.__indicators[self.__indicators.index(indicator)]
        # get the max value for attribute in the countries list
        maximum = max(self.__countries, key=lambda country: getattr(country, attribute)) 
        # get the minimum value for attribute in countries list
        minimum = min(self.__countries, key=lambda country: getattr(country, attribute))
        # insert max country name and its value, min country name and value to vals list
        values.append(maximum.country_name)
        values.append(getattr(maximum, attribute))
        values.append(minimum.country_name)
        values.append(getattr(minimum, attribute))
        return values
    return None
    # -- end of min and max function --

  # Jude - uses GNI per capita to check if a country is developed or developing
  # if GNI per capita is less than $12695, then developing, if greater than or equal to, then developed. Returns 0 if developing, 1 if developed
  # may delete function (serves little purpose) or add other functions that can use developing vs developed comparisons
  def developed_or_developing(self, country_name):
    country = self.country_search(country_name)
    if float(country.GNI_per_capita) < float(12695):
      return 0
    else:
      return 1
    return None
    
  #simple csv to list converter
  def reader(self, csv_file_name):
    #creating an empty list variable
    my_list = [] 
    #opens csv file as it reads through it
    with open(csv_file_name, "r") as csvfile:
      #creating a variable to store the csv being read
      csvreader = csv.reader(csvfile)

      #for loop to adding the line data into my_list
      for lines in csvreader:
        #adding to my_list
        my_list.append(lines)

      #return the list after being read
      return my_list 

  #list to dictionary 
  def load_data2(self, data):

    #using previous function
    new_data = self.reader(data)
    
    #Create an empty dictionary
    organized_data = {}

    #loop through each of the new_data
    for row in new_data[1:]:

      #creating and assign the countries name/indicator
      country_name = row[0]
      country_indictor = row[2]

      #if this is the first time this country appears then create a new dictionary
      if country_name not in organized_data:
        organized_data[country_name]= {}

      #adds the indictor and country to the countries dictorionary
      organized_data[country_name][country_indictor] = row[4]

    #returns the new dictionary created
    return organized_data


  #create function to return country list
  def list_of_countries(self):

    #creates a string just to display the all of countries
    country_list = ""

    #using an i variable to keep track of the number of countries
    i = 1
    
    #for loop for the country class
    for country in self.__countries:

      #adding the country name to the string country_list
      country_list += str(i) + ") " + country.country_name + " \n"
      #adding one each time it goes through the loop
      i += 1

    #return a string of the countries
    return country_list

  def add_country_2(self, country, ag, ele, exp, pop, labor, gni):

    #create a country class
    country_add = Country()

    country_add.country_name = country
    country_add.agricultural_land = ag
    country_add.access_to_electricity = ele
    country_add.life_expectancy = exp
    country_add.total_population = pop
    country_add.labor_force = labor
    country_add.GNI_per_capita = gni

    #add the new country to the country list 
    self.__countries.append(country_add)

    return True
    
    
  #create a function to add a country
  def add_country(self):

    #create a country class
    country_add = Country()

    #assign the indictors for the new country added from the user's input
    country_add.country_name = str(input("What is the country name you would like to add?"))
    country_add.agricultural_land = float(input("What is " + country_add.country_name + " agricultural land % ?"))
    country_add.access_to_electricity = float(input("What is " + country_add.country_name + " access to electricity % ?"))
    country_add.life_expectancy = int(input("What is " + country_add.country_name + " life expectancy age?"))
    country_add.total_population = int(input("What is " + country_add.country_name + " total population?"))
    country_add.labor_force = int(input("What is " + country_add.country_name + " labor force?"))

    #add the new country to the country list 
    self.__countries.append(country_add)

    return True

  #create a function to remove a country
  def remove_country(self, user_country):
    country_removed = "The country " + user_country + " is not in our list."
    #for loop for list of countries
    for country in self.__countries:
      #check if the user's input is equal to the country
      if country.country_name == user_country:
        #remove the country from the list
        self.__countries.remove(country)
        #assign and return the country name
        country_removed = "The country " + user_country + " has been removed."
        
    #return
    return country_removed
 