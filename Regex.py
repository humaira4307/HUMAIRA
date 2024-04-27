import re
text = "The rain in Spain"
x = re.search("^The.*Spain$", text)

if x:
  print("YES! We have a match!")
else:
  print("No match")
  
  
text = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", text)
print(x)

text = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\d", text)
print(x)

text = "hello planet"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", text)
print(x)

text = "mango planet"

#Check if the string starts with 'hello':

x = re.findall("^mangos", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
  
text = "hello planet world"

#Check if the string ends with 'planet':

x = re.findall("planet$", text)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")
  
text = "hellcffgfo planet"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall("he.*o", txt)

print(x)

text = "heo planet"

#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

x = re.findall("he.+o", text)

print(x)

text = "hellhho planet"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.findall("he.{4}o", text)

print(x)

text = "The rain in Spain fallses mainly in the plain!"

#Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", text)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  
text = "The rain in Spain 125 take care"

#Return a match at every no-digit character:

x = re.findall("\D", text)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
 
text = "The rain in Spain"

#Return a match at every white-space character:

x = re.findall("\s", text)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
 
text = "The rain in Spain"

#Return a match at every NON white-space character:
