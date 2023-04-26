#-------------------------------------- Les Bonnes fonctions --------------------------------------#
import serial
import time
# Configuration de la communication série
ser = serial.Serial('COM3', 9600)

# Liste des keywords pour l'exécution des commandes de l'utilisateur
up = ["on", "allume", "Allume"]
down = ["off", "eteint", "éteint", "eteins", "éteins", "Eteint", "Eteins"]
colors = ["red", "yellow", "green", "rouge", "jaune", "vert", "verte", "Red", "Yellow", "Green", "Rouge", "Jaune", "Vert", "Verte"]
temp = ["température", "temperature", "Temperature", "Température"]
hum = ["humidity", "Humidity", "Humidité", "humidité", "humidite", "Humidite", "L'humidité", "l'humidité", "l'humidite", "L'humidite"]
bip = ["clignote", "clignoter", "bip"]


############################################## *000* ###############################################
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
############################################## *001* ###############################################
def prompt(data_words):
    action, color, my_int = "none", "none", "10"
    for i in data_words:
        if is_integer(i):
            my_int = i
            continue
        elif i in colors:
            color = i
            continue
        elif i in temp                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           :
            action = "temp"
            continue
        elif i in hum:
            action = "hum"
            continue
        elif i in up:
            action = "up"
            continue
        elif i in down:
            action = "down"
            continue
        elif i in bip:
            action = "bip"
            continue
        else:
            if action == "none":
                action = "none"

            if color == "none":
                color = "none"
            if my_int == '':
                my_int = '10'

    todo = action+" "+color+" "+my_int
    return todo

############################################## *002* ###############################################

def send_prompt(prompt):
    # Envoie la commande à l'Arduino
    ser.write(prompt.encode())

def get_message():
    message = ser.readline().decode('utf-8')
    return message
