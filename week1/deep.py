answer=input("What is the answer to the Great Question of Life, the Universe and Everything?  ")
k=answer.lower().strip()
if k=="42":
 print("Yes")
elif k=="forty two":
 print("Yes")
elif k=="forty-two":
 print("Yes")
else:
 print("no")
