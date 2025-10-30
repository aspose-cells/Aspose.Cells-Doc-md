---
title: Insertar Sparkline con Node.js a través de C++
linktitle: Gráficos de Chispa
type: docs
weight: 160
url: /es/nodejs-cpp/creating-sparklines/
description: Crear sparkline para Excel usando Aspose.Cells for Node.js via C++.
---

## **Insertar un gráfico de chispa**
{{% alert color="primary" %}} 

Sparkline es un pequeño gráfico en una celda de la hoja de cálculo que proporciona una representación visual de los datos. Use sparklines para mostrar tendencias en una serie de valores, como incrementos o disminuciones estacionales, ciclos económicos o para resaltar valores máximos y mínimos. Coloque un sparkline cerca de sus datos para mayor impacto. Hay tres tipos de Sparkline: Línea, Columna y Apilado.

{{% /alert %}} 

Es fácil crear un sparkline con Aspose.Cells for Node.js via C++ con los siguientes ejemplos de código:



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const book = new AsposeCells.Workbook(filePath);
const sheet = book.getWorksheets().get(0);

sheet.getCells().get("A1").putValue(5);
sheet.getCells().get("B1").putValue(2);
sheet.getCells().get("C1").putValue(1);
sheet.getCells().get("D1").putValue(3);

// Define the CellArea
const ca = AsposeCells.CellArea.createCellArea(0, 4, 0, 4);

const idx = sheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, `${sheet.getName()}!A1:D1`, false, ca);

const group = sheet.getSparklineGroups().get(idx);
group.getSparklines().add(`${sheet.getName()}!A1:D1`, 0, 4);

// Customize Sparklines

// Create CellsColor
const clr = book.createCellsColor();
clr.setColor(AsposeCells.Color.Orange);
group.setSeriesColor(clr);

// Set the high points are colored green and the low points are colored red
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.getHighPointColor().setColor(AsposeCells.Color.Green);
group.getLowPointColor().setColor(AsposeCells.Color.Red);
// Set line weight 
group.setLineWeight(1.0);

// Saving the Excel file
book.save(path.join(dataDir, "output.xlsx"));
```

## **Temas avanzados**
- [Usar Gráficos de Chispa y Configuración de Formato 3D](/cells/es/nodejs-cpp/using-sparklines-and-settings-3d-format/)
{{< app/cells/assistant language="nodejs-cpp" >}}
