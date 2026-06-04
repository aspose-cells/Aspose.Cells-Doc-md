---
title: Dividir archivos Excel en varios archivos
description: Aspose.Cells es una biblioteca de Python a través de Java para trabajar con archivos de hojas de cálculo, que admite dividir un único archivo Excel en varios archivos. Este artículo presentará cómo dividir archivos Excel copiando cada hoja de cálculo en un libro de trabajo separado y copiando rangos de celdas específicos en otros libros de trabajo.
keywords: Aspose.Cells, biblioteca de Python a través de Java, hoja de cálculo, dividir archivo Excel, copiar hoja de cálculo, copiar rango, múltiples libros de trabajo, guardar como archivos separados
type: docs
weight: 195
url: /es/python-java/splitting-excel-files-into-multiple-files/
---

{{% alert color="primary" %}}

Aspose.Cells admite dividir un único archivo Excel en varios archivos. Hay dos formas principales de hacerlo: (1) copiando cada hoja de cálculo del libro de trabajo de origen en un nuevo libro de trabajo y guardando cada uno como un archivo separado, y (2) copiando un rango de celdas específico de una hoja de cálculo en un nuevo libro de trabajo. Ambos enfoques son útiles cuando necesita distribuir subconjuntos de datos, crear informes más pequeños para diferentes destinatarios o aislar datos para su procesamiento individual.

{{% /alert %}}

## **Introducción**

Existen muchos escenarios del mundo real en los que un desarrollador necesita dividir un único archivo Excel en varios archivos más pequeños. Por ejemplo, un libro de trabajo puede contener una hoja de cálculo por departamento, y cada jefe de departamento necesita recibir solo su propia hoja. En otros casos, es posible que desee extraer una tabla o bloque de datos particular de una hoja de cálculo y enviarla como un archivo independiente por correo electrónico, sin exponer el resto del libro de trabajo. También puede ser necesario dividir libros de trabajo consolidados grandes en piezas más pequeñas para facilitar su manejo, una carga más rápida o el procesamiento posterior por parte de otros sistemas.

Aspose.Cells proporciona dos enfoques flexibles para esta tarea. El primer enfoque itera a través de cada hoja de cálculo en el libro de trabajo de origen y copia su contenido en una nueva instancia de `Workbook`, guardando cada una como un archivo separado. El segundo enfoque se centra en un rango de celdas específico dentro de una hoja de cálculo y copia solo ese rango en un nuevo libro de trabajo. En ambos casos, el flujo general es el mismo: cargue el libro de trabajo de origen utilizando la clase `Workbook`, acceda a los datos relevantes a través de los objetos `Worksheet` y `Cells`, transfiera el contenido a un `Workbook` de destino y luego guárdelo en disco.

## **Dividir un archivo Excel copiando cada hoja de cálculo en un nuevo libro de trabajo**

### **Descripción del enfoque**

En este enfoque, el libro de trabajo de origen se abre una vez, y luego para cada `Worksheet` en su colección `Worksheets`, se crea un nuevo `Workbook` de destino. El contenido de la hoja de cálculo de origen se copia en la primera hoja de cálculo del libro de trabajo de destino, y el libro de trabajo de destino se guarda como un archivo cuyo nombre se deriva del nombre de la hoja de cálculo de origen. El resultado es un archivo de salida por hoja de cálculo, donde cada archivo de salida contiene los datos de una sola hoja de origen.

Este método es la opción correcta cuando cada hoja de cálculo en su libro de trabajo de origen representa una unidad de información lógicamente independiente (como un departamento, región, mes o línea de productos) y desea entregar o procesar cada unidad por sí misma.

### **Pasos**

Los siguientes pasos describen cómo dividir un archivo Excel copiando cada hoja de cálculo en un nuevo libro de trabajo:

1. Abra el archivo Excel de origen creando una instancia de un objeto `Workbook` y pasando la ruta del archivo a su constructor.
2. Itere a través de la colección `Workbook.Worksheets` utilizando un bucle `for` o `foreach` para que se procese cada `Worksheet` en el archivo de origen.
3. Dentro del bucle, cree una nueva instancia de `Workbook` de destino (un libro de trabajo vacío) para la hoja de cálculo actual.
4. Agregue una nueva `Worksheet` al libro de trabajo de destino (o use la primera hoja de cálculo predeterminada) y asígnele un nombre significativo, idealmente el mismo que la propiedad `Name` de la hoja de cálculo de origen.
5. Copie el contenido de la hoja de cálculo de origen en la hoja de cálculo de destino. Esto se puede hacer iterando las celdas de la colección `Cells` de la hoja de cálculo de origen y escribiendo sus valores en las celdas correspondientes de la hoja de cálculo de destino, o utilizando el método `Cells.copy` para transferir un rango completo de una vez.
6. Construya una ruta de archivo de salida que incorpore el nombre de la hoja de cálculo de origen (por ejemplo, `dataDir + worksheet.Name + ".xls"`) para que cada archivo generado tenga un nombre único.
7. Llame al método `Workbook.save` del destino para escribir el archivo en disco.
8. Repita los pasos del 3 al 7 para la siguiente hoja de cálculo hasta que se hayan procesado todas las hojas de cálculo.

### **Ejemplo de código**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat

dataDir = "data/"
workbook = Workbook(dataDir + "book1.xls")

for i in range(workbook.getWorksheets().getCount()):
    sourceSheet = workbook.getWorksheets().get(i)
    sheetName = sourceSheet.getName()
    
    destWorkbook = Workbook()
    destIndex = destWorkbook.getWorksheets().add()
    destSheet = destWorkbook.getWorksheets().get(destIndex)
    destSheet.setName(sheetName)
    
    destSheet.copy(sourceSheet)
    
    destFile = dataDir + sheetName + ".xls"
    destWorkbook.save(destFile, SaveFormat.Excel97To2003)

jpype.shutdownJVM()
```

El resultado esperado es un conjunto de nuevos archivos en el directorio de datos, un archivo por hoja de cálculo del libro de trabajo de origen. Cada archivo lleva el nombre de su hoja de origen correspondiente, y el archivo contiene los datos (y opcionalmente el formato) de esa única hoja.

## **Dividir un archivo Excel copiando un rango en un nuevo libro de trabajo**

### **Descripción del enfoque**

A veces, los datos que necesita dividir no corresponden a una hoja de cálculo completa, sino a una región rectangular específica de una hoja de cálculo, como `A1:D10` o un rango con nombre que representa una tabla particular. En estos casos, copiar hojas de cálculo completas es un desperdicio, y se requiere un enfoque más preciso: identifique el rango de origen, copie solo ese rango en un nuevo libro de trabajo y guarde el nuevo archivo.

Este enfoque es ideal cuando desea extraer una sola tabla, bloque de informes o área de datos de una hoja de cálculo más grande descartando todo el contenido no relacionado. También es útil para exportar regiones seleccionadas por el usuario de una hoja como archivos independientes.

### **Pasos**

Los siguientes pasos describen cómo dividir un archivo Excel copiando un rango específico en un nuevo libro de trabajo:

1. Abra el archivo Excel de origen creando una instancia de un objeto `Workbook` con la ruta del archivo.
2. Recupere la `Worksheet` de destino que contiene el rango que desea copiar, ya sea por índice (por ejemplo, la primera hoja) o por nombre de la colección `Worksheets`.
3. Identifique el rango que se va a copiar. Puede ser un rango de celdas codificado de forma fija como `A1:C10`, o un rango con nombre obtenido a través de la colección `Worksheet.Cells`, o un rango creado mediante `Worksheet.Cells.createRange`.
4. Cree una nueva instancia de `Workbook` de destino.
5. Acceda a la primera `Worksheet` del libro de trabajo de destino (la hoja predeterminada).
6. Copie el rango de origen en la hoja de cálculo de destino, normalmente comenzando desde la celda `A1`. Se puede utilizar el método `Cells.copy` en la colección `Cells` de destino para copiar un rango completo, o puede iterar a través de las celdas del rango de origen y escribir sus valores en las celdas de destino con `putValue`. Se pueden proporcionar `CopyOptions` opcionales para controlar lo que se transfiere (solo valores, valores y estilos, fórmulas, etc.).
7. Guarde el libro de trabajo de destino en una nueva ruta de archivo en disco utilizando el método `Workbook.save`.

### **Ejemplo de código**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat

# Definir el directorio de datos y las rutas de los archivos
dataDir = "data/"
sourcePath = dataDir + "book1.xls"
outputPath = dataDir + "outputrange.xls"

# Abrir el archivo Excel de origen
sourceWorkbook = Workbook(sourcePath)

# Obtener la primera hoja de cálculo del libro de origen
sourceWorksheet = sourceWorkbook.getWorksheets().get(0)

# Definir el rango de celdas de origen A1:C10 (10 filas, 3 columnas comenzando en fila 0, columna 0)
sourceRange = sourceWorksheet.getCells().createRange(0, 0, 10, 3)

# Crear un nuevo libro de destino
destWorkbook = Workbook()

# Acceder a la primera hoja de cálculo del libro de destino
destWorksheet = destWorkbook.getWorksheets().get(0)

# Crear el rango de destino en A1 con las mismas dimensiones que el rango de origen
destRange = destWorksheet.getCells().createRange(0, 0, 10, 3)

# Copiar el rango de origen al rango de destino
destRange.copy(sourceRange)

# Guardar el libro de destino en un nuevo archivo .xls
destWorkbook.save(outputPath, SaveFormat.Excel97To2003)

jpype.shutdownJVM()
```

El resultado esperado es un único archivo nuevo en el directorio de datos que contiene solo los valores (y opcionalmente el formato) del rango especificado extraído del libro de trabajo de origen. El archivo de destino no tiene relación con ningún otro dato del archivo de origen; contiene solo el rango extraído, comenzando en la celda `A1` de su primera hoja de cálculo.



{{< app/cells/assistant language="python" >}}