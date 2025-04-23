---
title: 通过 C++ 在 Node.js 中生成工作表缩略图
linktitle: 生成工作表的缩略图
type: docs
weight: 110
url: /zh/nodejs-cpp/generate-thumbnail-of-the-worksheet/
description: 学习如何使用 Aspose.Cells for Node.js via C++ 从工作表生成缩略图图片。在文档和演示中创建预览的小图片。
---

{{% alert color="primary" %}} 

从工作表生成缩略图可能很有用。缩略图是一个小图像，可以粘贴到 Word 文档或 PowerPoint 演示文稿中，以预览工作表内容。它可以添加到网页，用于提供下载原始文档的链接，并且具有各种其他用途。

{{% /alert %}} 

Aspose.Cells for Node.js via C++ 允许您将工作表导出为图像文件，因此制作缩略图变得轻而易举。下面的示例代码展示了如何将工作表导出为图像文件。

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
