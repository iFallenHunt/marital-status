idade = int(input('Inform the age of the netx people, or type zero to and: '))
ncasado = int
ndivorciado = int
nsolteiro = int 
nviuva = int 
estado = str(input('Informe o estado Civil: '))

ncasado = 0
nsolteiro = 0
nviuva = 0
ndivorciado = 0

while idade <= 0:
    while idade !=0:
        if estado == 'C' or estado == 'D' or estado == 'S' or estado == 'V':
            if estado == 'C':
                ncasado == ncasado + 1
            if estado == 'S':
                nsolteiro == nsolteiro + 1
            if estado == 'D':
                ndivorciado == ndivorciado + 1
            if estado == 'V':
                nviuva == nviuva + 1
    while idade !=0:
        idade = int(input('informe a idade: '))
        print('o Numero de casados é: ', ncasado)
        print('o Numero de solteiros é: ', nsolteiro)
        print('o Numero de separados é: ', ndivorciado)
        print('o Numero de viuvas é: ', nviuva)