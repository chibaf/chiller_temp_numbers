from stemp_class import stemp  # get setting temperature
from mtemp_class import mtemp  # get measurement temperature

temp=stemp()  # get setting temperature
print(temp.get())

temp=mtemp() # get measurement temperature
print(temp.get())