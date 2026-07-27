---
title: Agregar campos de fila y columna a una tabla dinámica en Aspose.Cells para .NET
linktitle: Campos de fila y columna
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.setSubtotals in Aspose.Cells for Python via Java.
keywords: Aspose.Cells, Python via Java, pivot table, row field, column field, PivotField, setSubtotals, PivotFieldSubtotalType, subtotals
type: docs
weight: 220
url: /es/python-java/pivot-table-add-row-column-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Agregar un campo a la región de fila o columna**

El método `PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` mueve un campo base desde los datos de origen a una de las cuatro regiones de la tabla dinámica. El argumento `fieldType` acepta uno de los siguientes valores de `PivotFieldType`.

- `ROW` — campos colocados verticalmente a la izquierda
- `COLUMN` — campos colocados horizontalmente en la parte superior
- `DATA` — campos cuyos valores se agregan
- `PAGE` — campos utilizados como filtros de informe

Después de agregar los campos, puede acceder a ellos a través de los métodos `PivotTable.getRowFields()` y `PivotTable.getColumnFields()`. Cada método devuelve un `PivotFieldCollection`. El campo en el índice 0 de `RowFields` es el campo de fila más externo, y los índices siguientes representan campos anidados dentro de él. La misma convención de indexación se aplica a `ColumnFields`.

El orden de anidamiento de los campos es importante. Agregar `Category` a la región de fila primero y luego `Item` produce una tabla dinámica cuya agrupación externa es `Category` y cuya agrupación interna es `Item`. Invertir el orden invierte la jerarquía.

## **Subtotales de campo de pivote**

El método `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` controla qué filas de subtotal aparecen para un campo de pivote. Cada llamada activa o desactiva un único tipo de subtotal de forma independiente. Pasar `shown = true` muestra el subtotal, mientras que `shown = false` lo oculta. Como cada llamada solo afecta a un tipo, llamar al método varias veces con diferentes valores de `subtotalType` crea un subconjunto personalizado de subtotales.

La enumeración `PivotFieldSubtotalType` define los tipos de subtotales disponibles.

- `AUTOMATIC` — Aspose.Cells elige la selección predeterminada (normalmente `SUM` para campos numéricos)
- `NONE` — suprime todas las filas de subtotal
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STD_DEV`
- `STD_DEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
Los subtotales solo se representan cuando hay dos o más campos de pivote en la región de fila (o en la región de columna). Un solo campo no tiene nada significativo que subtotalizar entre ellos, por lo que las llamadas a `setSubtotals` no tienen ningún efecto visible en ese caso. Por lo tanto, este artículo coloca dos campos de fila (`Category` externo, `Item` interno) en cada ejemplo para que el límite del subtotal entre cada grupo `Category` sea visible.
{{% /alert %}}

## **Escenario 1 — Subtotales automáticos (predeterminados)**

Cuando no se llama a `setSubtotals` en absoluto, Aspose.Cells aplica la selección `AUTOMATIC` a los campos numéricos. El siguiente ejemplo confirma explícitamente este comportamiento llamando a `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` en el campo de fila `Category` externo.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, PivotTable, PivotField, PivotFieldType, PivotFieldSubtotalType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")

worksheet.getCells().get(0, 0).putValue("Category")
worksheet.getCells().get(0, 1).putValue("Item")
worksheet.getCells().get(0, 2).putValue("Year")
worksheet.getCells().get(0, 3).putValue("Amount")

worksheet.getCells().get(1, 0).putValue("Fruit")
worksheet.getCells().get(1, 1).putValue("Apple")
worksheet.getCells().get(1, 2).putValue(2020)
worksheet.getCells().get(1, 3).putValue(100)

worksheet.getCells().get(2, 0).putValue("Fruit")
worksheet.getCells().get(2, 1).putValue("Apple")
worksheet.getCells().get(2, 2).putValue(2021)
worksheet.getCells().get(2, 3).putValue(150)

worksheet.getCells().get(3, 0).putValue("Fruit")
worksheet.getCells().get(3, 1).putValue("Banana")
worksheet.getCells().get(3, 2).putValue(2020)
worksheet.getCells().get(3, 3).putValue(80)

worksheet.getCells().get(4, 0).putValue("Fruit")
worksheet.getCells().get(4, 1).putValue("Banana")
worksheet.getCells().get(4, 2).putValue(2021)
worksheet.getCells().get(4, 3).putValue(90)

worksheet.getCells().get(5, 0).putValue("Vegetable")
worksheet.getCells().get(5, 1).putValue("Carrot")
worksheet.getCells().get(5, 2).putValue(2020)
worksheet.getCells().get(5, 3).putValue(50)

worksheet.getCells().get(6, 0).putValue("Vegetable")
worksheet.getCells().get(6, 1).putValue("Carrot")
worksheet.getCells().get(6, 2).putValue(2021)
worksheet.getCells().get(6, 3).putValue(60)

worksheet.getCells().get(7, 0).putValue("Vegetable")
worksheet.getCells().get(7, 1).putValue("Daikon")
worksheet.getCells().get(7, 2).putValue(2020)
worksheet.getCells().get(7, 3).putValue(40)

worksheet.getCells().get(8, 0).putValue("Vegetable")
worksheet.getCells().get(8, 1).putValue("Daikon")
worksheet.getCells().get(8, 2).putValue(2021)
worksheet.getCells().get(8, 3).putValue(45)

pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.AUTOMATIC, True)

pivotTable.calculateData()

workbook.save("output_automatic.xlsx")

jpype.shutdownJVM()
```

## **Escenario 2 — Suprimir todos los subtotales (Ninguno)**

Llamar a `setSubtotals(PivotFieldSubtotalType.NONE, true)` elimina todas las filas de subtotal de la tabla dinámica, dejando solo las filas de campo y el total general en la parte inferior. Esto es útil cuando desea los datos agrupados sin procesar sin ninguna fila de resumen.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PivotFieldSubtotalType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")

headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.getCells().get(0, j).putValue(headers[j])

data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020, 80 ],
    ["Fruit",     "Banana", 2021, 90 ],
    ["Vegetable", "Carrot", 2020, 50 ],
    ["Vegetable", "Carrot", 2021, 60 ],
    ["Vegetable", "Daikon", 2020, 40 ],
    ["Vegetable", "Daikon", 2021, 45 ]
]

for i in range(len(data)):
    for j in range(len(data[0])):
        worksheet.getCells().get(i + 1, j).putValue(data[i][j])

pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.NONE, True)
pivotTable.calculateData()

workbook.save("output_none.xlsx")

jpype.shutdownJVM()
```

## **Escenario 3 — Subconjunto de subtotales personalizado (Suma + Promedio)**

No está limitado a un solo tipo de subtotal. Cada llamada a `setSubtotals` opera de forma independiente en un tipo, por lo que llamar al método dos veces — una vez con `SUM` y otra con `AVERAGE` — produce un subconjunto personalizado de dos filas de subtotal para cada grupo `Category`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTableCollection, PivotTable, PivotFieldType, PivotField, PivotFieldSubtotalType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")

worksheet.getCells().get("A1").putValue("Category")
worksheet.getCells().get("B1").putValue("Item")
worksheet.getCells().get("C1").putValue("Year")
worksheet.getCells().get("D1").putValue("Amount")

worksheet.getCells().get(1, 0).putValue("Fruit")
worksheet.getCells().get(1, 1).putValue("Apple")
worksheet.getCells().get(1, 2).putValue(2020)
worksheet.getCells().get(1, 3).putValue(100)

worksheet.getCells().get(2, 0).putValue("Fruit")
worksheet.getCells().get(2, 1).putValue("Apple")
worksheet.getCells().get(2, 2).putValue(2021)
worksheet.getCells().get(2, 3).putValue(150)

worksheet.getCells().get(3, 0).putValue("Fruit")
worksheet.getCells().get(3, 1).putValue("Banana")
worksheet.getCells().get(3, 2).putValue(2020)
worksheet.getCells().get(3, 3).putValue(80)

worksheet.getCells().get(4, 0).putValue("Fruit")
worksheet.getCells().get(4, 1).putValue("Banana")
worksheet.getCells().get(4, 2).putValue(2021)
worksheet.getCells().get(4, 3).putValue(90)

worksheet.getCells().get(5, 0).putValue("Vegetable")
worksheet.getCells().get(5, 1).putValue("Carrot")
worksheet.getCells().get(5, 2).putValue(2020)
worksheet.getCells().get(5, 3).putValue(50)

worksheet.getCells().get(6, 0).putValue("Vegetable")
worksheet.getCells().get(6, 1).putValue("Carrot")
worksheet.getCells().get(6, 2).putValue(2021)
worksheet.getCells().get(6, 3).putValue(60)

worksheet.getCells().get(7, 0).putValue("Vegetable")
worksheet.getCells().get(7, 1).putValue("Daikon")
worksheet.getCells().get(7, 2).putValue(2020)
worksheet.getCells().get(7, 3).putValue(40)

worksheet.getCells().get(8, 0).putValue("Vegetable")
worksheet.getCells().get(8, 1).putValue("Daikon")
worksheet.getCells().get(8, 2).putValue(2021)
worksheet.getCells().get(8, 3).putValue(45)

pivotTables = worksheet.getPivotTables()
pivotIndex = pivotTables.add("A1:D9", "F3", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.Row, "Category")
pivotTable.addFieldToArea(PivotFieldType.Row, "Item")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.Sum, True)
categoryField.setSubtotals(PivotFieldSubtotalType.Average, True)

pivotTable.calculateData()

workbook.save("output_custom.xlsx")

jpype.shutdownJVM()
```
## **Resumen**

Los tres escenarios anteriores comparten el mismo conjunto de datos y la misma estructura de tabla dinámica. La única diferencia entre ellos es la llamada a `setSubtotals` aplicada al campo de fila `Category` externo. Recuerde la regla de los dos campos: un solo campo en una región no tiene nada que subtotalizar entre ellos, por lo que siempre debe colocar al menos dos campos en la región de fila o columna cuando desee que `setSubtotals` tenga un efecto visible.

## **Artículos relacionados**

- [Campos de página en tablas dinámicas](/cells/es/python-java/add-page-field-in-pivot-table/)
- [Actualizar tablas dinámicas en Aspose.Cells for Python via Java](/cells/es/python-java/refresh-pivot-table/)
- [Aplicar estilos a tablas dinámicas](/cells/es/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}
