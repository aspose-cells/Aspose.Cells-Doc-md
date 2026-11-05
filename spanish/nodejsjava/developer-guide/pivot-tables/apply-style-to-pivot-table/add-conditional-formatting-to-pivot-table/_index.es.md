---
title: Agregar formato condicional a una tabla dinámica
linktitle: Agregar formato condicional a una tabla dinámica
description: Agregar formato condicional a una tabla dinámica en Aspose.Cells for Node.js via Java, anclar una regla a la región de datos con applyTo y un ámbito PivotConditionFormatScopeType, o definir el objetivo con addCellArea y getPivotAreas, luego adjuntar reglas y estilos mediante getFormatConditions().addCondition.
keywords: Aspose.Cells, tabla dinámica, formato condicional, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Node.js via Java
type: docs
weight: 30
url: /es/nodejs-java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de uso posibles**
Los estilos descritos en la página principal y en la página hermana son estáticos: una región `PivotArea` o `CellArea` se pinta una sola vez y conserva su estilo sin importar los valores. El formato condicional es la contraparte basada en reglas: resaltar cada cantidad superior a 200, sombrear el 50 % central o marcar los elementos con menor clasificación; y el resaltado se actualiza según los valores siempre que la tabla dinámica se recalcula o actualiza.  
En Aspose.Cells for Node.js via Java, el formato condicional de tablas dinámicas vive en la colección `pivotTable.getConditionalFormats()`. Cada entrada es un `PivotConditionalFormat` que responde a dos preguntas de forma independiente:
- **¿Dónde se aplica la regla?** La región objetivo se define mediante `applyTo(int row, int column, PivotConditionFormatScopeType scope)`, que refleja el selector de ámbito de la interfaz de usuario de Excel, o mediante `addCellArea(CellArea)` y la colección `getPivotAreas()`, que nombran la región explícitamente.
- **¿Qué evalúa la regla?** Se añaden una o más condiciones a `getFormatConditions()` con `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`, y cada condición lleva su propio `getStyle()`.

{{% alert color="primary" %}}
No llame a `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` ni a `FormatConditionCollection.addArea(CellArea)` sobre el objeto `getFormatConditions()` de un formato condicional de pivote. Estas dos sobrecargas provienen de la API de formato condicional de hoja de cálculo ordinaria y no funcionan para tablas dinámicas: el área de celda nunca se convierte en un área de pivote, por lo que la solicitud se ignora silenciosamente. Defina siempre la región en el propio `PivotConditionalFormat` (`applyTo`, `addCellArea` o `getPivotAreas()`) y añada la regla con una de las sobrecargas `addCondition`.
{{% /alert %}}

## **Aplicar una regla con un ámbito (modo UI de Excel)**
La primera forma posiciona la regla como lo hace la interfaz de usuario de Excel. Una celda de la tabla dinámica se nombra por sus coordenadas de hoja de cálculo basadas en cero, y un ámbito `PivotConditionFormatScopeType` indica an Aspose.Cells hasta dónde debe llegar la regla desde esa celda:
- `PivotConditionFormatScopeType.DATA` – todas las celdas de valor que produce la tabla dinámica, incluidos los totales generales.
- `PivotConditionFormatScopeType.FIELD` – las celdas de valor que pertenecen al campo que identifica la celda, excluyendo los totales generales. La celda debe ser una celda de campo, como una etiqueta de fila; pasar una celda de valor genera una excepción.
- `PivotConditionFormatScopeType.SELECTION` – solo las celdas de valor en la intersección que la celda selecciona, normalmente una sola celda de valor.
El ejemplo a continuación crea una tabla dinámica de ventas de frutas cuya esquina superior izquierda está en E3, ancla un formato condicional en la celda F4 (fila 3, columna 5) con el ámbito `DATA`, y resalta cada cantidad mayor a 200 en negrita blanca sobre rojo. Con los valores Manzana 220, Plátano 330, Cereza 200 y el total general 750, la regla pinta F4, F5 y F7; la región resuelta es toda la columna de datos F4:F7, y solo las celdas cuyo valor cumple la regla se iluminan.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
// Tabla dinámica con su esquina superior izquierda en E3
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Anclar el formato condicional en F4 (fila 3, columna 5) con el alcance de Datos
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, AsposeCells.PivotConditionFormatScopeType.DATA);
// Regla - resaltar montos mayores a 200
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.GREATER_THAN,
    "200",
    null
);
const style = workbook.createStyle();
style.getFont().setBold(true);
style.getFont().setColor(AsposeCells.Color.getWhite());
style.setForegroundColor(AsposeCells.Color.getRed());
style.setPattern(AsposeCells.BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

Anclar la misma regla en la etiqueta de campo de fila E4 (fila 3, columna 4) con el ámbito `FIELD` se resuelve en F4:F6 — la misma columna de datos sin la fila de total general — porque el ámbito ahora describe el campo **Fruit** en lugar de todo el área de valores. El ámbito `SELECTION` anclado en F4 se resuelve únicamente en F4.

## **Definir la región manualmente**
La segunda forma omite el selector de ámbito y nombra la región explícitamente en el `PivotConditionalFormat`.

### **Un rectángulo de hoja de cálculo con addCellArea**
`addCellArea(CellArea)` registra el rectángulo proporcionado como el objetivo de la regla. Las coordenadas son coordenadas de hoja de cálculo basadas en cero, y la región es exactamente el rectángulo suministrado, sin expansión a la columna de datos y sin lógica de total general. Úselo cuando las celdas de interés forman un rectángulo fijo conocido del diseño actual de la tabla dinámica.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Objetivo del rectángulo F4:F6 (las celdas de valor sin el total general)
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const cellArea = new AsposeCells.CellArea();
cellArea.StartRow = 3;
cellArea.StartColumn = 5;
cellArea.EndRow = 5;
cellArea.EndColumn = 5;
format.addCellArea(cellArea);
// Regla - itálica en amarillo claro para montos entre 150 y 300
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.BETWEEN,
    "150",
    "300"
);
const style = workbook.createStyle();
style.getFont().setItalic(true);
style.setForegroundColor(AsposeCells.Color.fromArgb(0xFF, 255, 255, 224));
style.setPattern(AsposeCells.BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **Una región semántica de pivote con PivotAreas**
`getPivotAreas()` es el mismo modelo de región semántica que la página hermana utiliza para estilos estáticos. Construya un `PivotArea`, seleccione un campo o región con `select` o `selectField`, y añádalo con `getPivotAreas().addPivotArea(PivotArea)`. Una región semántica permanece vinculada a su campo, por lo que el formato condicional sigue al campo cuando la tabla dinámica se actualiza y el diseño cambia. La sobrecarga `getPivotAreas().add(PivotArea)` aún compila pero está marcada como obsoleta; prefiera `addPivotArea`.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Adjunte la regla al campo de datos Amount como una región semántica
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.PivotArea(pivotTable);
area.selectField(AsposeCells.PivotFieldType.DATA, "Amount");
format.getPivotAreas().addPivotArea(area);
// Regla - texto gris para montos por debajo de 150
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.LESS_THAN,
    "150",
    null
);
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.getGray());
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **Dónde se almacenan las reglas y cómo sobreviven a una recarga**
Cada llamada `add()` en `getConditionalFormats()` agrega un `PivotConditionalFormat` a la tabla dinámica. Las condiciones, sus fórmulas y sus estilos se guardan con el libro de trabajo; al volver a abrir el archivo en el ejemplo a continuación se muestran la misma regla con su tipo, operador y fórmula intactos, y `getCellAreas()` informa las mismas regiones. Las entradas que nunca recibieron una condición se descartan al guardar el libro, de la misma forma que Excel elimina un formato condicional sin regla.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("PivotConditionalFormatData.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const conditionalFormats = pivotTable.getConditionalFormats();
console.log("Conditional formats: " + conditionalFormats.getCount());
for (let i = 0; i < conditionalFormats.getCount(); i++) {
    const format = conditionalFormats.get(i);
    const formatConditions = format.getFormatConditions();
    for (let j = 0; j < formatConditions.getCount(); j++) {
        const condition = formatConditions.get(j);
        console.log(`Format ${i}: ${condition.getType()} ${condition.getOperator()} formula1=${condition.getFormula1()}`);
    }
    const cellAreas = format.getCellAreas();
    for (let k = 0; k < cellAreas.length; k++) {
        const area = cellAreas[k];
        console.log(`    rows ${area.StartRow + 1}-${area.EndRow + 1}, columns ${area.StartColumn + 1}-${area.EndColumn + 1}`);
    }
}
// Esto imprime:
// Formatos condicionales: 1
// Formato 0: CellValue GreaterThan formula1==200
//     filas 4-7, columnas 6-6        (F4:F7, la región de datos resuelta)
```

## **Artículos relacionados**
- [Aplicar estilo a una tabla dinámica](/cells/es/nodejs-java/apply-style-to-pivot-table/)
- [Formatear parte de una tabla dinámica](/cells/es/nodejs-java/format-part-of-pivot-table/)
- [Top 10 Mostrar o filtrar en tabla dinámica](/cells/es/nodejs-java/top-10-show-or-filter-in-pivot-table/)
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/nodejs-java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}