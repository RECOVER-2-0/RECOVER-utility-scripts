'''
Script written by Michael Ennis, ISU and Keith Weber, ISU GIS TReC

Cole Rosner 04 Apr 2023 - Merged CopyLayerFilesToFireFolders.py with fireZip.py
                          to make CopyZipShip.py
'''
# Libraries
import shutil
import os
import subprocess

# Get current directory
directory = os.getcwd()

# Get path to directory of files to be copied 
copyDir = os.path.join(directory, "CopyToEachFIREFolder")

# Counter for how many folders zipped
zipCount = 0
# Iterate over current directory
for filename in os.listdir(directory):
    # If the folder starts with "Fire_" and doesn't end with "zip", zip it
    if(filename.startswith("Fire_") and not (filename.endswith("zip"))):
        
        # Check if folder already has the files that need to be copied inside of it
        for file in os.listdir(copyDir):
            if os.path.isfile(os.path.join(filename, file)):
                pass # Do nothing, as the file already exists
            else:
                srcPath = os.path.join(copyDir, file)
                dstPath = os.path.join(filename, file)
                shutil.copy(srcPath, dstPath)
                # print("Copied {} to the {} folder.".format(file, filename))

        
        shutil.make_archive(filename,'zip', filename)
        # Increment the zip count
        zipCount+=1
        #print(filename, "zipped!")
print(zipCount, "fire folders zipped!")

subprocess.call([r'MoveZIPS_toServer.bat'])
print("zip files moved to server successfully")
