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
pokemon_information.config(font=("TimesNewRoman", 20))
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk.Label(window)
pokemon_types.config(font=("TimesNewRoman", 20))
pokemon_types.pack(padx=10, pady=10)

pokemon_height = tk.Label(window)
pokemon_height.config(font=("TimesNewRoman", 20))
pokemon_height.pack(padx=10, pady=10)

pokemon_weight = tk.Label(window)
pokemon_weight.config(font=("TimesNewRoman", 20))
pokemon_weight.pack(padx=10, pady=10)

pokemon_abilities = tk.Label(window)
pokemon_abilities.config(font=("TimesNewRoman", 20))
pokemon_abilities.pack(padx=10, pady=10)

pokemon_stats = tk.Label(window)
pokemon_stats.config(font=("TimesNewRoman", 20))
pokemon_stats.pack(padx=10, pady=10)

pokemon_stats_label = tk.Label(window)
pokemon_stats_label.config(font=("TimesNewRoman", 20))
pokemon_stats_label.pack(padx=10, pady=10)

pokemon_stats_value = tk.Label(window)
pokemon_stats_value.config(font=("TimesNewRoman", 20))
pokemon_stats_value.pack(padx=10, pady=10)

pokemon_stats_label2 = tk.Label(window)
pokemon_stats_label2.config(font=("TimesNewRoman", 20))
pokemon_stats_label2.pack(padx=10, pady=10)

pokemon_stats_value2 = tk.Label(window)
pokemon_stats_value2.config(font=("TimesNewRoman", 20))
pokemon_stats_value2.pack(padx=10, pady=10)

pokemon_stats_label3 = tk.Label(window)
pokemon_stats_label3.config(font=("TimesNewRoman", 20))
pokemon_stats_label3.pack(padx=10, pady=10)

pokemon_stats_value3 = tk.Label(window)
pokemon_stats_value3.config(font=("TimesNewRoman", 20))
pokemon_stats_value3.pack(padx=10, pady=10)

pokemon_stats_label4 = tk.Label(window)
pokemon_stats_label4.config(font=("TimesNewRoman", 20))
pokemon_stats_label4.pack(padx=10, pady=10)

pokemon_stats_value4 = tk.Label(window)
pokemon_stats_value4.config(font=("TimesNewRoman", 20))
pokemon_stats_value4.pack(padx=10, pady=10)


# Function to actually load in the Pokémon
def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))
    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))

    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title())
    pokemon_types.config(text=f"{pokemon.types}".title())
    pokemon_height.config(text=f"{pokemon.height}")
    pokemon_weight.config(text=f"{pokemon_weight}"


label_id_name = tk.Label(window, text="ID or Name")
label_id_name.config(font=("TimesNewRoman", 20))
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("TimesNewRoman", 20))
text_id_name.pack(padx=10, pady=10)

btn_load = tk.Button(window, text="Load Pokemon", command=load_pokemon)
btn_load.config(font=("TimesNewRoman", 20))
btn_load.pack(padx=10, pady=10)

window.mainloop()
