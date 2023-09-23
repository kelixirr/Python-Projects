import zipfile, os

def backupToZip(folder):

  # backup the entire contents of the folder into a Zip file

  folder = os.path.abspath(folder)

  # figure out the filename this code should use
  number = 1
  while True:
    zipFilename = os.path.basename(folder) + '_' + str(number) + ' .zip'
    if not os.path.exists(zipFilename):
      break

    number = number + 1

    # create the Zip file. 
    print('Creating %s...' %(zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    
    # walk the entire folder tree and compress the files in each folder. 

    for foldername, subfolders, filenames in os.walk(folder):
      print('Adding files in %s...' %(foldername))

      #Add the current folder to the Zip file
      backupZip.write(foldername)

      # Add all the files in this folder to the Zip file.

      for filename in filenames:
        newBase = os.path.basename(folder) + '_'
        if filename.startswith(newBase) and filename.endswith('.zip'):
          continue

        backupZip.write(os.path.join(foldername, filename))

  backupZip.clos()
  print('Done')


