class Country:
  # creating private variables for country class
  def __init__(self):
    self._country_name = ""
    self._country_code = ""
    self._series_code = ""
    self._agricultural_land = 0.0
    self._access_to_electricity = 0.0
    self._life_expectancy = 0.0
    self._total_population = 0
    self._labor_force = 0
    self._GNI_per_capita = 0.0

   
  # Isaac getter for country_name
  @property
  def country_name(self):
    #making sure this function is being called
    #print("getter called for country_name")
    return self._country_name
      
  # Isaac setter for country_name
  @country_name.setter
  def country_name(self, country_name):
    #checking the input value is a string
    assert isinstance(country_name, str), "insert only string values"
    #making sure this function is being called
    #print("setter called for country_name")
    self._country_name = country_name
      
  # Isaac getter for country_code
  @property
  def country_code(self):
    #making sure this function is being called
    #print("getter called for country_code")
    return self._country_code

  #Isaac setter for country_code
  @country_code.setter
  def country_code(self, country_code):
    #checking the input value is a string
    assert isinstance(country_code, str), "insert only string value"
    #making sure this function is being called
    #print("setter called for country_code")
    self._country_code = country_code
   
  #Isaac getter for series_code
  @property
  def series_code(self):
    #making sure this function is being called
    #print("getter called for series_code")
    return self._series_code
      
  #Isaac setter for series_code
  @series_code.setter
  def series_code(self, series_code):
    #checking the input value is a string
    assert isinstance(series_code, str), "insert only string value"
    #making sure this function is being called
    #print("setter called for series_code")
    self._series_code = series_code
      
  #Isaac getter for agricultural_land
  @property
  def agricultural_land(self):
    #making sure this function is being called
    #print("getter called for agricultutal_land")
    return self._agricultural_land

  #Isaac setter for agricultural_land
  @agricultural_land.setter
  def agricultural_land(self, agricultural_land):
    #checking the input value is a float or a int
    assert isinstance(agricultural_land, (int, float)), "is not a float/int"
    #making sure this function is being called
    #print("setter called for agricultural_land")
    self._agricultural_land = agricultural_land
  
  # Jude - getter and setter for access to electricity
  # If the value num is not a float or int, error message
  @property
  def access_to_electricity(self):
    return self._access_to_electricity
  @access_to_electricity.setter
  def access_to_electricity(self, num):
    assert isinstance(num, (float, int)), "not a float or int"
    self._access_to_electricity = num
  # Jude - getter and setter for life expectancy
  # If the value num is not a float or int, error message
  @property
  def life_expectancy(self):
    return self._life_expectancy
  @life_expectancy.setter
  def life_expectancy(self, num):
    assert isinstance(num, (float, int)), "not a float or int"
    self._life_expectancy = num
  # Jude - getter and setter for total population
  # If the value num is not an integer, error message
  @property
  def total_population(self):
    return self._total_population
  @total_population.setter 
  def total_population(self, num):
    assert isinstance(num, int), "not an integer"
    self._total_population = num
  # Jude - getter and setter for labor force
  # If the value num is not an integer, error message
  @property
  def labor_force(self):
    return self._labor_force
  @labor_force.setter
  def labor_force(self, num):
    assert isinstance(num, int), "not an integer"
    self._labor_force = num 

  @property
  def GNI_per_capita(self):
    return self._GNI_per_capita
  @GNI_per_capita.setter
  def GNI_per_capita(self, num):
    assert isinstance(num, (float, int)), "not a float or int"
    self._GNI_per_capita = num
  
  '''def __repr__(self):
    return "\n".join(["Country name is - " + self._country_name, "Ag land is - " + str(self._agricultural_land), "Access to elec is - " + str(self._access_to_electricity)])'''
  def __str__(self):
    lines = ("Country Name: " + str(self._country_name) + "\nAgricultural land: " + str(self._agricultural_land) + "\naccess to electricity: " + str(self._access_to_electricity) + "\nlife expectancy: " + str(self._life_expectancy) + "\ntotal population: " + str(self._total_population) + "\nlabor force: " + str(self._labor_force) + "\nGNI: " + str(self._GNI_per_capita))
    return lines