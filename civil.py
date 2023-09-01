age = int(input('Inform the age of the netx people, or type zero to and: '))
nmarried = int
ndivorced = int
nsingle = int 
nwidow = int 
status = str(input('Enter your marital status: '))

nmarried = 0
nsingle = 0
nwidow = 0
ndivorced = 0

while age <= 0:
    while age !=0:
        if status == 'C' or status == 'D' or status == 'S' or status == 'V':
            if status == 'C':
                nmarried == nmarried + 1
            if status == 'S':
                nsingle == nsingle + 1
            if status == 'D':
                ndivorced == ndivorced + 1
            if status == 'V':
                nwidow == nwidow + 1
    while age !=0:
        age = int(input('informe a idade: '))
        print('o Numero de casados é: ', nmarried)
        print('o Numero de solteiros é: ', nsingle)
        print('o Numero de separados é: ', ndivorced)
        print('o Numero de viuvas é: ', nwidow)