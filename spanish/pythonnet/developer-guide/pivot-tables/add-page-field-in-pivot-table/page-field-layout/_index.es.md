---
title: Modificar el diseño del campo de página en una tabla dinámica
linktitle: Modificar el diseño del campo de página en una tabla dinámica
description: Aprenda a controlar el diseño del área de campos de página en una tabla dinámica usando Aspose.Cells for Python via .NET, incluyendo establecer el orden de visualización, el número de ajuste y el orden de los campos de página en la parte superior de la tabla dinámica.
keywords: Aspose.Cells, biblioteca de Python via .NET, hoja de cálculo, tabla dinámica, campo de página, orden del campo de página, número de ajuste del campo de página, mover campo de página
type: docs
weight: 191
url: /es/python-net/change-page-field-layout/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Este artículo es una continuación del tema **Agregar campo de página en una tabla dinámica**. Demuestra cómo controlar el diseño del área de campos de página, la franja de controles de filtro en la parte superior de una tabla dinámica, incluyendo el orden de visualización, el número de ajuste y la reordenación de campos.
{{% /alert %}}

## **Introducción**
Una tabla dinámica en Microsoft Excel expone un **área de campos de página** dedicada que se sitúa encima del cuerpo de filas, columnas y datos de la tabla. Esta área se representa como una franja de controles desplegables de filtro (uno por cada campo de página) y es lo que los usuarios finales hacen clic para segmentar la tabla dinámica por criterios como año o región. Aspose.Cells for Python via .NET modela esta área a través de la colección `pivot_table.page_fields` y expone tres propiedades que controlan cómo se dispone visualmente la franja:
- `pivot_table.page_field_order` (un valor de tipo `PrintOrderType`) decide si los campos de página adicionales se colocan *junto a* los existentes o *debajo* de ellos.
- `pivot_table.page_field_wrap_count` establece cuántos campos de página se colocan por fila o columna antes de ajustar.
- `pivot_table.page_fields.move(curr_index, dest_index)` reordena los campos de página sin cambiar el modo de orden.
Este artículo recorre tres ejemplos de código que demuestran cada una de estas operaciones sobre un conjunto de datos compartido, para que pueda comparar los diseños resultantes uno junto al otro.

## **Datos de origen**
| Fruta  | Año  | Región | Cantidad |
|--------|------|--------|----------|
| Manzana | 2022 | Norte  | 150      |
| Manzana | 2023 | Norte  | 180      |
| Plátano | 2022 | Sur    | 120      |
| Plátano | 2023 | Sur    | 140      |
| Cereza  | 2022 | Este   | 200      |
| Cereza  | 2023 | Este   | 220      |
| Uva     | 2022 | Oeste  | 90       |
| Uva     | 2023 | Oeste  | 110      |
Las ocho filas se rellenan en cada ejemplo de código, en idéntico orden, de modo que los datos de origen nunca difieren entre escenarios; solo lo hacen las propiedades del diseño del campo de página.

## **Ejemplo 1: A lo ancho y luego hacia abajo**
En el primer escenario configuramos los dos campos de página (`Year`, `Region`) para que aparezcan **uno junto al otro en una sola fila** en la parte superior de la tabla dinámica. Asignamos `Fruit` al eje de filas, colocamos `Year` primero y `Region` segundo en el eje de página (el orden de las llamadas `add_field_to_area` determina el índice inicial), añadimos `Amount` (Suma) como campo de datos, y luego establecemos `page_field_order` en `PrintOrderType.OverThenDown` con `page_field_wrap_count = 2`. Con `OverThenDown` y un número de ajuste de 2, los dos campos de página se disponen horizontalmente uno junto al otro en una sola fila en la parte superior de la tabla dinámica, por lo que la franja ocupa una fila de ancho dos.

```python
import aspose.cells as ac
workbook = ac.Workbook()
data_sheet = workbook.worksheets[0]
data_sheet.name = "PivotData"
data_sheet.cells["A1"].put_value("Fruit")
data_sheet.cells["B1"].put_value("Year")
data_sheet.cells["C1"].put_value("Region")
data_sheet.cells["D1"].put_value("Amount")
data_sheet.cells["A2"].put_value("Apple")
data_sheet.cells["B2"].put_value(2022)
data_sheet.cells["C2"].put_value("North")
data_sheet.cells["D2"].put_value(150)
data_sheet.cells["A3"].put_value("Apple")
data_sheet.cells["B3"].put_value(2023)
data_sheet.cells["C3"].put_value("North")
data_sheet.cells["D3"].put_value(180)
data_sheet.cells["A4"].put_value("Banana")
data_sheet.cells["B4"].put_value(2022)
data_sheet.cells["C4"].put_value("South")
data_sheet.cells["D4"].put_value(120)
data_sheet.cells["A5"].put_value("Banana")
data_sheet.cells["B5"].put_value(2023)
data_sheet.cells["C5"].put_value("South")
data_sheet.cells["D5"].put_value(140)
data_sheet.cells["A6"].put_value("Cherry")
data_sheet.cells["B6"].put_value(2022)
data_sheet.cells["C6"].put_value("East")
data_sheet.cells["D6"].put_value(200)
data_sheet.cells["A7"].put_value("Cherry")
data_sheet.cells["B7"].put_value(2023)
data_sheet.cells["C7"].put_value("East")
data_sheet.cells["D7"].put_value(220)
data_sheet.cells["A8"].put_value("Grape")
data_sheet.cells["B8"].put_value(2022)
data_sheet.cells["C8"].put_value("West")
data_sheet.cells["D8"].put_value(90)
data_sheet.cells["A9"].put_value("Grape")
data_sheet.cells["B9"].put_value(2023)
data_sheet.cells["C9"].put_value("West")
data_sheet.cells["D9"].put_value(110)
pivot_sheet_idx = workbook.worksheets.add("PivotTableReport")
pivot_sheet = workbook.worksheets[pivot_sheet_idx]
pivot_idx = pivot_sheet.pivot_tables.add("PivotData!A1:D9", "A3", "PivotTable")
pivot_table = pivot_sheet.pivot_tables[pivot_idx]
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)
pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2
pivot_table.page_fields.move(0, 1)
pivot_table.calculate_data()
workbook.save("pageFieldLayout_move.xlsx")
```

## **Ejemplo 2: Hacia abajo y luego a lo ancho**
En este ejemplo colocamos `Fruit` en el eje de filas, `Year` y `Region` en el eje de página (con `Year` primero), y `Amount` (Suma) como campo de datos, exactamente como en el Ejemplo 1. Luego establecemos `page_field_order` en `PrintOrderType.DownThenOver` y `page_field_wrap_count` en `2`. Con `DownThenOver` y un número de ajuste de 2, los dos campos de página se apilan verticalmente: `Year` arriba, `Region` directamente debajo, formando una sola columna en la parte superior de la tabla dinámica. Por lo tanto, la franja ocupa dos filas de ancho uno, en contraste con el Ejemplo 1.

```python
import aspose.cells as ac
workbook = ac.Workbook()
pivot_data = workbook.worksheets[0]
pivot_data.name = "PivotData"
pivot_report_idx = workbook.worksheets.add("PivotTableReport")
pivot_report = workbook.worksheets[pivot_report_idx]
headers = ["Fruit", "Year", "Region", "Amount"]
for c in range(len(headers)):
    pivot_data.cells[0, c].put_value(headers[c])
data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
]
for r in range(len(data)):
    for c in range(len(data[r])):
        pivot_data.cells[r + 1, c].put_value(data[r][c])
idx = pivot_report.pivot_tables.add("PivotData!A1:D9", "A1", "PivotTable")
pivot_table = pivot_report.pivot_tables[idx]
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)
pivot_table.page_field_order = ac.PrintOrderType.DOWN_THEN_OVER
pivot_table.page_field_wrap_count = 2
pivot_table.calculate_data()
workbook.save("pageFieldLayout_downThenOver.xlsx")
```

## **Ejemplo 3: Mover un campo de página**
En el tercer escenario conservamos este conjunto de datos y la asignación de campos, establecemos un diseño neutro (`OverThenDown` con número de ajuste `2`), y luego demostramos la operación `page_fields.move`. La llamada `move(0, 1)` mueve el campo de página en el índice 0 (`Year`) a la posición 1, y el campo de página que estaba en la posición 1 (`Region`) se desplaza a la posición 0. Tras esta llamada, `Region` es el primer campo de página y `Year` es el segundo. El ajuste y el modo de orden no cambian, por lo que la franja se sigue representando horizontalmente uno junto al otro; solo se ha intercambiado el orden de los dos desplegables.

```python
import os
import aspose.cells as ac
data_dir = "output"
if not os.path.exists(data_dir):
    os.makedirs(data_dir, exist_ok=True)
workbook = ac.Workbook()
worksheets = workbook.worksheets
pivot_data_idx = worksheets.add("PivotData")
pivot_data_sheet = worksheets[pivot_data_idx]
pivot_data_cells = pivot_data_sheet.cells
# Headers (row 0)
pivot_data_cells[0, 0].put_value("Fruit")
pivot_data_cells[0, 1].put_value("Year")
pivot_data_cells[0, 2].put_value("Region")
pivot_data_cells[0, 3].put_value("Amount")
# Row 1: Apple, 2022, North, 150
pivot_data_cells[1, 0].put_value("Apple")
pivot_data_cells[1, 1].put_value(2022)
pivot_data_cells[1, 2].put_value("North")
pivot_data_cells[1, 3].put_value(150)
# Row 2: Apple, 2023, North, 180
pivot_data_cells[2, 0].put_value("Apple")
pivot_data_cells[2, 1].put_value(2023)
pivot_data_cells[2, 2].put_value("North")
pivot_data_cells[2, 3].put_value(180)
# Row 3: Banana, 2022, South, 120
pivot_data_cells[3, 0].put_value("Banana")
pivot_data_cells[3, 1].put_value(2022)
pivot_data_cells[3, 2].put_value("South")
pivot_data_cells[3, 3].put_value(120)
# Row 4: Banana, 2023, South, 140
pivot_data_cells[4, 0].put_value("Banana")
pivot_data_cells[4, 1].put_value(2023)
pivot_data_cells[4, 2].put_value("South")
pivot_data_cells[4, 3].put_value(140)
# Row 5: Cherry, 2022, East, 200
pivot_data_cells[5, 0].put_value("Cherry")
pivot_data_cells[5, 1].put_value(2022)
pivot_data_cells[5, 2].put_value("East")
pivot_data_cells[5, 3].put_value(200)
# Row 6: Cherry, 2023, East, 220
pivot_data_cells[6, 0].put_value("Cherry")
pivot_data_cells[6, 1].put_value(2023)
pivot_data_cells[6, 2].put_value("East")
pivot_data_cells[6, 3].put_value(220)
# Row 7: Grape, 2022, West, 90
pivot_data_cells[7, 0].put_value("Grape")
pivot_data_cells[7, 1].put_value(2022)
pivot_data_cells[7, 2].put_value("West")
pivot_data_cells[7, 3].put_value(90)
# Row 8: Grape, 2023, West, 110
pivot_data_cells[8, 0].put_value("Grape")
pivot_data_cells[8, 1].put_value(2023)
pivot_data_cells[8, 2].put_value("West")
pivot_data_cells[8, 3].put_value(110)
# Add PivotTableReport sheet
pivot_table_sheet_idx = worksheets.add("PivotTableReport")
pivot_table_sheet = worksheets[pivot_table_sheet_idx]
pivot_tables = pivot_table_sheet.pivot_tables
# Create pivot table sourced from PivotData!A1:D9 placed at A1 on PivotTableReport
pivot_index = pivot_tables.add("PivotData!A1:D9", "A1", "PivotTable1")
pivot_table = pivot_tables[pivot_index]
# Add fields
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)   # Fruit
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)  # Year
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)  # Region
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)  # Amount
pivot_table.data_fields[0].function = ac.ConsolidationFunction.SUM
# Configure page field area layout: place page fields across first, wrap after every 2
pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2
# Refresh and calculate
pivot_table.calculate_data()
# Save
workbook.save(os.path.join(data_dir, "pageFieldLayout_overThenDown.xlsx"))
```

## **Artículos relacionados**
- [Agregar campo de página en una tabla dinámica](/cells/es/python-net/add-page-field-in-pivot-table/) — la página principal que introduce cómo se añaden los campos de página a una tabla dinámica.
- [Campos de fila y columna en una tabla dinámica](/cells/es/python-net/row-and-column-fields/) — cubre la asignación de campos a los ejes de fila y columna, complementando el trabajo del eje de página mostrado aquí.
- [Administrar campos de valor en una tabla dinámica](/cells/es/python-net/manage-value-fields/) — describe cómo configurar el área de datos (valores), incluyendo la agregación `Sum` utilizada en este artículo.
- [Actualizar tabla dinámica](/cells/es/python-net/refresh-pivot-table/) — explica `refresh_data` y `calculate_data`, que son obligatorios tras reordenar campos de página.
- [Aplicar estilo a una tabla dinámica](/cells/es/python-net/apply-style-to-pivot-table/) — muestra cómo dar formato a la tabla dinámica representada después de haber dispuesto la franja de campos de página.

{{< app/cells/assistant language="python-net" >}}