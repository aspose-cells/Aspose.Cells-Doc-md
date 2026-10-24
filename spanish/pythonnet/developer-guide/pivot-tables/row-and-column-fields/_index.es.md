---
title: Agregar campos de fila y columna a una tabla dinámica en Aspose.Cells for Python via .NET
linktitle: Agregar campos de fila y columna a una tabla dinámica en Aspose.Cells for Python via .NET
description: Aprenda a agregar campos base a las regiones de filas y columnas de una tabla dinámica y a controlar los subtotales de los campos dinámicos mediante PivotField.set_subtotals en Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, Python via .NET, tabla dinámica, campo de fila, campo de columna, PivotField, set_subtotals, PivotFieldSubtotalType, subtotales
type: docs
weight: 220
url: /es/python-net/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Agregar un campo a la región de filas o columnas**
El método `PivotTable.add_field_to_area(PivotFieldType field_type, string field_name)` mueve un campo base desde los datos de origen a una de las cuatro regiones de la tabla dinámica. El argumento `field_type` acepta uno de los siguientes valores de `PivotFieldType`.
- `ROW` — campos colocados verticalmente a la izquierda
- `COLUMN` — campos colocados horizontalmente en la parte superior
- `DATA` — campos cuyos valores se agregan
- `PAGE` — campos utilizados como filtros de informe
El orden de anidamiento de los campos es importante. Agregar `Category` a la región de filas primero y luego `Item` produce una tabla dinámica cuya agrupación externa es `Category` y cuya agrupación interna es `Item`. Invertir el orden invierte la jerarquía.

## **Subtotales de campos dinámicos**
El método `PivotField.set_subtotals(PivotFieldSubtotalType subtotal_type, bool shown)` controla qué filas de subtotal aparecen para un campo dinámico. Cada llamada activa o desactiva un único tipo de subtotal de forma independiente. Pasar `shown = True` muestra el subtotal, mientras que `shown = False` lo oculta. Dado que cada llamada solo afecta a un tipo, llamar al método varias veces con diferentes valores de `subtotal_type` construye un subconjunto personalizado de subtotales.
La enumeración `PivotFieldSubtotalType` define los tipos de subtotal disponibles.
- `AUTOMATIC` — Aspose.Cells elige la selección predeterminada (normalmente `SUM` para campos numéricos)
- `NONE` — suprime todas las filas de subtotal
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STDDEV`
- `STDDEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
Los subtotales solo se representan cuando hay dos o más campos dinámicos en la región de filas (o en la región de columnas). Un único campo no tiene nada significativo entre lo que subtotalizar, por lo que las llamadas a `set_subtotals` no surten efecto visible en ese caso. Por ello, este artículo coloca dos campos de fila (`Category` externo, `Item` interno) en cada ejemplo para que el límite de subtotal entre cada grupo `Category` sea visible.
{{% /alert %}}

## **Escenario 1 — Subtotales automáticos (predeterminados)**
Cuando no se llama a `set_subtotals` en absoluto, Aspose.Cells aplica la selección `AUTOMATIC` a los campos numéricos. El siguiente ejemplo confirma explícitamente este comportamiento llamando a `set_subtotals(PivotFieldSubtotalType.AUTOMATIC, True)` sobre el campo de fila externo `Category`.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldSubtotalType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
worksheet.cells.get(0, 0).put_value("Category")
worksheet.cells.get(0, 1).put_value("Item")
worksheet.cells.get(0, 2).put_value("Year")
worksheet.cells.get(0, 3).put_value("Amount")
worksheet.cells.get(1, 0).put_value("Fruit")
worksheet.cells.get(1, 1).put_value("Apple")
worksheet.cells.get(1, 2).put_value(2020)
worksheet.cells.get(1, 3).put_value(100)
worksheet.cells.get(2, 0).put_value("Fruit")
worksheet.cells.get(2, 1).put_value("Apple")
worksheet.cells.get(2, 2).put_value(2021)
worksheet.cells.get(2, 3).put_value(150)
worksheet.cells.get(3, 0).put_value("Fruit")
worksheet.cells.get(3, 1).put_value("Banana")
worksheet.cells.get(3, 2).put_value(2020)
worksheet.cells.get(3, 3).put_value(80)
worksheet.cells.get(4, 0).put_value("Fruit")
worksheet.cells.get(4, 1).put_value("Banana")
worksheet.cells.get(4, 2).put_value(2021)
worksheet.cells.get(4, 3).put_value(90)
worksheet.cells.get(5, 0).put_value("Vegetable")
worksheet.cells.get(5, 1).put_value("Carrot")
worksheet.cells.get(5, 2).put_value(2020)
worksheet.cells.get(5, 3).put_value(50)
worksheet.cells.get(6, 0).put_value("Vegetable")
worksheet.cells.get(6, 1).put_value("Carrot")
worksheet.cells.get(6, 2).put_value(2021)
worksheet.cells.get(6, 3).put_value(60)
worksheet.cells.get(7, 0).put_value("Vegetable")
worksheet.cells.get(7, 1).put_value("Daikon")
worksheet.cells.get(7, 2).put_value(2020)
worksheet.cells.get(7, 3).put_value(40)
worksheet.cells.get(8, 0).put_value("Vegetable")
worksheet.cells.get(8, 1).put_value("Daikon")
worksheet.cells.get(8, 2).put_value(2021)
worksheet.cells.get(8, 3).put_value(45)
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
category_field.set_subtotals(PivotFieldSubtotalType.AUTOMATIC, True)
pivot_table.calculate_data()
workbook.save("output_automatic.xlsx")
```

## **Escenario 2 — Suprimir todos los subtotales (Ninguno)**
Llamar a `set_subtotals(PivotFieldSubtotalType.NONE, True)` elimina todas las filas de subtotal de la tabla dinámica, dejando solo las filas de campo y el total general en la parte inferior. Esto resulta útil cuando se desea obtener los datos agrupados sin ninguna fila de resumen.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldSubtotalType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.cells.get(0, j).put_value(headers[j])
data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020, 80],
    ["Fruit",     "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45],
]
for i in range(len(data)):
    for j in range(len(data[i])):
        worksheet.cells.get(i + 1, j).put_value(data[i][j])
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
for st in [PivotFieldSubtotalType.SUM, PivotFieldSubtotalType.COUNT, PivotFieldSubtotalType.AVERAGE, PivotFieldSubtotalType.MAX, PivotFieldSubtotalType.MIN, PivotFieldSubtotalType.PRODUCT]:
    category_field.set_subtotals(st, True)
pivot_table.calculate_data()
workbook.save("output_none.xlsx")
```

## **Escenario 3 — Subconjunto personalizado de subtotales (Suma + Promedio)**
No se limita a un solo tipo de subtotal. Cada llamada a `set_subtotals` opera de forma independiente sobre un tipo, por lo que llamar al método dos veces — una con `SUM` y otra con `AVERAGE` — produce un subconjunto personalizado de dos filas de subtotal para cada grupo `Category`.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldSubtotalType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
worksheet.cells.get("A1").put_value("Category")
worksheet.cells.get("B1").put_value("Item")
worksheet.cells.get("C1").put_value("Year")
worksheet.cells.get("D1").put_value("Amount")
worksheet.cells.get(1, 0).put_value("Fruit")
worksheet.cells.get(1, 1).put_value("Apple")
worksheet.cells.get(1, 2).put_value(2020)
worksheet.cells.get(1, 3).put_value(100)
worksheet.cells.get(2, 0).put_value("Fruit")
worksheet.cells.get(2, 1).put_value("Apple")
worksheet.cells.get(2, 2).put_value(2021)
worksheet.cells.get(2, 3).put_value(150)
worksheet.cells.get(3, 0).put_value("Fruit")
worksheet.cells.get(3, 1).put_value("Banana")
worksheet.cells.get(3, 2).put_value(2020)
worksheet.cells.get(3, 3).put_value(80)
worksheet.cells.get(4, 0).put_value("Fruit")
worksheet.cells.get(4, 1).put_value("Banana")
worksheet.cells.get(4, 2).put_value(2021)
worksheet.cells.get(4, 3).put_value(90)
worksheet.cells.get(5, 0).put_value("Vegetable")
worksheet.cells.get(5, 1).put_value("Carrot")
worksheet.cells.get(5, 2).put_value(2020)
worksheet.cells.get(5, 3).put_value(50)
worksheet.cells.get(6, 0).put_value("Vegetable")
worksheet.cells.get(6, 1).put_value("Carrot")
worksheet.cells.get(6, 2).put_value(2021)
worksheet.cells.get(6, 3).put_value(60)
worksheet.cells.get(7, 0).put_value("Vegetable")
worksheet.cells.get(7, 1).put_value("Daikon")
worksheet.cells.get(7, 2).put_value(2020)
worksheet.cells.get(7, 3).put_value(40)
worksheet.cells.get(8, 0).put_value("Vegetable")
worksheet.cells.get(8, 1).put_value("Daikon")
worksheet.cells.get(8, 2).put_value(2021)
worksheet.cells.get(8, 3).put_value(45)
pivot_tables = worksheet.pivot_tables
pivot_index = pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
category_field.set_subtotals(PivotFieldSubtotalType.SUM, True)
category_field.set_subtotals(PivotFieldSubtotalType.AVERAGE, True)
pivot_table.calculate_data()
workbook.save("output_custom.xlsx")
```

## **Resumen**

Los tres escenarios difieren únicamente en las llamadas a `set_subtotals`; todo lo demás —el conjunto de datos, los campos y las áreas a las que se asignan— es idéntico, lo que hace que los diseños sean directamente comparables.
- **Colocación de campos.** `PivotTable.add_field_to_area(PivotFieldType.ROW, fieldName)` mueve una columna de origen a una región. Dentro de una región, el orden de las llamadas determina el orden de visualización, por lo que la primera llamada se convierte en el grupo más externo. Para calcular subtotales se requieren dos o más campos en la misma región: con un único campo no existe nada entre los grupos sobre lo que calcular el subtotal.
- **Escenario 1 — subtotales automáticos.** No llamar a `set_subtotals` deja la decisión en manos de Excel, que aplica su subtotal predeterminado automáticamente a los campos numéricos. Llamar a `set_subtotals` con `PivotFieldSubtotalType.AUTOMATIC` registra explícitamente esa elección en lugar de dejarla implícita.
- **Escenario 2 — sin subtotales.** `set_subtotals` con `PivotFieldSubtotalType.NONE` desactiva el subtotal predeterminado, por lo que la tabla dinámica conserva las filas de campo y el total general, pero omite las filas de subtotales que Excel insertaría de otro modo entre ellas.
- **Escenario 3 — un subconjunto elegido.** Cada llamada activa o desactiva exactamente un tipo de subtotal, y las llamadas se acumulan en lugar de restablecerse entre sí. Por lo tanto, llamar una vez con `PivotFieldSubtotalType.SUM` y otra vez con `PivotFieldSubtotalType.AVERAGE` deja ambos habilitados, y la tabla dinámica muestra un subtotal de Suma, un subtotal de Promedio y un total general.

{{% alert color="primary" %}}
Nada acerca de los subtotales es específico de la región de filas. Las mismas llamadas a `set_subtotals` sobre un campo obtenido de `PivotTable.ColumnFields` producen los mismos tres diseños en el eje de columnas, porque la configuración pertenece al campo de tabla dinámica y no al eje en el que se encuentra.
{{% /alert %}}
## **Artículos relacionados**
- [Campos de página en tablas dinámicas](/cells/es/python-net/add-page-field-in-pivot-table/)
- [Actualizar tablas dinámicas en Aspose.Cells for Python via .NET](/cells/es/python-net/refresh-pivot-table/)
- [Aplicar estilos a las tablas dinámicas](/cells/es/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}