def escreva(txt):
    print("_"*txt )
    print(f"  {frase}")
    print("_"*txt )

    
frase= str(input("escreva uma frase:"))
escreva(len(frase)+ 4)
