from CountryIRSystem import CountryIRSystem
# import tkinter, a GUI toolkit on python
import tkinter as tk

# create a GUI static class, we will only be using one instance of the class.
class external_gui:
  @staticmethod

  # function that will create the entire GUI
  def extraGUI():
    # create IRSystem object
    irsys = CountryIRSystem()
    #creating a object from tkinter
    root = tk.Tk()
    
    # set the dimension of the window in pixels
    root.geometry("600x600")
    
    # Title of the window
    root.title("www.GUITEST.edu")
    
    # create a frame for the main menu to be in
    main_frame = tk.LabelFrame(root, text="Country IRSystem", padx=5, pady=5)
    main_frame.pack(fill=tk.BOTH, expand=1)
    

   
    # Jude - load_data
    def action_load():
      # create a new window called top, titled load data
      top = tk.Toplevel()
      top.geometry("600x600")
      top.title("Load data")
      
      # create an entry box for a user to input their value
      testinput = tk.Entry(top, width = 30)  # entrybox for user input
      testinput.insert(0, "Enter csv file name")
      testinput.pack(pady=10)
      
      # Jude - retrieves the string from the entry box, loads the data using load_data.
      # disables the load button and updates the feedback message on the main menu to inform that data has been loaded
      def load():
        csv_file = testinput.get()
        irsys.load_data(csv_file)
        button_load.config(state=tk.DISABLED)
        feedback.config(text="data loaded")
      # create a button to load the csv data given from the user 
      button_load = tk.Button(top, text="Load Data", command=load)
      button_load.pack()
      # return to main menu by destroying the window 'top'
      button_close = tk.Button(top, text="Return to Menu", command=top.destroy)
      button_close.pack(pady=10)
    
    # Jude - list_countries
    def action_list():
      # create a new window called top, titled list of countries
      top = tk.Toplevel()
      top.geometry("600x600")
      top.title("List of countries")

      # create a label to display the countries from the data
      test = tk.Label(top, text=irsys.list_of_countries(), font=("Times New Roman", 12))
      test.pack()
      
      # updates the feedback message on the main menu to inform that data has been loaded 
      feedback.config(text="countries listed")
      
      # return to main menu by destroying the window 'top'
      button_close = tk.Button(top, text="Return to Menu", command=top.destroy)
      button_close.pack(pady=10)

    #Isaac
    def compare_country():
      #creating a new window to compare countries
      top = tk.Toplevel()
      top.geometry("600x600")
      top.title("Comparing Countries")
      

      #Create entry boxes for the country and the information required
      #text insertion for country added
      C_one = tk.Entry(top, width = 30)
      C_one.insert(0, "Enter first country")
      C_one.pack(pady=10)
    

      #text insertion for indictor 
      C_two = tk.Entry(top, width = 30)
      C_two.insert(0, "Enter second country")
      C_two.pack(pady=10)

      #text insertion for indictor to agicultural land
      indicator_in = tk.Entry(top, width = 30)
      indicator_in.insert(0, "Enter indicator")
      indicator_in.pack(pady=10)

       # create an empty label to be updated with country info
      label = tk.Label(top, text = "", font=('Arial', 10))

      
      

      def compare():
        #storing the input from the user into variables
        c1 = C_one.get()
        c2 = C_two.get()
        indicator = indicator_in.get()
        #calling the compare method in the irsys class
        list_compare = irsys.country_compare(c1, c2, indicator)

        #comparing if c1 has a higher value than c2
        if list_compare[1] > list_compare[3]:
          label.config(text= "Comparing "+ indicator + " :\n" + list_compare[0] + " has a greater value of " + str(list_compare[1]) + " compared to " + list_compare[2] + " with " + str(list_compare[3]))
          
        #comparing if c2 has a higher value than c1
        elif list_compare[3] > list_compare[1]:
          label.config(text= "Comparing "+ indicator + " :\n" +  list_compare[2] + " has a greater value of " + str(list_compare[3]) + " compared to " + list_compare[0] + " with " + str(list_compare[1]))
        # c1 and c2 have the same value
        else:
          label.config(text= list_compare[0] + " and " + list_compare[2] + " have the same value of " + str(list_compare[1]))

        label.pack()
      
      
      # create button to compare country
      button_compare = tk.Button(top, text="Compare Countries", command=compare)
      button_compare.pack(pady=10)
      
      # return to main menu by destroying the window 'top'
      button_close = tk.Button(top, text="Return to Menu", command=top.destroy)
      button_close.pack(pady=10)
      
    # Isaac  
    def action_add():
      #creating a new window to add a new country
      top = tk.Toplevel()
      top.geometry("600x600")
      top.title("Add Country")

      #Create entry boxes for the country and the information required
      #text insertion for country added
      country_added = tk.Entry(top, width = 30)
      country_added.insert(0, "Enter the Country you would like to add")
      country_added.pack(pady=10)

      #text insertion for indictor to agicultural land
      country_ag = tk.Entry(top, width = 30)
      country_ag.insert(0, "Enter the Country's agricultural land %'")
      country_ag.pack(pady=10)
      

      #text insertion for indictor to access to electricity
      country_ele = tk.Entry(top, width = 30)
      country_ele.insert(0, "Enter the Country's access to electricity %")
      country_ele.pack(pady=10)

      #text insertion for indictor for life expectancy
      country_life = tk.Entry(top, width = 30)
      country_life.insert(0, "Enter the Country's life expectancy age")
      country_life.pack(pady=10)

      #text insertion for indicot for total population
      country_pop = tk.Entry(top, width = 30)
      country_pop.insert(0, "Enter the Country's total population")
      country_pop.pack(pady=10)

      #text insertion for indictor for labor force
      country_labor = tk.Entry(top, width = 30)
      country_labor.insert(0, "Enter the Country's labor force")
      country_labor.pack(pady=10)

      #text insertion for indictor for labor force
      country_gni = tk.Entry(top, width = 30)
      country_gni.insert(0, "Enter the Country's GNI per capita")
      country_gni.pack(pady=10)

      #use the data and add the country
      def add():
        country_str = country_added.get()
        ag_float = float(country_ag.get())
        ele_float = float(country_ele.get())
        exp_float = float(country_life.get())
        pop_int = int(country_pop.get())
        labor_int = int(country_labor.get())
        gni_float = float(country_gni.get())
        
        
        #irsys.hardcodeaddcountry()
        irsys.add_country_2(country_str, ag_float , ele_float, exp_float , pop_int, labor_int, gni_float)
        feedback.config(text="Country Added: " + country_str)

      # create button in top to add country
      button_added = tk.Button(top, text="Country Added to the list", command=add)
      button_added.pack(pady=10)
      #button_added.config(state=tk.DISABLED)
      #feedback.config(text="Country Added: " + country_added.get() )
      
      
      # return to main menu by destroying the window 'top'
      button_return = tk.Button(top, text="Return to Menu", command=top.destroy)
      button_return.pack(pady=10)

      
    # Jude - remove country
    def action_remove():
      # create a new window called top, titled remove country
      top = tk.Toplevel()
      top.geometry("600x600")
      top.title("remove country")
      
      # create an entry box for a user to input their value
      testinput = tk.Entry(top, width = 30)
      testinput.insert(0, "Enter Country to Remove")
      testinput.pack(pady=10)

      # removes country from the data list, updates feedback message in the main menu
      def remove():
        irsys.remove_country(testinput.get())
        feedback.config(text="Country Removed: " + testinput.get())
      
      # create button in top to remove country
      button_search = tk.Button(top, text="Remove Country", command=remove)
      button_search.pack(pady=10)
      
      # return to main menu by destroying the window 'top'
      button_close = tk.Button(top, text="Return to Menu", command=top.destroy)
      button_close.pack(pady=10)

      
    # Jude - country search
    def action_search():
      # create a new window called top, titled country search
      top = tk.Toplevel()
      top.geometry("600x600")
      top.title("Country Search")
      
      # create an entry box for a user to input their value
      testinput = tk.Entry(top, width = 30)
      testinput.insert(0, "Enter country to search")
      testinput.pack(pady=10)

      # create an empty label to be updated with country info
      label = tk.Label(top, text = "", font=('Arial', 18))
      
      # takes input from the entry box and searches for country
      # updates the label with the country's information
      def search():
        test = irsys.country_search(testinput.get())
        country = testinput.get()
        if test == None:
          label.config(text="not found")
        else:
          label.config(text= country + f'\nAgricultural Land: {test.agricultural_land}%\nAccess to Electricity: {test.access_to_electricity}%\nLife Expectancy: {test.life_expectancy}%\nTotal Population: {test.total_population} people\nLabor Force: {test.labor_force} people\nGNI per capita: ${test.GNI_per_capita}')
          label.pack()

      # creates button to search country
      button_search = tk.Button(top, text="Country Search", command=search)
      button_search.pack(pady=10)
      
      # return to main menu by destroying the window 'top'
      button_close = tk.Button(top, text="Return to Menu", command=top.destroy)
      button_close.pack(pady=10)
      
    # Abigail - developing or developed
    def action_dev():
      # creates new window 
      top = tk.Toplevel()
      top.geometry("600x600")
      top.title("Is Country Developed or Developing?")
      
      testinput = tk.Entry(top, width = 30)
      testinput.insert(0, "Enter country to check")
      testinput.pack(pady=10)
      # creates a label for country info
      
      label = tk.Label(top, text = "", font=('Arial', 14))

      
      # takes user input and checks to see if the country is developed or not
      # returns answer to the label
      def dev():
        deving_or_deved = irsys.developed_or_developing(testinput.get())
        country = testinput.get()
        
        if deving_or_deved == 0:
          label.config(text= country + " is a developing country")
        elif deving_or_deved == 1:
          label.config(text= country + " is a developed country")
          label.pack()
          
      button_developed = tk.Button(top, text = "Developed or Developing", command=dev)
      button_developed.pack(pady = 10)
  
      button_close = tk.Button(top, text = "Return to Menu", command=top.destroy)
      button_close.pack(pady = 10)

    # Abigail - max and min
    #finds the max and min for the indicator the user inputs
    def action_min():
      # creates new window 
      top = tk.Toplevel()
      top.geometry("600x600")
      top.title("Enter an  Indicator to find the Max and Min country values: ")
      
      testinput = tk.Entry(top, width = 30)
      testinput.insert(0, "")
      testinput.pack(pady=10)
      # creates a label for country info
      
      label = tk.Label(top, text = "", font=('Arial', 14))
      label1 = tk.Label(top, text = "", font=('Arial', 14))
      label2 = tk.Label(top, text = "", font=('Arial', 14))
      pass
      def min_max():
        indicator = testinput.get()
        min_max_list = irsys.min_and_max(testinput.get())

        label.config(text = "maximum and minimum for: " + indicator)
        label1.config(text = min_max_list[0] + " has the highest value of " + str(min_max_list[1]))
        label2.config(text = min_max_list[2] + " has the lowest value of " + str(min_max_list[3]))
        label.pack()
        label1.pack()
        label2.pack()

      button_min_max = tk.Button(top, text = "Search", command=min_max)
      button_min_max.pack(pady = 10)
  
      button_close = tk.Button(top, text = "Return to Menu", command=top.destroy)
      button_close.pack(pady = 10)
      
      
    
    # Label that has the title 'Menu'
    title = tk.Label(main_frame, text = "Menu", font=('Times New Roman', 18))
    
    # Jude - create the for load data on menu
    button_load = tk.Button(main_frame, text="Load Data", command=action_load)
   
    # Jude - create button for country list on menu
    button_list = tk.Button(main_frame, text="List Countries", command=action_list)

    # Jude - create button for country compare on menu
    button_compare = tk.Button(main_frame, text="Compare Countries", command = compare_country)

    # Abigail - create button for min and max on menu
    button_min_max = tk.Button(main_frame, text="Min and Max for Indicator", command = action_min)

    # create button for add country on menu
    button_add = tk.Button(main_frame, text="Add Country", command=action_add)

    # Abigail - create button for developed or developing on menu
    button_developed = tk.Button(main_frame, text="Is a Country Developed or Developing", command = action_dev)
    
    # Jude - create button for country remove on menu
    button_remove = tk.Button(main_frame, text="Remove Country", command=action_remove)
    
    # create button for country search on menu
    button_search = tk.Button(main_frame, text="Country Search", command=action_search)

    # Jude - create button for exit program on menu
    button_exit = tk.Button(main_frame, text="Exit Program", command=root.quit)

    # Jude - creates update message in the main menu (ex. "data loaded" or "countries listed")
    feedback = tk.Label(main_frame, text = "", font=('Arial', 18))
    
  
    # Jude - create the main menu button list
    def create_interface():
      title.pack(pady=10)
      button_load.pack(pady=10)
      button_list.pack(pady=10)
      button_compare.pack(pady=10)
      button_min_max.pack(pady=10)
      button_developed.pack(pady=10)
      button_add.pack(pady=10)
      button_remove.pack(pady=10)
      button_search.pack(pady=10)
      button_exit.pack(pady=10)
      feedback.pack(pady=10)
      
    create_interface()
    
    root.mainloop()

