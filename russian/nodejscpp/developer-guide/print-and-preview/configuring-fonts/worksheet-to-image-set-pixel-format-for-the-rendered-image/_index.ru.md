---  
title: Таблица Изображение  Установка формата пикселей для рендеренного изображения с помощью Node.js через C++  
linktitle: Рабочий лист в изображение  установите формат пикселей для полученного изображения  
type: docs  
weight: 200  
url: /ru/nodejs-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/  
---  

{{% alert color="primary" %}}  
Иногда вам нужно указать формат пикселей при рендеринге рабочего листа в формат изображения. По умолчанию Aspose.Cells использует 32 бита на пиксель. Aspose.Cells позволяет настраивать формат пикселей (глубину бит) с помощью параметров для полученного изображения.  
{{% /alert %}}  

Пожалуйста, см. приведенный ниже образец кода, демонстрирующий, как установить желаемый формат пикселей при рендеринге изображений листов.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Load an Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleSetPixelFormatRenderedImage.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set the ImageOrPrintOptions with desired color depth (24 bits per pixel) and image format type
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setTiffColorDepth(AsposeCells.ColorDepth.Format24bpp);
opts.setImageType(AsposeCells.ImageType.Tiff);

// Instantiate SheetRender object based on the first worksheet
const sheetRender = new AsposeCells.SheetRender(worksheet, opts);

// Save the image (first page of the sheet) with the specified options
sheetRender.toImage(0, path.join(outputDir, "outputSetPixelFormatRenderedImage.tiff"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
