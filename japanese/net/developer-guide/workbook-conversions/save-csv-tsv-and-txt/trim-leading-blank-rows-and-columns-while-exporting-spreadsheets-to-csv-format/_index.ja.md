---
title: スプレッドシートをCSV形式にエクスポートする際に先行する空白行と列をトリミングします
type: docs
weight: 100
url: /ja/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---

## **可能な使用シナリオ**

ExcelまたはCSVファイルには先行する空白の列または行が含まれている場合があります。 たとえば、この行を考えてみてください

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

ここでは、最初の3つのセルまたは列が空白です。 このようなCSVファイルをMicrosoft Excelで開くと、Microsoft Excelはこれらの先行する空白行と列を破棄します。

デフォルトでは、Aspose.Cellsは先行する空白の列と行を保存時に破棄しませんが、Microsoft Excelと同様にそれらを除去したい場合は、Aspose.Cellsが[**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)を提供します。 それを**true**に設定すると、すべての先行する空白行と列が保存時に破棄されます。

{{% alert color="primary" %}}

Aspose.Cells for .NET 20.4のリリース前は、[**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)のデフォルト値は**false**でした。 20.4リリース以降、[**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)のデフォルト値は**true**です。

{{% /alert %}}

## **スプレッドシートをCSV形式にエクスポートする際に先行する空白行と列をトリミングします。**

[ソースExcelファイル](sampleTrimBlankColumns.xlsx)をロードします。先に変更せずにExcelファイルをCSV形式で保存し、その後[**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn)プロパティを**true**に設定して再度保存します。スクリーンショットには、[ソースExcelファイル](sampleTrimBlankColumns.xlsx)、トリミングを行わない[出力CSVファイル](outputWithoutTrimBlankColumns.csv)、およびトリミングを行った[出力CSVファイル](outputTrimBlankColumns.csv)が含まれています。

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCSVFormat.cs" >}}
{{< app/cells/assistant language="csharp" >}}
