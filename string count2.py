test_string=input("enter the string:")
l=[]
l=test_string.split()
wordfreq=[l.count(p)for p in l]
print(dict(zip(l,wordfreq)))

#in this pgm zip pairs the words given in string and it's count same as in dictionary
