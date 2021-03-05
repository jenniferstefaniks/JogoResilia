
# Variável Global
mensagem = "BEM-VINDO AO JOGO - VIDA DE PROGRAMADOR"
pontos = 0

# Funções e metodos:
def tema(titulo):
    print(titulo.center(100, " "))

def limpa_tela():
    print("\x1b[2J")

def separador(asterisco):
    print( 80* (asterisco))

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

def Jogo_Jennifer():
    
    msg_casa_derrota = '''
        Como dizia sua mãe:
        "Celular não da futuro não, viu?"
        Devia ouvir mais ela... 

        Fim de jogo! 

        OBRIGADA POR JOGAR!
        '''

    msg_emprego_derrota = '''
        Maturidade emocional é o poder de controla-lo a seu favor.
        Você poderia ter evitado esse confronto! 
        Agora você está desempregada, boa sorte!

        OBRIGADA POR JOGAR!
        '''

    msg_parente_derrota = '''
        Que pena que você deu ouvidos a opiniões alheias... novamente...
        Estava quase conseguindo... Mas se continuar dando ouvidos às pessoas,
        você nunca irá conseguir!
        O sonho é seu, quem vivera ele é você. Pense nisso!

        OBRIGADA POR JOGAR!
        '''

    msg_vitoria1 = '''
        Por mais desafiador que foi conseguir estar aqui, você enfrentou e 
        conseguiu a vitória sobre os obstáculos de sua vida de programadora. 
        E agora você é tudo que sempre sonhou! Comemore muito, 
        você se tornou a diretora das empresa mais famosa do Brasil.

        PARABÉNS!

        OBRIGADA POR JOGAR!
        '''

    msg_vitoria2 = '''
        Felizmente, com tudo que sobreveio sobre seu caminho até aqui, 
        você venceu com honra e determinação. Por mais que não esteja 
        onde deseja estar, ainda, você está no caminho certo!
        Você se tornou a Coordenadora geral da empresa mais famosa do Estado. 
        Já está no lucro, não?
        MEUS PARABÉNS.

        OBRIGADA POR JOGAR!
        '''

    def cenario_Casa():
        print('''
        CENÁRIO: Casa
        HORÁRIO E DATA: 10h am - Sábado 
        PERSONAGEM: Jênnifer

        Você está na sala de sua casa, juntamente com seu marido…
        Você sabe que tem coisas importantes a se fazer, como por exemplo aprender
        mais sobre Python e se desempenhar mais nos estudos. Você vê o notebook ligado
        e o celular do seu lado.
        Sabendo que o celular te distrai muito com conteúdos que não são eficazes para o
        seu aprendizado profissional, você tem uma escolha a fazer:
        
        Escolhas:
        A) Pegar o celular e se distrair por horas
        B) Pegar o notebook e jogar 
        C) Pegar o notebook e estudar
        obs: Sua escolha determina como será sua vida
        \n''')

    def cenario_Emprego():
        print('''
        CENÁRIO: Emprego
        HORÁRIO E DATA: 08h am - Segunda-Feira
        PERSONAGEM: Jênnifer
        
        Você está no seu emprego, onde não te valorizam e te tratam com maior desprezo e seu salário é péssimo.
        Sua chefe entra na sua sala e pede que você faça coisas que não são de sua função na empresa e diz isso
        com toda arrogância do mundo a você:“Estes são os arquivos que você deve revisar e arquivar até amanhã
        neste mesmo horário, então, pare de pensar em ser uma programadora e faça o que você está aqui para fazer
        que é, lógico, fazer tudo que eu mando! HAHAHA”
        Com isso você tem escolhas para fazer que afetará seu futuro na empresa.
        
        Escolhas:
        A) Explodir com sua chefe e dizer tudo que pensa sobre ela e a empresa (Warn: Perder emprego)
        B) Responder com a mesma arrogância e não fazer
        C) Responder com educação e ética sua chefe e aceitar mesmo assim com elegância a função proposta. 
        obs: Sua escolha determina como será sua vida''')

    def cenario_Parente():
        print('''
        CENÁRIO: Casa de Parente
        HORÁRIO: 12:30 PM DOMINGO
        PERSONAGEM: jênnifer
        
        Hoje é final de semana e como de costume, sua família se reuni para fazer um churrasco, 
        beber e passar vergonha.
        Está todo mundo da sua família reunido, e graças a Deus você se dá muito bem com a maioria 
        da sua família, porém, o que você mais temia aconteceu… O parente não tão desejado por você
        com seu jeito arrogante e ignorante de falar, especialmente quando se trata de você, está
        vindo em sua direção e com a sobrancelha arqueada e com humor irritável estampado em seu
        rosto e você já revira os olhos e vira as costas na chance que ele passe direto por você
        mas ele lhe dá uns tapinha nas costas e diz:

        “Olá queridinha, tem alguma novidade? Além de estar “estudando” programação, que eu particularmente acho uma perda de tempo haha”
        Você vê o tom de ironia na voz dele e diz: 

        Escolhas: 
        A) “Bom, talvez você tenha razão, vou desistir de tudo isso! :(”
        B) “Você sempre tem que ser essa pessoa tóxica?"
        C) “Grandes novidades, querido. A minha vida ainda reserva muitas surpresas para você! Fique esperto nos próximos capítulos,
        já que você está tão interessado! :)”
        obs: Sua escolha determina como será sua vida
        ''')
    
    def pontuacao(escolha, points, msg1, msg2):
        global pontos
        if escolha == 'c':
            pontos += 3
        elif escolha == 'b':
            pontos += 2
        elif escolha == 'a':
            pontos = 0
    def futuro():
        
        if(pontos >= 9):
            separador("*")
            print(msg_vitoria1)
            separador("*")
        elif(pontos >= 6 and pontos < 9 ):
            separador("*")
            print(msg_vitoria1)
            separador("*")
    
    #INICIO
    print("Bem vinda, Jênnifer!")
    print('''
        Jênnifer é uma mulher inconstante em tudo que faz e a sua vida
    é cheia de desafios e decisões para o futuro… 
    Quando ela tinha 17 anos, fez curso de computação
    que a fez amar tudo relacionado a tecnologia. 
    Seus pais sempre a apoiaram em tudo, porém ela mesma não acreditava muito 
    em si mesma e desistia fácil muitas vezes por conta de minorias que duvidam 
    da sua capacidade.
    Passados alguns anos... com 23 anos ela se inscreveu em um 
    curso gratuito com parceria com o ifood, sobre ciências de 
    dados e passou no teste e na entrevista para participar deste curso por 6 meses 
    e dessa vez ela está empenhada em aprender tudo e não jogar fora mais 
    uma oportunidade para leva-la ao futuro que tanto almeja...
    \n''')
    limpa_tela()
    
    separador("*")
    cenario_Casa()
    separador("*")
    escolha_cenario1 = input("Qual sua escolha: A, B ou C: ").lower()
    print('\n')
    if escolha_cenario1 == 'b' or escolha_cenario1 == 'c':
        pontuacao(escolha_cenario1, pontos, msg_vitoria1, msg_vitoria2)
        if(escolha_cenario1 == 'b'):
            print('''
                Por mais que você ter escolhido jogar... 
                30min depois você pensa melhor e decide estudar. 
                UFA!
                ''')
        elif(escolha_cenario1 == 'c'):
            print('''
                MUITO BEM! 
                FOCO TOTAL!
                ''')
        
        continuar = bool(input("Pressione Enter para continuar..."))
        print("\x1b[2J")

        # Cenario 2
        separador("*")
        cenario_Emprego()
        separador("*")
        escolha_cenario2 = input("Qual sua escolha: A, B ou C: ").lower()
        separador('*')

        if escolha_cenario2 == 'b' or escolha_cenario2 == 'c':
            pontuacao(escolha_cenario1, pontos, msg_vitoria1, msg_vitoria2)
            
            if(escolha_cenario2 == 'b' ):
                print('''
                Você é uma doida! 
                Sorte sua que ela está em um dia bom e relevou sua atitude...
                Tá difícil arranjar emprego, viu? 

                Você ganhou mais uma chance, não a desperdice. 
                ''')
            elif(escolha_cenario2 == 'c'):
                print('''
                    Admiro sua paciência e classe por evitar esse confronto... 
                    Muito bem!
                    ''')
            separador("*")
            continuar = bool(input("Pressione Enter para continuar..."))
            limpa_tela()
             
             # Cenario 3
            separador("*")
            cenario_Parente()
            separador("*")
            escolha_cenario3 = input("Qual sua escolha: A, B ou C: ").lower()
            separador("*")
            
            if escolha_cenario3 == 'b' or escolha_cenario3 == 'c':
                pontuacao(escolha_cenario1, pontos, msg_vitoria1, msg_vitoria2)
                
                if(escolha_cenario2 == 'b' ):
                    print('''
                    Ele se ofende e diz: 
                    "Eu só fiz uma pergunta, garota estúpida!"
                    A festa fica com clima estranho com ele te olhando 
                    de um jeito incrivelmente assustador... 
                    
                    Porém, por via das duvidas, você só fez uma pergunta também... haha :) 
                    ''')
                elif(escolha_cenario2 == 'c'):
                    print('''
                    Ele se surpreende com sua resposta e sorri, desconcertado e sem graça...
                    Depois vira as coisas e sai andando. 

                    Acho que ele não irá mais te perturbar...haha
                    Faça valer a pena!
                    ''')
            
                separador("*")
                continuar = bool(input("Pressione Enter para continuar..."))
                print("\x1b[2J")
                print('\n')
                # fim de jogo
                futuro()
            
            elif escolha_cenario3 == 'a':
                print(msg_parente_derrota)
                            
            else:
                print("Resposta inválida!")
        
        elif escolha_cenario2 == 'a':
                print(msg_emprego_derrota)
        
        else:
            print("Resposta inválida!")
    
    elif escolha_cenario1 == 'a':
        print(msg_casa_derrota)
    else:
        print("Resposta inválida!")

def jogo_Olivia():

    pontos = 0
    
    mensagem_final1 = '''
    As suas escolhas no presente definem o seu futuro; E por isso, tudo que você fez até 
    aqui foram atos de coragem e decisões de uma grande mulher, que te tornou possível 
    realizar o seu sonho, saindo de estagiária para diretora de projetos de uma grande 
    empresa e tendo programas com seu nome sendo usados pelo mundo todo! Chupa sociedade!
    PARABÉNS, VOCÊ MERECEU!
    '''

    mensagem_final2 = '''
    As suas escolhas no presente definem seu futuro; felizmente, por mais desafiador que 
    seja escolher ser uma programadora, esteja certa que vale a pena. Não é a diretora de
    projetos da empresa onde trabalha ainda, mas, está se dedicando cada dia mais com foco 
    e coragem nos seus sonhos. Um dia você chega lá, acredite em si mesma!
    '''

    def pontuacao(points, mensagem1, mensagem2):
        global mensagem_final1, mensagem_final2
        if points >= 15 and points < 30:
            print(mensagem2)
        elif points >= 30:
            print(mensagem1)
            
    #1:  a - errado / b -  certo / c - mais ou menos
    #2: a - mais ou menos / b - certo / c - errado
    #3: a - errado / b - mais ou menos / c -  certo 
    
    def cenario_amigos():
        print('''
        CENÁRIO: Casa de amigos
        HORÁRIO E DATA: 20h pm / Sábado
        PERSONAGEM: Olivia

        Você está na casa de uns amigos, fazendo uma social para relembrar os
        velhos tempos de escola. Todos sabem que você é apaixonada por programação,
        mas nem todos concordam que você deveria seguir em frente com os seus sonhos.
        Alisson, seu amigo não tão próximo, chega até você e diz: 
        “Sério que você gosta tanto desse negócio de programação? Porque você não faz 
        jornalismo ou ADM igual as outras meninas da nossa turma do colégio?!”
        Eu acho que combina mais com você, por ser mulher… 
        
        Escolhas: 
        A) Rir do que ele disse e agir com ignorância
        B) Relevar por ele estar meio alterado por conta do álcool e mudar de assunto
        C) Dizer: Talvez você mude de mentalidade quando você usar algum programa 
        que terá meu nome!” com tom de superioridade e orgulho.
        ''')

    def cenario_Faculdade():
        print('''
        CENÁRIO: Faculdade
        HORÁRIO E DATA: 19h pm / Segunda
        PERSONAGEM: Olivia

        Você faz faculdade a noite, e hoje é um dia especial e importante para você,
        pois irá apresentar um projeto para toda a turma e seus professores que decidirá
        se você irá pegar seu diploma ou não, e isso é tudo o que você mais quer! 
        Chegou o seu momento… Você apresenta todo seu programa e explica tudo detalhadamente 
        para todos através de slides. Quando você acaba, você está bem nervosa e ansiosa e 
        todos aplaudem seu programa... Seu professor olha para você e faz um comentário, como: 
        “Excelente, Olivia, você está de parabéns. “
        Porém, outro professor que não é tanto seu fã, diz:
        “Você aprende rápido, Olivia! Entretanto, para estar onde você diz querer estar 
        deverá ser melhor que isso. Ou talvez, optar por fazer algo mais conveniente para 
        você... como vendas já tem um caminho andado por ser bonitinha assim.” - com tom de sarcasmo repugnante.

        Escolhas: 
        A) Você deixa a raiva e a inconformidade te consumir e desistir de tudo por estar no seu limite.
        B) Sorrir para ele e dizer que ele não deveria ser professor.
        C) Reconhecer que isso é machismo e ignorância da parte dele, sorrir e agradecer o elogio.
        ''')

    def cenario_empresa():
        print('''
        CENÁRIO: Empresa
        HORÁRIO E DATA: 07h pm / Segunda
        PERSONAGEM: Olivia

        Já é segunda de novo e o emprego dos seus sonhos te aguarda...
        Você está indo para o seu escritório quando de repente se depara com alguém
        na sala da sua chefe mexendo com algum documento e resolve entrar para ver
        o que está acontecendo, nessa hora você percebe que ele está bem agitado e
        tirando fotos de alguns papéis que estão na mesa com o celular. Ele se assusta
        com a sua entrada e guarda o celular no bolso rapidamente… Com isso você tem a
        certeza que o que ele estava fazendo coisa boa não é…

        Escolhas: 
        A) Perguntar o que ele estava lá e acusá-lo de roubo de dados
        B) Sair desconfiada da sala, porém, deixar quieto já que você é somente uma estagiária recente
        C) Contactar sua chefe dizendo o que viu e dizer sobre sua preocupação com a empresa.
        ''')

    #-------------------------------------------------------------------------------
    # HISTORIA 
    historia_olivia = '''
        Bem-Vinda Olivia!

        Olivia, 25 anos, atualmente estuda ciência da computação e tem um emprego
        como estagiária na Softline (empresa de desenvolvimento de software e sites)
        e desde novinha, sonhava em fazer seus próprios programas para facilitar a vida
        das pessoas cada vez mais. No momento, seu principal objetivo é virar diretora
        de projetos da empresa que trabalha, porém, para que isso aconteça, ela deverá
        seguir alguns passos e se desviar de outros para que ela possa ter o futuro que
        ela tanto almeja…     
        '''

    #------------------------------------------------------------------------------
    # STRINGS CENARIO AMIGOS    
    amigos_a = '''
        Por mais que, o que ele disse foi algo desnecessário, ele era seu amigo e 
        não devia tratá-lo desse modo, pois ele não falou com má intenção. 
        Todos estão olhando para você, sem entender o que aconteceu e a social acaba 
        com um clima chato entre vocês! 
        Seu emocional não está preparado, infelizmente não podemos prosseguir!
        - Perda de amizade. 
        - Fim de jogo
    '''
    amigos_b = '''
        Por mais irritada que você ficou com o comentário desnecessário dele, 
        você não dá bola e segue o assunto perguntando sobre a carreira dele e não 
        se surpreende em saber que ele está desempregado... com isso você percebe que 
        às vezes o que sai das pessoas dizem mais sobre elas do que sobre você. 
        A social acaba e você vai embora feliz, por rever seus amigos de infância.  
        + Sabedoria
    '''
    amigos_c = '''
        Sua atitude de superioridade não é bem vista entre seus amigos e principalmente
        para o cargo que você deseja conseguir. Inferiorizar uma pessoa não é o correto a
        se fazer, mesmo que você tenha “seus motivos”. Tente lidar melhor com os conflitos
        para evitar confrontos… Felizmente, vocês reconhecem estarem alterados por conta do 
        álcool e se acertam, mesmo assim você sai da social desconfortável com a situação.
        - perda de amizade
        '''
    
    #---------------------------------------------------------------------
    # STRINGS CENARIO FACULDADE
    faculdade_a = '''
        Por mais que você tenha razão de estar com raiva, você deveria ter agido de
        outra forma, pois não podemos controlar o que sai de outras pessoas somente 
        de nós mesmo.
        * Expulsa da faculdade
        * perda de oportunidade
        * fim de jogo
        '''
    faculdade_b = '''
        Ele ameaça te reprovar pela sua “falta de respeito” porém nada é feito, pois 
        sabiam como ele era com as alunas. Mas, infelizmente você ficará de exame 
        nas férias.
        * ganho de coragem 
        '''
    faculdade_c = '''
        Ele fica sem graça com sua resposta e reconhece que você tem talento e coragem 
        para o ramo e diz:  “Até a formatura!” e te dá um aperto de mão.
        * ganho de desempenho
        * diploma na mão.
        '''

    #-----------------------------------------------------------------------------
    # STRING CENARIO EMPRESA       
    empresa_a = '''
        Por mais que seu ato de acusação foi precipitado, você estava certa. 
        Ganhou pontos com sua chefe por ter tomado uma atitude.
        * Ganhos de coragem
        '''
    empresa_b = '''
        Infelizmente, seu ato não ajudou muito no seu crescimento na empresa e com isso 
        te acusaram de ser cúmplice por não deleta-lo.
        * Presa
        * Fim de jogo!
        '''
    empresa_c = '''
        Sua chefe agradece a informação e confirma que realmente foi um roubo de dados 
        e que você será contratada quando seu estágio da faculdade acabar!
        * Ganho de promoção
        * PASS
        '''

    

    #print("Bem-vinda, Olivia!")
    
    separador('*')
    print(historia_olivia)
    separador('*')
    continuar = bool(input("Pressione Enter para continuar..."))
    limpa_tela()

    cenario_amigos()
    escolha_amigos = input("Qual sua escolha: A, B ou C: ").lower()
    if(escolha_amigos == 'a'): #errado
        print(amigos_a)
        pontos = 0

    elif(escolha_amigos == 'b'): #certo
        print(amigos_b)
        continuar = bool(input("Pressione Enter para continuar..."))
        pontos = pontos + 10
        limpa_tela()

        cenario_empresa()
        escolha_empresa = input("Qual sua escolha: A, B ou C: ").lower()
        limpa_tela()

        if(escolha_empresa == 'a'):
            print(empresa_a) 
            pontos = pontos + 5 
            continuar = bool(input("Pressione Enter para continuar..."))
            limpa_tela()

            cenario_Faculdade()
            escolha_Faculdade = input("Qual sua escolha: A, B ou C:")
            if(escolha_Faculdade == 'a'):
                print(faculdade_a)
                pontos = 0
                
            elif(escolha_Faculdade == 'b'):
                print(faculdade_b)
                pontos = pontos + 5
                pontuacao(pontos, mensagem_final1, mensagem_final2)
                
            elif(escolha_Faculdade == 'c'):
                print(faculdade_c)
                pontos = pontos + 10
                print(pontos)
                pontuacao(pontos, mensagem_final1, mensagem_final2)
                
            else:
                limpa_tela()
                print("Opção invalida! Tente novamente!")             

        elif(escolha_empresa == 'b'):
            print(empresa_b)
            pontos = 0

        elif(escolha_empresa == 'c'):
            print(empresa_c)
            pontos = pontos +10
            continuar = bool(input("Pressione Enter para continuar..."))
            limpa_tela()

            
            cenario_Faculdade()
            escolha_Faculdade = input("Qual sua escolha: A, B ou C:")
            if(escolha_Faculdade == 'a'):
                print(faculdade_a)
                pontos = 0

            elif(escolha_Faculdade == 'b'):
                print(faculdade_b)
                pontos = pontos + 5
                pontuacao(pontos, mensagem_final1, mensagem_final2)
                
            elif(escolha_Faculdade == 'c'):
                print(faculdade_c)
                pontos = pontos + 10
                pontuacao(pontos, mensagem_final1, mensagem_final2)
                
            else:
                limpa_tela()
                print("Opção invalida! Tente novamente!")
                
        else:
            print("Opção invalida! Tente novamente!")    

    elif(escolha_amigos == 'c'): #mais ou menos
        print(amigos_c)
        pontos = pontos + 5
        continuar = bool(input("Pressione Enter para continuar..."))
        limpa_tela()
        
        cenario_empresa()
        escolha_empresa = input("Qual sua escolha: A, B ou C: ").lower()
        limpa_tela()
        if(escolha_empresa == 'a'):
            print(empresa_a) 
            pontos = pontos + 5  
            continuar = bool(input("Pressione Enter para continuar..."))
            limpa_tela()

            cenario_Faculdade()
            escolha_Faculdade = input("Qual sua escolha: A, B ou C:")
            if(escolha_Faculdade == 'a'):
                print(faculdade_a)
                pontos = 0

            elif(escolha_Faculdade == 'b'):
                print(faculdade_b)
                pontos = pontos + 5
                pontuacao(pontos, mensagem_final1, mensagem_final2)
                
            elif(escolha_Faculdade == 'c'):
                print(faculdade_c)
                pontos = pontos + 10
                print(pontos)
                pontuacao(pontos, mensagem_final1, mensagem_final2)
                
            else:
                limpa_tela()
                print("Opção invalida! Tente novamente!")            

        elif(escolha_empresa == 'b'):
            print(empresa_b)
            pontos = 0

        elif(escolha_empresa == 'c'):
            print(empresa_c)
            pontos = pontos +10
            continuar = bool(input("Pressione Enter para continuar..."))
            limpa_tela()
            
            cenario_Faculdade()
            escolha_Faculdade = input("Qual sua escolha: A, B ou C:")
            if(escolha_Faculdade == 'a'):
                print(faculdade_a)
                pontos = 0

            elif(escolha_Faculdade == 'b'):
                print(faculdade_b)
                pontos = pontos + 5
                pontuacao(pontos, mensagem_final1, mensagem_final2)
                
            elif(escolha_Faculdade == 'c'):
                print(faculdade_c)
                pontos = pontos + 10
                print(pontos)
                pontuacao(pontos, mensagem_final1, mensagem_final2)
                
            else:
                limpa_tela()
                print("Opção invalida! Tente novamente!")
        
    else:
        limpa_tela()
        print('Opção invalida! Tente novamente!')
            
def Jogo_Carla():
    pontos = 0

    msg_final15 = '''
        “Infelizmente, você não valorizou as oportunidades que te 
        apareceram e nem fez as suas próprias oportunidades… 
        Tente se manter focada no que você realmente quer e procure estudar 
        e ser mais responsável com seus objetivos!
        
        OBRIGADA POR JOGAR!
        '''
    msg_final30 = '''
        Uau, que decisões desafiadoras você encarou em? 
        Que bom que você está muito bem focada no seus objetivos e 
        com caminho andado para se dar bem na empresa com o curso que começou. 
        Continue assim e só terá sucesso na sua caminhada!
        PARABÉNS!

        OBRIGADA POR JOGAR!
        '''
    msg_final20 = '''
        Você continua com os clientes freelancers, porém, perdeu a oportunidade de 
        entrar em uma empresa que seria ótima para sua carreira. 
        Infelizmente, não foi dessa vez que você realizou seu sonho.
        OBRIGADA POR JOGAR!
        '''

    msg_final4 = '''
        Por mais que você não tenha escolhido fazer um curso para aprender mais 
        sobre JavaScript, a empresa gostou tanto de você e por isso decidiram te 
        dar uma bolsa para aprender melhor sobre JavaScript e aprimorar seus 
        conhecimentos em Web Designer. 
        Parabéns por ter conseguido realizar seu sonho! Você merece!

        OBRIGADA POR JOGAR!
        '''
    msg_final5 = '''
        É uma pena ter perdido alguns clientes…
        Porém, você realizou seu sonho em trabalhar em uma empresa
        do ramo que você deseja seguir e com isso terá a oportunidade
        de fazer as telas mais lindas da Web, né?!
        Que sucesso!!!
        Arrasa mulher!

        OBRIGADA POR JOGAR!
        '''
    msg_final6 = '''
        Alem de perder alguns clientes importantes do trabalho Freelancer,
        também perdeu a oportunidade de entrar em uma empresa que seria o
        ponta pé para realizar seus objetivos... 
        Infelizmente, não foi dessa vez que você realizou seu sonho.

        OBRIGADA POR JOGAR!
        '''
    
    historia_Carla = '''
        Bem-Vinda Carla!

        Carla é uma Jovem adulta de 30 anos, formada em design gráfico 
        e fazendo freelancer como criadora de conteúdo digital na internet. 
        Seu hobby é desenhar tudo que estiver em sua mente. 
        É apaixonada por desenvolvimento de sites, principalmente arquitetura 
        e design e, seu maior sonho é aprender a desenvolver as páginas web 
        mais lindas da internet mundial. E para isso, seu principal objetivo 
        agora é entrar em uma empresa de tecnologia que lhe permitirá começar
        a viver o seu sonho. 
        Porém, para que isso aconteça, ela deverá seguir alguns passos e se 
        desviar de outros para que ela possa ter o futuro que ela tanto almeja… 
        '''
    casa_a = '''
        Infelizmente, esse “pouco” a mais na cama levou a metade do dia… 
        Você ultrapassou o tempo limite combinado para entregar o trabalho
        a alguns cliente e com isso você perdeu a confiança deles e eles pagou menos
        pelo atraso na entrega. Porém, felizmente deu tempo de enviar os currículos… 
        por desapontar os clientes e a si mesma, você passa o resto da noite 
        pensando como poderia ter agido diferente...
        * Perda de dinheiro
        * Perda de desempenho
        + 5 pontos por enviar os currículos
        '''
    casa_b = '''
        Já ouviu aquele ditado? 
        “Não deixe para amanhã o que você pode fazer hoje?”
        Infelizmente, você não entregou a tempo os trabalhos freelance e os 
        clientes estão descontentes e cancelaram tudo. E o processo seletivo 
        da empresa onde você quer trabalhar fechou ontem, e você não participou… 
        * Fim de jogo. 
        * Perda de desempenho
        * Perda de serviço
        * Fim de jogo
        '''
    casa_c = '''
        Com certeza suas prioridades são mais importantes que dormir… 
        com isso você entregou seus trabalhos freelancer em dia para os clientes 
        e eles aprovaram com excelência, além de você ter enviado seu currículo a 
        tempo para participar do processo seletivo e conseguir uma entrevista. 
        Agora você pode voltar a dormir e aproveitar a chuvinha mais um pouco… 
        + 10 pontos
        * Ganho de desempenho 
        * Processo do sonho 50%
        '''

    estudo_a = '''
        Você achou caro? R$20,90 por mês? Uau, mão de vaca! Isso é para seu aprimoramento 
        profissional, não quer ser uma designer de sites? 
        Para sua sorte tem muitos cursos gratuitos no youtube…  
        * Perda de oportunidade
        + 5 pontos por olhar o e-mail=
        '''
    estudo_b = '''
        Você se inscreve no curso e tem até certificado, além do conhecimento 
        que você necessita para conquistar a vaga dos seus sonhos… 
        Sem esforços não há conquista, né mesmo? 
        * Ganho de desempenho
        + 10 pontos
        * Processo do sonho 80%
        '''
    estudo_c = '''
        Infelizmente era uma oportunidade que você deixou escorrer pelos seus 
        dedos… diga adeus aos seus sonhos… Com esse interesse é difícil conseguir 
        o que deseja!
        * perda de oportunidade
        * Fim de jogo
        '''

    entrevista_a = '''
        Que bom que você foi uma mulher premeditada e chegou antes da chuva na entrevista… com isso, deu tempo de respirar fundo e mandar o nervosismo embora e fazer a entrevista com sucesso e com a roupa seca aliás.
        Você volta para casa, orando e torcendo que tudo dê certo e de repente seu celular toca e você atende na expectativa e ouvindo a voz do outro lado da linha, sorri percebendo que era da empresa, te dizendo que gostaram de você e querem 
        te contratar de imediato! Uau, que sucesso!
        * Ganho de desempenho
        * Passou na entrevista
        + 10 pontos
        '''
    entrevista_b = '''
        Se você enviou currículo é porque você está precisando né? 
        Infelizmente, como você saiu em cima da hora, a chuva veio e alagou 
        a rua onde você passava e acabou se atrasando para a entrevista. 
        O atraso, por mais que tivesse um “motivo”, deu uma má impressão e eles 
        não prosseguiram com você na seleção da entrevista...
        * Perda de oportunidade
        * Perda de desempenho
        + 5 pontos por fazer a entrevista (pelo menos)
        '''
    entrevista_c = '''
        Sério isso? Não é assim que você terá um emprego e muito menos na 
        empresa onde quer trabalhar… 
        * Perdeu tudo!
        * fim de jogo
        '''
    

    def c_cenario_Casa():
        print('''
        CENÁRIO: Casa
        HORÁRIO E DATA: 8h am / Segunda-Feira 
        PERSONAGEM: Carla

        É segunda de manhã, você vê pela janela que o tempo está nublado e isso te atinge 
        como uma preguiça imensa e vontade de voltar para a cama… Você deita novamente na 
        cama fecha os olhos, porém, lembra que tem algumas coisas importantes para fazer hoje
        como entregar algumas propostas para clientes e enviar alguns currículos para a empresa 
        que tanto quer trabalhar... 
        Escolhas: 

        A) Ficar na cama mais um pouco...
        B) Deixar a preguiça te vencer e adiar as tarefas de hoje para amanhã e voltar a dormir...
        C) Levantar, tomar um café e priorizar tudo que precisa 
        fazer hoje antes de dormir de novo… 
        ''')
    
    def cenario_Estudo():
        print('''
        CENÁRIO: Sala de Estudo
        HORÁRIO E DATA: 8h am / Terça-Feira 
        PERSONAGEM: Carla

        Mais um dia começa e como de costume, você acorda e faz sua rotina matinal: 
        verifica seus e-mail tomando um café preto e comendo uma torrada maravilhosa 
        que você aprendeu a fazer esses dias… e falando em aprender, você recebeu 
        um e-mail de algum anunciante dizendo que estava aberta as incrições 
        para fazer o curso de JavaScript e CSS… Que coincidência… que maravilha… ou não? 
        
        Escolhas: 
        A) Abrir e-mail, porém achar muito caro..."
        B) Abrir o e-mail e aproveitar essa oportunidade excelente para seu
           currículo e para o seus objetivos futuros”
        C) Apagar e-mail e ignorar
        ''') 
    
    def cenarioA_Entrevista():
        print('''
        CENÁRIO: Entrevista
        HORÁRIO E DATA: 8h am / Quarta-Feira
        PERSONAGEM: Carla

        O dia de ontem passou rápido e hoje é um grande dia… Seu telefone toca:
        “trim trim trim” 
        você o atende e fica feliz em saber que é uma empresa te convidando a fazer
        uma entrevista, hoje às 13h00 PM que é daqui a 1h \º0º/, meu Deus.
        Você aceita e desliga, em seguida você almoça e vai direto para o banho 
        agradecendo que por mais irresponsável que você tenha sido ontem, você ganhou 
        mais uma chance de acertar… “Hoje é o dia!”  
        Quando sai do banho percebe que hoje irá chover de novo e parece que o tempo está 
        para tempestade... 
        
        Escolhas: 
        A)Sair mais cedo para não pegar chuva
        B)Chegar em ponto, para não acharem que você está desesperada (por que você está mesmo)
        C) Enrolar e depois ligar pedindo para remarcar a entrevista por conta da chuva 
           (warn - perder oportunidade)
        ''')
    
    def cenarioB_Entrevista():
        print('''
        CENÁRIO: Entrevista
        HORÁRIO E DATA: 8h am / Quarta-Feira
        PERSONAGEM: Carla

        O dia de ontem passou rápido e hoje é um grande dia… Seu telefone toca:
         “trim trim trim” 
        você o atende e fica feliz em saber que é uma empresa te convidando a fazer 
        uma entrevista, hoje às 13h00 PM que é daqui a 1h \°0°/, meu Deus. 
        Você aceita e desliga, em seguida você almoça e vai direto para o banho agradecendo
        que você ganhou a oportunidade que você mais queria… “Hoje é o dia!”  
        Quando sai do banho percebe que hoje irá chover de novo e parece que o tempo 
        está para tempestade... 
        
        Escolhas:
        A) Sair mais cedo para não pegar chuva
        B) Chegar em ponto, para não acharem que você está desesperada (por que você está mesmo)
        C) Enrolar e depois ligar pedindo para remarcar a entrevista por conta da chuva 
           (warn - perder oportunidade)
        ''')


    separador('*')
    print(historia_Carla)
    separador('*')
    continuar = bool(input("Pressione Enter para continuar..."))
    limpa_tela()

    c_cenario_Casa()
    escolha_casa = input("Qual sua escolha: A, B ou C: ").lower()
    if(escolha_casa == 'a'):
        print(casa_a)
        continuar = bool(input("Pressione Enter para continuar..."))
        limpa_tela()

        cenario_Estudo()
        escolha_estudo = input("Qual sua escolha: A, B ou C: ").lower()
        if(escolha_estudo == 'a'):
            print(estudo_a)
            pontos = pontos + 5
            continuar = bool(input("Pressione Enter para continuar..."))
            limpa_tela()
            
            cenarioB_Entrevista()
            escolha_entrevista = input("Qual sua escolha: A, B ou C: ").lower()
            if(escolha_entrevista == 'a'):
                print(entrevista_a)
                continuar = bool(input("Pressione Enter para continuar..."))
                limpa_tela()
                
                
            elif(escolha_entrevista == 'b'):
                print(entrevista_b)
                pontos = pontos + 5
                continuar = bool(input("Pressione Enter para continuar..."))
                limpa_tela()
                

            elif(escolha_entrevista == 'c'):
                pontos = 0
                print(entrevista_c)

        elif(escolha_estudo == 'b'):
            print(estudo_b)
            pontos = pontos + 10
            continuar = bool(input("Pressione Enter para continuar..."))
            limpa_tela()
            
            cenarioA_Entrevista()
            escolha_entrevista = input("Qual sua escolha: A, B ou C: ").lower()
            if(escolha_entrevista == 'a'):
                print(entrevista_a)
                continuar = bool(input("Pressione Enter para continuar..."))
                limpa_tela()
                
            elif(escolha_entrevista == 'b'):
                print(entrevista_b)
                pontos = pontos + 5
                continuar = bool(input("Pressione Enter para continuar..."))
                limpa_tela()

            elif(escolha_entrevista == 'c'):
                pontos = 0
                print(entrevista_c)

        elif(escolha_estudo == 'c'):
            print(estudo_c)
            pontos = 0
        else:
            print("Opçaõ invalida! Tente novamente!")
    elif(escolha_casa == 'b'):
        print(casa_b)
        pontos = 0
    elif(escolha_casa == 'c'):
        print(casa_c)
        continuar = bool(input("Pressione Enter para continuar..."))
        limpa_tela()

        cenario_Estudo()
        escolha_estudo = input("Qual sua escolha: A, B ou C: ").lower()
        if(escolha_estudo == 'a'):
            print(estudo_a)
            continuar = bool(input("Pressione Enter para continuar..."))
            limpa_tela()
            
            cenarioA_Entrevista()
            escolha_entrevista = input("Qual sua escolha: A, B ou C: ").lower()
            if(escolha_entrevista == 'a'):
                print(entrevista_a)
                continuar = bool(input("Pressione Enter para continuar..."))
                limpa_tela()
                print(msg_final4)
                
            elif(escolha_entrevista == 'b'):
                print(entrevista_b)
                pontos = pontos + 5
                continuar = bool(input("Pressione Enter para continuar..."))
                limpa_tela()
                print(msg_final15)

            elif(escolha_entrevista == 'c'):
                print(entrevista_c)

        elif(escolha_estudo == 'b'):
            print(estudo_b)
            pontos = pontos + 10

            cenarioA_Entrevista()
            escolha_entrevista = input("Qual sua escolha: A, B ou C: ").lower()
            if(escolha_entrevista == 'a'):
                print(entrevista_a)
                continuar = bool(input("Pressione Enter para continuar..."))
                limpa_tela()
                print(msg_final4)
                
            elif(escolha_entrevista == 'b'):
                print(entrevista_b)
                pontos = pontos + 5
                continuar = bool(input("Pressione Enter para continuar..."))
                limpa_tela()
                print(msg_final15)

            elif(escolha_entrevista == 'c'):
                pontos = 0
                print(entrevista_c)

            
        elif(escolha_estudo == 'c'):
            print(estudo_c)
        else:
            print("Opçaõ invalida! Tente novamente!")
    else:
        print("Opçaõ invalida! Tente novamente!")
    
    #casa_a 5 + estudo_a 5 + entrevista_b 5 = perdeu tudo
    if(escolha_casa == 'a' and escolha_estudo == 'a' and escolha_entrevista == 'b'):
        print(msg_final15)
    
    #casa_a 5 + estudo_b 10 + entrevista_b 5 = perdeu cliente, fez curso, perdeu emprego 
    if(escolha_casa == 'a' and escolha_estudo == 'b' and escolha_entrevista == 'b'):
        print(msg_final20)
    
    #casa_a 5 + estudo_a 5 + entrevista_a 10 = perdeu cliente, perdeu curso, ganhou emprego
    if(escolha_casa == 'a' and escolha_estudo == 'a' and escolha_entrevista == 'a'):
        print(msg_final4)
    
    #casa_a 5 + estudo_b 10 + entrevista_a 10 = perdeu cliente, fez curso, ganhou emprego
    if(escolha_casa == 'a' and escolha_estudo == 'b' and escolha_entrevista == 'a'):
        print(msg_final5)
    
    #casa_c 10 + estudo_a 5 + entrevista_b 5 = continua cliente, perdeu estudo, perdeu emprego
    if(escolha_casa == 'c' and escolha_estudo == 'a' and escolha_entrevista == 'b'):
        print(msg_final20)
    
    #casa_c 10 + estudo_b 10 + entrevisa_a 10 = ganhou tudo
    if(escolha_casa == 'c' and escolha_estudo == 'b' and escolha_entrevista == 'a'):
        print(msg_final30)
    
    #casa_c 10 + estudo_a 5+ entrevista_a 10 = continua cliente, perdeu curso, ganhou emprego
    if(escolha_casa == 'c' and escolha_estudo == 'a' and escolha_entrevista == 'a'):
        print(msg_final4)
    
    #casa_c 10 + estudo_b 10 + entrevista_b 5 = continua cliente, fez curso, perdeu emprego 
    if(escolha_casa == 'c' and escolha_estudo == 'a' and escolha_entrevista == 'a'):
        print(msg_final20)

def jogo():
    
    resposta = 'sim'
    while resposta == 'sim':
        personagem = escolha_personagem()
        continuar = bool(input("Pressione Enter para continuar..."))
        limpa_tela()
        if personagem == "Jênnifer":
            separador("*")
            Jogo_Jennifer()
            separador("*")
        elif personagem == "Olivia":
            separador("*")
            jogo_Olivia()
            separador("*")
        elif personagem == "Carla":
            separador("*")
            Jogo_Carla()
            separador("*")
        else: 
            print("Opçao invalida! Escolha novamente!") 
        resposta = input('Deseja jogar novamente? [sim/não]:')

    print("\x1b[2J")
    print("Fim de jogo!")
   
# -------------------------------------------------------------
# INICIO
jogo()