---
title: Formato de una Parte de una Tabla Dinámica
description: Formatear una parte de una tabla dinámica en Aspose.Cells for Node.js via Java aplicando estilos a regiones semánticas PivotArea o rectángulos CellArea mediante PivotTable.format, con los formatos almacenados en PivotTable.getPivotFormats() y preservados cuando la tabla dinámica se actualiza.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells for Node.js via Java, tabla dinámica, formato, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Node.js via Java
type: docs
weight: 20
url: /es/nodejs-java/format-part-of-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de Uso Posibles**
`PivotTable.formatAll` aplica un solo estilo a toda la tabla dinámica y se describe en la página principal. No distingue entre etiquetas, valores, totales o regiones específicas del informe.
En la práctica, sólo una parte de una tabla dinámica suele necesitar resaltarse. Los objetivos comunes incluyen las etiquetas pertenecientes a un campo de fila, las celdas de valor producidas por un campo, la fila de total general o un rectángulo arbitrario como las dos primeras filas de elementos.
Aplicar un estilo directamente a las celdas de la hoja de cálculo de una tabla dinámica no es equivalente. Excel almacena el formato de la tabla dinámica como regiones semánticas `PivotArea` en lugar de registros tradicionales de estilo de celda. Un formato de zona pivot se mantiene asociado a una región como las etiquetas o los valores de datos de un campo, y se vuelve a resolver cuando la tabla dinámica se recalcula, actualiza o expande. Por otro lado, un estilo escrito directamente en una celda pertenece a esa posición de celda y no es rastreado por el modelo de tabla dinámica.
Aspose.Cells expone la familia completa de sobrecargas `PivotTable.format` para que ambos tipos de formato estén disponibles:
- `format(PivotArea, Style)` ancla un estilo a una región semántica que se construye con `PivotArea.select` o `PivotArea.selectField`.
- `format(CellArea, Style)` ancla un estilo a un rectángulo de la hoja dentro de la tabla dinámica.
- `format(int row, int column, Style)` se dirige a una única celda.
- `formatAll(Style)` forma toda la tabla dinámica.

## **Formatear un Área Pivot**
El flujo de trabajo basado en áreas semánticas es el enfoque recomendado cuando un resaltado debe seguir a un campo o a una región del informe.
1. Cree un `PivotArea` con `new PivotArea(pivotTable)`. El objeto describe una región semántica que pertenece a esa tabla dinámica específica.
1. Seleccione un campo por su posición basada en cero en un eje dado con `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DATA_AND_LABEL` selecciona tanto las etiquetas como los datos del campo.
   - `PivotTableSelectionType.LABEL_ONLY` selecciona sólo las etiquetas del campo.
   - `PivotTableSelectionType.DATA_ONLY` selecciona sólo las celdas de datos del campo.
1. Seleccione un campo por nombre con `PivotArea.selectField(PivotFieldType axisType, string fieldName)`. Cuando se selecciona un campo de fila por nombre, la región se resuelve en las celdas de valor producidas por los elementos de ese campo.
1. Cree un `Style` con `Workbook.createStyle()`, configure su fuente, color de primer plano y patrón de fondo sólido, y pase el estilo a `PivotTable.format(area, style)`.
1. Cada llamada a la sobrecarga `PivotArea` agrega una entrada `PivotTableFormat` a `PivotTable.getPivotFormats()`.
1. Los formatos anclados a campos se pintan cuando se calculan los datos de la tabla dinámica. Por lo tanto, llame a `PivotTable.calculateData()` después de aplicar los formatos para que los estilos se vuelvan visibles.
El siguiente ejemplo crea una pequeña tabla dinámica de ventas de frutas, aplica estilos a las etiquetas de fila `Fruit` con `PivotArea.select` y `PivotTableSelectionType.LABEL_ONLY`, aplica estilos a las celdas de valor producidas por ese mismo campo de fila con `PivotArea.selectField`, y luego recalcula la tabla dinámica para que ambos estilos se pinten.

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
const labelStyle = workbook.createStyle();
labelStyle.getFont().setBold(true);
labelStyle.setForegroundColor(AsposeCells.Color.getYellow());
labelStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const labelArea = new AsposeCells.PivotArea(pivotTable);
labelArea.select(
    AsposeCells.PivotFieldType.ROW,
    0,
    AsposeCells.PivotTableSelectionType.LABEL_ONLY
);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
const valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(AsposeCells.Color.getLightGreen());
valueStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const valueArea = new AsposeCells.PivotArea(pivotTable);
valueArea.selectField(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **Formatear un Área de Celda de la Tabla Dinámica**
Utilice `PivotTable.format(CellArea, Style)` cuando la región de interés sea un simple rectángulo de hoja de cálculo en lugar de una región pivot semántica.
`CellArea` se describe mediante los campos públicos `StartRow`, `StartColumn`, `EndRow` y `EndColumn`. Los valores son coordenadas de hoja basadas en cero, y las coordenadas finales identifican la última fila y columna incluidas en el rectángulo, de modo que el área cubre las celdas desde la posición inicial hasta la posición final inclusive.
A diferencia de un formato anclado a un campo, un formato `CellArea` se aplica a las celdas de inmediato. No se necesita otra llamada a `calculateData()` para que el estilo aparezca.
Un rectángulo `CellArea` puede contener celdas de etiquetas y celdas de valores juntas. La sección siguiente describe cómo Aspose.Cells y Excel representan internamente ese rectángulo.
El siguiente ejemplo formatea el rectángulo `E4:F5` de la tabla dinámica con un estilo cursiva, azul claro, y guarda el libro de trabajo sin necesidad de recalculación adicional.

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
// Highlight the first two fruit rows (the rectangle E4:F5)
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(
    AsposeCells.Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF)
);
highlightStyle.setPattern(AsposeCells.BackgroundType.SOLID);
const rectangle = new AsposeCells.CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **Cómo se Relacionan las Áreas Pivot y las Áreas de Celda**
Excel almacena el formato de la tabla dinámica como registros `pivotArea` en lugar de registros tradicionales de estilo de celda de hoja. El mismo modelo lo utiliza Aspose.Cells, por lo que una solicitud de formato se traduce en áreas pivot cuando se registra.
La relación entre el `CellArea` proporcionado por el usuario y las áreas pivot almacenadas internamente es de muchos a muchos en ambas direcciones.
- Un `CellArea` puede producir varias áreas pivot. Si el rectángulo abarca tanto celdas de etiqueta como de valor, se descompone en reglas separadas de etiqueta y datos, porque el modelo pivot trata el formato de etiquetas y el de datos de forma independiente.
- Una área pivot puede resolverse en varias instancias `CellArea` disjuntas. Una región semántica como una fila de total general, o un campo cuyos elementos no son contiguos, puede cubrir varios rectángulos. Por eso `PivotArea.getCellAreas()` devuelve una colección en lugar de un único rectángulo.
Cada operación de formato realizada a través de `PivotTable.format` se registra en `PivotTable.getPivotFormats()`. Cada entrada `PivotTableFormat` expone el `PivotArea` asociado y el `Style` que se aplica. La sobrecarga `PivotArea` agrega exactamente una entrada por llamada, mientras que un `CellArea` que contiene diferentes regiones semánticas puede agregar múltiples entradas.
Para distinguir las regiones almacenadas, cada `PivotArea` expone las banderas `getOnlyLabel()` y `getOnlyData()`. El ejemplo a continuación formatea un único rectángulo que cubre tanto etiquetas como valores, inspecciona `PivotTable.getPivotFormats()` y muestra las coordenadas `CellArea` a las que cada área pivot almacenada se resuelve.

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
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(AsposeCells.BackgroundType.SOLID);
// ONE rectangle in...
const rectangle = new AsposeCells.CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
console.log("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (let i = 0; i < pivotTable.getPivotFormats().getCount(); i++) {
    const storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    console.log(
        `Format ${i}: OnlyLabel=${storedArea.getOnlyLabel()}, OnlyData=${storedArea.getOnlyData()}`
    );
    const resolvedAreas = storedArea.getCellAreas();
    for (let j = 0; j < resolvedAreas.length; j++) {
        const resolved = resolvedAreas[j];
        console.log(
            `    rows ${resolved.StartRow + 1}-${resolved.EndRow + 1}, columns ${resolved.StartColumn + 1}-${resolved.EndColumn + 1}`
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
Porque los formatos se almacenan como áreas pivot en lugar de como estilos de celda ordinarios, sobreviven a la recalculación y a la actualización. Cuando la tabla dinámica se actualiza con `PivotTable.refreshData()`, se recalcula con `calculateData()`, o se guarda y se vuelve a cargar, cada área pivot almacenada se vuelve a resolver a la posición actual de su región y su estilo se vuelve a aplicar.
{{% /alert %}}

Utilice un `PivotArea` construido con `select` o `selectField` cuando un resaltado debe permanecer unido a un campo o a una región semántica a través de actualizaciones, y use un `CellArea` cuando sea suficiente formatear un rectángulo fijo en el diseño actual de la tabla dinámica. La sobrecarga de una sola celda `format(int row, int column, Style)` se dirige a una celda individual. Use `formatAll`, descrito en la página principal, cuando toda la tabla dinámica deba volver a formatearse de una sola vez.

## **Artículos Relacionados**
- [Aplicar estilo a tabla dinámica](/cells/es/nodejs-java/apply-style-to-pivot-table/)
- [Agregar campos de fila y columna a la tabla dinámica](/cells/es/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Administrar campos de valores en la tabla dinámica](/cells/es/nodejs-java/manage-value-fields/)
- [Actualizar tabla dinámica](/cells/es/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}