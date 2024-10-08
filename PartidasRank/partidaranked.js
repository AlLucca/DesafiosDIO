let vitorias = 0
let derrotas = 0
let saldo = vitorias - derrotas

console.log("O Herói tem de saldo de "+ saldo +" está no nível de "+ classificarRanked(vitorias,derrotas))

function classificarRanked(vit, der){
    saldo = vit - der
    if(saldo >= 101){
        return "Imortal"
    }
    else if(saldo >=91 && saldo <= 100){
        return "Lendário"
    }
    else if(saldo >=81 && saldo <= 90){
        return "Diamante"   
    }
    else if(saldo >=51 && saldo <= 80){
        return "Ouro"
    }
    else if(saldo >=21 && saldo <= 50){
        return "Prata"
    }
    else if(saldo >=11 && saldo <= 20){
        return "Bronze"
    }
    else{
        return "Ferro"
    }
}
