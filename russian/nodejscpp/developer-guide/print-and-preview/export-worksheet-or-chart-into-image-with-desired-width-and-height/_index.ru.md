---  
title: Экспорт листа или графика в изображение с желаемой шириной и высотой через Node.js  
linktitle: Экспорт рабочего листа или диаграммы в изображение с желаемой шириной и высотой  
type: docs  
weight: 290  
url: /ru/nodejs-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/  
description: Узнайте, как экспортировать лист или график в изображение с указанной шириной и высотой, используя Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Вы можете использовать Aspose.Cells for Node.js via C++ для экспорта вашего листа или графика в изображение с желаемой шириной и высотой. Он предоставляет метод [**ImageOrPrintOptions.setDesiredSize(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#setDesiredSize-number-number-boolean-) для установки желаемой ширины и высоты экспортируемого изображения. Размеры указываются в пикселях.  
{{% /alert %}}  

Приведенный ниже код экспортирует рабочий лист в изображение размером 400x400.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook object from source file
const filePath = path.join(sourceDir, "sampleWorksheetToImageDesiredSize.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set image or print options we want one page per sheet. The image format is in png and desired dimensions are 400x400
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setOnePagePerSheet(true);
opts.setImageType(AsposeCells.ImageType.Png);
opts.setDesiredSize(400, 400, false);

// Render sheet into image
const sr = new AsposeCells.SheetRender(worksheet, opts);
sr.toImage(0, path.join(outputDir, "outputWorksheetToImageDesiredSize.png"));
```  

