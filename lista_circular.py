from nodo import Nodo

class ListaCircular:
    def __init__(self):
        self.cabeza = None

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

    def insertar_planificacion(self):
        print("\n=== PLANIFICACION ===")
        municipios = []

        while True:
            print(f"\n  Municipio #{len(municipios) + 1} (o escribe 'listo' para terminar)")
            nombre = input("  -> Nombre del municipio: ").strip()
            if nombre.lower() == "listo":
                if len(municipios) == 0:
                    print("  Debes ingresar al menos un municipio.")
                    continue
                break
            hectareas = input(f"  -> Hectareas en {nombre}: ").strip()
            variedad  = input(f"  -> Variedad de papa en {nombre}: ").strip()
            municipios.append({
                "municipio": nombre,
                "hectareas": hectareas,
                "variedad":  variedad
            })
            print(f"  {nombre} agregado.")

        resumen = " | ".join(
            f"{m['municipio']} ({m['hectareas']} ha, {m['variedad']})"
            for m in municipios
        )
        dato = f"PLANIFICACION\n     Municipios: {resumen}"
        self.insertar(dato)
        return [m["municipio"] for m in municipios]

    def insertar_abastecimiento(self, municipios_disponibles):
        print("\n=== ABASTECIMIENTO ===")
        print("  Municipios registrados en Planificacion:")
        for i, m in enumerate(municipios_disponibles, 1):
            print(f"    {i}. {m}")

        origenes = input("\n  -> De que municipios proviene la papa? (numeros separados por coma): ")
        indices = [int(x.strip()) - 1 for x in origenes.split(",") if x.strip().isdigit()]
        seleccionados = [municipios_disponibles[i] for i in indices if 0 <= i < len(municipios_disponibles)]

        toneladas = input("  -> Total de toneladas recolectadas: ").strip()
        proveedor = input("  -> Nombre del proveedor / asociacion: ").strip()

        dato = (
            f"ABASTECIMIENTO\n"
            f"     Origen: {', '.join(seleccionados)}\n"
            f"     Toneladas: {toneladas}t  |  Proveedor: {proveedor}"
        )
        self.insertar(dato)

    def insertar_fabricacion(self):
        import time

        etapas = [
            ("🧺 Recepcion de materia prima",      "Pesaje y clasificacion de papa en bruto",          1.5),
            ("🪨  Remocion de tierra",              "Cepillado en seco para retirar barro y piedras",   1.0),
            ("💧 Lavado",                           "Inmersion en agua con ozono a 4C por 8 minutos",   2.0),
            ("🔪 Pelado",                           "Pelado abrasivo mecanico, perdida ~12% del peso",  1.5),
            ("✂️  Corte",                           "Corte en cubos/laminas segun presentacion",        1.5),
            ("🌊 Segundo lavado y desinfeccion",    "Agua clorada 50 ppm, elimina almidon superficial", 2.0),
            ("💨 Centrifugado / Escurrido",         "Eliminacion de exceso de agua, humedad < 5%",      1.0),
            ("🌡️  Control de calidad",              "Inspeccion visual y de textura, descarte piezas",  1.5),
            ("📦 Empaque en atmosfera modificada",  "Sellado al vacio con N2/CO2, prolonga vida util",  2.0),
            ("❄️  Cadena de frio",                  "Almacenamiento a 2C hasta despacho",               1.0),
        ]

        print("\n=== FABRICACION — Proceso Gama IV ===\n")
        print(f"  {'ETAPA':<40} {'DETALLE'}")
        print("  " + "-" * 70)

        etapas_resumen = []

        for nombre, detalle, duracion in etapas:
            print(f"  {nombre:<38} {detalle}")
            time.sleep(duracion)
            print(f"  Completado\n")
            etapas_resumen.append(nombre)

        print("  " + "-" * 70)
        print("  Proceso Gama IV finalizado — Papa lista para distribucion\n")

        dato = (
            "FABRICACION — Proceso Gama IV\n"
            "     Planta: Fusagasuga\n"
            "     Etapas: " + " -> ".join(etapas_resumen)
        )
        self.insertar(dato)

    def insertar_entrega(self):

        DISTANCIAS = {
            "bogota":        {"nombre": "Bogota",        "km": 71},
            "bogotá":        {"nombre": "Bogota",        "km": 71},
            "girardot":      {"nombre": "Girardot",      "km": 49},
            "melgar":        {"nombre": "Melgar",        "km": 34},
            "ibague":        {"nombre": "Ibague",        "km": 97},
            "ibagué":        {"nombre": "Ibague",        "km": 97},
            "villavicencio": {"nombre": "Villavicencio", "km": 85},
        }

        VELOCIDAD_CAMION = 60

        TIPOS_DESTINO = ["Supermercado", "Tienda de barrio", "Plaza de mercado",
                         "Restaurante", "Exportacion"]

        print("\n=== ENTREGA ===")
        print("  Ciudades disponibles: Bogota, Girardot, Melgar, Ibague, Villavicencio")
        destinos = []

        while True:
            print(f"\n  Destino #{len(destinos) + 1} (o escribe 'listo' para terminar)")
            ciudad_input = input("  -> Ciudad de entrega: ").strip()

            if ciudad_input.lower() == "listo":
                if len(destinos) == 0:
                    print("  Debes ingresar al menos un destino.")
                    continue
                break

            clave = ciudad_input.lower()
            if clave not in DISTANCIAS:
                print("  Ciudad no disponible. Elige entre: Bogota, Girardot, Melgar, Ibague, Villavicencio")
                continue

            info  = DISTANCIAS[clave]
            km    = info["km"]
            horas = round(km / VELOCIDAD_CAMION, 1)
            print(f"  {info['nombre']} — {km} km | Tiempo estimado: {horas}h en camion")

            print("\n  -> Tipos de destino:")
            for i, t in enumerate(TIPOS_DESTINO, 1):
                print(f"       {i}. {t}")
            seleccion = input("  -> Selecciona los tipos (numeros separados por coma): ")
            indices   = [int(x.strip()) - 1 for x in seleccion.split(",") if x.strip().isdigit()]
            tipos_sel = [TIPOS_DESTINO[i] for i in indices if 0 <= i < len(TIPOS_DESTINO)]

            destinos.append({
                "ciudad": info["nombre"],
                "km":     km,
                "horas":  horas,
                "tipos":  tipos_sel,
            })
            print(f"  {info['nombre']} agregada.")

        lineas = []
        for d in destinos:
            lineas.append(
                f"       {d['ciudad']}: {d['km']} km | "
                f"Camion ~{d['horas']}h | {', '.join(d['tipos'])}"
            )
        dato = "ENTREGA\n" + "\n".join(lineas)
        self.insertar(dato)

    def insertar_logistica_inversa(self):
        print("\n=== LOGISTICA INVERSA ===")
        tipo_residuo  = input("  -> Tipo de residuo (ej. Cascaras): ").strip()
        destino_final = input("  -> Destino final del residuo: ").strip()
        kg_retorno    = input("  -> Kilogramos de retorno: ").strip()

        dato = (
            f"LOGISTICA INVERSA\n"
            f"     Residuo: {tipo_residuo}  |  Destino: {destino_final}  |  Retorno: {kg_retorno} kg"
        )
        self.insertar(dato)

    def mostrar_ciclo(self, vueltas=2):
        if self.cabeza is None:
            print("Lista vacia")
            return

        actual   = self.cabeza
        contador = 0

        print("\n" + "="*55)
        print("   CICLO SUPPLY CHAIN — Papa Region Sumapaz")
        print("="*55)

        while contador < vueltas:
            print(f"\n-> {actual.dato}")
            actual = actual.siguiente
            if actual == self.cabeza:
                contador += 1
                print("\n" + "-"*45 + f" VUELTA {contador} COMPLETA\n")
