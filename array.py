heros=['spider man','thor','hulk','iron man','captain america']
print (len(heros))
heros.append('balck panther')
print(heros)
heros.remove(heros[-1])
print(heros)
for i in range(len(heros)):
    if heros[i]=='hulk':
        heros.insert(i+1, 'black panther')
        break
print(heros)
i=0
while i<len(heros) :
    if heros[i] == 'thor':
        heros[i] = 'Dr. Strange'
    if heros[i] == 'hulk':
        heros.remove(heros[i])
    i+=1
print(heros)
heros.sort(key=str.lower, reverse=True)
print((heros))