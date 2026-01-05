def juft_topish(royhat):

    juftlar = []
    for son in royhat:
        if son % 2 == 0:
            juftlar.append(son)

    return juftlar

def toq_topish(royhat):

    toqlar = []
    for son in royhat:
        if son % 2 != 0 and son > 0:
            toqlar.append(son)

    return toqlar

def musbat_topish(royhat):

    musbatlar = []
    for son in royhat:
        if son < 0:
            musbatlar.append(son)

    return musbatlar
