---
title: Agregar formato condicional a una tabla dinámica
linktitle: Agregar formato condicional a una tabla dinámica
description: Agregar formato condicional a una tabla dinámica en Aspose.Cells for Java - anclar una regla a la región de datos con applyTo y un ámbito PivotConditionFormatScopeType, o definir el objetivo con addCellArea y getPivotAreas, luego adjuntar reglas y estilos mediante FormatConditions.addCondition.
keywords: Aspose.Cells for Java, tabla dinámica, formato condicional, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Java
type: docs
weight: 30
url: /es/java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de uso posibles**
Los estilos descritos en la página principal y en la página hermana son estáticos: una región `PivotArea` o `CellArea` se pinta una sola vez y conserva su estilo sin importar los valores. El formato condicional es la contraparte basada en reglas: resaltar cada cantidad superior a 200, sombrear el cincuenta por ciento intermedio o marcar los elementos con menor rango, y el resaltado sigue a los valores cada vez que la tabla dinámica se recalcula o se actualiza.  
En Aspose.Cells, el formato condicional de tablas dinámicas se encuentra en la colección `PivotTable.getConditionalFormats()`. Cada entrada es un `PivotConditionalFormat` que responde a dos preguntas independientemente:
- **¿Dónde se aplica la regla?** La región objetivo se define mediante `applyTo(int row, int column, PivotConditionFormatScopeType scope)`, que refleja el selector de ámbito de la interfaz de usuario de Excel, o mediante `addCellArea(CellArea)` y la colección `getPivotAreas()`, que nombran la región explícitamente.
- **¿Qué evalúa la regla?** Se añaden una o más condiciones a `getFormatConditions()` con `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`, y cada condición lleva su propio `Style`.

{{% alert color="primary" %}}
No llame a `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` ni a `FormatConditionCollection.addArea(CellArea)` en la colección `getFormatConditions()` de un formato condicional pivote. Estas dos sobrecargas se heredan de la API de formato condicional ordinaria de la hoja de cálculo y no funcionan para tablas dinámicas: el área de celda nunca se convierte en un área pivote, por lo que la solicitud se ignora silenciosamente. Defina siempre la región en el propio `PivotConditionalFormat` (`applyTo`, `addCellArea` o `getPivotAreas()`) y añada la regla con una de las sobrecargas `addCondition`.
{{% /alert %}}

## **Aplicar una regla con un ámbito (como en la interfaz de Excel)**
El primer método posiciona la regla de la misma forma que lo hace la interfaz de usuario de Excel. Una celda de la tabla dinámica se nombra mediante sus coordenadas de hoja de cálculo basadas en cero, y un ámbito `PivotConditionFormatScopeType` indica an Aspose.Cells hasta dónde debe llegar la regla desde esa celda:
- `PivotConditionFormatScopeType.DATA` – todas las celdas de valor que produce la tabla dinámica, incluidos los totales generales.
- `PivotConditionFormatScopeType.FIELD` – las celdas de valor que pertenecen al campo que identifica la celda, excluyendo los totales generales. La celda debe ser una celda de campo, como una etiqueta de fila; pasar una celda de valor genera una excepción.
- `PivotConditionFormatScopeType.SELECTION` – solo las celdas de valor en la intersección que la celda selecciona, típicamente una única celda de valor.
El ejemplo a continuación crea una tabla dinámica de ventas de frutas cuyo extremo superior‑izquierdo está en E3, ancla un formato condicional en la celda F4 (fila 3, columna 5) con el ámbito `DATA`, y resalta cada cantidad mayor que 200 en negrita blanca sobre rojo. Con los valores Manzana 220, Plátano 330, Cereza 200 y el total general 750, la regla pinta F4, F5 y F7 – la región resuelta es toda la columna de datos F4:F7, y solo las celdas cuyo valor cumple la regla se iluminan.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
// Tabla dinámica con su esquina superior izquierda en E3
PivotTable pivotTable = sheet.getPivotTables().add("A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Anclar el formato condicional en F4 (fila 3, columna 5) con el alcance de Datos
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, PivotConditionFormatScopeType.DATA);
// Regla - resaltar montos mayores a 200
int conditionIndex = format.getFormatConditions().addCondition(
        FormatConditionType.CELL_VALUE, OperatorType.GREATER_THAN, "200", null);
Style style = workbook.createStyle();
style.getFont().setBold(true);
style.getFont().setColor(Color.getWhite());
style.setForegroundColor(Color.getRed());
style.setPattern(BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

Anclar la misma regla en la etiqueta de campo de fila E4 (fila 3, columna 4) con el ámbito `FIELD` se resuelve en F4:F6 – la misma columna de datos sin la fila del total general – porque el ámbito ahora describe el campo `Fruit` en lugar de toda el área de valores. El ámbito `SELECTION` anclado en F4 se resuelve únicamente en F4.

## **Definir la región manualmente**
El segundo método omite el selector de ámbito y nombra la región explícitamente en el `PivotConditionalFormat`.

### **Un rectángulo de hoja de cálculo con addCellArea**
`addCellArea(CellArea)` registra el rectángulo proporcionado como el objetivo de la regla. Las coordenadas son coordenadas de hoja de cálculo basadas en cero, y la región es exactamente el rectángulo suministrado – sin expansión a la columna de datos y sin lógica de totales generales. Úselo cuando las celdas de interés forman un rectángulo fijo conocido del diseño actual de la tabla dinámica.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Target the rectangle F4:F6 (the value cells without the grand total)
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
CellArea cellArea = new CellArea();
cellArea.StartRow = 3;
cellArea.StartColumn = 5;
cellArea.EndRow = 5;
cellArea.EndColumn = 5;
format.addCellArea(cellArea);
// Rule - italic on light yellow for amounts between 150 and 300
int conditionIndex = format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE, OperatorType.BETWEEN, "150", "300");
Style style = workbook.createStyle();
style.getFont().setItalic(true);
style.setForegroundColor(Color.getLightYellow());
style.setPattern(BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **Una región pivote semántica con getPivotAreas**
`getPivotAreas()` devuelve el mismo modelo de región semántica que la página hermana usa para estilos estáticos. Construya un `PivotArea`, seleccione un campo o región con `select` o `selectField`, y añádalo con `getPivotAreas().addPivotArea(PivotArea)`. Una región semántica permanece vinculada a su campo, de modo que el formato condicional sigue al campo cuando la tabla dinámica se actualiza y el diseño cambia. La sobrecarga `getPivotAreas().add(PivotArea)` aún compila pero está marcada como obsoleta – prefiera `addPivotArea`.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Adjuntar la regla al campo de datos Amount como una región semántica
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
PivotArea area = new PivotArea(pivotTable);
area.selectField(PivotFieldType.DATA, "Amount");
format.getPivotAreas().addPivotArea(area);
// Regla - texto gris para cantidades inferiores a 150
int conditionIndex = format.getFormatConditions().addCondition(
        FormatConditionType.CELL_VALUE, OperatorType.LESS_THAN, "150", null);
Style style = workbook.createStyle();
style.getFont().setColor(Color.getGray());
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **Dónde se almacenan las reglas y cómo sobreviven a una recarga**
Cada llamada `getConditionalFormats().add()` agrega un `PivotConditionalFormat` a la tabla dinámica. Las condiciones, sus fórmulas y sus estilos se guardan con el libro de trabajo – reabrir el archivo en el ejemplo a continuación muestra la misma regla con su tipo, operador y fórmula intacta, y `getCellAreas()` informa de las mismas regiones. Las entradas que nunca recibieron una condición se descartan al guardar el libro de trabajo, de la misma forma que Excel elimina un formato condicional sin regla.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("PivotConditionalFormatData.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
System.out.println("Conditional formats: " + pivotTable.getConditionalFormats().getCount());
for (int i = 0; i < pivotTable.getConditionalFormats().getCount(); i++)
{
    PivotConditionalFormat format = pivotTable.getConditionalFormats().get(i);
    for (int j = 0; j < format.getFormatConditions().getCount(); j++)
    {
        FormatCondition condition = format.getFormatConditions().get(j);
        System.out.println("Format " + i + ": " + condition.getType() + " " + condition.getOperator() + " formula1=" + condition.getFormula1());
    }
    for (CellArea area : format.getCellAreas())
    {
        System.out.println("    rows " + (area.StartRow + 1) + "-" + (area.EndRow + 1)
                + ", columns " + (area.StartColumn + 1) + "-" + (area.EndColumn + 1));
    }
}
// Esto imprime:
// Formatos condicionales: 1
// Formato 0: CellValue GreaterThan formula1==200
//     filas 4-7, columnas 6-6        (F4:F7, la región de datos resuelta)
```

## **Artículos relacionados**
- [Aplicar estilo a una tabla dinámica](/cells/es/java/apply-style-to-pivot-table/)
- [Formatear parte de una tabla dinámica](/cells/es/java/format-part-of-pivot-table/)
- [Top 10 mostrar o filtrar en tabla dinámica](/cells/es/java/top-10-show-or-filter-in-pivot-table/)
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="java" >}}