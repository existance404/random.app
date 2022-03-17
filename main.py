import tkinter as tk
msgstr2 = "This app is useless. You are useless. Everyone is useless."
print(msgstr2)

window = tk.Tk()
window.title("UselessApp")
window.geometry("400x400")

hello = tk.Label(text="This app is pretty useless.")
hello.pack()
button = tk.Button(text="Don't click here.")
button.pack()

tk.mainloop()

