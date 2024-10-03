message = input('Ingresa el mensaje: ')
espacios = 1
while espacios > 0:
    clave = input('Ingresa tu palabra clave para cifrar: ')
    espacios = clave.count(' ')
    if clave.isalpha() == False:
        espacios += 1
key = len(clave)

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

translated = ''

for symbol in message:
    # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
        translatedIndex = symbolIndex + key
        
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        # Append the symbol without encrypting/decrypting:
        translated = translated + symbol

print(translated)

f= open ("Texto cifrado Cesar.txt", "w")
f.write(translated)
f.close()

if f.close():
    print("Se ha creado un archivo de texto con el mensaje cifrado, con el nombre: Texto cifrado Cesar.")
