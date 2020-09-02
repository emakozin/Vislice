# izpiše vsa praštevila do 200

def je_deljivo_s_katerim_od(n, seznam):
    for d in seznam:
        if n % d == 0:
            return True
    return False

def prastevila_do(n):
    if n <= 1:
        return []
    else:
        k = prastevila_do(n - 1)
        if je_deljivo_s_katerim_od(n, k):
            return k
        else:
            return k + [n]

print(prastevila_do(200))