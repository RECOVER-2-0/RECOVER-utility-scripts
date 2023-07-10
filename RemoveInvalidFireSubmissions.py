'''
This script removes records from the Community Fire Submissions
hosted feature layer on ArcGIS Online. Fire shapes and attributes
will be permanently deleted if the creator of a shape does not 
provide a valid email address. The purpose of requiring a valid 
email address for fires submitted to RECOVER 2.0 is two-fold: 
    
    1. Allows a communication avenue between RECOVER 2.0
    maintainers and the post-wildfire decision-making 
    community
    2. Helps to prevent spam and therefore improves 
    RECOVER 2.0's automated data publishing processes

This script may include other criteria for a shape's exclusion 
from RECOVER 2.0. Those additional criteria will be listed here.
'''

# Libraries
from arcgis.gis import GIS 

# Connect to portal
username = input("Enter your username: ")
password = input("Enter your password: ")
portal = "http://www.arcgis.com"
print("Logging in to your portal...")

gis = GIS(portal, username, password)
me = gis.users.me
print(f"Success. Welcome, {me.firstName}.")
