import tkinter as tk
import random


def generate_key(word):
    word = word.upper()
    letters = list(word)

    random.shuffle(letters)
    block13 = ''.join(letters[:3])

    indexes = [(ord(char) - ord('A') + 1) % 10 for char in word]
    block2 = ''.join(str(index) for index in indexes)

    key = f"{block13}-{block2[:6]}-{block13}"
    return key


def generate_button():
    input_word = entry.get()
    generated_key = generate_key(input_word)
    key_var.set(generated_key)


root = tk.Tk()
root.title("Keygen App")
root.geometry("650x433")

image = "cs2.png"
bg_image = tk.PhotoImage(file=image)
background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)

entry_label = tk.Label(root, text="Введите слово из 6 английских букв")
entry_label.pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=10)

generate_button = tk.Button(root, text="Создать ключ", command=generate_button)
generate_button.pack(pady=10)

key_var = tk.StringVar()
key_label = tk.Label(root, textvariable=key_var)
key_label.pack(pady=10)

root.mainloop()
