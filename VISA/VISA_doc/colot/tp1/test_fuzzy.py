import matplotlib.pyplot as plt
import numpy as np

#==========
#EXERCICE 1
#==========

#Question 1
def basse(t):
    return np.clip((-t + 20.) * 0.1, 0., 1.)

def moyenne(t):
    return 1. - np.clip(np.sign(t - 20) * (t - 20) * 0.1, 0., 1.)

def elevee(t):
    return np.clip((t - 20.) * 0.1, 0., 1.)

def plot_3():
    t = np.arange(0., 45., 5.)

    plt.plot(t, basse(t), label="Basse")
    plt.plot(t, moyenne(t), label="Moyenne")
    plt.plot(t, elevee(t), label="Élevée")

    plt.legend(loc='center left', shadow=True)
    plt.axis([0, 40, -0.1, 1.1])
    plt.xlabel('Température (°C)')
    plt.ylabel('Discours (%)')
    plt.title("Partition floue de l'univers du discours")
    plt.grid(True)
    plt.savefig("plot_3.png")
    plt.show()

#Question 2
def get_appartenance(t):
    return [basse(t), moyenne(t), elevee(t)]

def print_appartenance(t):
    l = get_appartenance(t)
    print("Basse = ", l[0] * 100., "%")
    print("Moyenne = ", l[1] * 100., "%")
    print("Elevee = ", l[2] * 100., "%")

#Question 3
def basse_ou_moyenne(t):
    return np.maximum(basse(t), moyenne(t))

def plot_basse_ou_moyenne():
    t = np.arange(0., 45., 5.)

    plt.plot(t, basse_ou_moyenne(t), label="Basse OU Moyenne")

    plt.legend(loc='lower left', shadow=True)
    plt.axis([0, 40, -0.1, 1.1])
    plt.xlabel('Température (°C)')
    plt.ylabel('Discours (%)')
    plt.title("Partition floue de l'univers du discours")
    plt.grid(True)
    plt.savefig("plot_basse_ou_moyenne.png")
    plt.show()

#==========
#EXERCICE 2
#==========

#Question 1
def op_min(fs, t):
    res = []
    for f in fs:
        if res == []:
            res = f(t)
        else :
            newRes = np.minimum(res, f(t))
            res = newRes
    return res

def plot_test_min():
    t = np.arange(0., 45., 5.)
    res = op_min([basse, moyenne, elevee], t)
    plt.plot(t, res, label="Min(Basse, Moyenne, Élevée)")

    plt.legend(loc='upper left', shadow=True)
    plt.axis([0, 40, -0.1, 1.1])
    plt.xlabel('Température (°C)')
    plt.ylabel('Discours (%)')
    plt.title("Partition floue de l'univers du discours")
    plt.grid(True)
    plt.savefig("plot_test_min.png")
    plt.show()


#Question 2
def op_max(fs, t):
    res = []
    for f in fs:
        if res == []:
            res = f(t)
        else :
            newRes = np.maximum(res, f(t))
            res = newRes
    return res

def plot_test_max():
    t = np.arange(0., 45., 5.)
    res = op_max([basse, moyenne, elevee], t)
    plt.plot(t, res, label="Max(Basse, Moyenne, Elevee)")

    plt.legend(loc='lower left', shadow=True)
    plt.axis([0, 40, -0.1, 1.1])
    plt.xlabel('Température (°C)')
    plt.ylabel('Discours (%)')
    plt.title("Partition floue de l'univers du discours")
    plt.grid(True)
    plt.savefig("plot_test_max.png")
    plt.show()

#==========
#EXERCICE 3
#==========

def chauffer_fort(t):
    return np.clip((t - 8.) * 0.5, 0., 1.)

def plot_chauffer_fort():
    t = np.arange(0., 20., 1.)

    plt.plot(t, chauffer_fort(t), label="Chauffer Fort")

    plt.legend(loc='center left', shadow=True)
    plt.axis([0, 15, -0.1, 1.1])
    plt.xlabel('Puissance chauffe (kW)')
    plt.ylabel('Discours (%)')
    plt.title("Partition floue de l'univers du discours")
    plt.grid(True)
    plt.savefig("chauffer_fort.png")
    plt.show()

def mamdani(predicate, x0, conclusion, y):
    return np.minimum(predicate(x0), conclusion(y))

def plot_mamdani_chauffer_fort(temp):
    t = np.arange(0., 15.1, 0.1)

    plt.plot(t, mamdani(basse, temp, chauffer_fort, t), label="Chauffer Fort (" + str(temp) + "°C)")

    plt.legend(loc='center left', shadow=True)
    plt.axis([0, 15, -0.1, 1.1])
    plt.xlabel('Puissance chauffe (kW)')
    plt.ylabel('Discours (%)')
    plt.title("Partition floue de l'univers du discours")
    plt.grid(True)
    plt.savefig("chauffer_fort_" + str(temp) +".png")
    plt.show()



#EXERCICE 3
print("EXERCICE 3")
print('Sous-ensemble flou "Chauffer fort"')
plot_chauffer_fort()
print('Sous-ensemble flou "Chauffer fort" pour 12°C')
plot_mamdani_chauffer_fort(12.)
