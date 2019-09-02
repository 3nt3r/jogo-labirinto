arquivo = open("Labirinto.txt", "r")
lab = arquivo.readlines()


resul = ""
subs = []
junt = ""
posi = lab[0].find(".")

for cont in range(0, 8):
    subs = subs + [lab[0][cont]]
subs[posi] = "*"
for cont in range(0, 8):
    junt = junt + subs[cont]
lab[0] = junt


def encPosi():
    co = 0
    li = 0
    resul = []
    for cont in range(0, 8):
        if lab[cont].find("*") > 0:
            co = lab[cont].find("*")
            li = cont
    return co, li


def movW():
    Qpos = []
    Qcima = []
    Jpos = ""
    Jcima = ""
    c, l = encPosi()
    if l-1 < 0 or lab[l-1][c] == "#":
        print("Movimento não Permitido!")
    else:
        for cont in range(0, 8):
            Qcima = Qcima + [lab[l-1][cont]]
            Qpos = Qpos + [lab[l][cont]]
        Qcima[c] = "*"
        Qpos[c] = "."
        for cont in range(0, 8):
            Jcima = Jcima + Qcima[cont]
            Jpos = Jpos + Qpos[cont]
        lab[l-1] = Jcima
        lab[l] = Jpos


def movS():
    Qbaixo = []
    Qpos = []
    Jbaixo = ""
    Jpos = ""
    c, l = encPosi()
    if l+1 > 7 or lab[l+1][c] == "#":
        print("Movimento não Permitido!")
    else:
        for cont in range(0, 8):
            Qpos = Qpos + [lab[l][cont]]
            Qbaixo = Qbaixo + [lab[l+1][cont]]
        Qpos[c] = "."
        Qbaixo[c] = "*"
        for cont in range(0, 8):
            Jpos = Jpos + Qpos[cont]
            Jbaixo = Jbaixo + Qbaixo[cont]
        lab[l] = Jpos
        lab[l+1] = Jbaixo
    g = lab[7].find("*")
    if g > -1:
        print("===================")
        print("     LABIRINTO     ")
        for cont in lab:
            print(cont.strip())
        print("===============================")
        print("PARABÉNS, VOCÊ CHEGOU AO FINAL!!!")
        print("===============================")
        return "ganhou"


def movA():
    Qpos = []
    Jpos = ""
    c, l = encPosi()
    if c-1 < 0 or lab[l][c-1] == "#":
        print("Movimento não Permitido!")
    else:
        for cont in range(0, 8):
            Qpos = Qpos + [lab[l][cont]]
        Qpos[c] = "."
        Qpos[c-1] = "*"
        for cont in range(0, 8):
            Jpos = Jpos + Qpos[cont]
        lab[l] = Jpos


def movD():
    Qpos = []
    Jpos = ""
    c, l = encPosi()
    if c+1 > 7 or lab[l][c+1] == "#":
        print("Movimento não Permitido!")
    else:
        for cont in range(0, 8):
            Qpos = Qpos + [lab[l][cont]]
        Qpos[c] = "."
        Qpos[c+1] = "*"
        for cont in range(0, 8):
            Jpos = Jpos + Qpos[cont]
        lab[l] = Jpos


while resul != "ganhou":
    print("===================")
    print("     LABIRINTO     ")
    for cont in lab:
        print(cont.strip())
    print("""
    =========== CONTROLES ===========
    S = BAIXO
    W = CIMA
    A = ESQUERDA
    D = DIREITA
    =================================""")
    usu = input("Digite o comando desejado: ").lower()
    if usu == "w":
        movW()
    elif usu == "s":
        resul = movS()
    elif usu == "a":
        movA()
    elif usu == "d":
        movD()
    else:
        print("Comando Inválido!")
