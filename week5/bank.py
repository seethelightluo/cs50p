def main():
 answer=input("Greeting:")
 k=answer.lower().strip()
 print("$",value(k))


def value(k):
  if k[0:5]=="hello":
   return 0
  elif k[0]=="h":
   return 20

  else:
    return 100


if __name__ == "__main__":
    main()
