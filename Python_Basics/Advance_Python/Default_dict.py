
from collections import defaultdict 

# Function to return a default 
# values for keys that is not 
# present 
def def_value(): 
	return "Not Present"
	
d = defaultdict(def_value) 
d["a"] = 1
d["b"] = 2

print(d["a"]) 
print(d["b"]) 
print(d["c"]) 
