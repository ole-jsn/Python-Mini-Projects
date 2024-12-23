import requests

url = "https://www.passwordrandom.com/query?command=password"

print("Willkommen beim Password Ninja!")
print("Wir beraten dich, für deine ideale Password Sicherheit!")
input_password = input("Dein aktuelles Passwort: ")

def crack_password(password):
    length_password = len(password)
    available_characters = 94
    available_password_options = available_characters ** length_password
    attempts_per_second = 10**9
    cracking_time = available_password_options / attempts_per_second
    return cracking_time

def cracking_time(time_in_seconds):
    if time_in_seconds < 60:
        return time_in_seconds, "Sekunden"
    if time_in_seconds < 3600:
        return time_in_seconds / 60, "Minuten"
    if time_in_seconds < 86400:
        return time_in_seconds / 3600, "Stunden"
    if time_in_seconds < 2592000:
        return time_in_seconds / 86400, "Tage"
    return time_in_seconds / 2592000, "Jahre"

def fetch_secure_password():
    try:
        response = requests.get(url)
        return response.text
    
    except:
        Fehler = "Leider ist ein Fehler aufgetreten..."
        return Fehler
 

if input_password.isdigit():
    print("Dein Passwort enthält nur Zahlen.")
    print("Du solltest unbedingt auf eine Kombination aus Zahlen, Buchstaben und Sonderzeichen achten.")
    new_password = fetch_secure_password()
    time_in_seconds = crack_password(new_password)
    time, unit = cracking_time(time_in_seconds)
    if new_password and time_in_seconds and time and unit:
        print(f"Hier wäre ein neues, sicheres Passwort: {new_password}")
        print(f"Ein Hacker mit einem leistungsstarken PC bräuchte im Schnitt {time:.2f} {unit}, um dein Passwort zu knacken.")

elif input_password.isalpha():
    print("Dein Passwort enthält nur Buchstaben.")
    print("Du solltest unbedingt auf eine Kombination aus Zahlen, Buchstaben und Sonderzeichen achten.")
    new_password = fetch_secure_password()
    time_in_seconds = crack_password(new_password)
    time, unit = cracking_time(time_in_seconds)
    if new_password and time_in_seconds and time and unit:
        print(f"Hier wäre ein sicheres Passwort: {new_password}")
        print(f"Ein Hacker mit einem leistungsstarken PC bräuchte im Schnitt {time:.2f} {unit}, um dein Passwort zu knacken.")

else:
    time_in_seconds = crack_password(input_password)
    time, unit = cracking_time(time_in_seconds)
    print(f"Ein Hacker mit einem leistungsstarken PC bräuchte im Schnitt {time:.2f} {unit}, um dein Passwort zu knacken.")

    if unit == "Sekunden" or unit == "Minuten" or unit == "Stunden":
        print("Du solltest lieber ein neues Password wählen...")
        new_password = fetch_secure_password()
        time_in_seconds = crack_password(new_password)
        time, unit = cracking_time(time_in_seconds)
    if new_password and time_in_seconds and time and unit:
        print(f"Hier wäre ein sicheres Passwort: {new_password}")
        print(f"Ein Hacker mit einem leistungsstarken PC bräuchte im Schnitt {time:.2f} {unit}, um dein Passwort zu knacken.")
