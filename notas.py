nome= input("digite o nome do vagabundo:")
nota1=float(input("digite a nota do primeiro bimestre: "))
nota2=float(input("digite a nota do segundo bimestre: "))
nota3=float(input("digite a nota do terceiro bimestre: "))
nota4=float(input("digite a nota do quarto bimestre: "))
media=((nota2 + nota2 + nota3+ nota4)/4)
if media <=3:
    print("reprovado")
elif media >=4 and media<=6:
    print("recoperação")
else:
    print("aprovado")
    print(media)