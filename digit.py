import math 
  
def countDigit(n): 
    return math.floor(math.log10(n)+1 )
  
n = 8411079284
print ("Number of digits : ",countDigit(n)) 
