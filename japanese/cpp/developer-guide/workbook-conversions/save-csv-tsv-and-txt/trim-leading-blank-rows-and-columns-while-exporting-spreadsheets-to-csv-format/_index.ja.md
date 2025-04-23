---
title: C++を使用してスプレッドシートをCSV形式にエクスポートする際に先頭の空白行と列をトリム
linktitle: 先頭の空白行と列のトリム
type: docs
weight: 100
url: /ja/cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Aspose.Cells for C++を使用してスプレッドシートをCSVにエクスポートする際に先頭の空白行と列をトリムする方法を学びます。
---

## **可能な使用シナリオ**

時には、ExcelやCSVファイルの先頭に空白行や列が存在します。例えば、この行を考えてみてください：

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

ここでは、最初の3つのセルまたは列が空白です。 このようなCSVファイルをMicrosoft Excelで開くと、Microsoft Excelはこれらの先行する空白行と列を破棄します。

デフォルトでは、Aspose.Cellsは先行する空白の列と行を保存時に破棄しませんが、Microsoft Excelと同様にそれらを除去したい場合は、Aspose.Cellsが[**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/)を提供します。 それを**true**に設定すると、すべての先行する空白行と列が保存時に破棄されます。

{{% alert color="primary" %}}

Aspose.Cells for C++ 20.4リリース以前は、[**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/)のデフォルト値は**false**でした。20.4リリース以降は、[**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/)のデフォルト値は**true**です。

{{% /alert %}}

## **スプレッドシートをCSV形式にエクスポートする際に先行する空白行と列をトリミングします。**

[ソースExcelファイル](sampleTrimBlankColumns.xlsx)をロードします。先に変更せずにExcelファイルをCSV形式で保存し、その後[**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/)プロパティを**true**に設定して再度保存します。スクリーンショットには、[ソースExcelファイル](sampleTrimBlankColumns.xlsx)、トリミングを行わない[出力CSVファイル](outputWithoutTrimBlankColumns.csv)、およびトリミングを行った[出力CSVファイル](outputTrimBlankColumns.csv)が含まれています。

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **サンプルコード**

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
