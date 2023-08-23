import pandas as pd

def get_OR_records():
    df = pd.read_csv("Wildland_Fire_Incident_Locations.csv", low_memory=False)
    df_clear = df[(df['POOState'] == 'US-OR') & (df['IncidentTypeCategory'] == 'WF')]
    df_column = df_clear[['X', 'Y', 'FireDiscoveryDateTime', 'InitialLatitude', 'InitialLongitude', 
                        'POOCounty', 'IncidentSize', 'FireCause']]
    df_column.to_csv("Oregon_Fire_Record.csv")



get_OR_records()