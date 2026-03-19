from lista_circular import ListaCircular

def main():
    while True:
        print("  SUPPLY CHAIN — Papa Región Sumapaz          ")
        print("  Ingresa los datos de cada eslabón           ")

        sc = ListaCircular()

        municipios = sc.insertar_planificacion()
        sc.insertar_abastecimiento(municipios)
        sc.insertar_fabricacion()
        sc.insertar_entrega()
        sc.insertar_logistica_inversa()

        vueltas = input("\n¿Cuántas vueltas quieres ver del ciclo? (Enter = 2): ").strip()
        vueltas = int(vueltas) if vueltas.isdigit() else 2
        sc.mostrar_ciclo(vueltas)

        # ── Después de imprimir, pregunta si reiniciar ──
        print("  ¿Deseas registrar una nueva cadena?         ")
        print("  1. Sí, iniciar de nuevo                     ")
        print("  2. No, salir del programa                   ")
        opcion = input("  → Opción: ").strip()

        if opcion == "2":
            print("\n   Hasta luego.\n")
            break

if __name__ == "__main__":
    main()
