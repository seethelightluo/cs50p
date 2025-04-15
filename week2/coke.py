def caculate(due):
    while due > 0:
        print("amount due:", due)
        money = int(input("Insert coin:"))
        if money == 25 or money == 10 or money == 5:
            due = due - money
        if due < 0:
            break
    return due


def main():
    due = 50
    due = caculate(due)
    if due <=0:
        print("Change owed:", -due)



if __name__ == "__main__":
    main()











