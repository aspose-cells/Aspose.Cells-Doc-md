---
title: Agregar campos de filtro a una tabla dinámica en Aspose.Cells para .NET
linktitle: Agregar campos de filtro
description: Aprenda a añadir y configurar campos de filtro en tablas dinámicas usando Aspose.Cells for Python via Java, incluyendo añadir campos de filtro, filtrado de selección única y filtrado de selección múltiple.
keywords: Aspose.Cells, Python, Java, tabla dinámica, campo de filtro, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtro
type: docs
weight: 250
url: /es/python-java/add-filter-field-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells admite el ciclo de vida completo de los campos de filtro en tablas dinámicas. Puede añadir un campo de filtro mediante una API de conveniencia de alto nivel o mediante la colección de nivel inferior `page_fields`, y puede controlar el filtro de página en modo de selección única, limpiarlo para mostrar todos los elementos de la página, o cambiar el campo a selección múltiple para que los usuarios puedan elegir varios elementos de la página a la vez a través de la interfaz de casillas de verificación en Excel.
{{% /alert %}}

## **Introducción**

Un campo de filtro es un campo dinámico que controla *qué subconjunto* de los datos de origen muestra el cuerpo de la tabla dinámica. Los usuarios finales lo ven como un menú desplegable en la parte superior de una tabla dinámica renderizada en Excel, y al seleccionar uno de los elementos de página disponibles, el cuerpo de la tabla dinámica se reconstruye de modo que solo se resuman los registros que pertenecen a ese elemento de página. Un campo dinámico se convierte en un campo de filtro cuando se registra como `PivotFieldType.PAGE` en lugar de `PivotFieldType.ROW`, `PivotFieldType.COLUMN` o `PivotFieldType.DATA`.

Un campo de filtro puede operar en dos comportamientos. En el comportamiento predeterminado de **selección única**, solo un elemento de página es visible a la vez, por lo que el cuerpo de la tabla dinámica resume exactamente un subconjunto. En el comportamiento de **selección múltiple**, el campo expone una lista de casillas de verificación, y el cuerpo de la tabla dinámica resume la unión de cada elemento de página marcado. El mismo campo de origen se puede mover de un lado a otro entre estos comportamientos alternando una sola propiedad.

Aspose.Cells for Python via Java expone dos formas equivalentes de registrar un campo de filtro. La API de alto nivel es `PivotTable.add_field_to_area(PivotFieldType.PAGE, "fieldName")`, que toma el nombre de la columna de origen y añade el campo en una sola llamada. La API de nivel inferior es `PivotTable.page_fields.add(PivotField)`, que se utiliza cuando ya tiene una referencia `PivotField` y desea añadir la misma instancia de campo al área de filtro. Ambas APIs terminan rellenando la misma colección `page_fields`, y el resto de este artículo demuestra cómo elegir entre ellas y cómo controlar cada modo de filtrado.

## **Añadir un campo de filtro**

Hay dos formas de registrar un campo dinámico en el área de filtro. La llamada de alto nivel toma el nombre de la columna de origen como una cadena de texto y es la ruta más común. La llamada de nivel inferior acepta una instancia existente de `PivotField` y es conveniente cuando el mismo objeto de campo debe reutilizarse en múltiples áreas dinámicas. Ambas llamadas colocan el campo en `PivotTable.page_fields`, tras lo cual aparece como el menú desplegable de página en la parte superior de la tabla dinámica renderizada.

### Añadir un campo de filtro con add_field_to_area

El siguiente ejemplo construye un pequeño conjunto de datos de Fruta / Año / Cantidad, coloca una tabla dinámica en la celda E3 con `Fruit` en el área de filas, `Amount` en el área de datos, y `Year` en el área de filtro, actualiza la tabla dinámica y guarda el libro.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType

# Crear un nuevo libro de trabajo
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")

# Configurar la fila de encabezado
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Poblar 9 filas de datos de muestra: Fruta, Año, Cantidad
data = [
    ["apple", 2020, 100],
    ["banana", 2021, 200],
    ["apple", 2021, 150],
    ["grape", 2020, 120],
    ["orange", 2022, 180],
    ["banana", 2020, 90],
    ["grape", 2021, 130],
    ["apple", 2022, 170],
    ["orange", 2021, 110]
]

for i in range(len(data)):
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0])
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1])
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2])

# Agregar una tabla dinámica anclada en la celda E3
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Agregar campos a sus áreas: Fruta como Fila, Cantidad como Dato, Año como campo de Página
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# Actualizar y calcular los datos de la tabla dinámica
pivotTable.refreshData()
pivotTable.calculateData()

# Guardar el libro de trabajo
workbook.save("pageFieldSample.xlsx")

jpype.shutdownJVM()
```

### Añadir un campo de filtro con page_fields.add

Cuando ya trabaja con una instancia de `PivotField`, puede pasarla directamente a `PivotTable.page_fields.add`. La tabla dinámica y el campo de filtro se construyen exactamente como en el escenario anterior; solo se reemplaza el registro final del área de filtro con la llamada a la API de nivel inferior.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotFieldType

# — La tabla dinámica y el campo de página se construyen exactamente como en
#   el Escenario 1a (datos de Fruta/Año/Cantidad, pivote en E3, Fruta→Fila,
#   Cantidad→Datos). A continuación obtenemos el PivotField de Año de
#   la colección BaseFields y lo pasamos a PageFields.Add — la
#   alternativa de bajo nivel a AddFieldToArea. El resultado es
#   funcionalmente idéntico al Escenario 1a.

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# Encabezados
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

# Datos de muestra (9 filas)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100)
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150)
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200)
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300)
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400)
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500)
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250)
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350)
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450)

# Agregar tabla dinámica en E3 cubriendo A1:C10
pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1")
pivotTable = sheet.getPivotTables().get(pivotIndex)

# Fruta -> Fila, Cantidad -> Datos (Año irá a la Página abajo)
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Enfoque de bajo nivel: tomar el PivotField de Año existente de BaseFields
# y registrarlo en el área de Página mediante PageFields.Add(PivotField).
yearField = pivotTable.getBaseFields().get("Year")
pivotTable.getPageFields().add(yearField)

# Actualizar para que el nuevo campo de página se refleje en el libro guardado
pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Filtrado de selección única (mostrando un elemento de página)**

En el comportamiento predeterminado de selección única, el campo de filtro se renderiza como un único menú desplegable y el entero `PivotField.current_page_item` selecciona qué elemento de página dirige el cuerpo de la tabla dinámica. Asignar un índice específico elige ese único elemento; asignar el centinela especial `0x7FFD` (decimal 32765) limpia el filtro para que cada elemento de página se resuma a la vez. La selección única es el valor predeterminado; no necesita habilitarla explícitamente.

### Mostrar todos los elementos

Establecer `current_page_item` al valor mágico `0x7FFD` equivale a limpiar el filtro de página: el cuerpo de la tabla dinámica resume cada elemento de página como si no se aplicara ningún filtro.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Crear un nuevo libro de trabajo
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# Poblar datos de Fruta/Año/Cantidad
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
]

for r in range(len(data)):
    for c in range(len(data[r])):
        sheet.getCells().get(r + 1, c).putValue(data[r][c])

# Crear tabla dinámica en E3
pivotTables = sheet.getPivotTables()
index = pivotTables.add("=A1:C7", "E3", "PivotTable1")
pivotTable = pivotTables.get(index)

# Configurar campos dinámicos: Fruta→Fila, Cantidad→Datos, Año→Página
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year")

pivotTable.refreshData()
pivotTable.calculateData()

# Limpiar el filtro de página para que cada elemento del campo de página sea visible.
# 0x7FFD (decimal 32765) es el valor centinela especial que significa "todos los elementos" —
# equivalente a seleccionar "(Todos)" en el menú desplegable del campo de página de Excel.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD)

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

### Mostrar un elemento específico

Establecer `current_page_item` a un índice real elige solo ese elemento de página. El índice es la posición del elemento en la lista ordenada de elementos del campo de filtro, por ejemplo, `1` selecciona el segundo elemento después de ordenar.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# Crear libro de trabajo
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Agregar datos de muestra (Fruta/Año/Monto)
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")

cells.get("A2").putValue("Apple")
cells.get("B2").putValue("2020")
cells.get("C2").putValue("100")

cells.get("A3").putValue("Apple")
cells.get("B3").putValue("2021")
cells.get("C3").putValue("150")

cells.get("A4").putValue("Banana")
cells.get("B4").putValue("2020")
cells.get("C4").putValue("200")

cells.get("A5").putValue("Banana")
cells.get("B5").putValue("2021")
cells.get("C5").putValue("250")

# Agregar tabla dinámica en E3
pivotTables = sheet.getPivotTables()
pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)

# Agregar campos: Fruta→Fila, Monto→Dato, Año→Página
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# Operaciones específicas del campo de página
pivotTable.getPageFields().get(0).setCurrentPageItem(1) # 1 = segundo elemento en orden ordenado (p. ej. "2021")

# Actualizar y calcular la tabla dinámica
pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Filtrado de selección múltiple**

El filtrado de selección múltiple convierte el menú desplegable de página en una lista de casillas de verificación y permite al usuario final seleccionar varios elementos de página simultáneamente. Aspose.Cells expone dos propiedades que trabajan juntas. `PivotField.is_multiple_item_selection_allowed` debe establecerse en `True` antes de que la interfaz de selección múltiple surta efecto. Una vez habilitada, `PivotItem.is_hidden` controla qué elementos aparecen en la lista de casillas de verificación, por lo que puede mostrar cada elemento o incluir en la lista blanca solo elementos específicos.

El código siguiente habilita la selección múltiple en el mismo campo de filtro Year construido en el Escenario 1a, y luego muestra dos patrones: la Parte A revela cada elemento de página dejando `is_hidden` establecido en `False` para cada entrada, mientras que la Parte B incluye en la lista blanca solo los valores de origen que elija y oculta todo lo demás mediante un bloque `switch (pivot_items[i].get_string_value())`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
import os
import re

# — La tabla dinámica y el campo de página se construyen exactamente como en
#   Escenario 1a (datos de Fruta/Año/Cantidad, pivote en E3, Fruta→Fila,
#   Cantidad→Datos, Año→Página mediante AddFieldToArea).
#   A continuación aplicamos el filtrado de selección múltiple en el campo de página.

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Datos de ejemplo: Fruta | Año | Cantidad
cells.get(0, 0).putValue("Fruit")
cells.get(0, 1).putValue("Year")
cells.get(0, 2).putValue("Amount")

data = [
    ["apple",  "2019", "100"],
    ["apple",  "2020", "150"],
    ["apple",  "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape",  "2019", "120"],
    ["grape",  "2020", "170"],
    ["grape",  "2021", "220"]
]

for i in range(len(data)):
    cells.get(i + 1, 0).putValue(data[i][0])
    cells.get(i + 1, 1).putValue(int(data[i][1]))
    cells.get(i + 1, 2).putValue(int(data[i][2]))

pivotSheet = workbook.getWorksheets().add("Pivot")
pivots = pivotSheet.getPivotTables()
pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1")
pivotTable = pivots.get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# — Habilitar selección múltiple en el campo de página
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(True)

# Parte A — seleccionar TODOS los elementos (hacer visible cada elemento)
pivotItems = pivotTable.getPageFields().get(0).getPivotItems()
for i in range(pivotItems.getCount()):
    pivotItems.get(i).setHidden(False)

# Parte B — seleccionar solo elementos específicos por valor de origen
for i in range(pivotItems.getCount()):
    value = pivotItems.get(i).getStringValue()
    if value == "2020" or value == "grape" or value == "blueberry":
        pivotItems.get(i).setHidden(False)
    else:
        pivotItems.get(i).setHidden(True)

pivotTable.refreshData()
pivotTable.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

> **Nota:** Cuando use el filtrado de selección múltiple a través de `PivotItem.is_hidden`, **al menos un `PivotItem` debe permanecer visible** (`is_hidden == False`). Si cada elemento está oculto, Excel se bloquea al abrir el archivo o renderiza una tabla dinámica en blanco. Verifique siempre que su lista blanca de selección múltiple incluya al menos un elemento de sus datos de origen.

## **¿Qué API y qué modo debo usar?**

La tabla siguiente resume cuándo usar cada API y modo para que pueda elegir la combinación correcta sin leer cada escenario en detalle.

| Escenario / Caso de uso | API recomendada | Propiedad utilizada | Notas |
|---|---|---|---|
| Añadir un campo de filtro por nombre de columna de origen (lo más común) | `PivotTable.add_field_to_area(PivotFieldType.PAGE, "fieldName")` | n/a | Alto nivel, una sola línea. Use esto a menos que necesite una referencia `PivotField`. |
| Añadir un campo de filtro cuando ya tiene un objeto `PivotField` | `PivotTable.page_fields.add(PivotField)` | n/a | Use cuando el objeto de campo se obtuvo en otro lugar o necesita reutilizarse. |
| Filtrar a un único elemento de página (modo predeterminado) | `PivotField.current_page_item` | establecido a un índice específico | Por ejemplo, `1` muestra el segundo elemento en la lista ordenada. |
| Mostrar todos los elementos / limpiar el filtro de página | `PivotField.current_page_item` | establecido a `0x7FFD` | El valor mágico `0x7FFD` (decimal 32765) es el centinela de "todos los elementos". |
| Habilitar la interfaz de selección múltiple en Excel | `PivotField.is_multiple_item_selection_allowed` | establecido a `True` | Requerido antes de que cualquier llamada a `is_hidden` surta efecto. |
| Ocultar / mostrar elementos individuales en una lista de selección múltiple | `PivotItem.is_hidden` | establecido por elemento | Al menos un elemento debe permanecer visible (`is_hidden == False`). |

{{% alert color="primary" %}}
Recuerde siempre la restricción de visibilidad al configurar el filtrado de selección múltiple. Si cada `PivotItem` en un campo de filtro de selección múltiple está oculto, Excel se bloquea al abrir o renderiza una tabla dinámica en blanco. Construya su lista blanca contra sus datos de origen para que al menos un elemento permanezca visible, y sus libros guardados se abrirán de forma fiable en cualquier máquina.
{{% /alert %}}



{{< app/cells/assistant language="python" >}}