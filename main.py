# Enunciado:
"""
Escreva um programa que
informe se o usuário vai pagar
taxa de serviço por excesso de
bagagem em sua viagem.

# Taxa de serviço por excesso de bagagem.

Status Premier          | Núm. de malas sem taxas    | Tamanho máximo                      | Peso máximo por
MileagePlus             | de serviço                 | (comprimento + largura + altura)    | mala

1 - Premier Silver      | 1 mala                     | 158 cm (62 pol)                     | 32 kg (70 lb)
2 - Premier Gold        | 2 malas                    | 158 cm (62 pol)                     | 32 kg (70 lb)
3 - Premier Platinum    | 3 malas                    | 158 cm (62 pol)                     | 32 kg (70 lb)
4 - Premier 1K          | 3 malas                    | 158 cm (62 pol)                     | 32 kg (70 lb)

Solicite ao usuário os seguintes dados: Status (de 1 a 4), a quantidade de malas. Se o número de malas
for maior que o permitido para o status, imprima “Você terá que pagar uma taxa de serviço por excesso
de bagagem”, caso contrário, solicite o comprimento, largura, altura e peso para cada uma das malas,
informando a mesma frase caso ultrapassem os valores permitidos que foram informados na tabela
acima. Caso contrário, imprima “Tudo ok com as bagagens, tenha uma boa viagem.”
"""

# Entrada de dados
stt = int(input("Informe o status do passageiro:\n"
                "1 - Premier Silver\n"
                "2 - Premier Gold\n"
                "3 - Premier Platinum\n"
                "4 - Premier 1K\n"
               "Resposta:"))
qtd = int(input("Informe a quantidade de malas: "))
if ((stt==1 and qtd>1) or (stt==2 and qtd>2) or (stt==3 and qtd>3) or (stt==4 and qtd>3)):
    print("Você terá que pagar uma taxa de serviço por excesso de bagagem.")
else:
# Mala 1
  comp = float(input("Informe o comprimento da mala 1: "))
  larg = float(input("Informe a largura da mala 1: "))
  alt = float(input("Informe a altura da mala 1: "))
  peso = float(input("Informe o peso da mala 1: "))
  if((comp + larg + alt > 158) or (peso > 32)):
    print("Você terá que pagar uma taxa de serviço por excesso de bagagem.")
  
  else:
      if qtd > 1:
      # Mala 2
        comp = float(input("Informe o comprimento da mala 2: "))
        larg = float(input("Informe a largura da mala 2: "))
        alt = float(input("Informe a altura da mala 2: "))
        peso = float(input("Informe o peso da mala 2: "))
        if ((comp + larg + alt > 158) or (peso > 32)):
          print("Você terá que pagar uma taxa de serviço por excesso de bagagem.")
        else:
          if qtd > 2:
          # Mala 3
            comp = float(input("Informe o comprimento da mala 3: "))
            larg = float(input("Informe a largura da mala 3: "))
            alt = float(input("Informe a altura da mala 3: "))
            peso = float(input("Informe o peso da mala 3: "))
            if ((comp + larg + alt > 158) or (peso > 32)):
              print("Você terá que pagar uma taxa de serviço por excesso de bagagem.")
            else:
              print("Tudo ok com as bagagens, tenha uma boa viagem.")
          else:
            print("Tudo ok com as bagagens, tenha uma boa viagem.")
      else:
        print("Tudo ok com as bagagens, tenha uma boa viagem.")
