# -*- coding: utf-8 -*-
import os

#Idiomas permitidos en internacionalización
LANGUAGES = {
    'en': 'English',
    'es': 'Español'
}
#Carpeta donde subir archivos
upload_folder = os.path.dirname(os.path.realpath(__file__))+"\\ficheros"
translations_folder = os.path.dirname(os.path.realpath(__file__))+"\\translations"