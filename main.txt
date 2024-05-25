import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO

window = tk.Tk()
window.geometry("600x500")
window.title("Mew's Pokedex")
window.config(padx=10, pady=10)

title_label = tk.Label(window, text="Mew's Pokedex")
title_label.config(font=("TimesNewRoman", 32))
title_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(window)
pokemon_image.pack(padx=10, pady=10)

pokemon_information = tk.Label(window)
pokemon_information.config(font= ("TimesNewRoman", 20))
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk.Label(window)
pokemon_types.config(font= ("TimesNewRoman", 20))
pokemon_types.pack(padx=10, pady=10)

# Function to actually load in the pokemons

label_id_name = tk.Label(window, text="ID or Name")
label_id_name.config(font=("TimesNewRoman", 20))
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("TimesNewRoman", 20))
text_id_name.pack(padx=10, pady=10)

btn_load = tk.Button(window, text="Load Pokemon")
btn_load.config(font=("TimesNewRoman", 20))
btn_load.pack(padx=10, pady=10)

window.mainloop()
