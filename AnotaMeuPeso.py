import time
import datetime

def Mostra_Data(x = []):
    return f'{x[0]}/{x[1]}/{x[2]}'

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
            elif y > 600:
                print('\033[31mImpossível, a pessoa mais pesada do mundo tem 600KL\033[m')
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

data_Primeiro_Peso = f'{datetime.date.today()}'.split('-')
nome = Análise_nome('Digite seu nome: ')
primeiro_Peso = Análise_float('Quanto você está pesando hoje: ')
print(f'\033[32mNa data de {Mostra_Data(data_Primeiro_Peso)} você está pesando {primeiro_Peso} \nParabens!! para seu 1º dia até que você tá bem, continue assim {nome}\033[m')