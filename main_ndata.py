from num2str_class import num2str  # get measurement temperature
import sys

tmpstr=num2str()  # tempersature in 8 length str
print(tmpstr.tdata(sys.argv[1]))
