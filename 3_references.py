import os
import re

def get_title(linea):
    save_flag = False
    current = ""
    for c in linea:
        if c == ">":
            save_flag = True
        elif save_flag and c=="<":
            break
        elif save_flag:
            current +=c
    return current

def get_full_name(linea):
    name = ""
    save_flag = False
    for c in linea:
        if c == ">":
            save_flag = True
        elif save_flag and c=="<":
            save_flag = False
        elif save_flag:
            name +=c
            
    name_split = re.findall('[A-Z][^A-Z]*', name)
    name_final = ""
    
    for elem in name_split:
        name_final+=elem+" "
        
    return name_final.strip()
    
def crear_referencia(lista):
    ref = ""
    i = len(lista)-1
    while i>=0:
        ref+=lista[i][:-1]
        if i >0:
            ref+=", "
        else:
            ref+="."
        i-=1
    return ref

ruta = "pdfsOut"
ficheros = os.listdir(ruta)

out = open("paper_references.txt","wt",encoding="utf8")
out.write("Paper References\n")
out.write("-"*100)
out.write("\n")

for fichero in ficheros:
    fp = open(ruta +"/"+fichero,encoding="utf8")
    nombre = (fichero[:-len(".grobid.tei.xml")]+".pdf")
    out.write("\n")
    out.write("-"*100)
    out.write("\n\n")
    out.write(f"Fichero {nombre}:\n\n")
    
    new_entry = []
    is_bio_flag = False
    for linea in fp:
        if linea.count("<biblStruct") > 0:
            is_bio_flag = True
        elif is_bio_flag:
            if linea.count('<title level="a"') + linea.count('<title level="m"') >0:
                new_entry.insert(0,get_title(linea))
            elif linea.count('<persName>') >0:
                new_entry.append(get_full_name(linea))
            elif linea.count('</biblStruct>'):
                is_bio_flag = False
                out.write(f"\t{crear_referencia(new_entry)}\n")
                new_entry = []
    