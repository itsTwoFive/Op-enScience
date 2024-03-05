import os

ruta = "pdfsOut"
ficheros = os.listdir(ruta)

print("Number of figures per file")
print("-"*55)
total = 0

for fichero in ficheros:
    fp = open(ruta +"\\"+fichero,encoding="utf8")
    conte = fp.read()
    numero_fig = conte.count("<figure")
    total += numero_fig
    nombre = (fichero[:-len(".grobid.tei.xml")]+".pdf").ljust(45)
    print(f"{nombre} ==> {numero_fig}")
    
print("-"*55)
print(f"{'Total number of figures'.ljust(45)} ==> {total}")