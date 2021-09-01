import random

def multipless():
  global multiples
  multiples = []
  for i in onetoeleven:
    multiple = randomnum * i
    multiples.append(multiple)
  if len(multiples) > 0:
      randomnumber2 = random.randint(0,len(multiples)-1)
      randommultiple = multiples[randomnumber2]
      removal = randommultiple/randomnum
      onetoeleven.remove(removal)
      print('A multiple of your number is', randommultiple)
      check()
  elif len(multiples) < 1:
    print ('No more multiples to give. :(')
    global boo1
    boo1 = False
    k.remove(1)
    try:
      if len(divisibles) > 0:
        print ('But...')
        divisbleby()
      else:
        final()
    except:
      check()

def divisbleby():
  global divisibles
  divisibles = []
  for i in rangee:
    if randomnum%i == 0:
      divisibles.append(i) 
  if len(divisibles) > 0:
    randomnumber1 = random.randint(0, len(divisibles)-1)
    randomdivisible = divisibles[randomnumber1]
    rangee.remove(randomdivisible)
    print ('The number is divisible by ', randomdivisible)
    check()
  elif len(divisibles) < 1:
    print('No more divisibles!!!')
    global boo2
    boo2 = False
    k.remove(2)
    try:
      if len(multiples) > 0:
        print ('But...')
        multipless()
      else:
        final()
    except:
        check()

def final():
  guess = input('You have received all the hints possible. This is your final chance. What is the number: ')
  if int(guess) == int(randomnum):
    print('Congratulations!')
  else:
    print ('Nope. Maybe next time.')

def check():
  #print(boo1, boo2)
  guess = input('Guess the number: ')
  if int(guess) == int(randomnum):
    print('Congratulations!')
  else:
    print('Whoops, that is wrong.')
    try:
      j = random.choice(k)
      #print (j)
    finally:
      if (boo1 == False and boo2 == False) and (len(k) == 0):
        final()
      elif j == 1 and boo1:
          multipless()
      elif j == 2 and boo2:
          divisbleby()


def getnumber(minvalue, maxvalue):
  maxvalue += 1
  lst = list(range(minvalue, maxvalue))
  randomnumber0 = random.randint(0, len(lst)-1)
  global randomnum
  randomnum = lst[randomnumber0]
  #print(randomnum)
  check()

def main():
  try:
    global min
    min = int(input('Welcome to the number guessing game. Put in the minimium number for the number range: '))
    global max
    max = int(input('Put in the maximum number: '))
    max1 = max + 1
    global rangee
    rangee = list(range(2,max1))
    global onetoeleven
    onetoeleven = list(range(1,11))
    getnumber(min, max)
  except ValueError:
    print('Please put in a number!!!!!!!')
    main()

if __name__ == "__main__":
  boo1 = True
  boo2 = True
  k = [1,2]
  main()
  