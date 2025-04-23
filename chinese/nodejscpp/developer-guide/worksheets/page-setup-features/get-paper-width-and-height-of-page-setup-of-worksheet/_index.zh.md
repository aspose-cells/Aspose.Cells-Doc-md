---
title: 用 Node.js 和 C++ 获取工作表页面设置的纸张宽度和高度
linktitle: 获取工作表页面设置的纸张宽度和高度
type: docs
weight: 50
url: /zh/nodejs-cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: 探索如何通过 Node.js 和 C++ 程序编程获取 Excel 工作表页面设置的纸张宽度和高度。
keywords: 用节点.js 和 C++ 获取 Excel 页面设置的纸张宽度和高度
---

## **可能的使用场景**

有时，你需要知道工作表页面设置中的纸张宽度和高度。请使用 [**PageSetup.getPaperWidth()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperWidth--) 和 [**PageSetup.getPaperHeight()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperHeight--) 属性实现此目的。

## **获取工作表页面设置的纸张宽度和高度**

以下示例代码说明如何使用 [**PageSetup.getPaperWidth()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperWidth--) 和 [**PageSetup.getPaperHeight()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperHeight--) 属性。它首先将纸张大小更改为 *A2*，然后找到纸张的宽度和高度，再依次更改为 *A3*，*A4*，*Letter*，并找到对应的宽度和高度。

### **示例代码**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create an instance of Workbook class
const book = new AsposeCells.Workbook();

// Access first worksheet
const sheet = book.getWorksheets().get(0);

// Set paper size to A2 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA2);
console.log("PaperA2: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to A3 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA3);
console.log("PaperA3: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to A4 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);
console.log("PaperA4: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to Letter and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperLetter);
console.log("PaperLetter: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());
```

### **控制台输出**

这是上面示例代码的控制台输出。

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
