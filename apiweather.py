import requests   #requests importieren, um API Call machen zu können

while True:
  api_key  = "9fc8725604d441d74052f9c278620d77"  #API Key definieren
  city = input("Von welcher Stadt möchtest du das Wetter abfragen?: ")  #Stadt wird abgefragt und gespeichert
  url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"  #API mit verlangten Variablen; "f" um anzuzeigen, dass Variablen in URL sind; "&units=metric" für richtige Einheiten


  data = requests.get(url).plain()  #Get Request wird durchgeführt und in json formatiert
  status = requests.get(url)

  print(data)

  if status.status_code == 200:

     average_temperature = data["main"]["temp"]    #Einzelne Informationen, die ich haben möchte werden formatiert/ isoliert
     min_temperature = data["main"]["temp_min"]
     max_temperature = data["main"]["temp_max"]
     humidity = data["main"]["humidity"]
     wind_speed = data["wind"]["speed"]
     wind_temperature = data["wind"]["deg"]

     print("Hier sind die aktuellen Wetterwerte von " + city + ".")                #Alle Informationen werden entsprechend angezeigt
     print("Durchschnittstemperatur: " ,average_temperature, "°C")
     print("Mindesttemperatur:" ,min_temperature, "°C")
     print("Höchsttemperatur:" ,max_temperature, "°C")
     print("Luftfeuchtigkeit:" ,humidity,"%")
     print("Windgeschwindigkeit:" ,wind_speed, "km/h")
     print("Windtemperatur:" ,wind_temperature, "°C")

        
     print("")
     print("Um eine weite Stadt zu nenen, tippe 'weiter'")
     print("Um das Programm zu verlassen, tippe 'schließen'.")
     user_chice_2 = input("Eingabe: ")

     if user_chice_2 == "schließen":
        break
     
     else:
        continue
        


  else:
     print("Es konnte leider keine Verbindung hergestellt werden.")
     print("Bitte überprüfe, ob die Stadt richtig geschrieben wurde.")
     continue






