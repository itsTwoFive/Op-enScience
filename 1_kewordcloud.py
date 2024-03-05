import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def get_key_words(contenido: str) -> list:
    pos0 = contenido.find("<keywords>")
    pos1 = contenido.find("</keywords>")

    keywords = contenido[pos0:pos1]

    save_flag = False
    acount = 0
    current = ""

    keyword_list = []

    for c in keywords:
        if c == ">":
            acount+=1
        if acount == 2:
            save_flag = True
            acount = 0
        elif save_flag == True:
            if c == "<":
                save_flag = False
                keyword_list.append(current)
                current = ""
            else:
                current += c
    return keyword_list

keywords = []

ruta = "pdfsOut"
ficheros = os.listdir(ruta)
for fichero in ficheros:
    fp = open(ruta +"/"+fichero,encoding="utf8")
    conte = fp.read()
    keywords.extend(get_key_words(conte))

texto = " ".join(keywords)
wordcloud = WordCloud(width=1920,height=1080,background_color="white").generate(text=texto)

# plt.figure(figsize=(10, 5))
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis('off')
# plt.show()

wordcloud.to_file("wordcloud.png")

