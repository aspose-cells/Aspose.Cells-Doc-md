---
title: Agregar formato condicional a una tabla dinámica
linktitle: Agregar formato condicional a una tabla dinámica
description: Agregar formato condicional a una tabla dinámica en Aspose.Cells for Python via .NET - anclar una regla a la región de datos con apply_to y un ámbito PivotConditionFormatScopeType, o definir el objetivo con add_cell_area y pivot_areas, luego adjuntar reglas y estilos mediante format_conditions.add_condition.
keywords: Aspose.Cells, Aspose.Cells for Python via .NET, tabla dinámica, formato condicional, PivotConditionalFormat, conditional_formats, apply_to, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, add_cell_area, pivot_areas, add_pivot_area, format_conditions, add_condition, FormatConditionType, Python
type: docs
weight: 30
url: /es/python-net/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
Los estilos descritos en la página principal y en la página hermana son estáticos: una región `PivotArea` o `CellArea` se pinta una sola vez y conserva su estilo sin importar los valores. El formato condicional es la contraparte basado en reglas: resaltar cada cantidad superior a 200, sombrear el cincuenta por ciento central o marcar los elementos con menor rango; y el resaltado sigue a los valores cada vez que la tabla dinámica se recalcula o actualiza.  
En Aspose.Cells, el formato condicional de tablas dinámicas se encuentra en la colección `pivot_table.conditional_formats`. Cada entrada es un `PivotConditionalFormat` que responde de forma independiente a dos preguntas:
- **¿Dónde se aplica la regla?** La región objetivo se define ya sea mediante `apply_to(row: int, column: int, scope: PivotConditionFormatScopeType)`, que replica el selector de ámbito de la interfaz de usuario de Excel, o mediante `add_cell_area(cell_area: CellArea)` y la colección `pivot_areas`, que nombran la región explícitamente.
- **¿Qué evalúa la regla?** Una o más condiciones se añaden a `format_conditions` con `format_conditions.add_condition(type: FormatConditionType, operator_type: OperatorType, formula1: str, formula2: str)`, y cada condición lleva su propio `style`.

{{% alert color="primary" %}}
No llame a `format_conditions.add(cell_area: CellArea, type: FormatConditionType, operator_type: OperatorType, formula1: str, formula2: str)` ni a `format_conditions.add_area(cell_area: CellArea)` sobre el objeto `format_conditions` de un formato condicional de pivote. Estas dos sobrecargas provienen de la API de formato condicional de hoja de cálculo ordinaria y no funcionan para tablas dinámicas: el área de celdas nunca se convierte en un área de pivote, por lo que la solicitud se ignora silenciosamente. Siempre defina la región en el propio `pivot_conditional_format` (`apply_to`, `add_cell_area` o `pivot_areas`) y añada la regla con una de las sobrecargas `add_condition`.
{{% /alert %}}

## **Aplicar una regla con un ámbito (modo de la UI de Excel)**
La primera forma posiciona la regla tal como lo hace la interfaz de usuario de Excel. Una celda de la tabla dinámica se nombra mediante sus coordenadas de hoja de cálculo basadas en cero, y un ámbito `PivotConditionFormatScopeType` indica an Aspose.Cells hasta dónde debe extenderse la regla desde esa celda:
- `PivotConditionFormatScopeType.DATA` – todas las celdas de valor que genera la tabla dinámica, incluidos los totales generales.
- `PivotConditionFormatScopeType.FIELD` – las celdas de valor que pertenecen al campo que identifica la celda, excluyendo los totales generales. La celda debe ser una celda de campo, como una etiqueta de fila; pasar una celda de valor genera una excepción.
- `PivotConditionFormatScopeType.SELECTION` – solo las celdas de valor en la intersección que la celda selecciona, típicamente una única celda de valor.
El ejemplo a continuación crea una tabla dinámica de ventas de frutas cuya esquina superior izquierda está en E3, ancla un formato condicional en la celda F4 (fila 3, columna 5) con el ámbito `PivotConditionFormatScopeType.DATA`, y resalta cada cantidad mayor que 200 en negrita, blanco sobre rojo. Con los valores Apple 220, Banana 330, Cherry 200 y el total general 750, la regla pinta F4, F5 y F7; la región resuelta es toda la columna de datos F4:F7, y solo las celdas cuyo valor cumple la regla se iluminan.

```python
from aspose.cells.pivot import PivotFieldType, PivotConditionFormatScopeType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
# Tabla dinámica con su esquina superior izquierda en E3
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Anclar el formato condicional en F4 (fila 3, columna 5) con el alcance Data
index = pivot_table.conditional_formats.add()
format = pivot_table.conditional_formats[index]
format.apply_to(3, 5, PivotConditionFormatScopeType.DATA)
# Regla - resaltar cantidades mayores a 200
condition_index = format.format_conditions.add_condition(
    ac.FormatConditionType.CELL_VALUE,
    ac.OperatorType.GREATER_THAN,
    "200",
    None
)
style = workbook.create_style()
style.font.is_bold = True
style.font.color = Color.white
style.foreground_color = Color.red
style.pattern = ac.BackgroundType.SOLID
format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatData.xlsx")
```

Anclar la misma regla en la etiqueta de campo de fila E4 (fila 3, columna 4) con el ámbito `PivotConditionFormatScopeType.FIELD` resuelve a F4:F6 en su lugar – la misma columna de datos sin la fila de total general – porque el ámbito ahora describe el campo `Fruit` en lugar de todo el área de valores. El ámbito `PivotConditionFormatScopeType.SELECTION` anclado en F4 se resuelve únicamente a F4.

## **Definir la región manualmente**
La segunda forma omite el selector de ámbito y nombra la región explícitamente en el `PivotConditionalFormat`.

### **Un rectángulo de hoja de cálculo con add_cell_area**
`add_cell_area(cell_area: CellArea)` registra el rectángulo proporcionado como el objetivo de la regla. Las coordenadas son coordenadas de hoja de cálculo basadas en cero, y la región es exactamente el rectángulo suministrado, sin expansión a la columna de datos y sin lógica de totales generales. Úselo cuando las celdas de interés forman un rectángulo fijo conocido del diseño actual de la tabla dinámica.

```python
from aspose.cells import BackgroundType, FormatConditionType, OperatorType
from aspose.cells.pivot import PivotFieldType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Apuntar al rectángulo F4:F6 (las celdas de valor sin el total general)
index = pivot_table.conditional_formats.add()
conditional_format = pivot_table.conditional_formats[index]
area = ac.CellArea()
area.start_row = 3
area.start_column = 5
area.end_row = 5
area.end_column = 5
conditional_format.add_cell_area(area)
# Regla - cursiva en amarillo claro para montos entre 150 y 300
condition_index = conditional_format.format_conditions.add_condition(
    FormatConditionType.CELL_VALUE, OperatorType.BETWEEN, "150", "300"
)
style = workbook.create_style()
style.font.is_italic = True
style.foreground_color = Color.light_yellow
style.pattern = BackgroundType.SOLID
conditional_format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatCellArea.xlsx")
```

### **Una región pivot semántica con pivot_areas**
`pivot_areas` es el mismo modelo de región semántica que la página hermana utiliza para estilos estáticos. Construya un `PivotArea`, seleccione un campo o región con `select` o `select_field`, y añádalo con `pivot_areas.add_pivot_area(pivot_area)`. Una región semántica permanece vinculada a su campo, por lo que el formato condicional sigue al campo cuando la tabla dinámica se actualiza y el diseño cambia. La sobrecarga `pivot_areas.add(pivot_area)` sigue compilando pero está marcada como obsoleta; prefiera `add_pivot_area`.

```python
from aspose.cells.pivot import PivotFieldType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Adjuntar la regla al campo de datos Amount como una región semántica
index = pivot_table.conditional_formats.add()
format = pivot_table.conditional_formats[index]
area = ac.PivotArea(pivot_table)
area.select_field(PivotFieldType.DATA, "Amount")
format.pivot_areas.add_pivot_area(area)
# Regla - texto gris para montos por debajo de 150
condition_index = format.format_conditions.add_condition(
    ac.FormatConditionType.CELL_VALUE,
    ac.OperatorType.LESS_THAN,
    "150",
    None
)
style = workbook.create_style()
style.font.color = Color.gray
format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatPivotArea.xlsx")
```

## **Dónde se almacenan las reglas y cómo sobreviven a una recarga**
Cada llamada a `pivot_table.conditional_formats.add()` agrega un `PivotConditionalFormat` a la tabla dinámica. Las condiciones, sus fórmulas y sus estilos se guardan con el libro de trabajo; al volver a abrir el archivo en el ejemplo siguiente se muestran las dos mismas reglas con sus tipos, operadores y fórmulas intactas, y `get_cell_areas()` informa las mismas regiones. Las entradas que nunca recibieron una condición se eliminan al guardar el libro de trabajo, de la misma manera que Excel descarta un formato condicional sin regla.

```python
import aspose.cells as ac
workbook = ac.Workbook("PivotConditionalFormatData.xlsx")
pivot_table = workbook.worksheets[0].pivot_tables[0]
print("Conditional formats: " + str(pivot_table.conditional_formats.count))
for i in range(pivot_table.conditional_formats.count):
    format = pivot_table.conditional_formats[i]
    for j in range(format.format_conditions.count):
        condition = format.format_conditions[j]
        print(f"Format {i}: {condition.type} {condition.operator} formula1={condition.formula1}")
    for area in format.get_cell_areas():
        print(
            f"    rows {area.start_row + 1}-{area.end_row + 1}, "
            f"columns {area.start_column + 1}-{area.end_column + 1}"
        )
# Esto imprime:
# Formatos condicionales: 1
# Formato 0: CellValue GreaterThan formula1==200
#     filas 4-7, columnas 6-6        (F4:F7, la región de datos resuelta)
```

## **Artículos relacionados**
- [Aplicar estilo a la tabla dinámica](/cells/es/python-net/apply-style-to-pivot-table/)
- [Formato de parte de una tabla dinámica](/cells/es/python-net/format-part-of-pivot-table/)
- [Top 10 mostrar o filtrar en tabla dinámica](/cells/es/python-net/top-10-show-or-filter-in-pivot-table/)
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/python-net/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="python-net" >}}