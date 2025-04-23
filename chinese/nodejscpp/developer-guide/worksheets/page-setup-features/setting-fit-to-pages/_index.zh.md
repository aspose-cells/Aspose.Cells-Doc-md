---
title: 如何通过 Node.js 和 C++ 将 Excel 打印为宽和高适应页面
linktitle: 如何将Excel打印为宽度和高度适应的页面
type: docs
weight: 200
url: /zh/nodejs-cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: 本文展示了如何使用 Aspose.Cells for Node.js via C++ 设置 FitToPagesWide 和 FitToPagesTall 的代码示例。
keywords: 通过 Node.js 和 C++ 设置 FitToPagesWide 和 FitToPagesTall，如何在 Node.js 中添加 FitToPagesWide 和 FitToPagesTall，如何在 Excel 中设置 FitToPagesWide 和 FitToPagesTall，如何清除 Excel 中的 FitToPagesWide 和 FitToPagesTall，如何将 Excel 打印为宽和高适应页面，如何将工作表打印为一页，如何将工作表所有列打印在一页。
---

## **介绍**

FitToPagesWide和FitToPagesTall设置用于电子表格应用（如Microsoft Excel），用于控制打印时电子表格的缩放方式。这些设置确保你的打印输出在水平和垂直方向上都在指定的页数内。以下是每个设置的详细说明：

1. FitToPagesWide：此设置指定打印输出应适合的页宽。例如，将FitToPagesWide设置为1，表示内容缩放至适合一页宽，无论电子表格有多宽。
2. FitToPagesTall：该设置指定打印输出应适合的页数高。例如，将 FitToPagesTall 设置为 1，意味着内容将缩放以适应单页的高度，无论行数多少。

## **为什么使用适合页面宽度和高度**
以下是设置适合页面宽度和高度的一些原因：
1. 控制打印布局：通过指定页面宽度和高度的页数，可以确保打印的文档易于阅读且布局合理，没有列或行被尴尬地拆分到不同的页面上。
2. 一致性：如果你要打印多个工作表或报告，使用这些设置有助于保持格式一致，便于比较和分析打印的文档。
3. 专业呈现：正确缩放和适应内容到指定的页数可以使你的数据展示更专业、更有条理。

## **如何在Excel中将文件打印为宽度和高度都适合的页面**

要在Microsoft Excel中设置适合页面宽度和高度的设置，请按照以下步骤操作：

1. 打开你的Excel工作簿，转到你想打印的工作表。
2. 转到功能区的页面布局选项卡。
3. 在页面设置组中，点击右下角的小箭头打开页面设置对话框。
4. 在页面设置对话框中，切换到页面标签。
5. 在缩放下，选择“适合”选项，然后指定你希望的宽和高的页数：在第一个框输入你希望的宽页面数（“适合 x 页宽”），在第二个框输入你希望的高页面数（“适合 y 页高”）。
<br>
<img src="2.png" width=60% />

6. 点击确定应用设置。

## **如何使用 Aspose.Cells for Node.js via C++ 打印 Excel 为宽和高适应页面**

要在特定工作表中设置 FitToPagesWide 和 FitToPagesTall：首先加载[示例文件](input.xlsx)，然后你需要修改 [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/) 对象的 [**PageSetup.getFitToPagesTall()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesTall--) 和 [**PageSetup.getFitToPagesWide()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesWide--) 属性以达到目标工作表。以下是 Node.js 的示例：

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the number of pages to which the length of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesTall(1);

// Setting the number of pages to which the width of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesWide(1);

// Save the workbook
workbook.save("out_net.pdf");
```

输出结果：
<br>
<img src="1.png" width=60% />

## **如何使用 Aspose.Cells for Node.js via C++ 将工作表打印为一页**

要将工作表打印为一页：首先加载[示例文件](sample.xlsx)，然后你需要设置 [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/) 对象的 [**PdfSaveOptions.getOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOnePagePerSheet--) 属性。以下是 Node.js 的示例：

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setOnePagePerSheet(true);

// Save the workbook.
workbook.save("OnePagePerSheet.pdf", options);
```

输出结果：
<br>
<img src="3.png" width=60% />

## **如何使用 Aspose.Cells for Node.js via C++ 将工作表所有列打印在一页**

要将工作表所有列打印在一页：首先加载[示例文件](sample.xlsx)，然后你需要设置 [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/) 对象的 [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) 属性。以下是 Node.js 的示例：

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setAllColumnsInOnePagePerSheet(true);

// Save the workbook.
workbook.save("AllColumnsInOnePagePerSheet.pdf", options);
```

输出结果：
<br>
<img src="4.png" width=60% />
