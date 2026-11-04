---
title: Formatear parte de una tabla dinámica
description: Formatear parte de una tabla dinámica en Aspose.Cells for Python via .NET, aplicando estilos a regiones semánticas PivotArea o rectángulos CellArea mediante PivotTable.format, con los formatos almacenados en PivotTable.pivot_formats y preservados al actualizar la tabla dinámica.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells for Python via .NET, tabla dinámica, formato, PivotArea, CellArea, PivotTable.format, pivot_formats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, select_field, format_all, Python via .NET
type: docs
weight: 20
url: /es/python-net/format-part-of-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de Uso Posibles**
`PivotTable.format_all` aplica un único estilo a toda la tabla dinámica y se describe en la página principal. No distingue entre etiquetas, valores, totales o regiones específicas del informe.  
En la práctica, solo una parte de la tabla dinámica suele necesitar resaltarse. Los objetivos habituales incluyen las etiquetas que pertenecen a un campo de fila, las celdas de valor generadas por un campo, la fila de total general o un rectángulo arbitrario como las dos primeras filas de ítems.  
Aplicar un estilo directamente a las celdas de la hoja de cálculo que contiene la tabla dinámica no es equivalente. Excel almacena el formato de la tabla dinámica como regiones semánticas `PivotArea` en lugar de registros ordinarios de estilo de celda. Un formato de área de pivot permanece asociado a una región como las etiquetas de un campo o los valores de datos, y se vuelve a resolver cuando la tabla dinámica se recalcula, actualiza o expande. Un estilo escrito directamente en una celda pertenece a esa posición y no es rastreado por el modelo de pivot.  
Aspose.Cells expone la familia completa de sobrecargas `PivotTable.format` para que ambos tipos de formato estén disponibles:
- `format(PivotArea, Style)` ancla un estilo a una región semántica construida con `PivotArea.select` o `PivotArea.select_field`.
- `format(CellArea, Style)` ancla un estilo a un rectángulo de hoja dentro de la tabla dinámica.
- `format(int row, int column, Style)` apunta a una sola celda.
- `format_all(Style)` formatea toda la tabla dinámica.

## **Formatear un Área de Pivot**
El flujo de trabajo basado en áreas semánticas es el enfoque recomendado cuando un resaltado debe seguir a un campo o una región del informe.
1. Crear un `PivotArea` con `PivotArea(pivot_table)`. El objeto describe una región semántica que pertenece a esa tabla dinámica específica.
2. Seleccionar un campo por su posición basada en cero en un eje determinado con `PivotArea.select(PivotFieldType axis_type, int field_position, PivotTableSelectionType selection_type)`.
   - `PivotTableSelectionType.DATA_AND_LABEL` selecciona tanto las etiquetas como los datos del campo.
   - `PivotTableSelectionType.LABEL_ONLY` selecciona solo las etiquetas del campo.
   - `PivotTableSelectionType.DATA_ONLY` selecciona solo las celdas de datos del campo.
3. Seleccionar un campo por nombre con `PivotArea.select_field(PivotFieldType axis_type, string field_name)`. Cuando se selecciona un campo de fila por nombre, la región se resuelve a las celdas de valor producidas por los ítems de ese campo.
4. Crear un `Style` con `Workbook.create_style()`, configurar su fuente, color de primer plano y patrón de fondo sólido, y pasar el estilo a `PivotTable.format(area, style)`.
5. Cada llamada a la sobrecarga `PivotArea` agrega una entrada `PivotTableFormat` a `PivotTable.pivot_formats`.
6. Los formatos anclados a campos se pintan cuando se calculan los datos del pivot. Por lo tanto, invoque `PivotTable.calculate_data()` después de aplicar los formatos para que los estilos sean visibles.  
El siguiente ejemplo crea una pequeña tabla dinámica de ventas de frutas, aplica estilo a las etiquetas de fila `Fruit` con `PivotArea.select` y `PivotTableSelectionType.LABEL_ONLY`, aplica estilo a las celdas de valor generadas por el mismo campo de fila con `PivotArea.select_field`, y luego recalcula la tabla dinámica para que ambos estilos se pinten.

```python
from aspose.cells.pivot import PivotArea, PivotFieldType, PivotTableSelectionType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
# Fruit sales data
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
# Pivot table with its top-left corner at E3
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Bold yellow fill on the row field's label cells
label_style = workbook.create_style()
label_style.font.is_bold = True
label_style.foreground_color = Color.yellow
label_style.pattern = ac.BackgroundType.SOLID
label_area = PivotArea(pivot_table)
label_area.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY)
pivot_table.format(label_area, label_style)
# Light green fill on the value cells the row field produces
value_style = workbook.create_style()
value_style.foreground_color = Color.light_green
value_style.pattern = ac.BackgroundType.SOLID
value_area = PivotArea(pivot_table)
value_area.select_field(PivotFieldType.ROW, "Fruit")
pivot_table.format(value_area, value_style)
# Field-anchored formats are painted when the data is calculated
pivot_table.calculate_data()
# Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx")
```

## **Formatear un Área de Celdas de la Tabla Dinámica**
Utilice `PivotTable.format(CellArea, Style)` cuando la región de interés sea un simple rectángulo de hoja en lugar de una región semántica de pivot.  
Un `CellArea` se describe mediante las propiedades `start_row`, `start_column`, `end_row` y `end_column`. Los valores son coordenadas de hoja basadas en cero, y las coordenadas finales identifican la última fila y columna incluidas en el rectángulo, de modo que el área cubre las celdas desde la posición inicial hasta la final inclusive.  
A diferencia de un formato anclado a un campo, un formato `CellArea` se aplica a las celdas de inmediato. No se necesita otra llamada a `calculate_data()` para que el estilo aparezca.  
Un rectángulo `CellArea` puede contener celdas de etiqueta y de valor simultáneamente. La siguiente sección describe cómo Aspose.Cells y Excel representan internamente ese rectángulo.  
El siguiente ejemplo formatea el rectángulo `E4:F5` de la tabla dinámica con un estilo cursiva y azul claro y guarda el libro sin necesidad de recalcular nuevamente.

```python
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
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Highlight the first two fruit rows (the rectangle E4:F5)
highlight_style = workbook.create_style()
highlight_style.font.is_italic = True
highlight_style.foreground_color = Color.from_argb(0xFF, 0x99, 0xCC, 0xFF)
highlight_style.pattern = ac.BackgroundType.SOLID
rectangle = ac.CellArea()
rectangle.start_row = 3
rectangle.start_column = 4
rectangle.end_row = 4
rectangle.end_column = 5
pivot_table.format(rectangle, highlight_style)
# E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx")
```

## **Cómo se Mapean las Áreas de Pivot y las Áreas de Celdas**
Excel almacena el formato de la tabla dinámica como registros `pivotArea` en lugar de registros ordinarios de estilo de celda. El mismo modelo lo utiliza Aspose.Cells, por lo que una solicitud de formato se traduce en áreas de pivot al registrarse.  
La relación entre el `CellArea` proporcionado por el usuario y las áreas de pivot almacenadas internamente es de muchos a muchos en ambas direcciones.
- Un `CellArea` puede generar varias áreas de pivot. Si el rectángulo abarca tanto celdas de etiqueta como de valor, se descompone en reglas separadas de etiqueta y datos, porque el modelo de pivot trata el formato de etiquetas y el de datos de manera independiente.
- Una área de pivot puede resolverse en varias instancias disjuntas de `CellArea`. Una región semántica como una fila de total general, o un campo cuyos ítems no son contiguos, puede cubrir múltiples rectángulos. Por eso `PivotArea.get_cell_areas()` devuelve una colección en lugar de un único rectángulo.  
Cada operación de formato realizada a través de `PivotTable.format` se registra en `PivotTable.pivot_formats`. Cada entrada `PivotTableFormat` expone el `PivotArea` asociado y el `Style` que se le aplica. La sobrecarga de `PivotArea` añade exactamente una entrada por llamada, mientras que un `CellArea` que contiene distintas regiones semánticas puede añadir varias entradas.  
Para distinguir las regiones almacenadas, cada `PivotArea` expone los indicadores `only_label` y `only_data`. El ejemplo a continuación formatea un único rectángulo que cubre tanto etiquetas como valores, inspecciona `PivotTable.pivot_formats` y muestra las coordenadas `CellArea` a las que cada área de pivot almacenada se resuelve.

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
highlight_style = workbook.create_style()
highlight_style.font.is_italic = True
highlight_style.foreground_color = Color.from_argb(0xFF, 0x99, 0xCC, 0xFF)
highlight_style.pattern = ac.BackgroundType.SOLID
# ONE rectangle in...
rectangle = ac.CellArea()
rectangle.start_row = 3
rectangle.start_column = 4
rectangle.end_row = 4
rectangle.end_column = 5
pivot_table.format(rectangle, highlight_style)
# ...TWO semantic pivot areas out: the label part and the data part are stored separately
print(f"Stored formats: {len(pivot_table.pivot_formats)}")
for i in range(len(pivot_table.pivot_formats)):
    stored_area = pivot_table.pivot_formats[i].pivot_area
    print(f"Format {i}: OnlyLabel={stored_area.only_label}, OnlyData={stored_area.only_data}")
    for resolved in stored_area.get_cell_areas():
        print(
            f"    rows {resolved.start_row + 1}-{resolved.end_row + 1}, "
            f"columns {resolved.start_column + 1}-{resolved.end_column + 1}"
        )
workbook.save("FormatPivotAreasMap.xlsx")
```

{{% alert color="primary" %}}
Porque los formatos se almacenan como áreas de pivot en lugar de estilos de celda ordinarios, sobreviven a la recalculación y actualización. Cuando la tabla dinámica se actualiza con `PivotTable.refresh_data`, se recalcula con `calculate_data`, o se guarda y vuelve a cargar, cada área de pivot almacenada se vuelve a resolver a la posición actual de su región y su estilo se vuelve a aplicar.
{{% /alert %}}

Utilice un `PivotArea` construido con `select` o `select_field` cuando un resaltado deba permanecer vinculado a un campo o a una región semántica a través de actualizaciones, y use un `CellArea` cuando sea suficiente formatear un rectángulo fijo en el diseño actual de la tabla dinámica. La sobrecarga `format(int row, int column, Style)` de una sola celda apunta a una celda individual. Use `format_all`, descrito en la página principal, cuando toda la tabla dinámica deba restilizarse de una vez.

## **Artículos Relacionados**
- [Aplicar estilo a la tabla dinámica](/cells/es/python-net/apply-style-to-pivot-table/)
- [Agregar campos de fila y columna a la tabla dinámica](/cells/es/python-net/pivot-table-add-row-and-column-fields/)
- [Administrar campos de valores en la tabla dinámica](/cells/es/python-net/manage-value-fields/)
- [Actualizar la tabla dinámica](/cells/es/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}