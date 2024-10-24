#programa estoque com frete
#variáveis de memória 
vcont="s"
vproduto=""
vquantidade=0
vvalor=0.0
vpeso=0.0
#criando lista
Lproduto=[]
Lvalor=[]
Lquantidade=[]
Lpeso=[]
print("SISTEMA DE VENDAS")
while vcont== "s":
    vproduto=input("digite o produto : ")
    vvalor=float(input("VALOR: "))
    vquantidade=int(input("QUANTIDADE:"))
    vpeso=float(input("PESO: "))
    Lproduto.append(vproduto)
    Lvalor.append(vvalor)
    Lquantidade.append(vquantidade)
    Lpeso.append(vpeso)
    vcont=input("DESEJA CONTINUAR <s/n>: ")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("---------------CALCULANDO PESO-----------------------")
