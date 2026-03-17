from nodo import Nodo

class ListaCircular:
    def __init__(self):
        self.cabeza = None

    # Insertar nodos
    def insertar(self, dato):
        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
            nuevo.siguiente = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente

            actual.siguiente = nuevo
            nuevo.siguiente = self.cabeza

    # Mostrar ciclo controlado (evitar infinito)
    def mostrar_ciclo(self, vueltas=2):
        if self.cabeza is None:
            print("Lista vacía")
            return

        actual = self.cabeza
        contador = 0

        print("\n--- CICLO DE LA SUPPLY CHAIN ---\n")

        while contador < vueltas:
            print(f"➡️ {actual.dato}")
            actual = actual.siguiente

            if actual == self.cabeza:
                contador += 1
                print("🔁 --- FIN DE UNA VUELTA ---\n")