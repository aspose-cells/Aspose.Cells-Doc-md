---
title: 使用 Node.js 和 C++ 判断工作表的纸张大小是否自动
linktitle: 确定工作表的纸张尺寸是否为自动
type: docs
weight: 90
url: /zh/nodejs-cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: 本文介绍如何借助 Node.js API 和 C++ 扩展，编程判断工作表的纸张大小是否设置为自动。
keywords: 用 Node.js 和 C++ 判断工作表的纸张大小是否自动
---

## **可能的使用场景**

大多时候，工作表的纸张大小是自动的。当设置为自动时，通常为*Letter*。有时用户会根据需求设置工作表的纸张大小。在这种情况下，纸张大小不是自动的。你可以利用 [**Worksheet.isAutomaticPaperSize()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isAutomaticPaperSize--) 属性判断工作表的纸张大小是否为自动。

## **确定工作表的纸张大小是否自动**

以下给出的示例代码加载以下两个Excel文件

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

并找到它们的第一个工作表的纸张尺寸是否为自动。在Microsoft Excel中，您可以通过页面设置窗口（如截图所示）检查纸张尺寸是否是自动的。

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const wb1 = new AsposeCells.Workbook(path.join(dataDir, "samplePageSetupIsAutomaticPaperSize-False.xlsx"));
const wb2 = new AsposeCells.Workbook(path.join(dataDir, "samplePageSetupIsAutomaticPaperSize-True.xlsx"));

// Access first worksheet of both workbooks
const ws11 = wb1.getWorksheets().get(0);
const ws12 = wb2.getWorksheets().get(0);

// Print the PageSetup.IsAutomaticPaperSize property of both worksheets
console.log("First Worksheet of First Workbook - IsAutomaticPaperSize: " + ws11.getPageSetup().isAutomaticPaperSize());
console.log("First Worksheet of Second Workbook - IsAutomaticPaperSize: " + ws12.getPageSetup().isAutomaticPaperSize());
```

## **控制台输出**

以下是上述示例代码在给定的示例Excel文件上执行时的控制台输出。

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
