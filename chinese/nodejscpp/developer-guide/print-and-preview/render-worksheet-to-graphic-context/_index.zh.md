---
title: 用 Node.js 通过 C++ 将工作表渲染为图形上下文
linktitle: 将工作表呈现到图形上下文
type: docs
weight: 300
url: /zh/nodejs-cpp/render-worksheet-to-graphic-context/
description: 学习如何用 Aspose.Cells for Node.js via C++ 将工作表渲染为图形上下文，包括渲染到图像文件、屏幕和打印机。
---

{{% alert color="primary" %}}

Aspose.Cells 现可将工作表渲染为图形上下文。图形上下文可以是任何物理或虚拟的媒介，例如图像文件、屏幕或打印机。请使用以下两种方法之一将工作表渲染为图形上下文。

- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)
- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)

{{% /alert %}}

以下代码演示如何使用 Aspose.Cells 将工作表渲染到图形上下文。一旦执行，它会打印整个工作表，并用蓝色填充剩余空白区域，保存为 **OutputImage_out_.png** 文件。你可以使用任何源 Excel 文件尝试这段代码，也请阅读代码中的注释以便更好理解。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleBook.xlsx");
// Create workbook object from source file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create empty image buffer
const bmpOptions = new AsposeCells.ImageOrPrintOptions();
bmpOptions.setOnePagePerSheet(true);

// Render worksheet to image
const sheetRender = new AsposeCells.SheetRender(worksheet, bmpOptions);
sheetRender.toImage(0, dataDir + "/OutputImage_out.png");

// Save the image in Png format
```
