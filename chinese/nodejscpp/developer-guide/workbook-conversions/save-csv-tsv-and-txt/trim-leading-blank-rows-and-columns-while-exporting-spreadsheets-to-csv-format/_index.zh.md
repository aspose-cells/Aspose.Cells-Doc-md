---
title: 在导出电子表格到 CSV 格式时修剪前导空白行和列，使用 Node.js 和 C++
linktitle: 导出电子表格到CSV格式时修剪前导空白行和列
type: docs
weight: 100
url: /zh/nodejs-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: 学习如何在使用 Aspose.Cells for Node.js via C++ 导出 CSV 格式时修剪前导空白行和列。
---

## **可能的使用场景**

有时，您的Excel或CSV文件具有前导空白列或行。例如，考虑这条线

{{< highlight javascript >}}

 ,,,data1,data2

{{< /highlight >}}

这里的前三个单元格或列是空白的。当您在Microsoft Excel中打开这样的CSV文件时，Microsoft Excel会丢弃这些前导空白行和列。

默认情况下，Aspose.Cells for Node.js via C++ 在保存时不会删除前导空白行和列，但如果你想像 Microsoft Excel 那样将它们删除，Aspose.Cells 提供 [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) 属性。请将其设置为 **true**，保存时所有前导空白行和列都将被删除。

{{% alert color="primary" %}}

在 Aspose.Cells for Node.js via C++ 20.4 版本发布之前，[**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) 的默认值是 **false**。自 20.4 版本起，[**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) 的默认值变为 **true**。

{{% /alert %}}

## **导出电子表格到CSV格式时修剪前导空白行和列**

以下示例代码加载了具有两个前导空白列的[源 Excel 文件]（sampleTrimBlankColumns.xlsx）。它首先不做任何更改地将 Excel 文件保存为 CSV 格式，然后将 [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) 属性设置为 **true**，再次保存。屏幕截图显示[源 Excel 文件]（sampleTrimBlankColumns.xlsx）、[不修剪空白列的输出 CSV 文件]（outputWithoutTrimBlankColumns.csv）以及[修剪空白列的输出 CSV 文件]（outputTrimBlankColumns.csv）。

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load source workbook
const wb = new AsposeCells.Workbook(path.join(dataDir, "sampleTrimBlankColumns.xlsx"));

// Save in csv format
wb.save(path.join(dataDir, "outputWithoutTrimBlankColumns.csv"), AsposeCells.SaveFormat.Csv);

// Now save again with TrimLeadingBlankRowAndColumn as true
const opts = new AsposeCells.TxtSaveOptions();
opts.setTrimLeadingBlankRowAndColumn(true);

// Save in csv format
wb.save(path.join(dataDir, "outputTrimBlankColumns.csv"), opts);
```
