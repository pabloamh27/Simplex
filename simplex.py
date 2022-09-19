# Este será un lector de archivos txt
def read_file():
    reader = open("operacion.txt", 'r')
    file = reader.read()
    reader.close()
    return file


# Este será un escritor de archivos txt
def write_file(text):
    reader = open("operacion.txt", 'w')
    reader.write(text)
    reader.close()


# Esta función se encargará de separar los datos del archivo txt
def separar_datos():
    datos = read_file()
    datos = datos.split()
    datos2 = []
    for i in range(len(datos)):
        datos2.append(datos[i].split(','))
    return datos2


def setNumeros(lista):
    for i in range(len(lista)):
        if (lista[i] == '<=') | (lista[i] == '>=') | (lista[i] == '=') | (lista[i] == '<') | (lista[i] == '>'):
            lista[i] = lista[i]
        else:
            lista[i] = float(lista[i]).__format__('0.4f')
    return lista


# Esta funcion agrega las variables de augura que necesita el problema


def agregar_variables_augura_objetivo(lista, cantidadRestricciones):
    print(lista)
    for i in range(cantidadRestricciones):
        lista.append(float(0))
    lista.append('=')
    lista.append(float(0))
    return lista


def agregar_variables_augura_restricciones(lista, cantidadRestricciones):
    listaFinal = []
    contador = 0
    for j in range(len(lista)):
        lista1 = []
        for i in range(len(lista[j])):
            if lista[j][i] == '<=':
                for k in range(contador):
                    lista1.append(float(0))
                lista1.append(float(1))
                for l in range(contador, cantidadRestricciones - 1):
                    lista1.append(float(0))
                contador += 1
                lista1.append('=')
            else:
                lista1.append(lista[j][i])

        listaFinal.append(lista1)
    return listaFinal


def metodoSimplex(problema):
    solucionInicial = problema.__solucionInicial__()
    colMenor = problema.__columnaMenor__()
    pivote = problema.__determinacionPivote__(colMenor)
    nuevaFila = problema.__nuevaFila__(pivote)


class problema:
    def __init__(self, lista):
        self.metodo = lista[0][0]
        self.optimizacion = lista[0][1]
        self.cant_v_decision = lista[0][2]
        self.cant_restricciones = lista[0][3]
        self.funcion_objetivo = lista[1]
        self.restricciones = lista[2:]

    def __getRestricciones__(self):
        restricciones = []
        for i in range(len(self.restricciones)):
            restricciones.append(self.restricciones[i])
        for j in range(len(restricciones)):
            restricciones[j] = setNumeros(restricciones[j])
        self.restricciones = restricciones
        return self.restricciones

    def __agregar_variables_simplex__(self):
        self.objetivo = agregar_variables_augura_objetivo(self.funcion_objetivo, int(self.cant_restricciones))
        self.objetivo = setNumeros(self.objetivo)
        self.restricciones = agregar_variables_augura_restricciones(self.restricciones, int(self.cant_restricciones))
        self.__getRestricciones__()
        return self

    def __tabularProblema__(self):
        tabla = []
        tabla1 = []
        for j in range(len(self.funcion_objetivo)):
            if self.funcion_objetivo[j] != '=':
                tabla1.append(float(self.funcion_objetivo[j]).__format__('0.4f'))
        tabla.append(tabla1)
        for i in range(len(self.restricciones)):
            tabla2 = []
            for j in range(len(self.restricciones[i])):
                if self.restricciones[i][j] != '=':
                    tabla2.append(float(self.restricciones[i][j]).__format__('0.4f'))
            tabla.append(tabla2)
        return tabla

    def __printTabla__(self):
        tabla = self.__tabularProblema__()
        for i in range(len(tabla)):
            print(tabla[i])

    def __print__(self):
        print("Metodo: " + self.metodo + "\n" +
              "Optimizacion: " + self.optimizacion + "\n" +
              "Cantidad de variables de decision: " + self.cant_v_decision + "\n" +
              "Cantidad de restricciones: " + self.cant_restricciones + "\n" +
              "Funcion objetivo: " + str(self.funcion_objetivo) + "\n" +
              "Restricciones: " + str(self.restricciones))

    def __solucionInicial__(self):
        tabla = self.__tabularProblema__()
        solucion = []
        for i in range(int(self.cant_v_decision)):
            solucion.append(float(0).__format__('0.4f'))
        for j in range(len(tabla) - 1):
            solucion.append(tabla[j + 1][-1])
        return solucion

    def __columnaMenor__(self):
        tabla = self.__tabularProblema__()
        columna = tabla[0]
        menor = columna[0]
        for i in range(len(columna)):
            if columna[i] < menor and columna[i] != float(0).__format__('0.4f'):
                menor = columna[i]
        print(columna.index(menor))
        return columna.index(menor)

    def __determinacionPivote__(self, columna):
        tabla = self.__tabularProblema__()
        divisiones = []
        for i in range(len(tabla) - 1):
            if tabla[i + 1][columna] > float(0).__format__('0.4f'):
                pair = [float(tabla[i + 1][-1]) / float(tabla[i + 1][columna]), [columna, i + 1]]
                divisiones.append(pair)
        pivote = divisiones[0]
        for i in range(len(divisiones)):
            if float(divisiones[i][0]) < float(pivote[0]):
                pivote = divisiones[i][0]
        print(pivote)
        return pivote

    def __nuevaFila__(self, pivote):
        tabla = self.__tabularProblema__()
        fila = []
        for i in range(len(tabla[int(pivote[1][1])])):
            print(float(
                float(tabla[int(pivote[1][1])][i]) / float(tabla[int(pivote[1][1])][int(pivote[1][0])])).__format__(
                '0.4f'))
            fila.append(float(
                float(tabla[int(pivote[1][1])][i]) / float(tabla[int(pivote[1][1])][int(pivote[1][0])])).__format__(
                '0.4f'))
        print(fila)
        return fila


def main(problema):
    problema.__agregar_variables_simplex__()
    problema.__print__()
    if problema.metodo == '1':  # Es simplex

        problema.__printTabla__()
        metodoSimplex(problema)


datos = separar_datos()
problema = problema(datos)
main(problema)
