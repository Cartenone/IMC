print("Vuoi calcolare il tuo IMC?")
risposta=input().capitalize()

if risposta=="Si":
    print("Inserisci la tua eta:")
    eta=int(input())
    print("Inserisci il tuo peso in Kg:")
    peso=int(input())
    print("Inserisci la tua altezza in m")
    altezza=float(input())
    while altezza >2.8:
        print("Valore di altezza:",altezza,"errato")
        print("Inserire di nuovo")
    
    imc=float(peso/(altezza*altezza))
    print("Il tuo IMC è:",imc)
    
else:
    print("Non hai voluto calcolare il tuo IMC")

if imc<16.0:
    print("Grave Magrezza!")
elif 16.0<imc<18.49:
    print("Sottopeso")
elif 18.50<imc<24.99:
    print("Normopes")
elif 25.0<imc<29.99:
    print("Sovrappeso")
elif 30.0<imc<34.99:
    print("Obeso Classe I")
elif 35.0<imc<34.99:
    print("Obeso Classe II")
elif imc>=40.0:
    print("Obeso Classe III")
    
