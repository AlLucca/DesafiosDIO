class hero {
    constructor(nome, idade, tipo){
        this.nome = nome
        this.idade = idade
        this.tipo = tipo
    }

    atacar(){
        let ataque = ""
        if (this.tipo === "mago"){
            ataque = "magia"    
        }
        if (this.tipo === "guerreiro"){
            ataque = "espada"    
        }
        if (this.tipo === "monge"){
            ataque = "artes marciais"    
        }
        if (this.tipo === "ninja"){
            ataque = "shuriken"    
        }
        console.log(`O ${this.tipo} ${this.nome} atacou usando ${ataque}`)
    }
}
let heroi = new hero("ronaldo",35,"guerreiro")
heroi.atacar()
