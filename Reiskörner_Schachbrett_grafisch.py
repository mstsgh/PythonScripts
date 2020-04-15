import matplotlib.pyplot as plt
summe = 0
feldListe = []

for feld in range(64):
    reiskorn = 2**feld
    feldListe.append(reiskorn)
    summe += reiskorn
    print(f"Feld {feld+1}. = {reiskorn:>30,} Reiskörner und damit insgesamt {summe:>30,} Reiskörner")
gewicht = summe * 0.02 / 1000 / 1000
print("Wenn ein Reiskorn 0,02 Gramm wiegt, wiegen die gesamten ")
print("Reiskörner {:18,.0f} Tonnen".format(gewicht))
plt.plot(feldListe)
plt.show()