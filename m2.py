# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:16:31 2024

@author: JJayanetti
"""
# import os
# token = os.environ.get('token')  # use my token in API calls
# print(f"Token: {token}")  # adding this for debugging

# importing os module  
# import os 
# import pprint 
  
# # Get the list of user's 
# env_var = os.environ 
  
# # Print the list of user's 
# print("User's Environment variable:") 
# pprint.pprint(dict(env_var), width = 1)

# importing os module  
# import os 

# # 'HOME' environment variable 
# home = os.environ['HOME'] 
  
# print("HOME:", home) 
   
# # 'JAVA_HOME' environment variable 
# java_home = os.environ.get('JAVA_HOME') 
  
# # 'JAVA_HOME' environment variable 
# print("JAVA_HOME:", java_home) 

def update_url(url):

    # example url = [~GNN]: https://img.shields.io/badge/GNN-0-E6A2A3

    # split the urls into parts
    parts = url.split("-")
    # parts = ["[~GNN]: https://img.shields.io/badge/GNN", "0", "E6A2A3"]


    # get the part of the string that contains the label
    label_string = str(parts[0])
    print(label_string)


update_url("https://img.shields.io/badge/GNN-0-E6A2A3")
