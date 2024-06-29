from randomfiles import *
from analysis import *
from Interface import Interface
from external_gui import external_gui

# run the time analysis for each data structure
def country_analysis():
  no_entries = 10000
  no_queries = 1000
  generate_data_csv("temp_rand.csv", no_entries)
  country_inventory_analysis("temp_rand.csv", no_queries, no_entries)

if __name__ == "__main__":
  #country_analysis()
  
  # command-line interface for list and bst implementation
  #Interface.bst_country_menu()
  #Interface.country_menu()
  
  # Using external GUI through tkinter
  external_gui.extraGUI()