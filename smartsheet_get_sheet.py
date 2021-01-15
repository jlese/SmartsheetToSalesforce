"""
Created on Fri Jan 15 11:34:39 2021

@author: jackw

This code will scrape a file off of Smartsheet and format it for import into Salesforce as Task objects
"""


import smartsheet

"""Downloading the task trackers from Smartsheet"""
#%%
# Set smartsheet api access token
SMARTSHEET_ACCESS_TOKEN = 'z36xvbgxqmlwhy26ww8nqdhbc0'

#%%
# Create base client object
smartsheet_client = smartsheet.Smartsheet(SMARTSHEET_ACCESS_TOKEN)

#%%
# Find campaign task tracker folder in Smartsheet workspace
response = smartsheet_client.Workspaces.list_sheets(include_all=True)
sheets = response.data

#%%
# Add task tracker sheet id's to list
sheet_id_list = []
sub = 'Tracker'
for sheet in sheets:
    if sub in sheet.name:
        sheet_id_list.append(sheet.id)
    else:
        continue

#%%
# Download task trackers as .csv files
folder = "" # ENTER YOUR DESIRED DOWNLOAD LOCATION FOR THE FILES
for id in sheet_id_list:
    smartsheet_client.Sheets.get_sheet_as_csv(id, folder)

#%%
"""Formating the .csv files for import"""
