---  
title: 指定如何在输出 PDF 和图片中跨字符串，使用 Node.js 和 C++  
linktitle: 指定输出PDF和图像中如何跨越字符串  
type: docs  
weight: 120  
url: /zh/nodejs-cpp/specify-how-to-cross-string-in-output-pdf-and-image/  
description: 学习如何通过使用 Aspose.Cells for Node.js via C++ 指定跨类型控制输出 PDF/图片中的文本溢出。  
---  

## **可能的使用场景**

当单元格包含文本或字符串且其长度超过单元格宽度时，如果下一列的单元格为空或无内容，字符串会溢出。当你将 Excel 文件保存为 PDF/图片时，可以通过使用 [**TextCrossType**](https://reference.aspose.com/cells/nodejs-cpp/textcrosstype) 枚举值来控制此溢出，枚举值如下：

- **TextCrossType.Default**：显示文本，类似于 MS Excel，其取决于下一单元格。如果下一单元格为空，字符串将溢出或截断。

- **TextCrossType.CrossKeep**：像 MS Excel 导出PDF/图片时那样显示字符串。

- **TextCrossType.CrossOverride**：允许文本跨越其他单元格显示，并覆盖被跨越单元格中的文本。

- **TextCrossType.StrictInCell**: 仅在单元格宽度内显示字符串。

## **使用TextCrossType指定输出PDF/图像中如何跨越字符串**

以下示例代码加载示例Excel文件，并通过指定不同的 [**TextCrossType**](https://reference.aspose.com/cells/nodejs-cpp/textcrosstype) 来保存为PDF/图片格式。示例Excel文件和输出文件可以从以下链接下载：

[sampleCrossType.xlsx](81920905.xlsx)  

[outputCrossType.pdf](81920903.pdf)  

[outputCrossType.png](81920904.png)  

### 示例代码

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load template Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCrosssType.xlsx"));

// Initialize PDF save options
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set text cross type
pdfSaveOptions.setTextCrossType(AsposeCells.TextCrossType.StrictInCell);

// Save PDF file
workbook.save(outputDir + "outputCrosssType.pdf", pdfSaveOptions);

// Initialize image or print options
const imageSaveOptions = new AsposeCells.ImageOrPrintOptions();

// Set text cross type
imageSaveOptions.setTextCrossType(AsposeCells.TextCrossType.StrictInCell);

// Initialize sheet renderer object
const sheetRenderer = new AsposeCells.SheetRender(workbook.getWorksheets().get(0), imageSaveOptions);

sheetRenderer.toImage(0, outputDir + "outputCrosssType.png");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
