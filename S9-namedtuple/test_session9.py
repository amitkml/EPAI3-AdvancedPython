# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 18:04:27 2021

@author: AKayal
"""
import session9
from session9 import *
from datetime import datetime
import pytest
from io import StringIO 
import sys
import time
import inspect
import os
import re

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100, "Make your README.md file interesting! Add atleast 100 words"
    

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session8, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def calculate_random_profile_info_named_tuple_tc():
    
    """
    This function is the test case repo calculate_random_profile_info  and it has following 5 test cases to execute

    Returns
    -------
    assert error or success.

    """
    value_namedtuple = calculate_random_profile_info(no=10000)()
    assert len(value_namedtuple) == 4
    assert any(["largest_blood_type" in o for o in list(value_namedtuple.keys())])
    assert any(["mean_current_location" in o for o in list(value_namedtuple.keys())])
    assert any(["oldest_person_age" in o for o in list(value_namedtuple.keys())])
    assert any(["average_age" in o for o in list(value_namedtuple.keys())])
    assert (value_namedtuple['largest_blood_type']) > 0
    assert (value_namedtuple['mean_current_location']) > 0
    assert (value_namedtuple['oldest_person_age']) > 0
    assert (value_namedtuple['average_age']) > 0  

def calculate_random_profile_info_dictionary_tc():
    
    """
    This function is the test case repo calculate_random_profile_info  and it has following 5 test cases to execute

    Returns
    -------
    assert error or success.

    """
    value_namedtuple = calculate_random_profile_info(no=10000, convert_nmd_tuple = False)()
    assert len(value_namedtuple) == 4
    assert any(["largest_blood_type" in o for o in list(value_namedtuple.keys())])
    assert any(["mean_current_location" in o for o in list(value_namedtuple.keys())])
    assert any(["oldest_person_age" in o for o in list(value_namedtuple.keys())])
    assert any(["average_age" in o for o in list(value_namedtuple.keys())])
    assert (value_namedtuple['largest_blood_type']) > 0
    assert (value_namedtuple['mean_current_location']) > 0
    assert (value_namedtuple['oldest_person_age']) > 0
    assert (value_namedtuple['average_age']) > 0  
    
def calculate_share_market_profile_tc():
    
    """
    This function is the test case repo for calculate_share_market_profile and it has following 11 test cases to execute

    Returns
    -------
    assert error or success.

    """
    value_dic_stockmarket, dlist = calculate_share_market_profile(no=100)()
    assert len(value_dic_stockmarket) == 3
    assert any(["starting_weighted_price" in o for o in list(value_dic_stockmarket.keys())])
    assert any(["max_weighted_price" in o for o in list(value_dic_stockmarket.keys())])
    assert any(["close_weighted_price" in o for o in list(value_dic_stockmarket.keys())])
    assert (value_dic_stockmarket['starting_weighted_price']) > 0
    assert (value_dic_stockmarket['max_weighted_price']) > 0
    assert (value_dic_stockmarket['close_weighted_price']) > 0
    assert (value_dic_stockmarket['close_weighted_price']) > 0
    assert (dlist.shape[0]) == 100 ## checking if we have 100 company data
    assert any(["company" in o for o in dlist.columns]) ## validating company feature
    assert any(["symbol" in o for o in dlist.columns]) ## validating symbol feature
    assert any(["open" in o for o in dlist.columns]) ## validating open feature
    assert any(["high" in o for o in dlist.columns]) ## validating high feature
    assert any(["close" in o for o in dlist.columns]) ## validating close feature
    assert any(["weight" in o for o in dlist.columns]) ## validating weight feature