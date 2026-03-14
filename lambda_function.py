import requests
import json
import pandas as pd

def lambda_handler(event,context):
    
    print("event data->",event)
    
    response=response.get("https://www.google.com/")
    
    print(response.text)
    
    d={
        'col1':[1,2],
        'col2':[3,2]
        
    }
    
    df=pd.DataFrame(data=d)
    
    print(df)
    
    print("demo completed")
    