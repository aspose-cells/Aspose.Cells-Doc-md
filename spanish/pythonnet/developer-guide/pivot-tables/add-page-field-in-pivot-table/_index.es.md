---
title: Agregar campos de filtro a una tabla dinámica en Aspose.Cells for Python via .NET
description: Aprenda a agregar y configurar campos de filtro en tablas dinámicas con Aspose.Cells for Python via .NET, incluyendo la adición de campos de filtro, el filtrado de selección única y el filtrado de selección múltiple.
keywords: Aspose.Cells, Python via .NET, tabla dinámica, campo de filtro, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtro
type: docs
weight: 250
url: /es/python-net/add-page-field-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
linktitle: Agregar campos de filtro
---

{{% alert color="primary" %}}
Aspose.Cells admite el ciclo de vida completo de los campos de filtro en las tablas dinámicas. Puede agregar un campo de filtro mediante una API de conveniencia de alto nivel o mediante la colección de bajo nivel `page_fields`, y puede controlar el filtro en modo de selección única, limpiarlo para mostrar todos los elementos del filtro o cambiar el campo a selección múltiple para que los usuarios puedan elegir varios elementos del filtro a la vez mediante la interfaz de usuario de casillas de verificación en Excel.
{{% /alert %}}

## **Introducción**
Un campo de filtro es un campo dinámico que controla *qué subconjunto* de los datos de origen muestra el cuerpo de la tabla dinámica. Los usuarios finales lo ven como un menú desplegable en la parte superior de una tabla dinámica ya representada en Excel, y al seleccionar uno de los elementos del filtro disponibles se reconstruye el cuerpo de la tabla dinámica de modo que solo se resuman los registros que pertenecen a ese elemento de filtro. Un campo dinámico se convierte en un campo de filtro cuando se registra como `PivotFieldType.PAGE` en lugar de `PivotFieldType.ROW`, `PivotFieldType.COLUMN` o `PivotFieldType.DATA`.

## **Agregar un campo de filtro**

### Agregar un campo de filtro con add_field_to_area
El siguiente ejemplo crea un pequeño conjunto de datos de Fruta / Año / Importe, coloca una tabla dinámica en la celda E3 con `Fruit` en el área de filas, `Amount` en el área de datos y `Year` en el área de filtro, actualiza la tabla dinámica y guarda el libro.

```python
import aspose.cells as ac
# Crear un nuevo libro de trabajo
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
# Configurar la fila de encabezado
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
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
    worksheet.cells[i + 1, 0].put_value(data[i][0])
    worksheet.cells[i + 1, 1].put_value(data[i][1])
    worksheet.cells[i + 1, 2].put_value(data[i][2])
# Agregar una tabla dinámica anclada en la celda E3
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
# Agregar campos a sus áreas: Fruta como Fila, Cantidad como Dato, Año como campo de Página
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.Page, "Year")
# Actualizar y calcular los datos de la tabla dinámica
pivot_table.calculate_data()
# Guardar el libro de trabajo
workbook.save("pageFieldSample.xlsx")
```

### Agregar un campo de filtro con page_fields.add
Cuando ya trabaja con una instancia de `PivotField`, puede pasarla directamente a `PivotTable.page_fields.add`. La tabla dinámica y el campo de filtro se construyen exactamente como en el escenario anterior; solo se reemplaza el registro final del área de filtro con la llamada a la API de bajo nivel.

```python
import aspose.cells as ac
# — La tabla dinámica y el campo de página se construyen exactamente como en
#   el Escenario 1a (datos de Fruta/Año/Importe, pivote en E3, Fruta→Fila,
#   Importe→Datos). A continuación obtenemos el PivotField de Año desde la
#   colección BaseFields y lo pasamos a PageFields.Add — la alternativa
#   de bajo nivel a AddFieldToArea. El resultado es funcionalmente
#   idéntico al Escenario 1a.
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
# Encabezados
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")
# Datos de muestra (9 filas)
sheet.cells["A2"].put_value("apple");    sheet.cells["B2"].put_value("2020"); sheet.cells["C2"].put_value(100)
sheet.cells["A3"].put_value("apple");    sheet.cells["B3"].put_value("2021"); sheet.cells["C3"].put_value(150)
sheet.cells["A4"].put_value("apple");    sheet.cells["B4"].put_value("2022"); sheet.cells["C4"].put_value(200)
sheet.cells["A5"].put_value("grape");    sheet.cells["B5"].put_value("2020"); sheet.cells["C5"].put_value(300)
sheet.cells["A6"].put_value("grape");    sheet.cells["B6"].put_value("2021"); sheet.cells["C6"].put_value(400)
sheet.cells["A7"].put_value("grape");    sheet.cells["B7"].put_value("2022"); sheet.cells["C7"].put_value(500)
sheet.cells["A8"].put_value("blueberry"); sheet.cells["B8"].put_value("2020"); sheet.cells["C8"].put_value(250)
sheet.cells["A9"].put_value("blueberry"); sheet.cells["B9"].put_value("2021"); sheet.cells["C9"].put_value(350)
sheet.cells["A10"].put_value("blueberry");sheet.cells["B10"].put_value("2022"); sheet.cells["C10"].put_value(450)
# Agregar tabla dinámica en E3 cubriendo A1:C10
pivot_index = sheet.pivot_tables.add("E3", "A1:C10", "PivotTable1")
pivot_table = sheet.pivot_tables[pivot_index]
# Fruta -> Fila, Importe -> Datos (Año irá a Página a continuación)
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
# Enfoque de bajo nivel: obtener el PivotField existente de Año desde BaseFields
# y registrarlo en el área de Página mediante PageFields.Add(PivotField).
year_field = pivot_table.base_fields["Year"]
pivot_table.page_fields.add(year_field)
# Actualizar para que el nuevo campo de página se refleje en el libro guardado
pivot_table.calculate_data()
workbook.save("output.xlsx")
```

## **Filtrado de selección única (mostrar un elemento de filtro)**
En el comportamiento predeterminado de selección única, el campo de filtro se representa como un único menú desplegable y el entero `PivotField.current_page_item` selecciona qué elemento de filtro dirige el cuerpo de la tabla dinámica. Asignar un índice específico elige ese único elemento; asignar el centinela especial `0x7FFD` (decimal 32765) limpia el filtro para que todos los elementos del filtro se resuman a la vez. La selección única es el comportamiento predeterminado; no necesita habilitarla explícitamente.

### Mostrar todos los elementos
Establecer `current_page_item` en el valor mágico `0x7FFD` equivale a limpiar el filtro: el cuerpo de la tabla dinámica resume todos los elementos del filtro como si no se hubiera aplicado ningún filtro.

```python
import aspose.cells as ac
# Crear un nuevo libro de trabajo
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
# Poblar datos de Fruta/Año/Cantidad
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")
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
        sheet.cells[r + 1, c].put_value(data[r][c])
# Crear tabla dinámica en E3
pivot_tables = sheet.pivot_tables
index = pivot_tables.add("=A1:C7", "E3", "PivotTable1")
pivot_table = pivot_tables[index]
# Configurar campos dinámicos: Fruta→Fila, Cantidad→Datos, Año→Página
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.Page, "Year")
pivot_table.calculate_data()
# Borrar el filtro de página para que cada elemento del campo de página sea visible.
# 0x7FFD (decimal 32765) es el valor centinela especial que significa "todos los elementos" —
# equivalente a seleccionar "(Todos)" en el menú desplegable del campo de página de Excel.
pivot_table.page_fields[0].current_page_item = 0x7FFD
workbook.save("output.xlsx")
```

### Mostrar un elemento específico
Establecer `current_page_item` en un índice real elige solamente ese elemento de filtro. El índice es la posición del elemento en la lista ordenada de elementos del campo de filtro, por lo que, por ejemplo, `1` selecciona el segundo elemento después de ordenar.

```python
import aspose.cells as ac
# Create workbook
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
# Add sample data (Fruit/Year/Amount)
cells["A1"].put_value("Fruit")
cells["B1"].put_value("Year")
cells["C1"].put_value("Amount")
cells["A2"].put_value("Apple")
cells["B2"].put_value("2020")
cells["C2"].put_value("100")
cells["A3"].put_value("Apple")
cells["B3"].put_value("2021")
cells["C3"].put_value("150")
cells["A4"].put_value("Banana")
cells["B4"].put_value("2020")
cells["C4"].put_value("200")
cells["A5"].put_value("Banana")
cells["B5"].put_value("2021")
cells["C5"].put_value("250")
# Add pivot table at E3
pivot_tables = sheet.pivot_tables
pivot_index = pivot_tables.add("A1:C5", "E3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]
# Add fields: Fruit→Row, Amount→Data, Year→Page
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, "Year")
# Page-field-specific operations
pivot_table.page_fields[0].current_page_item = 1  # 1 = second item in sorted order (e.g. "2021")
# Refresh and calculate pivot table
pivot_table.calculate_data()
workbook.save("output.xlsx")
```

## **Filtrado de selección múltiple**
El filtrado de selección múltiple convierte el menú desplegable del filtro en una lista de casillas de verificación y permite al usuario final elegir varios elementos del filtro simultáneamente. Aspose.Cells expone dos propiedades que trabajan juntas. `PivotField.is_multiple_item_selection_allowed` debe establecerse en `True` antes de que la interfaz de selección múltiple surta efecto. Una vez habilitada, `PivotItem.is_hidden` controla qué elementos aparecen en la lista de casillas de verificación, de modo que puede mostrar todos los elementos o incluir en una lista blanca únicamente elementos específicos.

```python
import aspose.cells as ac
# — La tabla dinámica y el campo de página se construyen exactamente como en
#   Escenario 1a (datos Fruta/Año/Cantidad, pivote en E3, Fruta→Fila,
#   Cantidad→Datos, Año→Página vía AddFieldToArea).
#   A continuación aplicamos filtrado de selección múltiple en el campo de página.
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
# Datos de muestra: Fruta | Año | Cantidad
cells[0, 0].put_value("Fruit")
cells[0, 1].put_value("Year")
cells[0, 2].put_value("Amount")
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
    cells[i + 1, 0].put_value(data[i][0])
    cells[i + 1, 1].put_value(int(data[i][1]))
    cells[i + 1, 2].put_value(int(data[i][2]))
pivot_sheet = workbook.worksheets.add("Pivot")
pivots = pivot_sheet.pivot_tables
pivot_index = pivots.add("E3", "A1:C10", "PivotTable1")
pivot_table = pivots[pivot_index]
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, "Year")
# — Habilitar selección múltiple en el campo de página
pivot_table.page_fields[0].is_multiple_item_selection_allowed = True
# Parte A — seleccionar TODOS los elementos (hacer visible cada elemento)
pivot_items = pivot_table.page_fields[0].pivot_items
for i in range(pivot_items.count):
    pivot_items[i].is_hidden = False
# Parte B — seleccionar solo elementos específicos por valor de origen
for i in range(pivot_items.count):
    value = pivot_items[i].get_string_value()
    if value == "2020" or value == "grape" or value == "blueberry":
        pivot_items[i].is_hidden = False
    else:
        pivot_items[i].is_hidden = True
pivot_table.calculate_data()
workbook.save("output.xlsx")
```

> **Nota:** Cuando utilice el filtrado de selección múltiple a través de `PivotItem.is_hidden`, **al menos un `PivotItem` debe permanecer visible** (`is_hidden == False`). Si todos los elementos están ocultos, Excel se bloquea al abrir el archivo o muestra una tabla dinámica en blanco. Verifique siempre que su lista blanca de selección múltiple incluya al menos un elemento de sus datos de origen.

## **¿Qué API y qué modo debo usar?**
La tabla siguiente resume cuándo usar cada API y modo para que pueda elegir la combinación correcta sin tener que leer cada escenario en detalle.
| Escenario / Caso de uso | API recomendada | Propiedad utilizada | Notas |
|---|---|---|---|
| Agregar un campo de filtro por nombre de columna de origen (el más común) | `PivotTable.add_field_to_area(PivotFieldType.PAGE, "field_name")` | n/a | Alto nivel, en una sola línea. Use esta opción a menos que necesite una referencia a `PivotField`. |
| Agregar un campo de filtro cuando ya tiene un objeto `PivotField` | `PivotTable.page_fields.add(PivotField)` | n/a | Use cuando el objeto del campo se haya obtenido en otro lugar o necesite reutilizarse. |
| Filtrar a un único elemento de filtro (modo predeterminado) | `PivotField.current_page_item` | establecer en un índice específico | Por ejemplo, `1` muestra el segundo elemento de la lista ordenada. |
| Mostrar todos los elementos / limpiar el filtro | `PivotField.current_page_item` | establecer en `0x7FFD` | El valor mágico `0x7FFD` (decimal 32765) es el centinela de "todos los elementos". |
| Habilitar la interfaz de selección múltiple en Excel | `PivotField.is_multiple_item_selection_allowed` | establecer en `True` | Requerido antes de que cualquier llamada a `is_hidden` surta efecto. |
| Ocultar / mostrar elementos individuales en una lista de selección múltiple | `PivotItem.is_hidden` | establecer por elemento | Al menos un elemento debe permanecer visible (`is_hidden == False`). |

{{% alert color="primary" %}}
Recuerde siempre la restricción de visibilidad cuando configure el filtrado de selección múltiple. Si todos los `PivotItem` de un campo de filtro de selección múltiple están ocultos, Excel se bloquea al abrir el archivo o muestra una tabla dinámica en blanco. Construya su lista blanca a partir de sus datos de origen para que al menos un elemento permanezca visible, y sus libros guardados se abrirán de manera confiable en cualquier equipo.
{{% /alert %}}

{{< app/cells/assistant language="python-net" >}}