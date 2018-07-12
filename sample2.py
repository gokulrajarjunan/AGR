a=input()
b=['a','e','i','o','u','A','E','I','O','U']
if a.isalpha():
  if a in b:
    print "Vowels"
  else:
    print"Consonant"
else:
  print "invalid"
