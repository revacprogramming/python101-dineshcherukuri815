score = input( 'Enter Score' )
s =float(score)
a =  'error'
if s >= 0.9:
  a='A'
elif s >= 0.8:
    a='B'
elif s >= 0.7:
    a = 'C'
elif s < 0.6:
    a = 'D' 
elif s < 0.6:
   a='F'
else:
  a ="out of range"
print(a)