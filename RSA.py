from random import randint
import math


def checkPrimo(num):
  if(num <=1):
    return False
  for i in range(2, int(num**0.5) + 1):
    if(num % i == 0):
      return False
  return True

def creatPri():
  num1 = randint(0,1000)
  while(not checkPrimo(num1)):
    num1 = num1 + 1
  return num1

def phi(p,q):
  return (q-1)*(p-1)

def creatE(N):
  E = randint(1,N -1)
  while(not math.gcd(E,N) == 1):
    E = randint(1,N - 1)
  return E


def mod(a,b):
  if(a<b):
    return a
  else:
    return a%b
  
def modD(E,N):
  D = 0

  while(not mod((D*E),N) == 1):
    D = D + 1
  return D

def criptografia(msg,E,n):
  cripto = []
  inte = []
  for i in msg:
    inte.append(ord(i))
    cripto.append((mod(ord(i)**E,n)))
  return cripto

def descripto(cy,private_key,n):
  msg = []
  for i in cy:
    k = i**private_key
    msg.append(chr(mod(k,n)))
  return msg


if __name__=='__main__':
    p = creatPri()
    q = creatPri()
    n = p*q
    public_key_one = phi(p,q)
    public_key_two = creatE(public_key_one)
    private_key = modD(public_key_two,public_key_one)
    public_key = [public_key_one,public_key_two]


    print('Suas chaves públicas:', public_key)
    print('Sua chave privada:', private_key)

    msg = input("\nInsira sua mensagem: ")

    text_cipher = criptografia(msg,public_key_two,n)
    print('\nMensagem encriptada:', text_cipher)

    original_text = descripto(text_cipher,private_key,n)
    print('\nSua mensagem original:', original_text)