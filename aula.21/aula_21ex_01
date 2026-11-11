def voto(data):
    from datetime import date
    atual = date.today().year
    idade= atual - data
    if idade >= 18 and idade < 70:
        return f"com {idade} anos o voto é obrigatorio! "
    elif idade< 18:
        return f'com {idade} anos nao tem direito ao voto ainda'
    elif idade >=  70:
        return f"com {idade} anos seu voto é opcional"


ano = int(input("em que ano vc nasceu ?"))
print(voto(ano))

