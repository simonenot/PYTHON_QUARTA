dizionario = {"a": 1, "b": 2, "c": 3}
dizionarioscambiato = {}
for chiave, valore in dizionario.items():
    dizionarioscambiato[valore] = chiave
print(dizionarioscambiato)
