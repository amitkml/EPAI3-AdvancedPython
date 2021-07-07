# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 11:53:11 2021 for Assignment 9 on namedtuple

@author: AKayal
"""
from decimal import *

def calculate_random_profile_info(no=10000,
                                  convert_nmd_tuple = True):
    """
    This function will call the Faker library to get 10000 random profiles. It will then using namedtuple, 
    will calculate the largest blood type, mean-current_location, oldest_person_age, and average age. 

    Returns
    -------
    calculate_stats through closure.

    """
    no = no
    from faker import Faker
    import collections
    from collections import namedtuple
    from datetime import date
    
    import pandas as pd
    
    Faker.seed(0)
    fake = Faker()
    
    dlist = []
    faker_profile = namedtuple('faker_profile',['largest_blood_type',
                                               'mean_current_location',
                                               'oldest_person_age',
                                               'average_age']) ## defining the namedtuple here with default assignment
    #fake_profile = fake.profiles()
    #profile_info_nt = faker_profile(0,0,0,0) ## initializing the object
    faker_profile_dictionary = {} ## declaring this
    convert_nmd_tuple = convert_nmd_tuple
    for _ in range(no):
        profile_dictonary = {}
        profile_dictonary.update(fake.profile(fields=['job','blood_group','current_location','birthdate']))
        profile_dictonary['age'] = (date.today() - profile_dictonary['birthdate']).days
        lat, long = profile_dictonary['current_location']
        profile_dictonary['lat'] = float(lat)
        profile_dictonary['long'] = float(long)
        dlist.append(profile_dictonary)
    
    profile_df = pd.DataFrame.from_dict(dlist) ## converting into dataframe
    
    def calculate_stats():
        """
        This function will refer the namedtuple earlier and faker data to calculate stats
        -------
        calculate_stats.
        """
        nonlocal convert_nmd_tuple
        
        oldest_person_age_days = max(profile_df['age'])
        avg_age_days = profile_df['age'].mean()
        mean_current_location = profile_df['lat'].mean(),profile_df['long'].mean()
        largest_blood_type = profile_df['blood_group'].value_counts().idxmax()
        profile_info_summary = faker_profile(largest_blood_type,
                                             mean_current_location,
                                             oldest_person_age_days,
                                             avg_age_days)
        # print(f"Faker profile info return from Closure:{faker_profile}")
        
        faker_profile_dictionary_temp = profile_info_summary._asdict()
        faker_profile_dictionary=dict(faker_profile_dictionary_temp)
        
        if (convert_nmd_tuple):
            return profile_info_summary
        else:
            return faker_profile_dictionary
        
    return calculate_stats

value = calculate_random_profile_info()()
print(f"Faker profile namedtuple output:{value}")


value_dic = calculate_random_profile_info(convert_nmd_tuple = False)()
print(f"Faker profile dictionary output:{value_dic}")
        

def calculate_share_market_profile(no=100):
    """
    This function will call the Faker library to get 500 company name. It will then generate random number for high, low and close figures in share market for these shares
    The company profile has been generated from random string also. Then the inner function calculate the market stats and return through closure. 

    Returns
    -------
    calculate_stats.

    """
    no = no
    from faker import Faker
    import collections
    from collections import namedtuple
    from datetime import date
    import string
    import random
    import pandas as pd
    
    Faker.seed(0)
    fake = Faker()
    
    dlist = []
    stock_market_stats = namedtuple('stock_market_stats',['starting_weighted_price',
                                               'max_weighted_price',
                                               'close_weighted_price']) ## defining the namedtuple here with default assignment

    #fake_profile = fake.profiles()
    #profile_info_nt = faker_profile(0,0,0,0) ## initializing the object
    faker_profile_dictionary = {} ## declaring this
    
    for _ in range(no):
        a_dictonary = {}
        a_dictonary.update(fake.profile(fields=['company']))
        a_dictonary['symbol'] = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 4))
        a_dictonary['open'] = int(''.join(random.sample(string.digits, 5)))
        a_dictonary['high'] = int(''.join(random.sample(string.digits, 5)))
        a_dictonary['close'] = int(''.join(random.sample(string.digits, 5)))
        a_dictonary['weight'] = random.uniform(0, 1)
        dlist.append(a_dictonary)

    stock_market_df = pd.DataFrame.from_dict(dlist) ## converting into dataframe
    
    def calculate_market_stats():
        """
        This function will refer the namedtuple earlier and faker data to calculate stats
        -------
        calculate_stats.
        """
        nonlocal stock_market_stats
        nonlocal stock_market_df
        stock_market_stats_profile = stock_market_stats(sum([row-1 for row in stock_market_df['open']*stock_market_df['weight']]),
                                                sum([row-1 for row in stock_market_df['high']*stock_market_df['weight']]),
                                                sum([row-1 for row in stock_market_df['close']*stock_market_df['weight']])                                                
                                                )     
      
        stock_market_stats_profile_temp = stock_market_stats_profile._asdict()
        stock_market_stats_profile_dic = dict(stock_market_stats_profile_temp)
        return stock_market_stats_profile_dic

        
    return calculate_market_stats


value_dic_stockmarket = calculate_share_market_profile()()
print(f"Stock market daily status:{value_dic_stockmarket}")
      