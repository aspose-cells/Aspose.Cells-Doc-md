---
title: Agregar formato condicional a una tabla dinámica
linktitle: Agregar formato condicional a una tabla dinámica
description: Agregar formato condicional a una tabla dinámica en Aspose.Cells for Node.js via C++ - anclar una regla a la región de datos con applyTo y un alcance PivotConditionFormatScopeType, o definir el objetivo con addCellArea y pivotAreas, y luego adjuntar reglas y estilos mediante formatConditions.addCondition.
keywords: Aspose.Cells for Node.js via C++, tabla dinámica, formato condicional, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Node.js via C++
type: docs
weight: 30
url: /es/nodejs-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de uso posibles**
Los estilos descritos en la página principal y en la página hermana son estáticos: una región `PivotArea` o `CellArea` se pinta una vez y mantiene su estilo sin importar los valores. El formato condicional es la contraparte basada en reglas: resaltar cada cantidad superior a 200, sombrear el 50 % medio o marcar los elementos de menor posición, y el resaltado sigue a los valores cada vez que la tabla dinámica se recalcula o se actualiza.  
En Aspose.Cells, el formato condicional de una tabla dinámica se encuentra en la colección `pivotTable.getConditionalFormats()`. Cada entrada es un `PivotConditionalFormat` que responde a dos preguntas de forma independiente:
- **¿Dónde se aplica la regla?** La región objetivo se define ya sea mediante `applyTo(row, column, scope)`, que refleja el selector de alcance de la interfaz de usuario de Excel, o mediante `addCellArea(cellArea)` y la colección `pivotConditionalFormat.getPivotAreas()`, que nombran la región explícitamente.
- **¿Qué evalúa la regla?** Se añaden una o más condiciones a `formatConditions`, obtenidas mediante `pivotConditionalFormat.getFormatConditions()`, con `formatConditions.addCondition(FormatConditionType type, OperatorType operatorType, string formula1, string formula2)`, y cada condición lleva su propio estilo a través de `getStyle()`.

{{% alert color="primary" %}}
No llame a `formatConditions.add(cellArea, type, operatorType, formula1, formula2)` ni a `formatConditions.addArea(cellArea)` en el objeto `formatConditions` de un formato condicional de tabla dinámica. Estas dos sobrecargas se heredan de la API de formato condicional de hoja de cálculo ordinaria y no funcionan para tablas dinámicas: el área de celda nunca se convierte en un área de pivote, por lo que la solicitud se ignora silenciosamente. Defina siempre la región en el propio objeto `pivotConditionalFormat` (`applyTo`, `addCellArea` o `getPivotAreas()`) y añada la regla con una de las sobrecargas `addCondition`.
{{% /alert %}}

## **Aplicar una regla con un alcance (como en la UI de Excel)**
La primera forma posiciona la regla de la misma manera que lo hace la interfaz de usuario de Excel. Una celda de la tabla dinámica se nombra mediante sus coordenadas de hoja de cálculo basadas en cero, y un alcance `PivotConditionFormatScopeType` indica an Aspose.Cells qué tan lejos debe llegar la regla desde esa celda:
- `PivotConditionFormatScopeType.DATA` – todas las celdas de valores que produce la tabla dinámica, incluidos los totales generales.
- `PivotConditionFormatScopeType.FIELD` – las celdas de valores que pertenecen al campo que identifica la celda, excluyendo los totales generales. La celda debe ser una celda de campo, como una etiqueta de fila de campo; pasar una celda de valor genera una excepción.
- `PivotConditionFormatScopeType.SELECTION` – solo las celdas de valor en la intersección que la celda selecciona, típicamente una única celda de valor.
El ejemplo a continuación crea una tabla dinámica de ventas de frutas cuya esquina superior izquierda está en E3, ancla un formato condicional en la celda F4 (fila 3, columna 5) con el alcance `DATA`, y resalta cada cantidad mayor que 200 en negrita, con texto blanco sobre fondo rojo. Con los valores Manzana 220, Plátano 330, Cereza 200 y el total general 750, la regla pinta F4, F5 y F7; la región resuelta es toda la columna de datos F4:F7, y solo las celdas cuyo valor cumple la regla se iluminan.

```javascript
const AsposeCells = require("aspose.cells.node");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Anclar el formato condicional en F4 (fila 3, columna 5) con el alcance de Datos
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, AsposeCells.PivotConditionFormatScopeType.Data);
// Regla - resaltar montos mayores a 200
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.GreaterThan,
    "200",
    null
);
const style = workbook.createStyle();
style.getFont().setIsBold(true);
style.getFont().setColor(AsposeCells.Color.White);
style.setForegroundColor(AsposeCells.Color.Red);
style.setPattern(AsposeCells.BackgroundType.Solid);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

Anclar la misma regla en la etiqueta de campo de fila E4 (fila 3, columna 4) con el alcance `FIELD` se resuelve en F4:F6 en lugar de F4:F7, es decir, la misma columna de datos sin la fila del total general, porque el alcance ahora describe el campo `Fruit` en lugar de todo el área de valores. El alcance `SELECTION` anclado en F4 se resuelve únicamente en F4.

## **Definir la región manualmente**
La segunda forma omite el selector de alcance y nombra la región explícitamente en el `PivotConditionalFormat`.

### **Un rectángulo de hoja de cálculo con addCellArea**
`addCellArea(cellArea)` registra el rectángulo proporcionado como el objetivo de la regla. Las coordenadas son coordenadas de hoja de cálculo basadas en cero, y la región es exactamente el rectángulo suministrado, sin expansión a la columna de datos y sin lógica de totales generales. Úselo cuando las celdas de interés formen un rectángulo fijo conocido del diseño actual de la tabla dinámica.

```javascript
const AsposeCells = require("aspose.cells.node");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Apuntar al rectángulo F4:F6 (las celdas de valor sin el total general)
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.CellArea();
area.startRow = 3;
area.startColumn = 5;
area.endRow = 5;
area.endColumn = 5;
format.addCellArea(area);
// Regla - cursiva en amarillo claro para cantidades entre 150 y 300
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.Between,
    "150",
    "300"
);
const style = workbook.createStyle();
style.getFont().setIsItalic(true);
style.setForegroundColor(AsposeCells.Color.LightYellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **Una región semántica de pivote con getPivotAreas**
`pivotConditionalFormat.getPivotAreas()` es el mismo modelo de región semántica que la página hermana usa para estilos estáticos. Construya un `PivotArea`, seleccione un campo o región con `select` o `selectField`, y añádalo con `pivotAreas.addPivotArea(pivotArea)`. Una región semántica permanece vinculada a su campo, por lo que el formato condicional sigue al campo cuando la tabla dinámica se actualiza y el diseño cambia. La sobrecarga `pivotAreas.add(pivotArea)` todavía compila pero está marcada como obsoleta; prefiérase `addPivotArea`.

```javascript
const AsposeCells = require("aspose.cells.node");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Adjuntar la regla al campo de datos Amount como una región semántica
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.PivotArea(pivotTable);
area.selectField(AsposeCells.PivotFieldType.Data, "Amount");
format.getPivotAreas().addPivotArea(area);
// Regla - texto gris para cantidades menores a 150
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.LessThan,
    "150",
    null
);
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.Gray);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **Dónde se almacenan las reglas y cómo sobreviven a una recarga**
Cada llamada a `conditionalFormats.add()` agrega un `PivotConditionalFormat` a la tabla dinámica. Las condiciones, sus fórmulas y sus estilos se guardan con el libro de trabajo; volver a abrir el archivo en el ejemplo siguiente muestra la misma regla con su tipo, operador y fórmula intactos, y `getCellAreas()` informa las mismas regiones. Las entradas que nunca recibieron una condición se eliminan al guardar el libro de trabajo, de la misma manera que Excel descarta un formato condicional sin regla.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("PivotConditionalFormatData.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
console.log("Conditional formats: " + pivotTable.getConditionalFormats().getCount());
for (let i = 0; i < pivotTable.getConditionalFormats().getCount(); i++) {
    const format = pivotTable.getConditionalFormats().get(i);
    for (let j = 0; j < format.getFormatConditions().getCount(); j++) {
        const condition = format.getFormatConditions().get(j);
        console.log(`Format ${i}: ${condition.getType()} ${condition.getOperator()} formula1=${condition.getFormula1()}`);
    }
    for (const area of format.getCellAreas()) {
        console.log(`    rows ${area.startRow + 1}-${area.endRow + 1}, columns ${area.startColumn + 1}-${area.endColumn + 1}`);
    }
}
// Esto imprime:
// Formatos condicionales: 1
// Formato 0: ValorDeCelda MayorQue formula1==200
//     filas 4-7, columnas 6-6        (F4:F7, la región de datos resuelta)
```

## **Artículos relacionados**
- [Aplicar estilo a tabla dinámica](/cells/es/nodejs-cpp/apply-style-to-pivot-table/)
- [Formatear parte de una tabla dinámica](/cells/es/nodejs-cpp/format-part-of-pivot-table/)
- [Top 10 Mostrar u Ocultar en tabla dinámica](/cells/es/nodejs-cpp/top-10-show-or-filter-in-pivot-table/)
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}