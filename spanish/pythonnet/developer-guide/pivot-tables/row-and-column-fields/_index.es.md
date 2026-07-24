---
title: Campos de Fila y Columna en Aspose.Cells for Python via .NET
linktitle: Campos de fila y columna
description: Aprenda a añadir campos base a las regiones de fila y columna de una tabla dinámica y a controlar los subtotales de campos dinámicos usando PivotField.set_subtotals en Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, Python via .NET, tabla dinámica, campo de fila, campo de columna, PivotField, set_subtotals, PivotFieldSubtotalType, subtotales
type: docs
weight: 220
url: /es/python-net/row-and-column-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Los campos de fila y columna son los componentes básicos de una tabla dinámica. Un campo colocado en la región de filas aparece verticalmente a la izquierda del pivote, mientras que un campo colocado en la región de columnas aparece horizontalmente en la parte superior. Este artículo muestra cómo añadir campos base a esas regiones mediante programación y cómo controlar los subtotales que se muestran entre los grupos de campos utilizando el método `PivotField.set_subtotals`.

## **Añadir un Campo a la Región de Fila o Columna**

El método `PivotTable.add_field_to_area(PivotFieldType field_type, string field_name)` mueve un campo base desde los datos de origen a una de las cuatro regiones del pivote. El argumento `field_type` acepta uno de los siguientes valores de `PivotFieldType`.

- `ROW` — campos colocados verticalmente a la izquierda
- `COLUMN` — campos colocados horizontalmente en la parte superior
- `DATA` — campos cuyos valores se agregan
- `PAGE` — campos utilizados como filtros de informe

Después de añadir los campos, puede acceder a ellos a través de las propiedades `PivotTable.row_fields` y `PivotTable.column_fields`. Cada propiedad devuelve un `PivotFieldCollection`. El campo en el índice 0 de `row_fields` es el campo de fila más externo, y los índices siguientes representan campos anidados dentro de él. La misma convención de indexación se aplica a `column_fields`.

El orden de anidamiento de los campos es importante. Añadir `Category` a la región de filas primero y luego `Item` produce un pivote cuya agrupación externa es `Category` y cuya agrupación interna es `Item`. Invertir el orden invierte la jerarquía.

## **Subtotales de Campos Dinámicos**

El método `PivotField.set_subtotals(PivotFieldSubtotalType subtotal_type, bool shown)` controla qué filas de subtotal aparecen para un campo dinámico. Cada llamada activa o desactiva un único tipo de subtotal de forma independiente. Pasar `shown = True` muestra el subtotal, mientras que `shown = False` lo oculta. Dado que cada llamada solo afecta a un tipo, llamar al método varias veces con diferentes valores de `subtotal_type` construye un subconjunto personalizado de subtotales.

La enumeración `PivotFieldSubtotalType` define los tipos de subtotales disponibles.

- `AUTOMATIC` — Aspose.Cells elige la selección por defecto (típicamente `SUM` para campos numéricos)
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
Los subtotales solo se muestran cuando hay dos o más campos dinámicos en la región de filas (o en la región de columnas). Un solo campo no tiene nada significativo entre qué subtotalizar, por lo que las llamadas a `set_subtotals` no tienen efecto visible en ese caso. Por lo tanto, este artículo coloca dos campos de fila (`Category` externo, `Item` interno) en cada ejemplo para que el límite de subtotal entre cada grupo `Category` sea visible.
{{% /alert %}}

## **Escenario 1 — Subtotales Automáticos (Por Defecto)**

Cuando no llama a `set_subtotals` en absoluto, Aspose.Cells aplica la selección `AUTOMATIC` a los campos numéricos. El siguiente ejemplo confirma explícitamente este comportamiento llamando a `set_subtotals(PivotFieldSubtotalType.AUTOMATIC, True)` sobre el campo de fila externo `Category`.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

worksheet.cells[0, 0].put_value("Category")
worksheet.cells[0, 1].put_value("Item")
worksheet.cells[0, 2].put_value("Year")
worksheet.cells[0, 3].put_value("Amount")

worksheet.cells[1, 0].put_value("Fruit")
worksheet.cells[1, 1].put_value("Apple")
worksheet.cells[1, 2].put_value(2020)
worksheet.cells[1, 3].put_value(100)

worksheet.cells[2, 0].put_value("Fruit")
worksheet.cells[2, 1].put_value("Apple")
worksheet.cells[2, 2].put_value(2021)
worksheet.cells[2, 3].put_value(150)

worksheet.cells[3, 0].put_value("Fruit")
worksheet.cells[3, 1].put_value("Banana")
worksheet.cells[3, 2].put_value(2020)
worksheet.cells[3, 3].put_value(80)

worksheet.cells[4, 0].put_value("Fruit")
worksheet.cells[4, 1].put_value("Banana")
worksheet.cells[4, 2].put_value(2021)
worksheet.cells[4, 3].put_value(90)

worksheet.cells[5, 0].put_value("Vegetable")
worksheet.cells[5, 1].put_value("Carrot")
worksheet.cells[5, 2].put_value(2020)
worksheet.cells[5, 3].put_value(50)

worksheet.cells[6, 0].put_value("Vegetable")
worksheet.cells[6, 1].put_value("Carrot")
worksheet.cells[6, 2].put_value(2021)
worksheet.cells[6, 3].put_value(60)

worksheet.cells[7, 0].put_value("Vegetable")
worksheet.cells[7, 1].put_value("Daikon")
worksheet.cells[7, 2].put_value(2020)
worksheet.cells[7, 3].put_value(40)

worksheet.cells[8, 0].put_value("Vegetable")
worksheet.cells[8, 1].put_value("Daikon")
worksheet.cells[8, 2].put_value(2021)
worksheet.cells[8, 3].put_value(45)

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

category_field = pivot_table.row_fields[0]
category_field.set_subtotals(ac.PivotFieldSubtotalType.AUTOMATIC, True)

pivot_table.refresh_data()
pivot_table.calculate_data()

workbook.save("output_automatic.xlsx")
```

## **Escenario 2 — Suprimir Todos los Subtotales (None)**

Llamar a `set_subtotals(PivotFieldSubtotalType.NONE, True)` elimina todas las filas de subtotal del pivote, dejando solo las filas de campos y el total general al final. Esto es útil cuando se desean los datos agrupados en bruto sin ninguna fila de resumen.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

worksheet.cells[0, 0].put_value("Category")
worksheet.cells[0, 1].put_value("Item")
worksheet.cells[0, 2].put_value("Year")
worksheet.cells[0, 3].put_value("Amount")

worksheet.cells[1, 0].put_value("Fruit")
worksheet.cells[1, 1].put_value("Apple")
worksheet.cells[1, 2].put_value(2020)
worksheet.cells[1, 3].put_value(100)

worksheet.cells[2, 0].put_value("Fruit")
worksheet.cells[2, 1].put_value("Apple")
worksheet.cells[2, 2].put_value(2021)
worksheet.cells[2, 3].put_value(150)

worksheet.cells[3, 0].put_value("Fruit")
worksheet.cells[3, 1].put_value("Banana")
worksheet.cells[3, 2].put_value(2020)
worksheet.cells[3, 3].put_value(80)

worksheet.cells[4, 0].put_value("Fruit")
worksheet.cells[4, 1].put_value("Banana")
worksheet.cells[4, 2].put_value(2021)
worksheet.cells[4, 3].put_value(90)

worksheet.cells[5, 0].put_value("Vegetable")
worksheet.cells[5, 1].put_value("Carrot")
worksheet.cells[5, 2].put_value(2020)
worksheet.cells[5, 3].put_value(50)

worksheet.cells[6, 0].put_value("Vegetable")
worksheet.cells[6, 1].put_value("Carrot")
worksheet.cells[6, 2].put_value(2021)
worksheet.cells[6, 3].put_value(60)

worksheet.cells[7, 0].put_value("Vegetable")
worksheet.cells[7, 1].put_value("Daikon")
worksheet.cells[7, 2].put_value(2020)
worksheet.cells[7, 3].put_value(40)

worksheet.cells[8, 0].put_value("Vegetable")
worksheet.cells[8, 1].put_value("Daikon")
worksheet.cells[8, 2].put_value(2021)
worksheet.cells[8, 3].put_value(45)

pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

category_field = pivot_table.row_fields[0]
category_field.set_subtotals(ac.PivotFieldSubtotalType.NONE, True)

pivot_table.refresh_data()
pivot_table.calculate_data()

workbook.save("output_none.xlsx")
```

## **Escenario 3 — Subconjunto Personalizado de Subtotales (Sum + Average)**

No está limitado a un único tipo de subtotal. Cada llamada a `set_subtotals` opera de forma independiente sobre un tipo, por lo que llamar al método dos veces — una vez con `SUM` y otra con `AVERAGE` — produce un subconjunto personalizado de dos filas de subtotal para cada grupo `Category`.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

worksheet.cells["A1"].put_value("Category")
worksheet.cells["B1"].put_value("Item")
worksheet.cells["C1"].put_value("Year")
worksheet.cells["D1"].put_value("Amount")

worksheet.cells[1, 0].put_value("Fruit")
worksheet.cells[1, 1].put_value("Apple")
worksheet.cells[1, 2].put_value(2020)
worksheet.cells[1, 3].put_value(100)

worksheet.cells[2, 0].put_value("Fruit")
worksheet.cells[2, 1].put_value("Apple")
worksheet.cells[2, 2].put_value(2021)
worksheet.cells[2, 3].put_value(150)

worksheet.cells[3, 0].put_value("Fruit")
worksheet.cells[3, 1].put_value("Banana")
worksheet.cells[3, 2].put_value(2020)
worksheet.cells[3, 3].put_value(80)

worksheet.cells[4, 0].put_value("Fruit")
worksheet.cells[4, 1].put_value("Banana")
worksheet.cells[4, 2].put_value(2021)
worksheet.cells[4, 3].put_value(90)

worksheet.cells[5, 0].put_value("Vegetable")
worksheet.cells[5, 1].put_value("Carrot")
worksheet.cells[5, 2].put_value(2020)
worksheet.cells[5, 3].put_value(50)

worksheet.cells[6, 0].put_value("Vegetable")
worksheet.cells[6, 1].put_value("Carrot")
worksheet.cells[6, 2].put_value(2021)
worksheet.cells[6, 3].put_value(60)

worksheet.cells[7, 0].put_value("Vegetable")
worksheet.cells[7, 1].put_value("Daikon")
worksheet.cells[7, 2].put_value(2020)
worksheet.cells[7, 3].put_value(40)

worksheet.cells[8, 0].put_value("Vegetable")
worksheet.cells[8, 1].put_value("Daikon")
worksheet.cells[8, 2].put_value(2021)
worksheet.cells[8, 3].put_value(45)

pivot_tables = worksheet.pivot_tables
pivot_index = pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

category_field = pivot_table.row_fields[0]
category_field.set_subtotals(ac.PivotFieldSubtotalType.SUM, True)
category_field.set_subtotals(ac.PivotFieldSubtotalType.AVERAGE, True)

pivot_table.refresh_data()
pivot_table.calculate_data()

workbook.save("output_custom.xlsx")
```

## **Resumen**

Los tres escenarios anteriores comparten el mismo conjunto de datos y la misma estructura de tabla dinámica. La única diferencia entre ellos es la llamada a `set_subtotals` aplicada al campo de fila externo `Category`. Recuerde la regla de los dos campos: un solo campo en una región no tiene nada entre qué calcular un subtotal, así que coloque siempre al menos dos campos en la región de filas o columnas cuando desee que `set_subtotals` tenga un efecto visible.

## **Artículos Relacionados**

- [Campos de Página en Tablas Dinámicas](/cells/es/python-net/add-page-field-in-pivot-table/)
- [Actualizar Tablas Dinámicas en Aspose.Cells for Python via .NET](/cells/es/python-net/refresh-pivot-table/)
- [Aplicar Estilos a Tablas Dinámicas](/cells/es/python-net/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
