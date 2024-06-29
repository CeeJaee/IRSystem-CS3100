# Linked List Dictionary Implementation of IR System
from dict.lldict import *
from dict.abstract import CountryIRSystemAbstract
from Country import Country
import csv

class Country_lldict(CountryIRSystemAbstract):

  def __init__(self):
    self.__country_dict = LLDict()
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
        

  # Jude - country_search, if countryname matches the key of each node, then return the value of the key (value is Country object)
  def country_search(self, countryname):
    if countryname in self.__country_dict:
      return self.__country_dict[countryname]
    return None

  # Jude - find the min and max value and associated country for an indicator.
  def min_and_max(self, indicator):
    # empty list to store the min and max values with country names
    maxmin_list = []
    # check if user input indicator exists
    for x in self.__indicators:
      if x == indicator:
        attribute = self.__indicators[self.__indicators.index(indicator)]
        # get a list of the all country names and values from the bst
        list = self.__country_dict.getatt_lldict(attribute)
        
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

  # Abigail - dev or developing
  # checks the GNI per capita to see if a country is developed or developing
  def developed_or_developing(self, country_name):
    country = self.country_search(country_name)
    #if it is less than $12695 then it is developing, if greater the country is developed
    if float(country.GNI_per_capita) < float(12695):
      return 0
    else:
      return 1
    return None
    pass

  # Abigail - compare country
  # compares two countries and returns the higher and lower values of those countries
  def country_compare(self, country1, country2, indicator):
    # list of the countries and their values
    values = []
    c1 = self.country_search(country1)
    c2 = self.country_search(country2)
    val1 = None
    val2 = None

    # checks for the indicator and if does exist then it access it
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
    pass

  #Isaac - list_of_countries: get the names of the countries so far we have collected
  #create function to return the list of countries
  def list_of_countries(self):
    
    #create an array for country
    country_list = self.__country_dict.getatt_lldict("country_name")

    #return an array
    return country_list

  #Isaac - add_country: giving the indictors of the country, add the new country to the list
  def add_country(self, country_name, agricultural_land, access_to_electricity, life_expectancy, total_population, labor_force, GNI_per_capita): 
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

  #Isaac - remove_country: if the giving country is in the list then remove it
  def remove_country(self, user_country):
    # loop through the list of country
    #for country in self.__country_dict:
    #check each country
    if user_country in self.__country_dict:
       #remove country from list
        self.__country_dict.pop(user_country)
       #let the user know the country has been removed
        return True 
    else: 
      #returns that country was not found
      return False
      
 

  def __str__(self):
    return str(self.__country_dict)

  