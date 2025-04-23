---  
title: Agregar marca de agua WordArt al gráfico con Node.js a través de C++  
linktitle: Agregar marca de agua WordArt al gráfico  
description: Aprende cómo usar Aspose.Cells for Node.js via C++ para agregar una marca de agua WordArt a un gráfico en Microsoft Excel. Nuestra guía demostrará cómo crear y posicionar una marca de agua WordArt para mejorar el atractivo visual y la singularidad de tu gráfico.  
keywords: Aspose.Cells para Node.js, marca de agua WordArt, marca de agua en gráfico, Microsoft Excel, atractivo visual, singularidad del gráfico.  
type: docs  
weight: 50  
url: /es/nodejs-cpp/add-wordart-watermark-to-chart/  
---  

{{% alert color="primary" %}}  

Puede usar WordArt para agregar efectos especiales de texto a las hojas de cálculo. Por ejemplo, estirar un título, decorar texto, hacer que el texto se ajuste a una forma preestablecida o aplicar el texto afectado al área de trazado de un gráfico como marca de agua. El WordArt se convierte en un objeto que puede mover o posicionar en sus hojas de cálculo para agregar decoración.  

El siguiente ejemplo muestra cómo agregar una forma de WordArt como marca de agua para el área de trazado del gráfico.  

{{% /alert %}}  

El siguiente ejemplo muestra cómo agregar una forma de WordArt como marca de agua para el área de trazado de un gráfico existente.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Open the existing excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Get the chart in the first worksheet.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Add a WordArt watermark (shape) to the chart's plot area.
const wordart = chart.getShapes().addTextEffectInChart(AsposeCells.MsoPresetTextEffect.TextEffect2,
"CONFIDENTIAL", "Arial Black", 66, false, false, 1200, 500, 2000, 3000);

// Get the shape's fill format.
const wordArtFormat = wordart.getFill();

// Set the transparency.
wordArtFormat.setTransparency(0.9);

// Get the line format.
const lineFormat = wordart.getLine();

// Set Line format to invisible.
lineFormat.setWeight(0.0);

// Save the excel file.
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

