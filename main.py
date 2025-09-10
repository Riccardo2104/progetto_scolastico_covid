import matplotlib.pyplot as plt
import requests
import json
datas = json.loads(requests.get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json").text)
data = [] #array

print(f"""
-----------------------------------------COVID-VISUALIZZER------------------------------------
                                      Made by Riccardo Viganò

    Positivi / positivi: Restituisce il grafico dei positivi in italia del covid
    CasiTotali / casitotali: Resitutisce il grafico del totale dei casi
    Tamponi: Resitutisce il grafico dei tamponi eseguiti in italia
    TerapiaIntensiva: Resitutisce il grafico del totale delle persone in terapia intensiva
    Deceduti / deceduti: Resitutisce il grafico del totale delle persone in decedute per Covid
                          ULTIMO AGGIORNAMENTO DEI DATI: {datas[-1]['data']}  
""")

input = input("Inserisci cosa vuoi visualizzare> ")


if input == "positivi" or input == "Positivi":    
    for i in datas:
        data.append(int(i["totale_positivi"])) 
elif input == "casitotali" or input == "CasiTotali":
    for i in datas:
        data.append(int(i["totale_casi"]))
elif input == "Tamponi" or input == "tamponi":
    for i in datas:
        data.append(int(i["tamponi"]))
elif input == "terapiaintensiva" or input == "TerapiaIntensiva":
    for i in datas:
        data.append(int(i["terapia_intensiva"]))
elif input == "deceduti" or input == "Deceduti":
    for i in datas:
        data.append(int(i["deceduti"]))
else:
    print("Commando non riconosciuto")
    exit(0)
plt.plot(data) #meotodo che usiamo per poter creare il plto
plt.show()  #meotodo per crearte l'imGFINE