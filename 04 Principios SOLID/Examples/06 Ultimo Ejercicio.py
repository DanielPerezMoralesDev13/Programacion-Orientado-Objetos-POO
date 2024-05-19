#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Correo electrónico: danielperezdev@proton.me

"""
Chatbot analizador de sentimientos

En este proyecto, podrias desarrollar un chatbot en python, que nos pida que le digamos algo y tome eso que le decimos, analice el sentimiento y no responda cual es el sentimiento.

Este proyecto te daria la oportunidad de trabajar con varios aspectos de la Programacion Orientada a Objetos, modulos, API, analisis de datos, etc.
"""

from types import FrameType
from typing import Optional, Any, List
import os, sys, subprocess, signal, pdb

def borrar() -> None:
    os.system(command = "cls" if os.name == "nt" else "clear")
    return None

def salirPrograma(sig: int ,frame: Optional[FrameType]) -> None:
    log.failure(message = f"{colored(text = 'Saliendo!', color = 'light_red')}")
    sys.exit(1)
    return None

signal.signal(signalnum = signal.SIGINT, handler = salirPrograma)
ENGLISH: str = "en"
ESPAÑOL: str = "es"

def installDependency(package_name: str) -> None | OSError:
    try:
        if sys.platform.startswith('linux') or sys.platform == 'darwin': subprocess.check_call(args = [sys.executable, '-m', 'pip', 'install', package_name])
        elif sys.platform == 'win32': subprocess.check_call(args=[sys.executable, '-m', 'pip', 'install', package_name])
        else: raise OSError("Sistema operativo no soportado para la instalación automática.")
    except subprocess.CalledProcessError as e: 
        print(f"Error al intentar instalar {package_name}: {e}",end = "\n")
        sys.exit(1)
    return None

try: import textblob
except ImportError:
    print("textblob no está instalado. Instalando ahora...",end = "\n")
    installDependency(package_name = "textblob")

try: from deep_translator import GoogleTranslator
except ImportError:
    print("deep_translator no está instalado. Instalando ahora...",end = "\n")
    installDependency(package_name = "deep_translator")

try: from pwn import *
except ImportError:
    print("pwn no está instalado. Instalando ahora...",end = "\n")
    installDependency(package_name = "pwn")

try: from termcolor import colored
except ImportError:
    print("termcolor no está instalado. Instalando ahora...",end = "\n")
    installDependency(package_name = "colored")

try: from langdetect import detect, DetectorFactory
except ImportError:
    print("langdetect no está instalado. Instalando ahora...",end = "\n")
    installDependency(package_name = "langdetect")

import time
# type: ignore[import-untyped]
from pwn import *
# pip3 install pwn
from termcolor import colored
# pip3 install termcolor
import textblob
from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# ! en-English
# ! es-Spanish

class Español:
    def __init__(self) -> None:
        self._traductor_español: GoogleTranslator = GoogleTranslator(source = 'auto', target = ESPAÑOL)
        # self._traductor_español: GoogleTranslator: Define un atributo de instancia _traductor_español que es de tipo GoogleTranslator.

        # GoogleTranslator(source = ENGLISH, target = ESPAÑOL): Crea una instancia de GoogleTranslator configurada para traducir del inglés al español.

        # source = ENGLISH: Especifica el idioma de origen como inglés ('en').
        # target = ESPAÑOL: Especifica el idioma de destino como español ('es').
        return None
    def _traducirTextoEspañol(self, texto: str) -> str:
        # self._traductor_español.translate(text=texto): Llama al método translate de la instancia GoogleTranslator para traducir el texto.

        # text = texto: Especifica el texto que se va a traducir.
        return self._traductor_español.translate(text = texto)


class Ingles:
    def __init__(self: 'Ingles') -> None:
        self._traductor_ingles: GoogleTranslator = GoogleTranslator(source = 'auto', target = ENGLISH)
        return None

    def _traducirTextoIngles(self: 'Ingles', texto: str) -> str:
        return self._traductor_ingles.translate(text = texto)

DetectorFactory.seed = 0

class Traductor(Ingles, Español):
    def __init__(self: 'Traductor') -> None:
        Ingles.__init__(self = self)
        Español.__init__(self = self)
        return None

    def _verIdioma(self: 'Traductor', texto: str) -> str:
        try:
            idioma: str = detect(text = texto)
            return idioma
        except LangDetectException: raise LangDetectException(message = f"{colored(text = 'No se pudo detectar el idioma', color = 'light_red')}", code = 1)


class AnalizadorSentimientos(Traductor):
    def __init__(self: 'AnalizadorSentimientos') -> None:
        super().__init__()
        return None

    def _analizadorSentimientos(self: 'AnalizadorSentimientos', texto: str) -> str:
        idioma: str = self._verIdioma(texto = texto)
        
        analisis: textblob.TextBlob = textblob.TextBlob(text = self._traducirTextoIngles(texto = texto))
        if analisis.sentiment.polarity > 0: return f"{colored(text = 'El comentario que hiciste indica que tu estado de animo es positivo',color = 'light_green')}"
        elif analisis.sentiment.polarity == 0: return f"{colored(text = 'El comentario que hiciste indica que tu estado de animo es neutral',color = 'light_yellow')}"
        else: return f"{colored(text = 'El comentario que hiciste indica que te sientes mal',color = 'light_red')}"

"""
# Códigos de colores ANSI. EL formato de texto van del 0 al 9, y los códigos para los colores del texto y del fondo van del 30 al 47.

\033[0m: Reset (restablece todos los atributos de formato)
\033[1m: Bright (aumenta la intensidad del color)
\033[2m: Dim (disminuye la intensidad del color)
\033[3m: Italic (texto en cursiva)
\033[4m: Underlined (texto subrayado)
\033[7m: Reverse (invierte los colores de fondo y de texto)
\033[8m: Hidden (texto oculto)


Para cambiar el color del texto:

\033[30m: Black (negro)
\033[31m: Red (rojo)
\033[32m: Green (verde)
\033[33m: Yellow (amarillo)
\033[34m: Blue (azul)
\033[35m: Magenta (magenta)
\033[36m: Cyan (cian)
\033[37m: White (blanco)
Para cambiar el color de fondo:

\033[40m: Black (negro)
\033[41m: Red (rojo)
\033[42m: Green (verde)
\033[43m: Yellow (amarillo)
\033[44m: Blue (azul)
\033[45m: Magenta (magenta)
\033[46m: Cyan (cian)
\033[47m: White (blanco)
"""

if __name__ == "__main__":
    borrar()
    daniel: AnalizadorSentimientos = AnalizadorSentimientos()
    print(f"{colored(text = 'Analizador de sentimiento hechos en python3',color = 'light_grey')}",end = "\n\r")
    while True:
        p1: Any = log.progress(message = f"{colored(text = 'Ingrese un texto de tu estado de animo (Salir -> Ctrl + C): ', color = 'light_cyan')}")
        texto_usuario: str = str(input('')).lower()

        # p1.failure("fail")
        # time.sleep(1)

        # log.info(f"{type(p1)}")
        # time.sleep(1)

        # Actualizar el estado
        emociones: List[str] = [
            "Felicidad", "Tristeza", "Ira", "Miedo", "Sorpresa", "Asco", "Amor", "Odio", "Alegría", "Depresión",
            "Ansiedad", "Esperanza", "Paz", "Euforia", "Desesperación", "Culpa", "Vergüenza", "Orgullo", "Cansancio",
            "Satisfacción", "Desagrado", "Enojo", "Desilusión", "Excitación", "Preocupación", "Aburrimiento",
            "Inseguridad", "Compasión", "Empatía", "Admiración", "Envidia", "Arrepentimiento", "Remordimiento",
            "Desamparo", "Resignación", "Enamoramiento", "Desdén", "Hostilidad", "Resentimiento", "Indignación",
            "Desesperanza", "Despreocupación", "Placer", "Tranquilidad", "Nostalgia", "Incredulidad", "Sorpresa",
            "Incredulidad", "Desesperación", "Curiosidad", "Satisfacción", "Escepticismo", "Euforia", "Compasión",
            "Ira", "Vergüenza", "Emoción", "Agobio", "Desprecio", "Asombro", "Sorpresa", "Desconsuelo", "Frustración",
            "Comprensión", "Perplejidad", "Despreocupación", "Respeto", "Inseguridad", "Resentimiento", "Remordimiento",
            "Desesperanza", "Desesperación", "Aburrimiento", "Cautela", "Pena", "Esperanza", "Miedo", "Desagrado",
            "Plenitud", "Arrepentimiento", "Desilusión", "Optimismo", "Incertidumbre", "Soledad", "Soledad", "Satisfacción",
            "Serenidad", "Admiración", "Envidia", "Esperanza", "Hostilidad", "Indiferencia", "Tranquilidad", "Felicidad",
            "Preocupación", "Alivio", "Compasión", "Ira", "Compasión"
        ]
        for i in emociones:
            p1.status(f"{colored(text = i, color = 'light_magenta')}")
            time.sleep(0.1)
    
        # Indicar éxito
        p1.success(f"{colored(text = '¡El anilisis ha sido completado con Exito!', color = 'light_green')}")
        time.sleep(1.0)
        print(daniel._analizadorSentimientos(texto = texto_usuario),end = "\n")



# Linux o Mac
# si no tenemos instalado pip sudo apt-get install python3-pip
# pip3 install textblob
# python3 -m pip install textblob

# Windows
# pip install textblob
# py -m pip install textblob


"""
    Todos los idiomas 
    lang
    en-English
    es-Spanish
    fr-French
    de-German
    it-Italian
    pt-Portuguese
    af-Afrikaans
    sq-Albanian
    am-Amharic
    ar-Arabic
    hy-Armenian
    az-Azerbaijani
    eu-Basque
    be-Belarusian
    bn-Bengali
    bs-Bosnian
    bg-Bulgarian
    ca-Catalan
    ceb-Cebuano
    ny-Chichewa
    zh-CN - Chinese (Simplified)
    zh-TW - Chinese (Traditional)
    co - Corsican
    hr - Croatian
    cs - Czech
    da - Danish
    nl - Dutch
    eo - Esperanto
    et - Estonian
    tl - Filipino
    fi - Finnish
    fy - Frisian
    gl - Galician
    ka - Georgian
    el - Greek
    gu - Gujarati
    ht - Haitian Creole
    ha - Hausa
    haw - Hawaiian
    iw - Hebrew
    hi - Hindi
    hmn - Hmong
    hu - Hungarian
    is - Icelandic
    ig - Igbo
    id - Indonesian
    ga - Irish
    ja - Japanese
    jw - Javanese
    kn - Kannada
    kk - Kazakh
    km - Khmer
    ko - Korean
    ku - Kurdish (Kurmanji)
    ky - Kyrgyz
    lo - Lao
    la - Latin
    lv - Latvian
    lt - Lithuanian
    lb - Luxembourgish
    mk - Macedonian
    mg - Malagasy
    ms - Malay
    ml - Malayalam
    mt - Maltese
    mi - Maori
    mr - Marathi
    mn - Mongolian
    my - Burmese
    ne - Nepali
    no - Norwegian
    ps - Pashto
    fa - Persian
    pl - Polish
    pa - Punjabi
    ro - Romanian
    ru - Russian
    sm - Samoan
    gd - Scots Gaelic
    sr - Serbian
    st - Sesotho
    sn - Shona
    sd - Sindhi
    si - Sinhala
    sk - Slovak
    sl - Slovenian
    so - Somali
    es - Spanish
    su - Sundanese
    sw - Swahili
    sv - Swedish
    tg - Tajik
    ta - Tamil
    te - Telugu
    th - Thai
    tr - Turkish
    uk - Ukrainian
    ur - Urdu
    uz - Uzbek
    vi - Vietnamese
    cy - Welsh
    xh - Xhosa
    yi - Yiddish
    yo - Yoruba
    zu - Zulu
    
"""
