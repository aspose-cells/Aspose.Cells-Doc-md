---  
title: 为渲染自动调整行高（Node.js通过C++）  
linktitle: 在渲染时自动调整列的行高  
type: docs  
weight: 130  
url: /zh/nodejs-cpp/autofit-rows-for-rendering/  
description: 学习如何使用Aspose.Cells for Node.js via C++为Excel渲染自动调整行高，防止保存的PDF中的文本被剪裁。  
---  

通常情况下，为了在单元格中显示全部文本，可以在Microsoft Excel中以普通视图（100%的缩放）自动调整行高。这允许在普通视图中完全显示文本，即使打印或保存为PDF，文本也会正确显示。

然而，在某些情况下，自动调整行高在普通视图中效果良好，但切换到打印视图或保存为PDF时，文本会被剪裁。请检查源文件[Book1.xlsx]及截图。

![打印视图中文本被截断](text_clipped_in_printview.png)

如果想防止在保存的PDF文件中剪裁文本，可以使用带有[AutoFitterOptions.getForRendering()](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getForRendering--)选项的自动调整行高。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Init workbook instance.
const workbook = new AsposeCells.Workbook(filePath);

// Set autofit options for rendering.
const autoFitterOptions = new AsposeCells.AutoFitterOptions();
autoFitterOptions.setForRendering(true);

// Autofit rows with options.
workbook.getWorksheets().get(0).autoFitRows(autoFitterOptions);

// Save to pdf.
workbook.save("output.pdf", AsposeCells.SaveFormat.Pdf);
```

现在，在输出的 PDF 文件中文本不再被截断。

![保存的 PDF 文件中文本未被截断](text_not_clipped_in_saved_pdf.png)  
