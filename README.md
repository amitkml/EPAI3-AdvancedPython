# Assignment Details

- Use the Faker (Links to an external site.)library to get 10000  random profiles. Using namedtuple, calculate the largest blood type,  mean-current_location, oldest_person_age, and average age (add proper  doc-strings). - 250 (including 5 test cases)
- Do the same thing above using a dictionary. Prove that namedtuple is faster. - 250 (including 5 test cases)
- Create fake data (you can use Faker for company names) for imaginary  stock exchange for top 100 companies (name, symbol, open, high, close).  Assign a random weight to all the companies. Calculate and show what  value the stock market started at, what was the highest value during the  day, and where did it end. Make sure your open, high, close are not  totally random. You can only use namedtuple. - 500  (including 10 test  cases)
- Once done, share a public link to your repo where we can find the  notebook, python files, readme file, and GitHub Actions executed.

## calculate_random_profile_info - namedtuple

This function has following logic

- Define a Faker object

- defined a namedtuple to store in decorator function

  - largest_blood_type
  - mean_current_location
  - oldest_person_age
  - average_age 

- Decorator function then ran loop for 10000 times to generate a faker object and inserted them into list. Faker object being created for selected column only.

  - Calculated age (days) by finding out day difference between DOB and current date
  - latitude and longitude being taken from tuple current_location and stored in separate key 

- It then been converted into dataframe

- Inner function then being called with following logic

  - dataframe max function being called on age column to find out max age
  - mean function being called on latitude and longitude column to find out mean location and then being converted into location
  - namedtuple then being created with these values as shown below which is then returned from inner function

  ```
  profile_info_summary = faker_profile(largest_blood_type,
                                               mean_current_location,
                                               oldest_person_age_days,
                                               avg_age_days)
  ```

  

  ## calculate_random_profile_info-dictionary

  

  This function has following logic

  - Define a Faker object
  - defined a dictionary to store in decorator function
    - largest_blood_type
    - mean_current_location
    - oldest_person_age
    - average_age 
  - Decorator function then ran loop for 10000 times to generate a faker object and inserted them into list. Faker object being created for selected column only.
    - Calculated age (days) by finding out day difference between DOB and current date
    - latitude and longitude being taken from tuple current_location and stored in separate key 
  - It then been converted into dataframe
  - Inner function then being called with following logic
    - dataframe max function being called on age column to find out max age
    - mean function being called on latitude and longitude column to find out mean location and then being converted into location
    - dictionary then being populated with these values as shown below which is then returned from inner function

## calculate_share_market_profile

This function has following logic

- Define a Faker object to get 100 company name
- generated randomly symbol for each of the company
- generated randomly open, high, close and weight for each of the company randomly as shared below.

```
        a_dictonary.update(fake.profile(fields=['company']))
        a_dictonary['symbol'] = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 4))
        a_dictonary['open'] = int(''.join(random.sample(string.digits, 5)))
        a_dictonary['high'] = int(''.join(random.sample(string.digits, 5)))
        a_dictonary['close'] = int(''.join(random.sample(string.digits, 5)))
        a_dictonary['weight'] = random.uniform(0, 1)
```

- It is then being converted into dataframe

- Inner function then being called with following logic

  - a tuple being defined to get values of market high, starting and closing

  ```
          nonlocal stock_market_stats
          nonlocal stock_market_df
          stock_market_stats_profile = stock_market_stats(sum([row-1 for row in stock_market_df['open']*stock_market_df['weight']]),
                                                  sum([row-1 for row in stock_market_df['high']*stock_market_df['weight']]),
                                                  sum([row-1 for row in stock_market_df['close']*stock_market_df['weight']])                                                
                                                  )     
  ```

  

# Referenced Article for github action

- [Automate Python Testing With GitHub Actions](https://medium.com/swlh/automate-python-testing-with-github-actions-7926b5d8a865)