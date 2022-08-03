import re


def validate_cpf(cpf):
    """Function that validates the CPF"""
    cpf = str(cpf)
    cpf = re.sub(r"[^0-9]", "", cpf)
    if not cpf or len(cpf) != 11:
        return False
    new_cpf = cpf[:-2]
    reverse = 10
    total = 0
    for index in range(19):

        if index > 8:
            index -= 9

        total += int(new_cpf[index]) * reverse
        reverse -= 1

        if reverse < 2:
            reverse = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0

            total = 0
            new_cpf += str(d)

    sequency = new_cpf == str(new_cpf[0]) * len(cpf)
    if cpf == new_cpf and not sequency:
        return True
    else:
        return False
