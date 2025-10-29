---  
title: Добавить водяной знак WordArt на график с помощью Node.js и C++  
linktitle: Добавить водяной знак WordArt к диаграмме  
description: Узнайте, как использовать Aspose.Cells for Node.js via C++ для добавления водяного знака WordArt на график в Microsoft Excel. Наше руководство покажет, как создавать и работать с позиционированием водяного знака WordArt для повышения визуальной привлекательности и уникальности вашего графика.  
keywords: Aspose.Cells for Node.js, Watermark WordArt, Водяной знак графика, Microsoft Excel, Визуальная привлекательность, Уникальность графика.  
type: docs  
weight: 50  
url: /ru/nodejs-cpp/add-wordart-watermark-to-chart/  
---  

{{% alert color="primary" %}}  

Вы можете использовать WordArt для добавления специальных текстовых эффектов в электронные таблицы. Например, растянуть заголовок, украсить текст, сделать текст подходящим под предварительно заданную форму или применить к тексту эффект водяного знака к области построения диаграммы. WordArt становится объектом, который можно перемещать или располагать в электронных таблицах для добавления украшения.  

В следующем примере показано, как добавить текст WordArt в качестве водяного знака для области построения диаграммы.  

{{% /alert %}}  

В следующем примере показано, как добавить фигуру WordArt в качестве водяного знака для существующей зоны построения диаграммы.  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
