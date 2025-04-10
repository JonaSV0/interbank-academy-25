import csv

class Transacciones :
    def __init__(self, file):
        #Declaracion de variables
        self.file = file
        self.transacciones = []
        self.suma_total = 0
        self.mayor_transaccion = {"id": None, "monto": 0.0}
        self.contador = {"Credito": 0, "Debito": 0}

    def lectura(self):
        #Leer el archivo y almacenarlo en una lista
        with open(self.file, mode='r', encoding='utf-8') as archivo:
            lector_csv = csv.reader(archivo)
            # Saltar encabezado
            next(lector_csv)
            for fila in lector_csv:
                self.transacciones.append({
                    "id": fila[0],
                    "tipo": fila[1],
                    "monto": float(fila[2])
                })

    def proceso(self):
        #Procesa las transacciones para calcular la suma total y la mayor transacción
        for transaccion in self.transacciones:
            tipo = transaccion["tipo"]
            monto = transaccion["monto"]

            # Sumar o restar según el tipo
            if tipo == "Crédito":
                self.suma_total += monto
                self.contador["Credito"] += 1
            elif tipo == "Débito":
                self.suma_total -= monto
                self.contador["Debito"] += 1
            # Verificar si es la transacción de mayor monto
            if monto > self.mayor_transaccion["monto"]:
                self.mayor_transaccion = {
                    "id": transaccion["id"],
                    "monto": monto
                }

    def resultado(self):
        #RESULTADOS
        print("Reporte de Transacciones")
        print("---------------------------------------------")
        print(f"Balance Final: {self.suma_total:.2f}")
        print(f"Transacción de Mayor Monto: ID {self.mayor_transaccion['id']} - {self.mayor_transaccion['monto']:.2f}")
        print(f"Conteo de Transacciones: Crédito: {self.contador['Credito']} Débito: {self.contador['Debito']}")
if __name__ == "__main__":
    try:
        
        file = "data.csv"
        processor = Transacciones(file)

        # Leer, procesar y mostrar resultados
        processor.lectura()
        processor.proceso()
        processor.resultado()
    
    #MANEJO DE ERRORES
    except FileNotFoundError:
        print(f"Error: El archivo '{processor.file}' no fue encontrado.")
    except (ValueError, IndexError):
        print(f"Advertencia: Fila inválida {processor.transactions[-1]} en el archivo.")
    except Exception as e:
        print(f"Error inesperado: {e}")