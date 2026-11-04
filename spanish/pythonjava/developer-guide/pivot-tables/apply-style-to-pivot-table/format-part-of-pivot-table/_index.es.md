---
title: Formato de una parte de una Tabla Dinámica
linktitle: Formato de una parte de una Tabla Dinámica
description: Formatear parte de una tabla dinámica en Aspose.Cells for Python via Java aplicando estilos a regiones semánticas PivotArea o rectángulos CellArea mediante PivotTable.format, con los formatos almacenados en PivotTable.getPivotFormats() y preservados cuando la tabla dinámica se actualiza.
keywords: Aspose.Cells, Aspose.Cells for Python via Java, tabla dinámica, formato, PivotArea, CellArea, PivotTable.format, getPivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Python
type: docs
weight: 20
url: /es/python-java/format-part-of-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de Uso Posibles**
`PivotTable.formatAll` aplica un único estilo a toda la tabla dinámica y se trata en la página principal. No distingue entre etiquetas, valores, totales o regiones específicas del informe.
En la práctica, sólo una parte de una tabla dinámica suele necesitar resaltarse. Los objetivos comunes incluyen las etiquetas pertenecientes a un campo de fila, las celdas de valor producidas por un campo, la fila de total general, o un rectángulo arbitrario como las dos primeras filas de elementos.
Aplicar un estilo directamente a las celdas de la hoja de cálculo de una tabla dinámica no es equivalente. Excel almacena el formato de tabla dinámica como regiones semánticas `PivotArea` en lugar de registros ordinarios de estilo de celda. Un formato de área pivot permanece asociado a una región, como las etiquetas o valores de datos de un campo, y se vuelve a resolver cuando la tabla dinámica se recalcula, actualiza o expande. Por otro lado, un estilo escrito directamente en una celda pertenece a esa posición de celda y no es rastreado por el modelo de tabla dinámica.
Aspose.Cells expone la familia completa de sobrecargas `PivotTable.format` para que ambos tipos de formato estén disponibles:
- `format(PivotArea, Style)` ancla un estilo a una región semántica construida con `PivotArea.select` o `PivotArea.selectField`.
- `format(CellArea, Style)` ancla un estilo a un rectángulo de la hoja de cálculo dentro de la tabla dinámica.
- `format(int row, int column, Style)` apunta a una sola celda.
- `formatAll(Style)` da formato a toda la tabla dinámica.

## **Formato de un Área Pivot**
El flujo de trabajo basado en áreas semánticas es el enfoque recomendado cuando un resaltado debe seguir a un campo o a una región del informe.
1. Crear un `PivotArea` con `PivotArea(pivot_table)`. El objeto describe una región semántica que pertenece a esa tabla dinámica específica.
2. Seleccionar un campo por su posición basada en cero en un eje determinado con `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DATA_AND_LABEL` selecciona tanto las etiquetas como los datos del campo.
   - `PivotTableSelectionType.LABEL_ONLY` selecciona sólo las etiquetas del campo.
   - `PivotTableSelectionType.DATA_ONLY` selecciona sólo las celdas de datos del campo.
3. Seleccionar un campo por nombre con `PivotArea.selectField(PivotFieldType axisType, String fieldName)`. Cuando se selecciona un campo de fila por nombre, la región se resuelve a las celdas de valor producidas por los elementos de ese campo.
4. Crear un `Style` con `workbook.createStyle()`, configurar su fuente, color de primer plano y patrón de fondo sólido, y pasar el estilo a `PivotTable.format(area, style)`.
5. Cada llamada a la sobrecarga `PivotArea` agrega una entrada `PivotTableFormat` a `PivotTable.getPivotFormats()`.
6. Los formatos anclados a campos se aplican cuando se calculan los datos de la tabla dinámica. Por lo tanto, llame a `PivotTable.calculateData()` después de aplicar los formatos para que los estilos sean visibles.
El siguiente ejemplo crea una pequeña tabla dinámica de ventas de frutas, aplica estilos a las etiquetas de fila `Fruit` con `PivotArea.select` y `PivotTableSelectionType.LABEL_ONLY`, aplica estilos a las celdas de valor producidas por ese mismo campo de fila con `PivotArea.selectField`, y luego recalcula la tabla dinámica para que ambos estilos se apliquen.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    Style,
    Color,
    BackgroundType,
    PivotArea,
    PivotFieldType,
    PivotTableSelectionType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
# Fruit sales data
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
# Pivot table with its top-left corner at E3
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Bold yellow fill on the row field's label cells
label_style = workbook.createStyle()
label_style.getFont().setBold(True)
label_style.setForegroundColor(Color.getYellow())
label_style.setPattern(BackgroundType.SOLID)
label_area = PivotArea(pivot_table)
label_area.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY)
pivot_table.format(label_area, label_style)
# Light green fill on the value cells the row field produces
value_style = workbook.createStyle()
value_style.setForegroundColor(Color.getLightGreen())
value_style.setPattern(BackgroundType.SOLID)
value_area = PivotArea(pivot_table)
value_area.selectField(PivotFieldType.ROW, "Fruit")
pivot_table.format(value_area, value_style)
# Field-anchored formats are painted when the data is calculated
pivot_table.calculateData()
# Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx")
jpype.shutdownJVM()
```

## **Formato de un Área de Celdas de la Tabla Dinámica**
Utilice `PivotTable.format(CellArea, Style)` cuando la región de interés sea un simple rectángulo de hoja de cálculo y no una región pivot semántica.
Un `CellArea` se describe mediante las propiedades `getStartRow()`, `getStartColumn()`, `getEndRow()` y `getEndColumn()`. Los valores son coordenadas de hoja de cálculo basadas en cero, y las coordenadas finales identifican la última fila y columna incluidas en el rectángulo, por lo que el área cubre las celdas desde la posición de inicio hasta la posición final inclusive.
A diferencia de un formato anclado a un campo, un formato `CellArea` se aplica a las celdas de inmediato. No se necesita otra llamada a `PivotTable.calculateData()` para que el estilo aparezca.
Un rectángulo `CellArea` puede contener celdas de etiqueta y celdas de valor juntas. La siguiente sección describe cómo Aspose.Cells y Excel representan internamente ese rectángulo.
El siguiente ejemplo da formato al rectángulo `E4:F5` de la tabla dinámica con un estilo cursiva, azul claro y guarda el libro de trabajo sin necesidad de recalcular.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    Color,
    BackgroundType,
    CellArea,
    PivotFieldType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Highlight the first two fruit rows (the rectangle E4:F5)
highlight_style = workbook.createStyle()
highlight_style.getFont().setItalic(True)
highlight_style.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF))
highlight_style.setPattern(BackgroundType.SOLID)
rectangle = CellArea()
rectangle.StartRow = 3
rectangle.StartColumn = 4
rectangle.EndRow = 4
rectangle.EndColumn = 5
pivot_table.format(rectangle, highlight_style)
# E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx")
jpype.shutdownJVM()
```

## **Cómo se asignan las Áreas Pivot y Áreas de Celdas**
Excel almacena el formato de tabla dinámica como registros `pivotArea` en lugar de registros ordinarios de estilo de celda de hoja de cálculo. El mismo modelo lo utiliza Aspose.Cells, por lo que una solicitud de formato se traduce en áreas pivot cuando se registra.
La relación entre el `CellArea` proporcionado por el usuario y las áreas pivot almacenadas internamente es de muchos a muchos en ambas direcciones.
- Un `CellArea` puede producir varias áreas pivot. Si el rectángulo abarca tanto celdas de etiqueta como celdas de valor, se descompone en reglas separadas de etiqueta y datos, porque el modelo pivot trata el formato de etiquetas y el de datos de forma independiente.
- Una área pivot puede resolver en varias instancias `CellArea` disjuntas. Una región semántica como una fila de total general, o un campo cuyos elementos no son contiguos, puede cubrir múltiples rectángulos. Por eso `PivotArea.getCellAreas()` devuelve una colección en lugar de un solo rectángulo.
Cada operación de formato realizada mediante `PivotTable.format` se registra en `PivotTable.getPivotFormats()`. Cada entrada `PivotTableFormat` expone el `PivotArea` asociado y el `Style` que se le aplica. La sobrecarga `PivotArea` agrega exactamente una entrada por llamada, mientras que un `CellArea` que contiene diferentes regiones semánticas puede agregar múltiples entradas.
Para distinguir las regiones almacenadas, cada `PivotArea` expone los indicadores `getOnlyLabel()` y `getOnlyData()`. El ejemplo a continuación da formato a un solo rectángulo que cubre tanto etiquetas como valores, inspecciona `PivotTable.getPivotFormats()` y muestra las coordenadas `CellArea` a las que cada área pivot almacenada se resuelve.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import Color, CellArea, Style, BackgroundType
from asposecells.api import PivotTable, PivotArea, PivotFieldType
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
highlight_style = workbook.createStyle()
highlight_style.getFont().setItalic(True)
highlight_style.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF))
highlight_style.setPattern(BackgroundType.SOLID)
# ONE rectangle in...
rectangle = CellArea()
rectangle.StartRow = 3
rectangle.StartColumn = 4
rectangle.EndRow = 4
rectangle.EndColumn = 5
pivot_table.format(rectangle, highlight_style)
# ...TWO semantic pivot areas out: the label part and the data part are stored separately
print("Stored formats: " + str(pivot_table.getPivotFormats().getCount()))
for i in range(pivot_table.getPivotFormats().getCount()):
    stored_area = pivot_table.getPivotFormats().get(i).getPivotArea()
    print(
        f"Format {i}: OnlyLabel={stored_area.getOnlyLabel()}, "
        f"OnlyData={stored_area.getOnlyData()}"
    )
    for resolved in stored_area.getCellAreas():
        print(
            f"    rows {resolved.StartRow + 1}-{resolved.EndRow + 1}, "
            f"columns {resolved.StartColumn + 1}-{resolved.EndColumn + 1}"
        )
# This prints:
# Stored formats: 2
# Format 0: OnlyLabel=True, OnlyData=False
#     rows 4-5, columns 5-5        (E4:E5, the label part)
# Format 1: OnlyLabel=False, OnlyData=True
#     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.save("FormatPivotAreasMap.xlsx")
jpype.shutdownJVM()
```

{{% alert color="primary" %}}
Porque los formatos se almacenan como áreas pivot en lugar de estilos de celda ordinarios, sobreviven a la recalculación y actualización. Cuando la tabla dinámica se actualiza con `PivotTable.refreshData()`, se recalcula con `PivotTable.calculateData()`, o se guarda y vuelve a cargar, cada área pivot almacenada se vuelve a resolver a la posición actual de su región y su estilo se vuelve a aplicar.
{{% /alert %}}

Utilice un `PivotArea` construido con `select` o `selectField` cuando un resaltado deba permanecer unido a un campo o a una región semántica a través de actualizaciones, y use un `CellArea` cuando sea suficiente formatear un rectángulo fijo en el diseño actual de la tabla dinámica. La sobrecarga de una sola celda `format(int row, int column, Style)` apunta a una celda individual. Use `formatAll`, cubierto en la página principal, cuando toda la tabla dinámica deba volver a formatearse de una vez.

## **Artículos Relacionados**
- [Aplicar estilo a la tabla dinámica](/cells/es/python-java/apply-style-to-pivot-table/)
- [Agregar campos de fila y columna a la tabla dinámica](/cells/es/python-java/pivot-table-add-row-and-column-fields/)
- [Administrar campos de valor en la tabla dinámica](/cells/es/python-java/manage-value-fields/)
- [Actualizar tabla dinámica](/cells/es/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}