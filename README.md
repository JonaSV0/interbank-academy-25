# Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)

1. **Introducción**
   El reto técnico "Procesamiento de Transacciones Bancarias (CLI)" tiene como propósito desarrollar una aplicación funcional y eficiente que permita procesar un archivo de transacciones bancarias en formato CSV.

2. **Instrucciones de Ejecución**
   1. **Instalación de Dependencias**
      La aplicación no requiere la instalación de dependencias externas, ya que utiliza únicamente la biblioteca estándar de Python. Asegúrate de que tengas instalada una versión de Python 3.6 o superior.

      Para verificar tu versión de Python, ejecuta:
      ```
      python --version
      ```
      o
      ```
      python3 --version
      ```
      Si necesitas instalar Python, visita python.org y descarga la última versión.
   2. **Clonar Repositorio**
      Clona el repositorio disponible en:
      ```
      https://github.com/JonaSV0/interbank-academy-25.git
      ```
   3. **Ejecución de la Aplicación**
      Abriendo un terminal de la carpeta donde se encuentre el clon de repositorio ejecutamos:
      ```
      python main.py
      ```

3. **Enfoque y Solución:**
   1. **Lógica Implementada**
      - Lectura del CSV: Se utiliza el módulo csv para cargar transacciones en una lista de diccionarios, asegurando un formato consistente.
      - Procesamiento: En una sola iteración:
         - Se calculan el balance final (créditos menos débitos).
         - Se identifica la transacción de mayor monto.
         - Se cuenta el número de transacciones por tipo.

      - Reporte: Los resultados se imprimen en un formato claro y legible.
   2. **Decisiones de Diseño**
      - Clases: La clase Transacciones encapsula la lógica, mejorando la organización y mantenibilidad.
      - Eficiencia: Procesamiento en una única pasada (complejidad O(n)).
      - Manejo de errores: Validación de archivo y datos con mensajes descriptivos para el usuario.

4. **Estructura del Proyecto:**
   La estructura del proyecto está organizada de manera simple y eficiente, manteniendo todo el código relacionado en una carpeta principal. A continuación, se presenta una posible organización:
   ```
   interbank-academy-25/
   │
   ├── main.py                  # Código principal para procesar transacciones
   ├── data.csv                 # Archivo CSV con las transacciones bancarias
   ├── README.md                # Descripción del proyecto y cómo usarlo
   ```

