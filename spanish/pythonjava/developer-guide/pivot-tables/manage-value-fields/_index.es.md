---
title: Campos de Valor en Aspose.Cells for Python via Java
description: Aprenda a añadir campos base a la región de datos de una tabla dinámica, cambie la función de resumen con PivotField.Function y coloque el campo de valor en el eje de filas o columnas en Aspose.Cells for Python via Java.
linktitle: Campos de Valor en Aspose.Cells for Python via Java
keywords: Aspose.Cells, Python via Java, tabla dinámica, campo de valor, PivotField, PivotField.Function, campo de datos, PivotTable.ValuesField, Suma, Promedio
type: docs
weight: 230
url: /es/python-java/manage-value-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Añadir un Campo a la Región de Datos
Añadir un campo base a la región de datos (valor) es el primer paso para dar forma a cómo una tabla dinámica agrega sus datos de origen. Aspose.Cells expone `PivotTable.addFieldToArea(PivotFieldType, string)`, una sobrecarga que acepta la constante `PivotFieldType.DATA` y el nombre de la columna de origen. Una vez que se añade un campo a la región de datos, la API lo expone a través de la colección `PivotTable.DataFields`, en el orden en que se añadieron los campos. Por defecto, una columna de origen numérica se resume con `ConsolidationFunction.SUM`, mientras que una columna no numérica utiliza `COUNT` por defecto.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.getCells().get(0, j).putValue(h)
data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45],
]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        worksheet.getCells().get(i + 1, j).putValue(val)
pivot_index = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", True, False)
pivot_table = worksheet.getPivotTables().get(pivot_index)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Category")
pivot_table.addFieldToArea(PivotFieldType.ROW, "Item")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
workbook.save("output_drag.xlsx")
jpype.shutdownJVM()
```

## Cambiar la Función de Resumen
Cada campo colocado en la región de datos se envuelve internamente como una instancia de `PivotField`, y su propiedad `Function` devuelve un valor de la enumeración `ConsolidationFunction`. El mismo setter `Function` le permite cambiar entre los agregados disponibles, incluyendo `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STDDEV`, `STDDEVP`, `VAR` y `VARP`.

{{% alert color="primary" %}}
Cambiar `Function` solo afecta al agregado, la columna de origen no cambia.
Por lo tanto, puede dejar un campo de datos como `SUM` mientras añade un segundo campo de datos que apunte a la misma columna de origen pero use `COUNT` o `AVERAGE`, todo en una sola tabla dinámica.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, ConsolidationFunction
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.getCells().get(0, j).putValue(h)
data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45],
]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        worksheet.getCells().get(i + 1, j).putValue(val)
pivot_index = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", True, False)
pivot_table = worksheet.getPivotTables().get(pivot_index)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Category")
pivot_table.addFieldToArea(PivotFieldType.ROW, "Item")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.getDataFields().get(1).setFunction(ConsolidationFunction.COUNT)
pivot_table.calculateData()
workbook.save("output_function.xlsx")
jpype.shutdownJVM()
```

## Colocar Campos de Valor en el Eje de Filas o Columnas
Cuando una tabla dinámica contiene dos o más campos de datos, Aspose.Cells expone un campo virtual adicional llamado `PivotTable.ValuesField`. Este campo virtual representa el agregado de cada campo de datos que reside en la región de datos. Puede arrastrarlo a la región de Filas o Columnas como un campo dinámico base, lo cual resulta útil para disponer múltiples medidas una junto a otra.

{{% alert color="primary" %}}
`PivotTable.ValuesField` no funciona si no hay ningún campo de valor o si solo hay uno.
Los escenarios a continuación recorren tres ejemplos de extremo a extremo que demuestran cada capacidad descrita anteriormente contra la misma estructura de tabla dinámica.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, ConsolidationFunction
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.getCells().get(0, j).putValue(h)
data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020,  80],
    ["Fruit",     "Banana", 2021,  90],
    ["Vegetable", "Carrot", 2020,  50],
    ["Vegetable", "Carrot", 2021,  60],
    ["Vegetable", "Daikon", 2020,  40],
    ["Vegetable", "Daikon", 2021,  45],
]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        worksheet.getCells().get(i + 1, j).putValue(val)
pivot_index = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", True, False)
pivot_table = worksheet.getPivotTables().get(pivot_index)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Category")
pivot_table.addFieldToArea(PivotFieldType.ROW, "Item")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.getDataFields().get(1).setFunction(ConsolidationFunction.COUNT)
pivot_table.addFieldToArea(PivotFieldType.COLUMN, pivot_table.getValuesField())
pivot_table.calculateData()
workbook.save("output_plot.xlsx")
jpype.shutdownJVM()
```

{{< app/cells/assistant language="python" >}}