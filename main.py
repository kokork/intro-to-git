from web import dohvati_5_kripto_valuta

# provjera je li ovo py file koji upravo pokrećemo ili nije
if __name__ == "__main__":
    kripto_valute =dohvati_5_kripto_valuta()


    for valuta in kripto_valute:
        print(valuta)