def main():
 s=input("Input: ")
 print(shorten(s))


def shorten(s):
   ans="".join([ch for ch in s if ch.lower() not in "aeiou"])
   return ans


if __name__ == "__main__":
    main()


