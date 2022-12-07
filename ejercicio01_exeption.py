lista=[1,2,3,4,5,6]

try:
    print(lista[9])
except Exception as e:
    #print("error elemento de la lista")    
    print(e)
    
try:
    print(lista[1])
except Exception as e:
    #print("error elemento de la lista")    
    print(e)
else:
    print("funciono correctamente")
    
  
#################
try:
    print(lista[122])
except Exception as e:
    #print("error elemento de la lista")    
    print(e)
else:
    print("funciono correctamente")
finally:
    print("siempre se ejecuta")