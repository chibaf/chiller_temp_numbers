import sys

num=sys.argv[1]
print(num)
nlen=len(num)
print(nlen)

tempstr=8*['_']

#print(tempstr)

if num[len(num)-1]==".":
  tempstr[7]="0"
  flg=0
else:
  tempstr[7]=num[len(num)-1]
  flg=1
  
tempstr[6]="."
  
if num[0]=="-":
  b0="-"
else:
  b0=""
  

print(tempstr)
