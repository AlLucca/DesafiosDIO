class hero:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        ataque = ""
        if (self.tipo == "mago"):
            ataque = "magia"    
        
        if (self.tipo == "guerreiro"):
            ataque = "espada"    
        
        if (self.tipo == "monge"):
            ataque = "artes marciais"    
        
        if (self.tipo == "ninja"):
            ataque = "shuriken"    
        
        print(f'O {self.tipo} {self.nome} atacou usando {ataque}')
    

heroi = hero("Ronaldo",35,"guerreiro")
heroi.atacar()