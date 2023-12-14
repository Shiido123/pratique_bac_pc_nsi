def inverse_chaine(chaine):
    result = ""
    for caractere in reversed(chaine):
        result = result + caractere
    return result


def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return chaine == inverse


def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)


print(inverse_chaine('bac'))
print(est_palindrome('NSI'))
print(est_palindrome('ISN-NSI'))
print(est_nbre_palindrome(213312))
