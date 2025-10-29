---
title: Создание миниатюры листа с помощью Node.js через C++
linktitle: Генерация миниатюры листа
type: docs
weight: 110
url: /ru/nodejs-cpp/generate-thumbnail-of-the-worksheet/
description: Узнайте, как создавать миниатюры изображений из листа с помощью Aspose.Cells for Node.js via C++. Создавайте маленькие изображения для предпросмотра в документах и презентациях.
---

{{% alert color="primary" %}} 

Генерация миниатюр листов может быть полезна. Миниатюра - это небольшое изображение, которое можно вставить в документ Word или презентацию PowerPoint, чтобы показать предварительный просмотр содержимого листа. Ее также можно добавить на веб-страницу с ссылкой для загрузки оригинального документа и использовать во многих других целях.

{{% /alert %}} 

Aspose.Cells for Node.js via C++ позволяет выводить листы в файлы изображений, поэтому создание миниатюры — это просто. Ниже показан пример кода, который показывает, как экспортировать листы в файлы изображений.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiate and open an Excel file
const filePath = path.join(sourceDir, "sampleGenerateThumbnailOfWorksheet.xlsx");
const book = new AsposeCells.Workbook(filePath);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Set the vertical and horizontal resolution
imgOptions.setVerticalResolution(200);
imgOptions.setHorizontalResolution(200);

// One page per sheet is enabled
imgOptions.setOnePagePerSheet(true);

// Set desired thumbnail dimensions
imgOptions.setDesiredSize(600, 600, true);

// Get the first worksheet
const sheet = book.getWorksheets().get(0);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Save the thumbnail directly
sr.toImage(0, path.join(outputDir, "outputGenerateThumbnailOfWorksheet.jpg"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
