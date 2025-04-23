---
title: Извлечение изображений из листов с помощью ImageOrPrintOptions с Node.js через C++
linktitle: Извлечение изображений из листов с использованием ImageOrPrintOptions
type: docs
weight: 140
url: /ru/nodejs-cpp/extract-images-from-worksheets-using-imageorprintoptions/
description: Узнайте, как извлекать изображения из листов Excel и сохранять их с помощью Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}} 

Пользователи Microsoft Excel могут добавлять изображения в таблицы. С помощью Aspose.Cells for Node.js via C++ можно читать изображения из файлов Microsoft Excel и сохранять их на локальный диск. В этой статье показано как.

{{% /alert %}} 

Приведенный ниже образец кода показывает, как извлечь изображения из файла Excel и сохранить их.



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleExtractImagesFromWorksheets.xlsx"));

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get the first Picture in the first worksheet
const pic = worksheet.getPictures().get(0);

// Set the output image file path
const picformat = pic.getImageType().toString();

// Note: you may evaluate the image format before specifying the image path
// Define ImageOrPrintOptions
const printoption = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
printoption.setImageType(AsposeCells.ImageType.Jpeg);

// Save the image
pic.toImage(path.join(outputDir, "outputExtractImagesFromWorksheets.jpg"), printoption);
```
