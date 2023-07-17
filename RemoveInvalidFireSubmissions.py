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

# Connect to portal and log in
username = input("Enter your username: ")
password = input("Enter your password: ")
portal = "http://www.arcgis.com"
print("Logging in to your portal...")

gis = GIS(portal, username, password)
me = gis.users.me
print(f"Success. Welcome, {me.firstName}.")

# Find Community Fire Submissions feature layer
fsLayer = gis.content.get('9a36d150d6b7441ba5cd9b0d21fd24b0').layers[0] # get Community Fire Submissions using item ID, and grab the layer that makes up the item
fsFeatSet = fsLayer.query(where="Email_Val='Invalid'")
fsFeatures = fsFeatSet.features
print(f"Found {len(fsFeatures)} fires with invalid email addresses. Proceeding to delete...")
for each in range(len(fsFeatures)):
    oidStr = str(fsFeatures[each].get_value('OBJECTID'))
    subfireName = fsFeatures[each].get_value('Fire_Name')
    delResult = fsLayer.edit_features(deletes = oidStr)
    print(f"Deleting {subfireName}.")
    delResult

print("Finished removing invalid fires from the Community Fire Submissions hosted feature layer.")
