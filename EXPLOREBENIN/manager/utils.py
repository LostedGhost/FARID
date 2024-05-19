import random, string
from manager.conf import *
from datetime import datetime

def truncatechars(string, max_length):
        if len(string) < max_length:
            return string
        else:
            return string[:max_length] + "..."

def nombre_de_jours(j1, j2):
    # Convertir les dates en objets datetime si elles ne le sont pas déjà
    if not isinstance(j1, datetime):
        j1 = datetime.strptime(j1, '%Y-%m-%d')
    if not isinstance(j2, datetime):
        j2 = datetime.strptime(j2, '%Y-%m-%d')

    # Calculer la différence entre les deux dates
    difference = j2 - j1

    # Retourner le nombre de jours en valeur absolue
    return difference.days

def date_to_text(date):
    return date.strftime('%Y-%m-%d')

def text_to_date(text):
    return datetime.strptime(text, '%Y-%m-%d')

def generate_strong_password(length=12):
    """Generate a strong password."""
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure at least one character from each set
    password = random.choice(lowercase_letters)
    password += random.choice(uppercase_letters)
    password += random.choice(digits)
    password += random.choice(special_characters)

    # Fill remaining length with random characters
    for _ in range(length - 4):
        password += random.choice(all_characters)

    # Shuffle the password to make it more random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def chiffrement_cesar(message) -> str:
    decalage = KEY
    message_chiffre = ""
    for caractere in message:
        # Vérifier si le caractère est une lettre majuscule
        if caractere.isupper():
            ascii_code = ord(caractere)
            nouveau_code = (ascii_code - ord('A') + decalage) % 26 + ord('A')
            message_chiffre += chr(nouveau_code)
        # Vérifier si le caractère est une lettre minuscule
        elif caractere.islower():
            ascii_code = ord(caractere)
            nouveau_code = (ascii_code - ord('a') + decalage) % 26 + ord('a')
            message_chiffre += chr(nouveau_code)
        # Vérifier si le caractère est un chiffre
        elif caractere.isdigit():
            ascii_code = ord(caractere)
            nouveau_code = (ascii_code - ord('0') + decalage) % 10 + ord('0')
            message_chiffre += chr(nouveau_code)
        # Si le caractère est un caractère spécial, le laisser inchangé
        else:
            message_chiffre += caractere
    return message_chiffre

def dechiffrement_cesar(message) -> str:
    decalage = -KEY
    message_chiffre = ""
    for caractere in message:
        # Vérifier si le caractère est une lettre majuscule
        if caractere.isupper():
            ascii_code = ord(caractere)
            nouveau_code = (ascii_code - ord('A') + decalage) % 26 + ord('A')
            message_chiffre += chr(nouveau_code)
        # Vérifier si le caractère est une lettre minuscule
        elif caractere.islower():
            ascii_code = ord(caractere)
            nouveau_code = (ascii_code - ord('a') + decalage) % 26 + ord('a')
            message_chiffre += chr(nouveau_code)
        # Vérifier si le caractère est un chiffre
        elif caractere.isdigit():
            ascii_code = ord(caractere)
            nouveau_code = (ascii_code - ord('0') + decalage) % 10 + ord('0')
            message_chiffre += chr(nouveau_code)
        # Si le caractère est un caractère spécial, le laisser inchangé
        else:
            message_chiffre += caractere
    return message_chiffre
