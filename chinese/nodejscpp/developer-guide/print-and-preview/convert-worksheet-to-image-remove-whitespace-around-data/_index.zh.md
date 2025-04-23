---
title: 通过C++在Node.js中转换工作表为图片  移除数据周围的空白区域
linktitle: 将工作表转换为图像  删除数据周围的空白
type: docs
weight: 40
url: /zh/nodejs-cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: 学习如何使用Aspose.Cells for Node.js via C++将Microsoft Excel工作表转换为图片，并移除数据周围的空白区域。 
---

{{% alert color="primary" %}}

有时，您需要在应用程序或网页中呈现工作表图像。例如，您可能需要将图像插入 Word 文档、PDF 文件、PowerPoint 演示文稿或其他文档中。基本上，您希望将工作表呈现为图像，以便将其粘贴到其他应用程序中。Aspose.Cells 允许您将 Microsoft Excel 工作表转换为图像。

{{% /alert %}}

## **删除数据周围的空白**

[**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender) API 可将工作表转换为带有任何指定属性（例如图像格式、分页工作表等）的图像文件。支持多种图像格式，包括 BMP、GIF、JPG、TIFF 和 EMF。

使用工作表转图像功能时，默认情况下输出图像具有周围的空白（即边框）。您可以通过将源工作表的顶部、底部、左侧和右侧的页面设置边距设置为 0，并相应地指定 [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions) 属性来删除这些空白。

以下代码片段删除输出图像中的数据周围的空白。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);
const options = new AsposeCells.LoadOptions();
options.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All));
// Specify your print area if you want
// sheet.getPageSetup().setPrintArea("A1:H8");

// To remove the white border around the image.
sheet.getPageSetup().setLeftMargin(0);
sheet.getPageSetup().setRightMargin(0);
sheet.getPageSetup().setBottomMargin(0);
sheet.getPageSetup().setTopMargin(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setImageType(AsposeCells.ImageType.Emf);

// Set only one page would be rendered for the image
imgOptions.setOnePagePerSheet(true);
imgOptions.setPrintingPage(AsposeCells.PrintingPageType.IgnoreBlank);

// Create the SheetRender object based on the sheet with its ImageOrPrintOptions attributes
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Convert the image
sr.toImage(0, path.join(outputDir, "outputRemoveWhitespaceAroundData.emf"));
```
