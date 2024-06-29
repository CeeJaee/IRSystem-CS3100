from CountryIRSystem import CountryIRSystem
from BSTCountryIRSystem import Country_BSTdict

# creating Interface class
class Interface:
  # Jude
  @staticmethod
  def print_menu():
    print("<><><><><><><><><><><><><><><><><><><><><>")
    print("|    COUNTRY DATA RETRIEVAL SYSTEM       |")
    print("<><><><><><><><><><><><><><><><><><><><><>")
    print("(1) - Input file")
    print("(2) - Country Search")
    print("(3) - Country Compare")
    print("(4) - Min and Max for an Indicator")
    print("(5) - Is a Country Developed or Developing")
    print("(6) - List Countries")
    print("(7) - Add Country")
    print("(8) - Remove Country")
    print("(9) - Exit Program")
  
  @staticmethod
  def country_menu():
    # Jude - print Interface menu
    Interface.print_menu()

    # create IRSystem object to call functions
    irsys = CountryIRSystem()
    
    options = 1
    while (options != 0 ):
      options = int(input("Please insert your option: "))

      # Jude - load_data
      if options == 1:
        csv_file = input("Enter name of csv file with country data: ")
        irsys.load_data(csv_file)
        print("loaded: " + csv_file + "\n")
      
      # Abigail Ezrre - country_search
      elif options == 2:
        # ask for country name 
        country = input("Enter country: ")
        # calls country search function 
        test = irsys.country_search(country)
        # if name not found, prints None; when found it prints country data
        if test == None:
          print("Not found")
        else:
          print(country + f'\nAgricultural Land: {test.agricultural_land}%\nAccess to Electricity: {test.access_to_electricity}%\nLife Expectancy: {test.life_expectancy}%\nTotal Population: {test.total_population} people\nLabor Force: {test.labor_force} people\nGNI per capita: ${test.GNI_per_capita}')
          
      # Jude - country_compare
      elif options == 3:
        # store 2 country names and indicator name
        c1 = input("Enter the name of the first country: ")
        c2 = input("Enter the name of the second country: ")
        indicator = input("Enter the indicator you want to compare: ")
        # call country_compare function; returns a list of country names and values
        list_compare = irsys.country_compare(c1, c2, indicator)
        # c1's value is higher than c2
        if list_compare[1] > list_compare[3]:
          print("Comparing "+ indicator)
          print(list_compare[0] + " has a greater value of " + str(list_compare[1]) + " compared to " + list_compare[2] + " with " + str(list_compare[3]))
        # c2's value is higher than c1
        elif list_compare[3] > list_compare[1]:
          print(list_compare[2] + " has a greater value of " + str(list_compare[3]) + " compared to " + list_compare[0] + " with " + str(list_compare[1]))
        # c1 and c2 have the same value
        else:
          print(list_compare[0] + " and " + list_compare[2] + " have the same value of " + str(list_compare[1]))
        
      
      # Jude - min_and_max
      elif options == 4: 
        # ask user for Indicator
        print("Indicators: agricultural_land, access_to_electricity, life_expectancy, total_population, labor_force, GNI_per_capita")
        # ask user to input an indicator to find its max and min country
        indicator = input("Enter an Indicator to find the maximum and minimum country values: ")
        # call min_and_max; returns a list of 2 country's name and their values
        min_max_list = irsys.min_and_max(indicator)
        print("maximum and minimum for: " + indicator)
        print(min_max_list[0] + " has the highest value of " + str(min_max_list[1]))
        print(min_max_list[2] + " has the lowest value of " + str(min_max_list[3]))
        
      
      # Abigail Ezrre - developed_or_developing
      elif options == 5:
        # asks for country name to check if it is developed or not
        country = input("Enter a country to see if it's developed or developing: ")
        # calls developed function 
        deving_or_deved = irsys.developed_or_developing(country)
        # if country equals 0, it is developing; if equals 1 then it is develped
        if deving_or_deved == 0:
          print(country + " is a developing country")
        elif deving_or_deved == 1:
          print(country + " is a developed country")
     
      # Isaac - countries_list
      elif options == 6:
        print(irsys.list_of_countries())
        
      # Isaac - add_country
      elif options == 7: 
        #calls in the add_country method from CountryIRSystem
        irsys.add_country()
        
        
      # Isaac - remove_country
      elif options == 8:
        #asks the user which country they want to remove
        remove_country_input = input(str("What country would you like to remove? "))
        #calls in the remove_country method from CountryIRSystem
        irsys.remove_country(remove_country_input)        
        
        
      # exit program
      elif options == 9:
        #breaks the while loop
        break
      
      elif options != 0:
        print("Invalid option")

  
  @staticmethod
  def bst_country_menu():
    Interface.print_menu()
    
    irsys = Country_BSTdict()
    options = 1
    while (options != 0 ):
      options = int(input("Please insert your option: "))
      
      # Jude - load data
      if options == 1:
        csv_file = input("Enter name of csv file with country data: ")
        irsys.load_data(csv_file)
        print("loaded: " + csv_file + "\n")
        pass

      # Abigail - country search
      if options == 2:
        # ask for country name 
        country = input("Enter country: ")
        # calls country search function 
        test = irsys.country_search(country)
        # if name not found, prints None; when found it prints country data
        if test == None:
          print("Not found")
        else:
          print(country + f'\nAgricultural Land: {test.agricultural_land}%\nAccess to Electricity: {test.access_to_electricity}%\nLife Expectancy: {test.life_expectancy}%\nTotal Population: {test.total_population} people\nLabor Force: {test.labor_force} people\nGNI per capita: ${test.GNI_per_capita}')
        pass
      
      # Abigail - country compare
      if options == 3:
        c1 = input("Enter the name of the first country: ")
        c2 = input("Enter the name of the second country: ")
        indicator = input("Enter the indicator you want to compare: ")
        list_compare = irsys.country_compare(c1,c2, indicator)
        if list_compare[1] > list_compare[3]:
          print("Comparing " + indicator)
          print(list_compare[0] + " has a greater value of " + str(list_compare[1]) + " compared to " + list_compare[2] + " with " + str(list_compare[3]))
        elif list_compare[3] > list_compare[1]:
          print(list_compare[2] + " has a greater value of " + str(list_compare[3]) + " compared to " + list_compare[0] + " with " + str(list_compare[1]))
        else:
          print(list_compare[0] + " and " + list_compare[2] + " have the same value of " + str(list_compare[1]))
        pass
      
      # Jude - min and max
      if options == 4:
        # ask user for Indicator
        print("Indicators: agricultural_land, access_to_electricity, life_expectancy, total_population, labor_force, GNI_per_capita")
        # ask user to input an indicator to find its max and min country
        indicator = input("Enter an Indicator to find the maximum and minimum country values: ")
        # call min_and_max; returns a list of 2 country's name and their values
        min_max_list = irsys.min_and_max(indicator)
        print("\nCalling max_and_min")
        print("maximum and minimum for: " + indicator)
        print(min_max_list[0] + " has the highest value of " + str(min_max_list[1]))
        print(min_max_list[2] + " has the lowest value of " + str(min_max_list[3]))
        pass

      # Abigail - developed_or_developing
      if options == 5:
        # asks for country name to check if it is developed or not
        country = input("Enter a country to see if it's developed or developing: ")
        # calls developed function 
        deving_or_deved = irsys.developed_or_developing(country)
        # if country equals 0, it is developing; if equals 1 then it is develped
        if deving_or_deved == 0:
          print(country + " is a developing country")
        elif deving_or_deved == 1:
          print(country + " is a developed country")
        pass

      # Isaac - countries list
      if options == 6:
        #creates an array of the countries but doubles each country
        country_list = irsys.list_of_countries()

        #print(country_list)
        #loops through so only display each country
        for i in range(0, len(country_list), 2):
          #new_country_list =+ country_list[i]
          print(country_list[i])
        pass

      # Isaac - add country
      if options == 7:

        #asking the user for the information needed to create a new country
        name = str(input("What is the country name you would like to add?"))
        ag = float(input("What is " + name + " agricultural land % "))
        ele = float(input("What is " + name + " access to electrivity?"))
        exp = float(input("What is " + name + " life expectancy?"))
        pop = int(input("What is" + name + " total population?"))
        labor = int(input("What is "+ name + " labor force?"))
        gni = float(input("What is " + name + " GNI per capita?"))

        #calling on the add metrod
        new_country = irsys.add_country(name, ag, ele, exp, pop, labor,gni )

        if new_country == True:
          print("Country " + name + " was successfully added!")
        else: 
          print("Country " + name + " was unsuccessfully added!")

        pass

      # Isaac - remove country
      if options == 8:
        name = input("What country would you like to remove?")
        remove = irsys.remove_country(name)
  
        if remove == True:
          print("The country " + name + " has been removed.")
        elif remove == False:
          print("The country " + name + " was not removed.")
        pass

      # exit program
      if options == 9:
        print("You have exited.")
        break
      pass