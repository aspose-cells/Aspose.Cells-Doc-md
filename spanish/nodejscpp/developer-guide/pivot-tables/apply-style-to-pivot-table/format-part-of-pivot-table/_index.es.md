---
title: Formato de una parte de una Tabla Dinámica
description: Formatea una parte de una tabla dinámica en Aspose.Cells for Node.js via C++ aplicando estilos a regiones semánticas de PivotArea o rectángulos de CellArea mediante PivotTable.format, con los formatos almacenados en PivotTable.getPivotFormats() y preservados cuando la tabla dinámica se actualiza.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells, Node.js via C++, tabla dinámica, formato, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, selectField, formatAll
type: docs
weight: 20
url: /es/nodejs-cpp/format-part-of-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
`PivotTable.formatAll` aplica un solo estilo a toda la tabla dinámica y se cubre en la página principal. No distingue entre etiquetas, valores, totales o regiones específicas del informe.
En la práctica, sólo una parte de una tabla dinámica suele necesitar resaltarse. Los objetivos comunes incluyen las etiquetas pertenecientes a un campo de fila, las celdas de valor generadas por un campo, la fila de total general o un rectángulo arbitrario como las dos primeras filas de ítems.
Aplicar un estilo directamente a las celdas de la hoja de cálculo de una tabla dinámica no es equivalente. Excel almacena el formato de la tabla dinámica como regiones semánticas `PivotArea` en lugar de como registros de estilo de celda ordinarios. Un formato de pivot‑area permanece vinculado a una región como las etiquetas de un campo o los valores de datos, y se vuelve a resolver cuando la tabla dinámica se recalcula, actualiza o expande. Un estilo escrito directamente en una celda, por otro lado, pertenece a la posición de esa celda y no es rastreado por el modelo de tabla dinámica.
Aspose.Cells expone la familia completa de sobrecargas `PivotTable.format` para que ambos tipos de formato estén disponibles:
- `format(PivotArea, Style)` ancla un estilo a una región semántica que se construye con `PivotArea.select` o `PivotArea.selectField`.
- `format(CellArea, Style)` ancla un estilo a un rectángulo de hoja de cálculo dentro de la tabla dinámica.
- `format(number row, number column, Style)` apunta a una celda.
- `formatAll(Style)` formatea toda la tabla dinámica.

## **Formatear un Pivot Area**
El flujo de trabajo de área semántica es el enfoque recomendado cuando un resaltado debe seguir a un campo o a una región del informe.
1. Crea un `PivotArea` con `new PivotArea(pivotTable)`. El objeto describe una región semántica que pertenece a esa tabla dinámica específica.
2. Selecciona un campo por su posición basada en cero en un eje dado con `PivotArea.select(PivotFieldType axisType, number fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DataAndLabel` selecciona tanto las etiquetas como los datos del campo.
   - `PivotTableSelectionType.LabelOnly` selecciona sólo las etiquetas del campo.
   - `PivotTableSelectionType.DataOnly` selecciona sólo las celdas de datos del campo.
3. Selecciona un campo por nombre con `PivotArea.selectField(PivotFieldType axisType, string fieldName)`. Cuando se selecciona un campo de fila por nombre, la región se resuelve a las celdas de valor producidas por los ítems de ese campo.
4. Crea un `Style` con `workbook.createStyle()`, configura su fuente, color de primer plano y patrón de fondo sólido, y pasa el estilo a `pivotTable.format(area, style)`.
5. Cada llamada a la sobrecarga `PivotArea` agrega una entrada `PivotTableFormat` a `pivotTable.getPivotFormats()`.
6. Los formatos anclados al campo se pintan cuando se calcula la información de la tabla dinámica. Por lo tanto, llama a `pivotTable.calculateData()` después de aplicar los formatos para que los estilos sean visibles.
El siguiente ejemplo crea una pequeña tabla dinámica de ventas de frutas, aplica estilo a las etiquetas de fila `Fruit` con `PivotArea.select` y `PivotTableSelectionType.LabelOnly`, aplica estilo a las celdas de valor generadas por ese mismo campo de fila con `PivotArea.selectField`, y luego recalcula la tabla dinámica para que ambos estilos se pinten.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
// Fruit sales data
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
// Pivot table with its top-left corner at E3
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
const labelStyle = workbook.createStyle();
labelStyle.getFont().setIsBold(true);
labelStyle.setForegroundColor(AsposeCells.Color.Yellow);
labelStyle.setPattern(AsposeCells.BackgroundType.Solid);
const labelArea = new AsposeCells.PivotArea(pivotTable);
labelArea.select(
    AsposeCells.PivotFieldType.Row,
    0,
    AsposeCells.PivotTableSelectionType.LabelOnly
);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
const valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(AsposeCells.Color.LightGreen);
valueStyle.setPattern(AsposeCells.BackgroundType.Solid);
const valueArea = new AsposeCells.PivotArea(pivotTable);
valueArea.selectField(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **Formatear un Cell Area de la tabla dinámica**
Usa `PivotTable.format(CellArea, Style)` cuando la región de interés es un rectángulo simple de hoja de cálculo en lugar de una región semántica de pivote.
Un `CellArea` se describe mediante sus propiedades `startRow`, `startColumn`, `endRow` y `endColumn`. Los valores son coordenadas de hoja de cálculo basadas en cero, y las coordenadas finales identifican la última fila y columna incluidas en el rectángulo, por lo que el área cubre las celdas desde la posición inicial hasta la posición final inclusive.
A diferencia de un formato anclado a un campo, un formato `CellArea` se aplica a las celdas inmediatamente. No se necesita otra llamada a `pivotTable.calculateData()` para que el estilo aparezca.
Un rectángulo `CellArea` puede contener celdas de etiqueta y celdas de valor juntas. La siguiente sección describe cómo Aspose.Cells y Excel representan ese rectángulo internamente.
El siguiente ejemplo formatea el rectángulo `E4:F5` de la tabla dinámica con un estilo itálico y azul claro y guarda el libro de trabajo sin necesidad de recalcular nuevamente.

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
// Highlight the first two fruit rows (the rectangle E4:F5)
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setIsItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.LightBlue);
highlightStyle.setPattern(AsposeCells.BackgroundType.Solid);
const rectangle = new AsposeCells.CellArea();
rectangle.startRow = 3;
rectangle.startColumn = 4;
rectangle.endRow = 4;
rectangle.endColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **Cómo se asignan los Pivot Areas y Cell Areas**
Excel almacena el formato de la tabla dinámica como registros `pivotArea` en lugar de como registros de estilo de celda ordinarios. El mismo modelo es utilizado por Aspose.Cells, de modo que una solicitud de formato se traduce en áreas de pivote cuando se registra.
La relación entre el `CellArea` proporcionado por el usuario y las áreas de pivote almacenadas internamente es de muchos a muchos en ambas direcciones.
- Un `CellArea` puede producir varias áreas de pivote. Si el rectángulo abarca tanto celdas de etiqueta como de valor, se descompone en reglas separadas de etiqueta y datos, porque el modelo de pivote trata el formato de etiquetas y de datos de forma independiente.
- Un área de pivote puede resolverse en varias instancias disjuntas de `CellArea`. Una región semántica como una fila de total general, o un campo cuyos ítems no son contiguos, puede cubrir múltiples rectángulos. Por eso `PivotArea.getCellAreas()` devuelve una colección en lugar de un único rectángulo.
Cada operación de formato realizada a través de `pivotTable.format()` se registra en `pivotTable.getPivotFormats()`. Cada entrada `PivotTableFormat` expone el `PivotArea` asociado y el `Style` que se le aplica. La sobrecarga `PivotArea` agrega exactamente una entrada por llamada, mientras que un `CellArea` que contiene diferentes regiones semánticas puede agregar varias entradas.
Para distinguir las regiones almacenadas, cada `PivotArea` expone las banderas `getOnlyLabel()` y `getOnlyData()`. El ejemplo a continuación formatea un único rectángulo que cubre tanto etiquetas como valores, inspecciona `pivotTable.getPivotFormats()` y muestra las coordenadas `CellArea` a las que cada área de pivote almacenada se resuelve.

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
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setIsItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.LightBlue);
highlightStyle.setPattern(AsposeCells.BackgroundType.Solid);
// ONE rectangle in...
const rectangle = new AsposeCells.CellArea();
rectangle.startRow = 3;
rectangle.startColumn = 4;
rectangle.endRow = 4;
rectangle.endColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
console.log("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (let i = 0; i < pivotTable.getPivotFormats().getCount(); i++) {
    const storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    console.log(
        `Format ${i}: OnlyLabel=${storedArea.getOnlyLabel()}, OnlyData=${storedArea.getOnlyData()}`
    );
    const resolvedAreas = storedArea.getCellAreas();
    for (const resolved of resolvedAreas) {
        console.log(
            `    rows ${resolved.startRow + 1}-${resolved.endRow + 1}, ` +
            `columns ${resolved.startColumn + 1}-${resolved.endColumn + 1}`
        );
    }
}
// This prints:
// Stored formats: 2
// Format 0: OnlyLabel=true, OnlyData=false
//     rows 4-5, columns 5-5        (E4:E5, the label part)
// Format 1: OnlyLabel=false, OnlyData=true
//     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.save("FormatPivotAreasMap.xlsx");
```

{{% alert color="primary" %}}
Porque los formatos se almacenan como áreas de pivote en lugar de como estilos de celda ordinarios, sobreviven a la recalculación y a la actualización. Cuando la tabla dinámica se actualiza con `pivotTable.refreshData()`, se recalcula con `pivotTable.calculateData()`, o se guarda y vuelve a cargar, cada área de pivote almacenada se vuelve a resolver a la posición actual de su región y su estilo se vuelve a aplicar.
{{% /alert %}}

Usa un `PivotArea` construido con `select` o `selectField` cuando un resaltado debe permanecer vinculado a un campo o a una región semántica a través de actualizaciones, y usa un `CellArea` cuando es suficiente formatear un rectángulo fijo en el diseño actual de la tabla dinámica. La sobrecarga de una sola celda `format(number row, number column, Style)` apunta a una celda individual. Usa `formatAll`, cubierto en la página principal, cuando toda la tabla dinámica debe volver a estilizarse de una sola vez.

## **Artículos relacionados**
- [Aplicar estilo a la tabla dinámica](/cells/es/nodejs-cpp/apply-style-to-pivot-table/)
- [Agregar campos de fila y columna a la tabla dinámica](/cells/es/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Administrar campos de valor en la tabla dinámica](/cells/es/nodejs-cpp/manage-value-fields/)
- [Actualizar tabla dinámica](/cells/es/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}