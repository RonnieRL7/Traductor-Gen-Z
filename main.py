meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso.",
            "LOL": "Una respuesta común a algo gracioso.",
            "idk": "Que desconoce de algo o que no sabe algo.",
            "pov": "Punto de vista de algo o alguien.",
            "afk": "Lejos del teclado o ausente en un videojuego."
            }
palabra = input("Que palabra deceas entender?")
if palabra in meme_dict.keys():
    print(meme_dict[palabra])
else:
    print('Todavia no tenemos esa palabra, pero la tendremos pronto!')
