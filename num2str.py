import sys

num=sys.argv[1]
print(num)
nlen=len(num)
print(nlen)
fflg=0

tempstr=8*['_']

#print(tempstr)

if num[nlen-1]==".":
  tempstr[7]="0"
  flg=2
else:
  tempstr[7]=num[nlen-1]
  flg=3
  
tempstr[6]="."

#if num[0]!="-"

if num[nlen-flg].isnumeric():
  tempstr[5]=num[nlen-flg]
elif num[nlen-flg]=="-":
  tempstr[4]="-"
  fflg=1
  
if nlen-flg-1==0:
  if num[0].isnumeric():
    tempstr[4]=num[0]
  elif num[0]=="-":
    tempstr[4]="_"
    tempstr[3]="-"

if nlen-flg-2==0:
  if num[0].isnumeric():
    tempstr[3]=num[0]
#  elif num[0]=="-":
#    tempstr[3]="_"
#    tempstr[2]="-"

print(num)

if nlen-flg-3==0:
  tempstr[4]=num[1]
#    tempstr[2]=num[1]
#  elif num[0]=="-":
#    tempstr[3]="_"
#    tempstr[2]="-"

print(tempstr)
