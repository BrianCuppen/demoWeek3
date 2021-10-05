# for
def bereken_som_getallen_for(aantal):
    som = 0
    for i in range(0, aantal):
        # print(i)
        som = som + i
    return som


print(
    f"Demo For > De som van de eerste 100 getallen is: {bereken_som_getallen_for(100)}.\n")

# while


def bereken_som_getallen_while(aantal):
    som = 0
    index = 1

    while index <= aantal:
        som = som + index
        index += 1
    return som


print(
    f"Demo while >  De som van de eerste 100 getallen is: {bereken_som_getallen_while(100)}.\n")

# for - break


def bereken_som_getallen_for_stop(aantal, stop):
    som = 0
    
    for i in range(0, aantal):
        som = som + i
        # controle: zit de som al niet boven de stop-parameter?
        if som >= stop:
            print(f"Stop bereikt aan {i} getallen.")
            break  # <--- for-lus wordt onderbroken
    return som


print(
    f"Demo break in for > bereikte som: {bereken_som_getallen_for_stop(100,1000)}\n ")

# while & break


def bereken_som_getallen_while_stop(aantal, stop):
    som = 0
    index = 1

    while index <= aantal:
        som = som + index
        # controle: zit de som al niet boven de stop-parameter?
        if som >= 1000:
            print(f"Stop bereikt aan {index} getallen.")
            break
        index += 1
    return som


print(
    f"Demo break in while > bereikte som: {bereken_som_getallen_while_stop(100,1000)}\n ")
