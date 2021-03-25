import Model


def escolha_personagem():

    valida_resposta = 'sim'
    while valida_resposta == 'sim':
        separador("*")
        tema(mensagem)
        separador("*")
        print("Selecione seu personagem: ")
        print('''
        A) Jênnifer - (Sonhadora)
        B) Olivia - (Jovem estagiaria de sucesso)
        C) Carla - (Batalhadora e determinada)
            ''')
        escolha_person = input("Personagem (A, B ou C): ").lower()

        if escolha_person == "a":
            person = "Jênnifer"
            valida_resposta = 'não'
        elif escolha_person == "b":
            person = "Olivia"      
            valida_resposta = 'não'    
        elif escolha_person == "c":
            person = "Carla"
            valida_resposta = 'não'
        else:
            print("Não existe essa opção! tente novamente!")
            continuar = bool(input("Pressione Enter para continuar..."))
            print("\x1b[2J")        
    return person  