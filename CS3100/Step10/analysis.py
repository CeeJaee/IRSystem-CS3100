from CountryIRSystem import CountryIRSystem
from BSTCountryIRSystem import *
from hashCountryIRSystem import Country_htDict
from LLCountryIRSystem import Country_lldict
from SLCountryIRSystem import Country_SLDict
import time # importing the time to calcuate the time needed to run the queries
import random # generating random numbers


def country_inventory_analysis(rand_file_name, no_queries,no_entries):
    # rand_file_name: the name of the file containing the random data
    # no_queries: the number of queries to run on the system
    # no_entries: the max number of entries in the file
    # this function is responsible for including all the necessary code to analyze the performance of the system

    # Country inventory based on list
    #cinvent = CountryIRSystem()
    #cinvent.load_data(rand_file_name)
    
    # Country inventory based on the BSTDict
    #cinvent_bstdict = Country_BSTdict()
    #cinvent_bstdict.load_data(rand_file_name)

    # Country inventory based on the LLDict
    #cinvent_lldict = Country_lldict()
    #cinvent_lldict.load_data(rand_file_name)

    # Country inventory based on the SLDict
    cinvent_sldict = Country_SLDict()
    cinvent_sldict.load_data(rand_file_name)

    # Country inventory based on the HTDict
    #cinvent_htdict = Country_htDict()
    #cinvent_htdict.load_data(rand_file_name)
    
    #generating no_queries random queries 
    # using the random vin numbers
    random_vin_list = []
    for i in range(0,no_queries):
        n = random.randint(1, no_entries)
        random_vin_list.append(n)
    print("No of entries: "+ str(no_entries))
    '''
    #starting time calculation
    start_time = time.time()
    results1 = []
    #running the no_queries query search
    for rand_vin in random_vin_list:
      result = cinvent.country_search("Philippines"+str(rand_vin))
      results1.append(result)
    #calculating the time after the for loop
    end_time = time.time()
    # calculating how long it took to run the 1000 queries
    print("No of entries: "+ str(no_entries))
    print("searching " + str(no_queries) + " queries using the List based implementation: --- %s seconds ---" % (end_time - start_time))  
    
    # starting the time calculation for the BSTDict based implementation
    start_time2 = time.time()
    results2 = []
    #running the no_queries query search
    for rand_vin in random_vin_list:
      result = cinvent_bstdict.country_search("Philippines"+str(rand_vin))
      results2.append(result)
    #calculating the time after the for loop
    end_time2 = time.time()
    # calculating how long it took to run the 1000 queries
    print("searching " + str(no_queries) + " queries using the BST Dict based implementation: --- %s seconds ---" % (end_time2 - start_time2)) 
    
     # starting the time calculation for the LLDict based implementation
    start_time3 = time.time()
    results3 = []
    #running the no_queries query search
    for rand_vin in random_vin_list:
      result = cinvent_lldict.country_search("Philippines"+str(rand_vin))
      results3.append(result)
    #calculating the time after the for loop
    end_time3 = time.time()
    # calculating how long it took to run the 1000 queries
    print("searching " + str(no_queries) + " queries using the Linked List Dict based implementation: --- %s seconds ---" % (end_time3 - start_time3)) 
    '''
    # starting the time calculation for the SLDict based implementation
    start_time4 = time.time()
    results4 = []
    #running the no_queries query search
    for rand_vin in random_vin_list:
      result = cinvent_sldict.country_search("Philippines"+str(rand_vin))
      results4.append(result)
    #calculating the time after the for loop
    end_time4 = time.time()
    # calculating how long it took to run the 1000 queries
    print("searching " + str(no_queries) + " queries using the Sorted List Dict based implementation: --- %s seconds ---" % (end_time4 - start_time4))
    
    '''
    # starting the time calculation for the SLDict based implementation
    start_time5 = time.time()
    results5 = []
    #running the no_queries query search
    for rand_vin in random_vin_list:
      result = cinvent_htdict.country_search("Philippines"+str(rand_vin))
      results5.append(result)
    #calculating the time after the for loop
    end_time5 = time.time()
    # calculating how long it took to run the 1000 queries
    print("searching " + str(no_queries) + " queries using the Hash Table Dict based implementation: --- %s seconds ---" % (end_time5 - start_time5)) 
    '''