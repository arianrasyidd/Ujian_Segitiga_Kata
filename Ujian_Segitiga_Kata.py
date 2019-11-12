kata = input('Sebutkan kalimat : ')

def segitigaKata(kata):
    kalimat = ("Purwadhika Startup and Coding School @BSD").replace (' ', '')
    listKalimat = list(kalimat)

    emptyList = []
    for a in range(len(listKalimat)):
        X = int((a * (a + 1 )) / 2)
        emptyList.append(X)

n=0
if len(listKalimat) not in emptyList:
    print ('Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.')
else:
    n= emptyList.index(len(listKalimat))
def segitigaAtas(n):   
    num = 0
    for i in range(0, n): 
        for j in range(0, i+1): 
            print(listKalimat[num], end=" ")  
            num = num + 1
        print("\r") 
def segitigaBawah(n):   
    num = 0
    for i in range(n, 0, -1): 
        for j in range(1, i+1): 
            print([num], end=" ")  
            num = num + 1
        print("\r") 
       
segitigaAtas(n)
segitigaBawah(n)

