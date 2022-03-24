a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# è possibile assegnare un sottoinsieme di una lista a un altra direttamente nella dichiarazione
# <lista2> = [ (espressione che contiene <var>) for <var> in <lista> if <condizione> ] 
b:int =[even for even in a if even%2==0]

print(b)
