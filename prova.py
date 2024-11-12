vereadores = [["11123", "Paulo Origa"], ["22333", "Dr Gilber"] ,["44444", "Dr Macário"], ["70000", "Zé Paroca"], ["44333", "Ellis Regina do SINDEPROF"]]
prefeitos = [["44", "Mariana Carvalho"], ["20", "Léo Moraes"], ["12", "Célio Lopes"]]
votosVereadores = []
votosPrefeitos = []

while True:
    while True:
        msg = input("Digite o número do seu candidato a vereador para votar ou aperte [2] para ver a lista de vereadores [0] para sair\n")

        if msg == "2":
            print(f"{vereadores[0]} - {vereadores[1]} - {vereadores[2]} - {vereadores[3]} - {vereadores[4]}")
        
        elif msg == "0":
            break
        else: 
            for vereador in vereadores:
                if msg == vereador[0]:
                    print(f"Voto confirmado em {vereador[1]}")
                    votosVereadores.append(msg)
                    break
            else:
                print("Número inválido")
                continue
            break
    if msg == "0":
        break
            
    while True:
        msg = input("Digite o número do seu candidato a prefeito para votar ou aperte [2] para ver a lista de prefeitos\n")
        if msg == "2":
            print(f"{prefeitos[0]} - {prefeitos[1]} - {prefeitos[2]}")
        
        else: 
            for prefeito in prefeitos:
                if msg == prefeito[0]:
                    print(f"Voto confirmado em {prefeito[1]}")
                    votosPrefeitos.append(msg)
                    break
            else:
                print("Número inválido")
                continue
            break    

##                            Resultado Vereadores                            ##       
paulo = votosVereadores.count("11123")
gilber = votosVereadores.count("22333")
macario = votosVereadores.count("44444")
paroca = votosVereadores.count("70000")
ellis = votosVereadores.count("44333")


print("""                  RESULTADO VEREADORES                 """)
print(f'''
        CANDIDATOS A VEREADOR   |  NÚMERO DE VOTOS  |
      --------------------------|-------------------|
      PAULO ORIGA               |        {paulo}          |
      DR GILBER                 |        {gilber}          |
      DR MACÁRIO                |        {macario}          |
      ZÉ PAROCA                 |        {paroca}          |
      ELLIS REGINA DO SINDERPROF|        {ellis}          |
      --------------------------|-------------------|
      TOTAL DE VOTOS            |         {len(votosVereadores)}         |
        ''')

vencedor = ""
if paulo > gilber and paulo > macario and paulo > paroca and paulo > ellis :
    vencedor = "Paulo Origa"
elif gilber > paulo and gilber > macario and gilber > paroca and gilber > ellis :
    vencedor = "Dr Gilber"
elif macario > paulo and macario > gilber and macario > paroca and macario > ellis :
    vencedor = "Dr Macário"
elif paroca > paulo and paroca > gilber and paroca > macario and paroca > ellis :
    vencedor = "Zé Paroca"
elif ellis > paulo and ellis > gilber and ellis > macario and ellis > paroca :
    vencedor = "Ellis Regina do SINDERPROF"

print (f"O candidato {vencedor} foi eleito.\n")

    
##                            Resultado Prefeitos                            ##    
mariana = votosPrefeitos.count("44")
leo = votosPrefeitos.count("20")
celio = votosPrefeitos.count("12")

percentMariana = (mariana / len(votosPrefeitos)) *100
percentLeo = (leo / len(votosPrefeitos)) *100
percentCelio = (celio / len(votosPrefeitos)) *100


print("""                  RESULTADO PREFEITOS                 """)
print(f'''
        CANDIDATOS A PREFEITO   |  NÚMERO DE VOTOS  |
      --------------------------|-------------------|
      MARIANA CARVALHO          |     {mariana} ({percentMariana:.2f}%)    |
      LÉO MORAES                |     {leo} ({percentLeo:.2f}%)    |
      CÉLIO LOPES               |     {celio} ({percentCelio:.2f}%)    |
      --------------------------|------------------|
      TOTAL DE VOTOS            |         {len(votosPrefeitos)}        |
        ''')

vencedor = ""
if mariana > leo and mariana > celio:
    vencedor = f"Mariana Carvalho foi eleita com {percentMariana:.2f}%"
elif leo > mariana and leo > celio:
    vencedor = f"Léo Moraes foi eleito com {percentLeo:.2f}%"
elif celio > mariana and celio > leo:
    vencedor = f"Célio Lopes foi eleito com {percentCelio:.2f}%"
else:
    vencedor = "Empate"

if vencedor == "Empate":
    print ("Eleição será definida no segundo turno.")
else:
    print (f"O candidato {vencedor} dos votos.\n")    
    




