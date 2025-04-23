---
title: 在导出电子表格为CSV格式时修剪前导空白行与列（C++）
linktitle: 修剪前导空白行与列
type: docs
weight: 100
url: /zh/cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: 学习如何在导出电子表格到CSV格式时修剪前导空白行和列，使用Aspose.Cells for C++。
---

## **可能的使用场景**

有时候，你的Excel或CSV文件中会有前导空白列或行。例如，考虑以下行：

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

这里的前三个单元格或列是空白的。当您在Microsoft Excel中打开这样的CSV文件时，Microsoft Excel会丢弃这些前导空白行和列。

默认情况下，Aspose.Cells 在保存时不会丢弃前导空白列和行，但如果您希望像 Microsoft Excel 一样移除它们，Aspose.Cells 提供了 [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/) 属性。请将其设置为 **true**，然后在保存时所有前导空白行和列将被丢弃。

{{% alert color="primary" %}}

在 Aspose.Cells for C++ 20.4 版本发布之前，[**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/) 的默认值是 **false**。自20.4版本起，[**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/) 的默认值是 **true**。

{{% /alert %}}

## **导出电子表格到CSV格式时修剪前导空白行和列**

以下示例代码加载了具有两个前导空白列的 [源 Excel 文件](sampleTrimBlankColumns.xlsx)。首先保存 Excel 文件为 CSV 格式而不进行任何更改，然后将 [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/) 属性设置为 **true** 并再次保存。截图显示了 [源 Excel 文件](sampleTrimBlankColumns.xlsx)，[未修剪的输出 CSV 文件](outputWithoutTrimBlankColumns.csv) 和 [修剪后的输出 CSV 文件](outputTrimBlankColumns.csv)。

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleTrimBlankColumns.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Save in csv format without trimming blank columns
    wb.Save(outDir + u"outputWithoutTrimBlankColumns.csv", SaveFormat::Csv);

    // Create TxtSaveOptions and set TrimLeadingBlankRowAndColumn to true
    TxtSaveOptions opts;
    opts.SetTrimLeadingBlankRowAndColumn(true);

    // Save in csv format with trimming blank columns
    wb.Save(outDir + u"outputTrimBlankColumns.csv", opts);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
