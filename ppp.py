import nasdaqdatalink
import pandas as pd
import json
import urllib.request
import pygal 

nasdaqdatalink.ApiConfig.api_key = '9vyxTwK9YbUPgpa3ZdBm'

def get_data():
    
   
########################################The big mac index for canada#################################################################
    data_list = []#open an empty list
   
    
    data = nasdaqdatalink.get(f'ECONOMIST/BIGMAC_CAN', start_date='2021-01-31', end_date='2022-01-31')

   
        
    url = 'https://restcountries.com/v3.1/alpha/CAN'
    request = urllib.request.urlopen(url)
    result = json.loads(request.read())
    #print(result)
    
    number = float(round(data.iloc[0,3],2))
    print(number, type(number))
    burger = "🍔" * (int(number))#How many hamburgers 
    burger_no = 1 * (int(number))
  
  
    country = {
    "burger_no":burger_no,
    "burger":burger,
    "local_price": round(data.iloc[0,0],2),
    "dollar_ex": round(data.iloc[0,1],2),
    "dollar_price": round(data.iloc[0,2],2),
    "dollar_ppp": round(data.iloc[0,3],2),
    "dollar_valuation":round(data.iloc[0,4],2),
    "dollar_adj_valuation":round(data.iloc[0,5],2),
    "flag":result[0]["flags"]["png"],
    "country_name":result[0]["name"]["common"],
    "currencies":result[0]["currencies"],
    }
    data_list.append(country)

    
    print(data_list[0]["burger"])


    ############################################The big mac index for Mexico############################################
    data_list1 = []
   
    
    data = nasdaqdatalink.get(f'ECONOMIST/BIGMAC_MEX', start_date='2021-01-31', end_date='2022-01-31')

   
        
    url = f'https://restcountries.com/v3.1/alpha/MEX'
    request = urllib.request.urlopen(url)
    result = json.loads(request.read())
    #print(result)
    
    number = float(round(data.iloc[0,3],2))
    print(number, type(number))
    burger = "🍔" * (int(number))#How many hamburgers 
    burger_no = 1 * (int(number))#Number of hamburgers
  
  
    country = {
    "burger_no":burger_no,
    "burger":burger,
    "local_price": round(data.iloc[0,0],2),
    "dollar_ex": round(data.iloc[0,1],2),
    "dollar_price": round(data.iloc[0,2],2),
    "dollar_ppp": round(data.iloc[0,3],2),
    "dollar_valuation":round(data.iloc[0,4],2),
    "dollar_adj_valuation":round(data.iloc[0,5],2),
    "flag":result[0]["flags"]["png"],
    "country_name":result[0]["name"]["common"],
    "currencies":result[0]["currencies"],
    }
    data_list1.append(country)

    
    print(data_list1[0]["burger"])

  #########################################The big mac index for Japan###################################################
    data_list2 = []
   
    
    data = nasdaqdatalink.get(f'ECONOMIST/BIGMAC_JPN', start_date='2021-01-31', end_date='2022-01-31')

   
        
    url = f'https://restcountries.com/v3.1/alpha/JPN'
    request = urllib.request.urlopen(url)
    result = json.loads(request.read())
    #print(result)
    
    number = float(round(data.iloc[0,3],2))
    print(number, type(number))
    burger = "🍔" * (int(number)) #How many hamburgers 
    burger_no = 1 * (int(number)) #Numbers of hamburgers
  
  
    country = {
    "burger_no":burger_no,
    "burger":burger,
    "local_price": round(data.iloc[0,0],2),
    "dollar_ex": round(data.iloc[0,1],2),
    "dollar_price": round(data.iloc[0,2],2),
    "dollar_ppp": round(data.iloc[0,3],2),
    "dollar_valuation":round(data.iloc[0,4],2),
    "dollar_adj_valuation":round(data.iloc[0,5],2),
    "flag":result[0]["flags"]["png"],
    "country_name":result[0]["name"]["common"],
    "currencies":result[0]["currencies"],
    }
    data_list2.append(country)

    
    print(data_list2[0]["burger"])

  ###################################################The big mac index for china##################################################
    data_list3 = []
   
    
    data = nasdaqdatalink.get(f'ECONOMIST/BIGMAC_CHN', start_date='2021-01-31', end_date='2022-01-31')

   
        
    url = f'https://restcountries.com/v3.1/alpha/CHN'
    request = urllib.request.urlopen(url)
    result = json.loads(request.read())
    #print(result)
    
    number = float(round(data.iloc[0,3],2))
    print(number, type(number))
    burger = "🍔" * (int(number))#How many hamburgers 
    burger_no = 1 * (int(number))#Numbers of hamburgers 
    #print(burger_no)
  
  
    country = {
    "burger_no":burger_no,
    "burger":burger,
    "local_price": round(data.iloc[0,0],2),
    "dollar_ex": round(data.iloc[0,1],2),
    "dollar_price": round(data.iloc[0,2],2),
    "dollar_ppp": round(data.iloc[0,3],2),
    "dollar_valuation":round(data.iloc[0,4],2),
    "dollar_adj_valuation":round(data.iloc[0,5],2),
    "flag":result[0]["flags"]["png"],
    "country_name":result[0]["name"]["common"],
    "currencies":result[0]["currencies"],
    }
    data_list3.append(country)

    
    print(data_list3[0]["burger"])
    
  #making a chat for burger
    bar_chart = pygal.HorizontalBar()
    bar_chart.title = 'Compariing Number of Hamburgers'
    bar_chart.add(data_list[0]["country_name"], data_list[0]["burger_no"])
    bar_chart.add(data_list1[0]["country_name"], data_list1[0]["burger_no"])
    bar_chart.add(data_list2[0]["country_name"], data_list2[0]["burger_no"])
    bar_chart.add(data_list3[0]["country_name"], data_list3[0]["burger_no"])
    bar_chart.render_to_file('static/img/bar_chart.svg') 
    
    
        
    
    return data_list,data_list1,data_list2,data_list3
