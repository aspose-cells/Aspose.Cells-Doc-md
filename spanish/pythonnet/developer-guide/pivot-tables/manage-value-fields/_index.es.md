---
title: Administrar campos de valor de tabla dinámica en Aspose.Cells for Python via .NET
linktitle: Administrar campos de valor de tabla dinámica en Aspose.Cells for Python via .NET
description: Aprenda a agregar campos base a la región de datos de una tabla dinámica, cambiar la función de resumen con PivotField.function y trazar el campo de valor en el eje Fila o Columna en Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, Python via .NET, tabla dinámica, campo de valor, PivotField, PivotField.function, campo de datos, PivotTable.values_field, Sum, Average
type: docs
weight: 230
url: /es/python-net/manage-value-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Agregar un campo a la región de datos
Agregar un campo base a la región de datos (valor) es el primer paso para dar forma a cómo una tabla dinámica agrega los datos de origen. Aspose.Cells expone `PivotTable.AddFieldToArea(PivotFieldType, string)`, una sobrecarga que acepta la constante `PivotFieldType.Data` y el nombre de la columna de origen. Una vez que se agrega un campo a la región de datos, la API lo expone a través de la colección `PivotTable.DataFields`, en el orden en que se agregaron los campos. De forma predeterminada, una columna de origen numérica se resume con `Sum`, mientras que una columna no numérica usa `Count` por defecto.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.cells.get(0, j).put_value(h)
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
        worksheet.cells.get(i + 1, j).put_value(val)
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1", True, False)
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
workbook.save("output_drag.xlsx")
```

## Cambiar la función de resumen
Una vez que un campo reside en la región de datos, Aspose.Cells lo expone a través del objeto `PivotField` en `PivotTable.DataFields`. Cada `PivotField` tiene una propiedad `Function` modificable de tipo `ConsolidationFunction`, que controla el agregado aplicado a los valores subyacentes de ese campo. `ConsolidationFunction` es una enumeración con los miembros `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` y `Varp` — los primeros seis cubren la gran mayoría de los casos de uso del mundo real, mientras que los últimos cuatro son agregados estadísticos útiles para el análisis de varianza.

{{% alert color="primary" %}}
Cambiar `Function` solo afecta al agregado; la columna de origen y la estructura de filas/columnas de la tabla dinámica no se modifican. Para cambiar el agregado de un campo de datos existente, establezca `pivotTable.DataFields[i].Function = ConsolidationFunction.<X>;` y luego llame a `pivotTable.CalculateData()` para volver a renderizar la tabla dinámica.
{{% /alert %}}

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, ConsolidationFunction
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.cells.get(0, j).put_value(h)
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
        worksheet.cells.get(i + 1, j).put_value(val)
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1", True, False)
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ConsolidationFunction.COUNT
pivot_table.calculate_data()
workbook.save("output_function.xlsx")
```

## Trazar campos de valor en el eje Fila o Columna
Cuando una tabla dinámica contiene dos o más campos de datos, Aspose.Cells expone un campo virtual adicional llamado `PivotTable.ValuesField`. Este campo virtual representa el agregado de cada campo de datos que reside en la región de datos. Puede arrastrarlo a la región Fila o Columna como un campo dinámico base, lo cual es útil para disponer múltiples medidas una al lado de la otra.

{{% alert color="primary" %}}
`PivotTable.ValuesField` no funciona si no hay campos de valor o si solo hay uno.
{{% /alert %}}

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, ConsolidationFunction
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
headers = ["Category", "Item", "Year", "Amount"]
for j, h in enumerate(headers):
    worksheet.cells.get(0, j).put_value(h)
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
        worksheet.cells.get(i + 1, j).put_value(val)
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1", True, False)
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.data_fields[1].function = ConsolidationFunction.COUNT
pivot_table.add_field_to_area(PivotFieldType.COLUMN, pivot_table.values_field)
pivot_table.calculate_data()
workbook.save("output_plot.xlsx")
```

{{< app/cells/assistant language="python-net" >}}