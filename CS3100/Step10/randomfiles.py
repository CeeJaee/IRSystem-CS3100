import random
import os
import csv

# Generating random data. The car information is not important, rather the car vin number needs to be unique
def generate_data_csv(rand_file_name, no_entries):
  # rand_file_name: the name of the random 
  # no_entries: the number of entries in the file
  
  file_name = "temp.csv" # temp file to hold the generated entries
  with open(file_name, 'w', encoding='UTF8', newline='') as f:
    writefile = csv.writer(f)
    for i in range(1, no_entries+1):
      country_name = "Philippines" + str(i)
      country_code = "PHI"
      agricultural_land = i
      access_to_electricity = i
      life_expectancy = i
      total_population = i
      labor_force = i
      GNI_per_capita = i
      row = [country_name, country_code, agricultural_land,access_to_electricity,life_expectancy,total_population,labor_force,GNI_per_capita]
      writefile.writerow(row)
   
  # randmize the entries in the file
  with open(file_name,'r', newline='') as source:
    csvreader = csv.reader(source)
    data = [ (random.random(), line) for line in csvreader ]
  data.sort()
  with open(rand_file_name,'w', newline='') as target:
    writefile = csv.writer(target)
    for _, line in data:
        writefile.writerow( line )

  # removing the temp file, not needed anymore
  os.remove(file_name)
