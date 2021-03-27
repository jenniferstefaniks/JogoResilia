
global points

def limpa_tela():
    print('clear')
    
def separador():
    print('-'*50)

def tema():
    string = 'BEM-VINDO AO JOGO: VIDA DE PROGRAMADORA'
    string.title()    

def escolha_personagem():

    while True:
        separador()
        tema()
        separador()
        print("Selecione seu personagem: ")
        print('''
        A) Olivia - (Jovem estagiaria de sucesso)
        B) Carla - (Batalhadora e determinada)
            ''')
        escolha_person = input("Personagem (A ou B ): ").upper()[0]

        if escolha_person in 'A':
            person = "Olivia"      
            break
        elif escolha_person in 'B':
            person = "Carla"
            break
        else:
            print("\x1b[2J")
            print("Não existe essa opção! tente novamente!")
    
    
    return person  

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
    
    separador()
    print(historia_olivia)
    separador()
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


    separador()
    print(historia_Carla)
    separador()
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
    
   
    while True:
        
        personagem = escolha_personagem()
        
        continuar = bool(input("Pressione Enter para continuar..."))
        
        limpa_tela()

        if personagem == "Olivia":
            separador()
            jogo_Olivia()
            separador()
        elif personagem == "Carla":
            separador()
            Jogo_Carla()
            separador()
        else: 
            print("Opçao invalida! Escolha novamente!") 
        resposta = input('Deseja jogar novamente? [sim/não]:').upper()[0]
        if resposta in 'N':
            break

    print("\x1b[2J")
    print("Fim de jogo!")
   
# -------------------------------------------------------------
# INICIO
jogo()