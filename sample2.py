a=str(input())
b='aeiouAEIOU'
if a.isalpha():
  if b.find(a):
    print "Vowels"
  else:
    print"Consonant"
else:
  print "invalid"
