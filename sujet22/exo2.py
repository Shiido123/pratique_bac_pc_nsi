def rendu_monnaie_centimes(s_due, s_versee):
    pieces = [1, 2, 5, 10, 20, 50, 100, 200]
    rendu = []
    a_rendre = s_versee - s_due
    print(a_rendre)
    i = len(pieces) - 1
    while a_rendre > 0:
        if pieces[i] <= a_rendre:
            rendu.append(pieces[i])
            a_rendre -= pieces[i]
        else:
            i -= 1

    return rendu


print(rendu_monnaie_centimes(700, 700))
print(rendu_monnaie_centimes(112, 500))
