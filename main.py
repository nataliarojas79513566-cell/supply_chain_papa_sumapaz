from lista_circular import ListaCircular

def main():
    supply_chain = ListaCircular()

    # 🔗 Eslabones reales del Sumapaz
    supply_chain.insertar("Planificación: Organización de cultivos en Sumapaz")
    supply_chain.insertar("Abastecimiento: Recolección en Pasca y Arbeláez")
    supply_chain.insertar("Fabricación: Procesamiento Gama IV en Fusagasugá")
    supply_chain.insertar("Entrega: Distribución a Bogotá")
    supply_chain.insertar("Logística Inversa: Retorno de residuos para bioabono")

    # Mostrar el ciclo (2 vueltas controladas)
    supply_chain.mostrar_ciclo(2)

if __name__ == "__main__":
    main()