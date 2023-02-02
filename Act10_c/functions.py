#Importamos pandas y matplotlib
import pandas as pd
import matplotlib.pyplot as plt
def fastProcess():
    # Leemos el csv y filtramos por las columnas que necesitamos, lo metemos en un df
    df = pd.read_csv('test.csv', usecols=('id', 'clock_speed'))
    # Creamos la lista de los valores escogidos
    # Estos valores esta con unos menos debido a que el indice empiza por 0 y no por 1
    listId = [2, 12, 33, 55, 69, 84, 109, 19, 209, 399]

    # Localizamos dentro del df las filas que tengan los id iguales a listId
    # Usamos .loc para selecionar las id especificas
    resul = df.loc[listId]

    plt.bar(resul.id, resul.clock_speed, color ='red', width=4)
    plt.xlabel("Numero de Id")
    plt.ylabel("Velocidad microprocessado")
    plt.show()

    # Delover resultado
    return resul




def numMpixels():

    # Leemos el csv y filtramos por las columnas que necesitamos, lo metemos en un df
    df = pd.read_csv('test.csv', usecols=('id','px_width'))

    # Creamos la lista de los valores escogidos
    # Estos valores esta con unos menos debido a que el indice empiza por 0 y no por 1
    listId = [2, 12, 33, 55, 69, 84, 109, 19, 209, 399]

    # Localizamos dentro del df las filas que tengan los id iguales a listId
    # Usamos .loc para selecionar las id especificas
    result = df.loc[listId]

    plt.bar(result.id, result.px_width, color='blue', width=4)
    plt.xlabel("Numero de Id")
    plt.ylabel("Numero de megapixeles ")
    plt.show()

    # Delover resultado
    return result

def batteryPower():

    # Leemos el csv y filtramos por las columnas que necesitamos, lo metemos en un df
    df = pd.read_csv('test.csv', usecols=('id','battery_power'))

    # Creamos la lista de los valores escogidos
    # Estos valores esta con unos menos debido a que el indice empiza por 0 y no por 1
    listId = [2, 12, 33, 55, 69, 84, 109, 19, 209, 399]

    # Localizamos dentro del df las filas que tengan los id iguales a listId
    # Usamos .loc para selecionar las id especificas
    result = df.loc[listId]

    plt.bar(result.id, result.battery_power, color='yellow', width=4)
    plt.xlabel("Numero de Id")
    plt.ylabel("mAh Bateria")
    plt.show()

    #Delover resultado
    return result

