# Naming Files with American-Style Dates to European-Style Dates 

# create a regex for American Style Dates

import shutil, os, re

datePattern = re.compile(r"""^(.*?)
                         ((0|1)?\d)-
                         ((0|1|2|3)?\d)-
                         ((19|20)\d\d)
                         (.*?)$""", re.VERBOSE)

# identify the date parts from the filenames

# loop over the files in the working directory

for amerFilename in os.listdir('.'):

  mo = datePattern.search(amerFilename)

  #skip files without a date
  if mo == None:
    continue

  # get the different parts of the filename
  beforePart = mo.group(1)
  monthPart = mo.group(2)
  dayPart = mo.group(4)
  yearPart = mo.group(6)
  afterPart = mo.group(8)

  # form the European-style filename.
  euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

  # get the full, absolute file paths
  absWorkingDir = os.path.abspath('.')
  amerFilename = os.path.join(absWorkingDir, amerFilename)
  euroFilename = os.path.join(absWorkingDir, euroFilename)

  # rename the files 
  print('renaming "%s" to "%s"...' (amerFilename, euroFilename))
  #shutil.move(amerFilename, euroFilename) 


  