---
title: 避免在输出PDF中生成空白页，使用Node.js via C++
linktitle: 避免输出PDF中的空白页在没有内容打印时
type: docs
weight: 30
url: /zh/nodejs-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: 学习如何在没有内容输出时避免输出PDF中的空白页，使用Aspose.Cells for Node.js via C++。
---

## **可能的使用场景**

当Excel文件为空且用户使用Aspose.Cells for Node.js via C++保存为PDF时，输出的PDF会显示空白页。有时这种默认行为是不希望的。Aspose.Cells提供了 [**PdfSaveOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOutputBlankPageWhenNothingToPrint--) 属性来处理此问题。如果将其设置为 **false**，则在没有内容打印时，将引发异常。

## **当没有需要打印的内容时，避免在输出PDF中出现空白页**

以下示例代码创建一个空工作簿，然后将其保存为PDF，并将[**PdfSaveOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOutputBlankPageWhenNothingToPrint--)属性设置为**false**。由于输出的PDF中没有任何内容可打印，因此会发生如下所示的异常。

## **示例代码**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Create Pdf save options.
const opts = new AsposeCells.PdfSaveOptions();

// Default value of OutputBlankPageWhenNothingToPrint is true.
// Setting false means - Do not output blank page when there is nothing to print.
opts.setOutputBlankPageWhenNothingToPrint(false);

// Save workbook to Pdf format, it will throw exception because workbook has nothing to print.
const ms = new Uint8Array();

try {
// Save to Pdf format. It will throw exception.
wb.save(ms, opts);
} catch (ex) {
console.error("Exception Message: " + ex.message + "\r\n");
}
```

## **异常**

{{< highlight javascript >}}

 exception was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
