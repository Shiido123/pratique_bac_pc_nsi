t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]


def mini(releve, date):
    temp_min = releve[0]
    indice_min = 0
    for indice, valeur in enumerate(releve):
        if valeur < temp_min:
            temp_min = valeur
            indice_min = indice

    date_assoc = date[indice_min]
    return temp_min, date_assoc


print(mini(t_moy, annees))
