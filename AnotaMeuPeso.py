def Análise_float(x = str):
    while True:
        try:
            y = float(input(x))
        except:
            print('\033[31mSó numeros decimais\033[m')
        else:
            if y < 0:
                print('\033[31mImpossível, ninguém pesa menos que zero\033[m')
            elif y == 0:
                print('\033[31mImpossível, ninguém pesa exatamente 0\033[m')
            elif y > 727:
                print('\033[31mImpossível, a pessoa mais pesada do mundo tem 727KL\033[m')
            else:
                return y
                break

def Análise_nome(x = 'Digite seu nome: '):
    while True:
        nome = str(input(x)).strip().capitalize()
        if nome == '':
            print('\033[31mNome sem valor\033[m')
        elif len(nome) > 30:
            print('\033[31mMenor que 30 caracteres\033[m')
        else:
            return nome
            break

Peso = Análise_float('Digite seu peso: ')
Altura = Análise_float('Digite sua altura: ')

imc = Peso / (Altura * Altura)

if imc <= 18.5:
    Classificação_de_peso = 'Abaixo do peso'
    dica = 
elif imc >= 18.6 and imc <= 24.9:
    Classificação_de_peso = 'Normal'
elif imc >= 24.9 and imc <= 29:
    Classificação_de_peso = 'Sobre Peso'  
elif imc >= 30 and imc <= 34.9:
    Classificação_de_peso = 'Obesidade Primeiro Grau'  
elif imc >= 35 and imc <= 39.9:  
    Classificação_de_peso = 'Obesidade Segundo Grau'
elif imc >= 40:
    Classificação_de_peso = 'Obesidade mobirda'