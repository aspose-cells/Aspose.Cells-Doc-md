---
title: Agregar formato condicional a una tabla dinámica
linktitle: Agregar formato condicional a una tabla dinámica
description: Agregar formato condicional a una tabla dinámica en Aspose.Cells for Python via Java, anclar una regla a la región de datos con applyTo y un alcance PivotConditionFormatScopeType, o definir el objetivo con addCellArea y getPivotAreas, luego adjuntar reglas y estilos mediante getFormatConditions().addCondition.
keywords: Aspose.Cells for Python via Java, tabla dinámica, formato condicional, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Python via Java
type: docs
weight: 30
url: /es/python-java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de uso posibles**
Los estilos descritos en la página principal y en la página hermana son estáticos: una región `PivotArea` o `CellArea` se pinta una vez y conserva su estilo sin importar los valores. El formato condicional es la contrapartida basada en reglas: resaltar cada cantidad superior a 200, sombrear el cincuenta por ciento medio o marcar los ítems con menor rango, y el resaltado sigue a los valores siempre que la tabla dinámica se recalcula o actualiza.  
En Aspose.Cells, el formato condicional de tablas dinámicas reside en la colección `PivotTable.getConditionalFormats()`. Cada entrada es un `PivotConditionalFormat` que responde a dos preguntas de forma independiente:
- **¿Dónde se aplica la regla?** La región de destino se define ya sea mediante `PivotConditionalFormat.applyTo(int row, int column, PivotConditionFormatScopeType scope)`, que reproduce el selector de alcance de la interfaz de usuario de Excel, o mediante `PivotConditionalFormat.addCellArea(CellArea)` y la colección `PivotConditionalFormat.getPivotAreas()`, que nombran la región explícitamente.
- **¿Qué evalúa la regla?** Una o más condiciones se añaden a `PivotConditionalFormat.getFormatConditions()` con `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`, y cada condición lleva su propio `Style`.

{{% alert color="primary" %}}
No llame a `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` ni a `FormatConditionCollection.addArea(CellArea)` sobre el objeto `PivotConditionalFormat.getFormatConditions()` de un formato condicional de tabla dinámica. Estas dos sobrecargas provienen de la API de formato condicional de hoja de cálculo convencional y no funcionan para tablas dinámicas: el área de celda nunca se convierte en un área de pivote, por lo que la solicitud se ignora silenciosamente. Siempre defina la región en el propio `PivotConditionalFormat` (`applyTo`, `addCellArea` o `getPivotAreas()`) y añada la regla con una de las sobrecargas `addCondition`.
{{% /alert %}}

## **Aplicar una regla con un alcance (el modo de la interfaz de Excel)**
La primera forma posiciona la regla tal como lo hace la interfaz de usuario de Excel. Una celda de la tabla dinámica se nombra mediante sus coordenadas de hoja de cálculo basadas en cero, y un alcance `PivotConditionFormatScopeType` indica an Aspose.Cells hasta dónde debe llegar la regla desde esa celda:
- `PivotConditionFormatScopeType.DATA` – todas las celdas de valor que produce la tabla dinámica, incluidos los totales generales.
- `PivotConditionFormatScopeType.FIELD` – las celdas de valor que pertenecen al campo que identifica la celda, excluyendo los totales generales. La celda debe ser una celda de campo, como la etiqueta de un campo de fila; pasar una celda de valor genera una excepción.
- `PivotConditionFormatScopeType.SELECTION` – solo las celdas de valor en la intersección que la celda selecciona, típicamente una única celda de valor.
El ejemplo a continuación crea una tabla dinámica de ventas de frutas cuyo extremo superior‑izquierdo está en E3, ancla un formato condicional en la celda F4 (fila 3, columna 5) con el alcance `DATA`, y resalta cada cantidad mayor que 200 en negrita, blanco sobre rojo. Con los valores Manzana 220, Banana 330, Cereza 200 y el total general 750, la regla colorea F4, F5 y F7 – la región resultante es toda la columna de datos F4:F7, y solo las celdas cuyo valor cumple la regla se iluminan.

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
    PivotFieldType,
    PivotConditionFormatScopeType,
    FormatConditionType,
    OperatorType,
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
# Tabla dinámica con su esquina superior izquierda en E3
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Anclar el formato condicional en F4 (fila 3, columna 5) con el alcance de Datos
index = pivot_table.getConditionalFormats().add()
format = pivot_table.getConditionalFormats().get(index)
format.applyTo(3, 5, PivotConditionFormatScopeType.DATA)
# Regla - resaltar montos mayores a 200
condition_index = format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.GREATER_THAN,
    "200",
    None,
)
style = workbook.createStyle()
style.getFont().setBold(True)
style.getFont().setColor(Color.getWhite())
style.setForegroundColor(Color.getRed())
style.setPattern(BackgroundType.SOLID)
format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatData.xlsx")
jpype.shutdownJVM()
```

Anclar la misma regla en la etiqueta del campo de fila E4 (fila 3, columna 4) con el alcance `FIELD` se resuelve en F4:F6 – la misma columna de datos sin la fila de total general – porque el alcance ahora describe el campo `Fruit` en lugar de todo el área de valores. El alcance `SELECTION` anclado en F4 se resuelve únicamente en F4.

## **Definir la región manualmente**

### **Un rectángulo de hoja de cálculo con addCellArea()**
`addCellArea(CellArea)` registra el rectángulo proporcionado como objetivo de la regla. Las coordenadas son coordenadas de hoja de cálculo basadas en cero, y la región es exactamente el rectángulo suministrado – sin expansión a la columna de datos y sin lógica de totales generales. Úselo cuando las celdas de interés forman un rectángulo fijo conocido del diseño actual de la tabla dinámica.

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
    CellArea,
    Color,
    BackgroundType,
    PivotFieldType,
    FormatConditionType,
    OperatorType,
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
# Apunta al rectángulo F4:F6 (las celdas de valores sin el total general)
index = pivot_table.getConditionalFormats().add()
conditional_format = pivot_table.getConditionalFormats().get(index)
area = CellArea()
area.StartRow = 3
area.StartColumn = 5
area.EndRow = 5
area.EndColumn = 5
conditional_format.addCellArea(area)
# Regla - cursiva en amarillo claro para cantidades entre 150 y 300
condition_index = conditional_format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.BETWEEN,
    "150",
    "300",
)
style = workbook.createStyle()
style.getFont().setItalic(True)
style.setForegroundColor(Color.getLightYellow())
style.setPattern(BackgroundType.SOLID)
conditional_format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatCellArea.xlsx")
jpype.shutdownJVM()
```

### **Una región semántica de pivote con getPivotAreas()**
La colección `getPivotAreas()` es el mismo modelo de región semántica que la página hermana emplea para estilos estáticos. Construya un `PivotArea`, seleccione un campo o región con `PivotArea.select(...)` o `PivotArea.selectField(...)`, y agréguelo mediante `getPivotAreas().addPivotArea(PivotArea)`. Una región semántica permanece vinculada a su campo, por lo que el formato condicional sigue al campo cuando la tabla dinámica se actualiza y el diseño cambia. La sobrecarga `getPivotAreas().add(PivotArea)` sigue compilando pero está marcada como obsoleta – prefiera `addPivotArea`.

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
    PivotArea,
    PivotFieldType,
    FormatConditionType,
    OperatorType,
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
# Adjunte la regla al campo de datos Amount como una región semántica
index = pivot_table.getConditionalFormats().add()
conditional_format = pivot_table.getConditionalFormats().get(index)
area = PivotArea(pivot_table)
area.selectField(PivotFieldType.DATA, "Amount")
conditional_format.getPivotAreas().addPivotArea(area)
# Regla - texto gris para cantidades inferiores a 150
condition_index = conditional_format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.LESS_THAN,
    "150",
    None,
)
style = workbook.createStyle()
style.getFont().setColor(Color.getGray())
conditional_format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatPivotArea.xlsx")
jpype.shutdownJVM()
```

## **Dónde se almacenan las reglas y cómo sobreviven a una recarga**
Cada llamada a `PivotTable.getConditionalFormats().add()` agrega un `PivotConditionalFormat` a la tabla dinámica. Las condiciones, sus fórmulas y sus estilos se guardan con el libro de trabajo – al volver a abrir el archivo en el ejemplo siguiente se muestran la misma regla con su tipo, operador y fórmula intactos, y `PivotConditionalFormat.getCellAreas()` informa de las mismas regiones. Las entradas que nunca recibieron una condición se descartan al guardar el libro de trabajo, del mismo modo que Excel elimina un formato condicional sin regla.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
workbook = Workbook("PivotConditionalFormatData.xlsx")
pivot_table = workbook.getWorksheets().get(0).getPivotTables().get(0)
print("Conditional formats: " + str(pivot_table.getConditionalFormats().getCount()))
for i in range(pivot_table.getConditionalFormats().getCount()):
    pivot_format = pivot_table.getConditionalFormats().get(i)
    format_conditions = pivot_format.getFormatConditions()
    for j in range(format_conditions.getCount()):
        condition = format_conditions.get(j)
        print(
            f"Format {i}: {condition.getType()} "
            f"{condition.getOperator()} formula1={condition.getFormula1()}"
        )
    for area in pivot_format.getCellAreas():
        print(
            f"    rows {area.StartRow + 1}-{area.EndRow + 1}, "
            f"columns {area.StartColumn + 1}-{area.EndColumn + 1}"
        )
# Esto imprime:
# Formatos condicionales: 1
# Formato 0: CellValue GreaterThan formula1==200
#     filas 4-7, columnas 6-6        (F4:F7, la región de datos resuelta)
jpype.shutdownJVM()
```

## **Artículos relacionados**
- [Aplicar estilo a tabla dinámica](/cells/es/python-java/apply-style-to-pivot-table/)
- [Formato de parte de una tabla dinámica](/cells/es/python-java/format-part-of-pivot-table/)
- [Top 10 mostrar o filtrar en tabla dinámica](/cells/es/python-java/top-10-show-or-filter-in-pivot-table/)
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/python-java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="python" >}}