import pandas
mydataset = {
  'players': ["Benzema", "Mbappe", "Salah"],
  'goals': [27, 20, 19]
}
data = pandas.DataFrame(mydataset)

print(data)

import socket

print(socket.gethostbyname(socket.gethostname()))

import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()

window.mainloop()

import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])

plt.ylabel('some numbers')

plt.show()


