import random
def CoolCade():
   #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 16
  rnd = rnd = random.randint(0, last)
  print(quotes[rnd])
  rnd = rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  CoolCade()
