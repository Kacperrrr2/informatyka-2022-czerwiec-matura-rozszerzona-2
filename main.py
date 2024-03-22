wiersz=open('przyklad.txt','r')
tab=[]
for line in wiersz:
    tab.append(line.strip())


print(tab)
licznik=0
#ZAD4.1
def odbicie(x):
    x = x.lower().replace(" ", "") #zmieniamy wszystkie literki na male i pozbywamy sie spacji
    n = len(x) #zmienna pomocnicza przechowujaca dlugosc slowa
    for i in range(n-1):
        x[i] = x[n-1-i]
    return x

for i in tab:
    if odbicie(i)%17==0:
        licznik+=1
