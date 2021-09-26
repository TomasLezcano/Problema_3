n=int(input("introduce el numero de escalones "))
for i in range(n+1):
    espacio=n-i
    print(" "*espacio+"#"*i)