import pyperclip, re

# create a regex for phone Numbers
phoneRegex = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?  # area code
                        (\s|-|\.)?       #separator 
                        (\d{3})          # first 3 digits
                        (\s|-|\.)        #separator
                        (\d{4})          # last 4 digits
                        (\s*(ext|x|ext.)\s*(\d{2,5}))            # extension

)''', re.VERBOSE)


# Create a Regex for Email Addresses
emailRegex = re.compile(r'''(
                        
                        [a-zA-Z0-9._%+-1]+   #username
                        @                    # @symbol
                        [a-zA-Z0-9.-]+       #domain name
                        (\.[a-zA-Z]{2,4})    #dot-something
)''', re.VERBOSE)

# fina all matches in the clipboard Text
text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
  phoneNum = '_'.join([groups[1], groups[3], groups[5]])
  if groups[8] != '':
    phoneNum += ' x' + groups[8]
  matches.append(groups[0])

for groups in emailRegex.findall(text):
  matches.append(groups[0])


# Join the matches into a string for the clipboard 
if len(matches) > 0:
  pyperclip.copy('\n'.join(matches))
  print('Copied to Clipboard:')
  print('\n'.join(matches))
  print(matches)

else:
  print('No phone numbers or email addresses found')