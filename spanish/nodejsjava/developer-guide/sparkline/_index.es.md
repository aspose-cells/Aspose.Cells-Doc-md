---
title: ...
description: ...
linktitle: ...
keywords: ...
type: docs
weight: 195
url: /es/nodejs-java/creating-sparklines/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

[alert block]

## **Introducción**

## **Minigráficos de líneas**

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();
// Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);
// Step 3: Build a CellArea pointing to destination cell F1
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // column F (0-indexed)
dest.setEndColumn(5);
dest.setStartRow(0);      // row 1 (0-indexed)
dest.setEndRow(0);
// Step 4: Add a Line sparkline from A1:E1 into F1
// SparklineGroups.Add returns the index of the newly added group
let index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(index);
// Step 5: Create a red CellsColor and assign it to the sparkline line color
let red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);
// Step 6: Enable high-point and low-point markers
group.setShowHighPoint(true);
group.setShowLowPoint(true);
// Step 7: Save the workbook
workbook.save("output_line.xlsx");
```

## **Minigráficos de columnas**

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Paso 2: Escribir valores de muestra en A1:E1
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// Paso 3: Construir un CellArea que apunte a F1 (índice de columna 5, índice de fila 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);
// Paso 4: Agregar un minigráfico de columna a la celda de destino
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);
// Paso 5: Confirmar el tipo de minigráfico leyendo group.Type
console.log("Tipo de minigráfico agregado: " + group.getType());
// Paso 6: Guardar el libro de trabajo
workbook.save("output_column.xlsx");
console.log("Libro de trabajo guardado como output_column.xlsx");
```

## **Minigráficos de victorias/derrotas**

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// Paso 2: Poblar datos de muestra en la fila 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Paso 3: Construir un CellArea apuntando a F1 (columna 5, fila 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // F
dest.setEndColumn(5);
dest.setStartRow(0);      // fila 1
dest.setEndRow(0);
// Paso 4: Agregar un minigráfico de Ganancias/Pérdidas (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest
);
let group = worksheet.getSparklineGroups().get(groupIndex);
// Paso 5: Personalizar el grupo de minigráficos
// Habilitar marcadores de punto alto y punto bajo
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Establecer el color del punto alto en verde
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.getGreen());
group.setHighPointColor(highColor);
// Establecer el color del punto bajo en rojo
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.getRed());
group.setLowPointColor(lowColor);
// Establecer el color del punto negativo en naranja
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.getOrange());
group.setNegativePointsColor(negColor);
// Establecer el color de serie predeterminado (usado para barras positivas)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.getSteelBlue());
group.setSeriesColor(seriesColor);
// Paso 6: Guardar el libro
workbook.save("output_winloss.xlsx");
console.log("Libro guardado exitosamente: output_winloss.xlsx");
```

## **Combinando los tres tipos de minigráficos**

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Paso 2: Poblar datos de muestra en la fila 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Paso 3: Agregar un grupo de minigráficos de línea en F1
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Personalizar el color del minigráfico de línea mediante CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);
// Paso 4: Agregar un grupo de minigráficos de columna en F2
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Personalizar el color de la serie del minigráfico de columna
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);
// Paso 5: Agregar un grupo de minigráficos de victoria/derrota (apilados) en F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Personalizar el color de la serie del minigráfico de victoria/derrota
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);
// Paso 6: Guardar el libro de trabajo
workbook.save("output_all.xlsx");
```

## **Personalización de la apariencia del minigráfico**

{{% alert color="primary" %}}
Aspose.Cells admite la creación de minigráficos dentro de celdas de hojas de cálculo. Los minigráficos son gráficos en miniatura que caben dentro de una sola celda y proporcionan una representación visual rápida de las tendencias de los datos. Aspose.Cells admite minigráficos de líneas, columnas y victorias/derrotas, y cada uno se puede personalizar en cuanto a color, grosor de línea, puntos altos/bajos y marcadores.
{{% /alert %}}

{{< app/cells/assistant language="javascript" >}}