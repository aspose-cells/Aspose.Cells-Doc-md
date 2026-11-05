---
title: Agregar formato condicional a una tabla dinámica
linktitle: Agregar formato condicional a una tabla dinámica
description: Agregar formato condicional a una tabla dinámica en Aspose.Cells for JavaScript via C++ - anclar una regla a la región de datos con applyTo y un alcance PivotConditionFormatScopeType, o definir el objetivo con addCellArea y pivotAreas, luego adjuntar reglas y estilos mediante formatConditions.addCondition.
keywords: Aspose.Cells for JavaScript via C++, tabla dinámica, formato condicional, PivotConditionalFormat, ConditionalFormats, applyTo, PivotConditionFormatScopeType, Data, Field, Selection, addCellArea, pivotAreas, addPivotArea, formatConditions, addCondition, FormatConditionType
type: docs
weight: 30
url: /es/javascript-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de uso posibles**
Los estilos descritos en la página principal y en la página hermana son estáticos: una región `PivotArea` o `CellArea` se pinta una vez y mantiene su estilo sin importar los valores. El formato condicional es la contraparte basada en reglas: resaltar cada cantidad superior a 200, sombrear el cincuenta por ciento medio o marcar los elementos con menor rango, y el resaltado sigue a los valores cada vez que la tabla dinámica se recalcula o se actualiza.  
En Aspose.Cells, el formato condicional de tabla dinámica vive en la colección `pivotTable.conditionalFormats`. Cada entrada es un `PivotConditionalFormat` que responde a dos preguntas de forma independiente:
- **¿Dónde se aplica la regla?** La región objetivo se define ya sea mediante `applyTo(row, column, scope)`, que refleja el selector de alcance de la interfaz de usuario de Excel, o mediante `addCellArea(cellArea)` y la colección `pivotAreas`, que nombran la región explícitamente.
- **¿Qué evalúa la regla?** Una o más condiciones se añaden a `formatConditions` con `addCondition(type, operatorType, formula1, formula2)`, y cada condición lleva su propio `style`.

{{% alert color="primary" %}}
No llame a `formatConditions.add(cellArea, type, operatorType, formula1, formula2)` o `formatConditions.addArea(cellArea)` en el objeto `formatConditions` de un formato condicional de pivote. Estas dos sobrecargas se heredan de la API de formato condicional ordinaria de la hoja de cálculo y no funcionan para tablas dinámicas: el área de celda nunca se convierte en un área de pivote, por lo que la solicitud se ignora silenciosamente. Siempre defina la región en el propio `PivotConditionalFormat` (`applyTo`, `addCellArea` o `pivotAreas`) y añada la regla con una de las sobrecargas de `addCondition`.
{{% /alert %}}

## **Aplicar una regla con un alcance (la forma de la UI de Excel)**
La primera manera coloca la regla como lo hace la interfaz de usuario de Excel. Una celda de la tabla dinámica se nombra por sus coordenadas de hoja de cálculo basadas en cero, y un alcance `PivotConditionFormatScopeType` indica an Aspose.Cells hasta dónde debe llegar la regla desde esa celda:
- `PivotConditionFormatScopeType.Data` - todas las celdas de valor que genera la tabla dinámica, incluidos los totales generales.
- `PivotConditionFormatScopeType.Field` - las celdas de valor que pertenecen al campo que identifica la celda, excluyendo los totales generales. La celda debe ser una celda de campo, como una etiqueta de fila de campo; proporcionar una celda de valor genera una excepción.
- `PivotConditionFormatScopeType.Selection` - solo las celdas de valor en la intersección que la celda selecciona, típicamente una única celda de valor.
El ejemplo a continuación crea una tabla dinámica de ventas de frutas cuya esquina superior izquierda está en E3, ancla un formato condicional en la celda F4 (fila 3, columna 5) con el alcance `Data`, y resalta cada cantidad mayor a 200 en blanco negrita sobre rojo. Con los valores Manzana 220, Plátano 330, Cereza 200 y el total general 750, la regla colorea F4, F5 y F7; la región resuelta es toda la columna de datos F4:F7, y solo las celdas cuyo valor cumple la regla se iluminan.

```html
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType, PivotConditionFormatScopeType,
        FormatConditionType, OperatorType, Color, BackgroundType } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Anclar el formato condicional en F4 (fila 3, columna 5) con el alcance Data
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    format.applyTo(3, 5, PivotConditionFormatScopeType.Data);
    // Regla - resaltar cantidades mayores a 200
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.GreaterThan, "200", null);
    const style = workbook.createStyle();
    style.font.isBold = true;
    style.font.color = Color.White;
    style.foregroundColor = Color.Red;
    style.pattern = BackgroundType.Solid;
    format.formatConditions.get(conditionIndex).style = style;
    // wb.save(SaveFormat.Xlsx) devuelve el archivo como bytes
    fs.writeFileSync("PivotConditionalFormatData.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule paints F4, F5, and F7");
    process.exit(0);
});
```

Anclar la misma regla en la etiqueta de fila de campo E4 (fila 3, columna 4) con el alcance `Field` se resuelve a F4:F6 en su lugar — la misma columna de datos sin la fila de total general — porque el alcance ahora describe el campo `Fruit` en lugar de todo el área de valores. El alcance `Selection` anclado en F4 se resuelve únicamente a F4.

## **Definir la región manualmente**

### **Un rectángulo de hoja de cálculo con addCellArea**
`addCellArea(cellArea)` registra el rectángulo proporcionado como el objetivo de la regla. Las coordenadas son coordenadas de hoja de cálculo basadas en cero, y la región es exactamente el rectángulo suministrado — sin expansión a la columna de datos y sin lógica de totales generales. Úselo cuando las celdas de interés son un rectángulo fijo conocido del diseño actual de la tabla dinámica.

```html
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType,
        FormatConditionType, OperatorType, Color, BackgroundType, CellArea } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Apuntar al rectángulo F4:F6 (las celdas de valor sin el total general)
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    const area = new CellArea();
    area.startRow = 3;
    area.startColumn = 5;
    area.endRow = 5;
    area.endColumn = 5;
    format.addCellArea(area);
    // Regla - cursiva en amarillo claro para montos entre 150 y 300
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.Between, "150", "300");
    const style = workbook.createStyle();
    style.font.isItalic = true;
    style.foregroundColor = Color.LightYellow;
    style.pattern = BackgroundType.Solid;
    format.formatConditions.get(conditionIndex).style = style;
    fs.writeFileSync("PivotConditionalFormatCellArea.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule paints F4 and F6");
    process.exit(0);
});
```

### **Una región pivot semántica con pivotAreas**
`pivotAreas` es el mismo modelo de región semántica que la página hermana utiliza para estilos estáticos. Construya un `PivotArea`, seleccione un campo o región con `select` o `selectField`, y añádalo con `pivotAreas.addPivotArea(pivotArea)`. Una región semántica permanece adjunta a su campo, por lo que el formato condicional sigue al campo cuando la tabla dinámica se actualiza y el diseño cambia. La sobrecarga `pivotAreas.add(pivotArea)` sigue funcionando pero está marcada como obsoleta — prefiera `addPivotArea`.

```html
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType, PivotArea,
        FormatConditionType, OperatorType, Color } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Adjuntar la regla al campo de datos Amount como una región semántica
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    const area = new PivotArea(pivotTable);
    area.selectField(PivotFieldType.Data, "Amount");
    format.pivotAreas.addPivotArea(area);
    // Regla - texto gris para montos menores a 150
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.LessThan, "150", null);
    const style = workbook.createStyle();
    style.font.color = Color.Gray;
    format.formatConditions.get(conditionIndex).style = style;
    fs.writeFileSync("PivotConditionalFormatPivotArea.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule is attached to the Amount value cells");
    process.exit(0);
});
```

## **Dónde se almacenan las reglas y cómo sobreviven a una recarga**
Cada llamada a `conditionalFormats.add()` agrega un `PivotConditionalFormat` a la tabla dinámica. Las condiciones, sus fórmulas y sus estilos se guardan con el libro de trabajo; volver a abrir el archivo guardado por el primer ejemplo en Node muestra la misma regla con su tipo, operador y fórmula intactos, y `getCellAreas()` informa la misma región. En esta plataforma, las propiedades `type` y `operator` de una condición aparecen como los valores numéricos del enumerado. Las entradas que nunca recibieron una condición se eliminan al guardar el libro de trabajo, de la misma manera que Excel descarta un formato condicional sin regla.

```html
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
AsposeCells.onReady().then(() => {
    // Recargar el archivo escrito por el primer ejemplo
    const workbook = new Workbook(new Uint8Array(fs.readFileSync("PivotConditionalFormatData.xlsx")));
    const pivotTable = workbook.worksheets.get(0).pivotTables.get(0);
    console.log("Conditional formats: " + pivotTable.conditionalFormats.count);
    for (let i = 0; i < pivotTable.conditionalFormats.count; i++) {
        const format = pivotTable.conditionalFormats.get(i);
        for (let j = 0; j < format.formatConditions.count; j++) {
            const condition = format.formatConditions.get(j);
            console.log("Format " + i + ": " + condition.type + " " + condition.operator + " formula1=" + condition.formula1);
        }
        const areas = format.getCellAreas();
        for (const area of areas)
            console.log("    rows " + (area.startRow + 1) + "-" + (area.endRow + 1) +
                        ", columns " + (area.startColumn + 1) + "-" + (area.endColumn + 1));
    }
    // Esto imprime:
    // Formatos condicionales: 1
    // Formato 0: 1 2 formula1==200   (tipo 1 = CellValue, operador 2 = GreaterThan)
    //     filas 4-7, columnas 6-6        (F4:F7, la región de datos resuelta)
    process.exit(0);
});
```

## **Artículos relacionados**
- [Aplicar estilo a tabla dinámica](/cells/es/javascript-cpp/apply-style-to-pivot-table/)
- [Formato de parte de una tabla dinámica](/cells/es/javascript-cpp/format-part-of-pivot-table/)
- [Mostrar o filtrar los 10 principales en tabla dinámica](/cells/es/javascript-cpp/top-10-show-or-filter-in-pivot-table/)
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/javascript-cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}