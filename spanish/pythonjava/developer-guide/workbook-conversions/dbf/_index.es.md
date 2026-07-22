---
title: Leer y Escribir Archivos DBF
linktitle: Leer y Escribir Archivos
description: Aspose.Cells es una biblioteca de Python vía Java para trabajar con archivos de hojas de cálculo, que admite leer y escribir archivos dBASE III y IV (DBF). Este artículo explica cómo importar datos desde y exportar datos a archivos DBF usando Aspose.Cells, incluyendo detalles del formato de archivo, características compatibles y ejemplos paso a paso.
keywords: Aspose.Cells, biblioteca Python vía Java, DBF, dBASE, leer DBF, escribir DBF, importar DBF, exportar DBF, formato de archivo, .dbf
type: docs
weight: 200
url: /es/python-java/reading-and-writing-dbf-files/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells proporciona soporte completo para leer y escribir archivos DBF (dBASE). Puede cargar archivos dBASE III y dBASE IV existentes en un objeto Workbook, manipular los datos usando la rica API de Aspose.Cells, y guardar el libro de trabajo de vuelta al formato DBF para su uso con aplicaciones de bases de datos legadas.

{{% /alert %}}

## **Introducción**

DBF (DataBase File) es un formato de archivo de base de datos legado introducido originalmente por dBASE a principios de la década de 1980. A pesar de la antigüedad del formato, los archivos DBF todavía se utilizan ampliamente en muchas industrias para almacenar datos estructurados, particularmente en contabilidad, SIG y otras aplicaciones especializadas. Aspose.Cells le permite integrar estos archivos legados en flujos de trabajo modernos de hojas de cálculo de Python vía Java sin problemas.

La biblioteca admite tanto la lectura como la escritura de archivos DBF, dándole la capacidad de:

- Importar datos desde archivos DBF existentes en objetos Workbook de Aspose.Cells para su posterior procesamiento o conversión a otros formatos.
- Crear nuevos archivos DBF desde cero o transformando datos desde otros formatos de hojas de cálculo.
- Mantener definiciones de campos, tipos de datos y estructuras de registros al transferir datos hacia y desde el formato DBF.

Los archivos DBF también se pueden abrir directamente en Microsoft Excel y otras aplicaciones de hojas de cálculo, lo que los convierte en un puente conveniente entre sistemas legados y herramientas modernas de hojas de cálculo.

## **Versiones y Características de DBF Compatibles**

Aspose.Cells es compatible con las siguientes versiones del formato DBF:

- **dBASE III** — La variante original y más ampliamente compatible del formato DBF.
- **dBASE IV** — Una versión extendida que admite tipos de datos adicionales y tamaños de campo más grandes.

### Características Compatibles

La biblioteca proporciona soporte completo para las siguientes operaciones:

- Lectura de datos DBF en un objeto Workbook, con todos los registros y definiciones de campos preservados.
- Escritura de datos del libro de trabajo de vuelta al formato DBF para exportación a aplicaciones compatibles con dBASE.
- Manejo de tipos de datos comunes utilizados en archivos DBF, incluyendo campos de caracteres, numéricos, de fecha y lógicos.
- Preservación de definiciones de campos como nombre de campo, tipo y longitud durante las operaciones de lectura/escritura.

### Limitaciones y Consideraciones

Cuando trabaje con archivos DBF, tenga en cuenta las siguientes restricciones:

- El número máximo de campos por archivo es **128**.
- El tamaño máximo de registro es **4000 bytes**.
- Los nombres de campo están limitados a **10 caracteres**, deben estar en mayúsculas y no pueden contener espacios.
- Los valores de fecha en archivos DBF se almacenan en formato `YYYYMMDD`.
- La codificación de caracteres puede variar dependiendo de la aplicación de origen (comúnmente Windows-1252 o páginas de código OEM).

## **Leer un Archivo DBF**

Aspose.Cells hace que sea sencillo cargar datos desde un archivo DBF en un objeto Workbook. La biblioteca utiliza la clase `LoadOptions` para especificar el formato de origen, asegurando que los datos se interpreten correctamente durante el proceso de carga.

### Leer un Archivo DBF con Aspose.Cells

Para leer un archivo DBF, necesita crear una instancia de `LoadOptions`, establecer su propiedad `LoadFormat` en `LoadFormat.Dbf`, y pasarla al constructor de `Workbook` junto con la ruta del archivo. Una vez cargado, los datos serán accesibles a través de la colección `Worksheets`, donde puede iterar a través de las celdas, extraer valores o manipular los datos según sea necesario.

El siguiente ejemplo demuestra cómo cargar un archivo DBF existente en Aspose.Cells, acceder a su primera hoja de cálculo y leer los valores de las celdas.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, LoadOptions, LoadFormat, SaveFormat

dataDir = "Data/"
filePath = os.path.join(dataDir, "example.dbf")

loadOptions = LoadOptions(LoadFormat.Dbf)

workbook = Workbook(filePath, loadOptions)

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

sb = []

maxRow = cells.getMaxDataRow()
maxCol = cells.getMaxDataColumn()

for i in range(maxRow + 1):
    for j in range(maxCol + 1):
        cell = cells.get(i, j)
        value = cell.getStringValue()
        sb.append("|" + value)
    sb.append("|" + "\n")

print("".join(sb))

outputPath = os.path.join(dataDir, "output.xlsx")
workbook.save(outputPath, SaveFormat.Xlsx)

print("DBF file loaded successfully. Converted XLSX saved at: " + outputPath)

jpype.shutdownJVM()
```

{{% alert color="primary" %}}

Puede abrir archivos DBF directamente en Microsoft Excel seleccionando el archivo en el cuadro de diálogo Abrir. Excel tratará el archivo DBF como una hoja de cálculo, mostrando sus registros en un diseño tabular. Esto es útil para verificar rápidamente los datos después de leerlos o escribirlos con Aspose.Cells.

{{% /alert %}}

## **Escribir un Archivo DBF**

Escribir datos en un archivo DBF sigue un patrón similar al de guardar cualquier otro formato de hoja de cálculo con Aspose.Cells. Crea o carga un Workbook, llena la hoja de cálculo con datos y luego llama al método `Save` especificando `SaveFormat.Dbf` como formato de destino.

### Escribir un Archivo DBF con Aspose.Cells

Para crear un archivo DBF, siga estos pasos:

1. Cree una nueva instancia de `Workbook`.
2. Acceda a la primera hoja de cálculo desde la colección `Worksheets`.
3. Llene la hoja de cálculo con sus datos, incluyendo encabezados en la primera fila y registros en las filas siguientes.
4. Llame al método `Workbook.save`, pasando la ruta del archivo y `SaveFormat.Dbf` como parámetros.

El siguiente ejemplo demuestra cómo crear un nuevo archivo DBF desde cero. Llena una hoja de cálculo con datos de muestra que contienen diferentes tipos de datos (cadenas, números y fechas) para ilustrar cómo se manejan los tipos de campo al exportar al formato DBF.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, SaveFormat
import java.time as _jt
import java.util as _ju

outputDir = "C:\\Output\\"
filePath = os.path.join(outputDir, "output.dbf")

if not os.path.exists(outputDir):
    os.makedirs(outputDir, exist_ok=True)

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()

# Encabezados de columna
cells.get(0, 0).putValue("ID")
cells.get(0, 1).putValue("Name")
cells.get(0, 2).putValue("Department")
cells.get(0, 3).putValue("Salary")
cells.get(0, 4).putValue("HireDate")

# Fila de datos 1
cells.get(1, 0).putValue(101)
cells.get(1, 1).putValue("John Smith")
cells.get(1, 2).putValue("Engineering")
cells.get(1, 3).putValue(75000.50)
cells.get(1, 4).putValue(_jt.LocalDate.of(2020, 3, 15))

# Fila de datos 2
cells.get(2, 0).putValue(102)
cells.get(2, 1).putValue("Jane Doe")
cells.get(2, 2).putValue("Marketing")
cells.get(2, 3).putValue(68000.75)
cells.get(2, 4).putValue(_jt.LocalDate.of(2019, 7, 22))

# Fila de datos 3
cells.get(3, 0).putValue(103)
cells.get(3, 1).putValue("Bob Johnson")
cells.get(3, 2).putValue("Finance")
cells.get(3, 3).putValue(82000.00)
cells.get(3, 4).putValue(_jt.LocalDate.of(2021, 1, 10))

# Fila de datos 4
cells.get(4, 0).putValue(104)
cells.get(4, 1).putValue("Alice Brown")
cells.get(4, 2).putValue("Human Resources")
cells.get(4, 3).putValue(71000.25)
cells.get(4, 4).putValue(_jt.LocalDate.of(2018, 11, 5))

# Fila de datos 5
cells.get(5, 0).putValue(105)
cells.get(5, 1).putValue("Charlie Wilson")
cells.get(5, 2).putValue("Operations")
cells.get(5, 3).putValue(79500.80)
cells.get(5, 4).putValue(_jt.LocalDate.of(2022, 5, 30))

# Establecer anchos de columna para mejor legibilidad
worksheet.getCells().setColumnWidth(0, 8)
worksheet.getCells().setColumnWidth(1, 20)
worksheet.getCells().setColumnWidth(2, 20)
worksheet.getCells().setColumnWidth(3, 12)
worksheet.getCells().setColumnWidth(4, 14)

workbook.save(filePath, SaveFormat.DBf)

jpype.shutdownJVM()
```

{{% alert color="primary" %}}

Al escribir datos en un archivo DBF, asegúrese de que sus datos se ajusten a las limitaciones del formato. Los nombres de campo no deben tener más de 10 caracteres y no deben contener espacios. Los registros que excedan los 4000 bytes en total no se guardarán correctamente. Las fechas deben ser valores de fecha válidos que puedan representarse en el formato AAAAMMDD.

{{% /alert %}}

## **Consideraciones sobre Tipos de Datos y Formato**

Al transferir datos entre Aspose.Cells y el formato DBF, es importante comprender cómo se mapean los tipos de datos entre los dos sistemas para garantizar la integridad de los datos.

### Tipos de Celdas a Tipos de Campos DBF

Los valores de celda de Aspose.Cells se convierten automáticamente a los tipos de campo DBF apropiados al guardar:

- Las **cadenas** se mapean a campos de caracteres (C).
- Los **valores numéricos** (enteros y decimales) se mapean a campos numéricos (N).
- Los **valores de fecha** se mapean a campos de fecha (D) en formato `AAAAMMDD`.
- Los **valores booleanos** se mapean a campos lógicos (L).

### Codificación

Los archivos DBF pueden usar diferentes codificaciones de caracteres dependiendo de la aplicación que los creó. Aspose.Cells maneja la codificación de forma transparente en la mayoría de los casos, pero si encuentra problemas de visualización de caracteres, es posible que necesite verificar la codificación del archivo de origen.

### Reglas de Nombres de Campo

Los nombres de campo DBF deben cumplir con las siguientes reglas:

- Longitud máxima de 10 caracteres.
- Deben comenzar con una letra.
- No pueden contener espacios ni caracteres especiales.
- Se almacenan en mayúsculas independientemente del caso utilizado en la entrada.

### Verificación del Resultado

Después de escribir un archivo DBF, puede verificar el resultado abriéndolo en Microsoft Excel o en cualquier aplicación compatible con dBASE. Los datos deben aparecer en un diseño tabular con los nombres de campo como encabezados de columna, y los registros poblados de acuerdo con los datos que proporcionó.

## **Conversión entre DBF y Otros Formatos**

Uno de los casos de uso más prácticos para leer y escribir archivos DBF con Aspose.Cells es la conversión de datos entre el formato DBF y formatos modernos de hojas de cálculo como XLSX, XLS o CSV. Dado que Aspose.Cells admite una amplia gama de formatos, puede cargar fácilmente un archivo DBF y volver a guardarlo en cualquier otro formato compatible, o viceversa.

Por ejemplo, puede leer un archivo DBF, aplicar formato o cálculos usando la API de Aspose.Cells y luego guardar el resultado como un archivo XLSX para distribuirlo a usuarios que trabajan con aplicaciones modernas de hojas de cálculo. Por el contrario, puede tomar datos de un archivo XLSX o CSV y exportarlos al formato DBF para integrarlos con sistemas legados.



{{< app/cells/assistant language="python" >}}