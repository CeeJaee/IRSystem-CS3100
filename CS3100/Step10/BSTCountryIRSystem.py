# Binary Search Tree Dictionary Implementation of IR System
from dict.bstdict import *
from dict.abstract import CountryIRSystemAbstract
from Country import Country
import csv

class Country_BSTdict(CountryIRSystemAbstract):
  
  def __init__(self):
    self.__country_dict = BSTDict()
    self.__indicators = ["agricultural_land", "access_to_electricity", "life_expectancy","total_population", "labor_force", "GNI_per_capita"]

  # Jude
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
        
        self.__country_dict[country.country_name] = country
    #self.print_tree()
        #print(self.__country_dict)

  # Jude - country_search
  def country_search(self, countryname):
    # if countryname matches key, return the value of the key
    if countryname in self.__country_dict:
      return self.__country_dict[countryname]
    return None

  # Jude
  def min_and_max(self, indicator):
    # prints bst dictionary
    #print(self.__country_dict.print_tree())
    maxmin_list = []
    for x in self.__indicators:
      if x == indicator:
        attribute = self.__indicators[self.__indicators.index(indicator)]
        # get a list of the all country names and values from the bst
        list = self.__country_dict.getatt_tree(attribute)
        
        # find the max value in the list
        maximum = max([i for i in list if isinstance(i, int) or isinstance(i, float)])
        # find the index of the maximum value, the index + 1 is the country name
        max_country = list.index(maximum)
        minimum = min([i for i in list if isinstance(i, int) or isinstance(i, float)])
        min_country = list.index(minimum)
        
        maxmin_list.append(list[max_country + 1])
        maxmin_list.append(maximum)
        maxmin_list.append(list[min_country + 1])
        maxmin_list.append(minimum)
    return maxmin_list
    # works
    #test = self.__country_dict["United States"]
    #print(self.__country_dict["United States"])
  # end of maxmin function

  #Abigail - dev or developing
  def developed_or_developing(self, country_name):
    country = self.country_search(country_name)
    if float(country.GNI_per_capita) < float(12695):
      return 0
    else:
      return 1
    return None

  #Abigail - country_compare
  def country_compare(self, country1, country2, indicator):
    values = []
    c1 = self.country_search(country1)
    c2 = self.country_search(country2)
    val1 = None
    val2 = None

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
    
  def add_country(self, country_name, agricultural_land, access_to_electricity, life_expectancy, total_population, labor_force, GNI_per_capita ):
    #create a country class
    country_add = Country()

    #assign values to indictors
    country_add.country_name = country_name 
    country_add.agricultural_land = agricultural_land
    country_add.access_to_electricity = access_to_electricity
    country_add.life_expectancy = life_expectancy
    country_add.total_population = total_population
    country_add.labor_force = labor_force
    country_add.GNI_per_capita = GNI_per_capita

    #add to the list country
    self.__country_dict[country_add.country_name] = country_add

    return True
    
  def remove_country(self, user_country):
    country_not_found = "The country " + user_country + " is not in our list."
     # loop through the list of country
    #for country in self.__country_dict:
      #check each country
    if user_country in self.__country_dict:
       #remove country from list
        self.__country_dict.pop(user_country)
       #let the user know the country has been removed
        country_removed = "The country " + user_country + " has been removed."
      #returns that the country has been removed
        return country_removed
    
    else: 
      #returns that country was not found
      return country_not_found
    

    

    
  #method to show the list of countries
  def list_of_countries(self):

    #create an array for the country
    country_list = self.__country_dict.getatt_tree("country_name")

    #return the array
    return country_list

    

    
  def __str__(self):
    return str(self.__country_dict)

  def __repr__(self):
    return str(self.__country_dict)
    
  def print_data(self):
    self.__country_dict.print_tree()

  '''def __str__(self):
    inventory = ""
    for country in self.__country_dict:
      inventory = inventory + str(country)

    return inventory'''
        

  