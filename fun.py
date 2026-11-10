import random
class jogador():
    def __init__(self, nome = '',vida = 100, atq = 0,df = 0):
        self.nome = nome
        self.vida = vida
        self.atq = atq
        self.df = df
    def equipamentes(self,arco = 70, espada = 50,escudo = 10):
        escolha = input('Escolha seu equipamento: \n1 - Arco\n2 - Espada\n3 - Escudo\n').strip()
        if escolha in ["1","arco"]:
            self.atq = arco
        elif escolha in ["2","espada"]:
            self.atq = espada
        elif escolha in ["3","escudo"]:
            self.df = escudo
        else:
            print("escolha errada user 1/2/3")
        print(f'Você escolheu o equipamento {escolha} e agora tem {self.atq} de ataque e {self.df} de defesa')
    def class_querreiro(self,atq = 70 , df = 100,vida = 100):
        self.atq += atq
        self.df += df
        self.vida += vida
        print(f'Você escolheu a classe Guerreiro e agora tem {self.atq} de ataque, {self.df} de defesa e {self.vida} de vida')
    def class_arco(self,atq = 300 , df = 50,vida = 50):
        self.atq += atq
        self.df += df
        self.vida += vida
        print(f'Você escolheu a classe Arqueiro e agora tem {self.atq} de ataque, {self.df} de defesa e {self.vida} de vida')
    def class_escudo(self,atq = 50 , df = 300,vida = 100):
        self.atq += atq
        self.df += df
        self.vida += vida
        print(f'Você escolheu a classe Escudeiro e agora tem {self.atq} de ataque, {self.df} de defesa e {self.vida} de vida')
    def escolha_classe(self):
        escolha = input("escolha sua classe: \n1 - Guerreiro\n2 - Arqueiro\n3 - Escudeiro\n").strip()
        if escolha in ["1","guerreiro"]:
            self.class_querreiro()
        elif escolha in ["2","arqueiro"]:
            self.class_arco()
        elif escolha in ["3","escudeiro"]:
            self.class_escudo()
        else:
            print("escolha errada user 1/2/3")

class inimigo_slime():
    def __init__(self, nome = 'Slime', atq = 10 , df = 5):
        self.nome = nome
        self.atq = atq
        self.df = df
    def tipos_de_ataque(self):
        def ataque_basico(self,atq_basico = 10):
            self.atq = atq_basico
            print(f'O inimigo {self.nome} usou ataque básico e agora tem {self.atq} de ataque')
        def ataque_especial(self,atq_especial = 20):
            self.atq = atq_especial
            print(f'O inimigo {self.nome} usou ataque especial e agora tem {self.atq} de ataque')
        def ataque_nulo(self,atq_nulo = 0):
            self.atq = atq_nulo
            print(f'O inimigo {self.nome} usou ataque nulo e agora tem {self.atq} de ataque')
        escolha = random.choice([ataque_basico, ataque_especial, ataque_nulo])
        escolha(self)

class inimigo_goblin():
    def __init__(self, nome = 'Goblin', atq = 20 , df = 10):
        self.nome = nome
        self.atq = atq
        self.df = df
if __name__ == "__main__":
    jogador1 = jogador()
    jogador1.nome = input("Digite o nome do jogador: ")
    jogador1.equipamentes()
    jogador1.escolha_classe()
    inimigo1 = inimigo_slime()
    inimigo1.tipos_de_ataque()
