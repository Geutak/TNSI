import astro as ast

while True:
    try:
        j, m, a = ast.demander_date()
        bis = ast.annee_bissextile(a)
        ast.verif_mois(m)
        ast.verif_jour(j, m, bis)
        break

    except:
        pass
print("Vous êtes né le {}/{}/{}.".format(j, m, a))

r, signe, genre = ast.signe_viet(a)

caractere = ast.get_caractere(r)

print("Selon votre année de naissance, vous êtes nés l'année ",genre,signe,".","\n",caractere)