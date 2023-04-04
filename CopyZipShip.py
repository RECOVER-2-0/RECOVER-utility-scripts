import shutil
import os
import subprocess

# Script written by Michael Ennis, ISU and Keith Weber, ISU GIS TReC
# Get current directory
directory = os.getcwd()
# Counter for how many folders zipped
zipCount = 0
# Iterate over that directory
for filename in os.listdir(directory):
    # If the folder starts with "Fire_" and doesn't end with "zip", zip it
    if(filename.startswith("Fire_") and not (filename.endswith("zip"))):
        shutil.make_archive(filename,'zip', filename)
        # Increment the zip count
        zipCount+=1
        #print(filename, "zipped!")
print(zipCount, "fire folders zipped!")

subprocess.call([r'MoveZIPS_toServer.bat'])
print("zip files moved to server successfully")