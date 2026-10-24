---
title: Agregar campos de fila y columna de tablas dinámicas en Aspose.Cells for Python via Java
linktitle: Agregar campos de fila y columna de tablas dinámicas en Aspose.Cells for Python via Java
description: Aprenda a agregar campos base a las regiones de fila y columna de una tabla dinámica y a controlar los subtotales de los campos de tabla dinámica mediante PivotField.setSubtotals en Aspose.Cells for Python via Java.
keywords: Aspose.Cells, Python via Java, tabla dinámica, campo de fila, campo de columna, PivotField, setSubtotals, PivotFieldSubtotalType, subtotales
type: docs
weight: 220
url: /es/python-java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Agregar un campo a la región de filas o columnas**
El método `PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` mueve un campo base de los datos de origen a una de las cuatro regiones de la tabla dinámica. El argumento `fieldType` acepta uno de los siguientes valores de `PivotFieldType`.
- `ROW` — campos colocados verticalmente a la izquierda
- `COLUMN` — campos colocados horizontalmente en la parte superior
- `DATA` — campos cuyos valores se agregan
- `PAGE` — campos utilizados como filtros del informe
El orden de anidamiento de los campos es importante. Agregar `Category` a la región de filas y luego `Item` produce una tabla dinámica cuya agrupación exterior es `Category` y cuya agrupación interior es `Item`. Invertir el orden invierte la jerarquía.

## **Subtotales de campos de tabla dinámica**
El método `PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` controla qué filas de subtotales aparecen para un campo de tabla dinámica. Cada llamada activa o desactiva de forma independiente un único tipo de subtotal. Al pasar `shown = true`, se muestra el subtotal, mientras que `shown = false` lo oculta. Como cada llamada solo afecta a un tipo, llamar al método varias veces con distintos valores de `subtotalType` permite crear un subconjunto personalizado de subtotales.
La enumeración `PivotFieldSubtotalType` define los tipos de subtotales disponibles.
- `AUTOMATIC` — Aspose.Cells selecciona la opción predeterminada (normalmente `SUM` para campos numéricos)
- `NONE` — suprime todas las filas de subtotales
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
Los subtotales solo se representan cuando hay dos o más campos de tabla dinámica en la región de filas o en la región de columnas. Un único campo no tiene elementos significativos entre los que calcular un subtotal, por lo que las llamadas a `setSubtotals` no tienen ningún efecto visible en ese caso. Por este motivo, este artículo coloca dos campos de fila (`Category` exterior e `Item` interior) en todos los ejemplos para que el límite del subtotal entre cada grupo `Category` sea visible.
{{% /alert %}}

## **Escenario 1 — Subtotales automáticos (predeterminados)**
Cuando no se llama a `setSubtotals` en absoluto, Aspose.Cells aplica la selección `AUTOMATIC` a los campos numéricos. El siguiente ejemplo confirma explícitamente este comportamiento al llamar a `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` en el campo de fila exterior `Category`.

```python
import jpype
import asposecells
jpype.startJVM()
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

## **Escenario 2 — Suprimir todos los subtotales (NONE)**
Llamar a `setSubtotals(PivotFieldSubtotalType.NONE, true)` elimina todas las filas de subtotales de la tabla dinámica y deja únicamente las filas de campos y el total general en la parte inferior. Esto resulta útil cuando se necesitan los datos agrupados sin ninguna fila de resumen.

```python
import jpype
import asposecells
jpype.startJVM()
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

## **Escenario 3 — Subconjunto personalizado de subtotales (SUM + AVERAGE)**
No se limita a un único tipo de subtotal. Cada llamada a `setSubtotals` opera de forma independiente sobre un tipo, por lo que llamar al método dos veces, una con `SUM` y otra con `AVERAGE`, produce un subconjunto personalizado de dos filas de subtotales para cada grupo `Category`.

```python
import jpype
import asposecells
jpype.startJVM()
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
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.SUM, True)
categoryField.setSubtotals(PivotFieldSubtotalType.AVERAGE, True)
pivotTable.calculateData()
workbook.save("output_custom.xlsx")
jpype.shutdownJVM()
```

## **Resumen**

Los tres escenarios difieren únicamente en las llamadas a `setSubtotals`. Todo lo demás —el conjunto de datos, los campos y las áreas a las que se asignan— es idéntico, lo que permite comparar directamente los diseños.
- **Colocación de campos.** `PivotTable.addFieldToArea(PivotFieldType.ROW, fieldName)` mueve una columna de origen a una región. Dentro de una misma región, el orden de las llamadas determina el orden de visualización, por lo que la primera llamada se convierte en el grupo más externo. Los subtotales requieren dos o más campos en la misma región: con un único campo no hay nada entre los grupos sobre lo cual calcular subtotales.
- **Escenario 1 — subtotales automáticos.** No invocar `setSubtotals` delega la decisión a Excel, que aplica su subtotal predeterminado a los campos numéricos. Invocar `setSubtotals` con `PivotFieldSubtotalType.AUTOMATIC` registra explícitamente esa elección en lugar de dejarla implícita.
- **Escenario 2 — sin subtotales.** `setSubtotals` con `PivotFieldSubtotalType.NONE` desactiva el subtotal predeterminado, por lo que el objeto pivot mantiene las filas del campo y el total general, pero elimina las filas de subtotal que Excel de otro modo insertaría entre ellas.
- **Escenario 3 — un subconjunto seleccionado.** Cada llamada activa o desactiva exactamente un tipo de subtotal, y las llamadas se acumulan en lugar de anularse mutuamente. Por lo tanto, invocarlo una vez con `PivotFieldSubtotalType.SUM` y otra vez con `PivotFieldSubtotalType.AVERAGE` deja ambos habilitados, y el objeto pivot muestra un subtotal de Suma, un subtotal de Promedio y un total general.

{{% alert color="primary" %}}
Nada sobre los subtotales es específico de la región de filas. Las mismas llamadas a `setSubtotals` sobre un campo obtenido de `PivotTable.ColumnFields` producen los mismos tres diseños en el eje de columnas, ya que la configuración pertenece al campo pivot y no al eje en el que se encuentra.
{{% /alert %}}
## **Artículos relacionados**
- [Campos de página en tablas dinámicas](/cells/es/python-java/add-page-field-in-pivot-table/)
- [Actualizar tablas dinámicas en Aspose.Cells for Python via Java](/cells/es/python-java/refresh-pivot-table/)
- [Aplicar estilos a tablas dinámicas](/cells/es/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}