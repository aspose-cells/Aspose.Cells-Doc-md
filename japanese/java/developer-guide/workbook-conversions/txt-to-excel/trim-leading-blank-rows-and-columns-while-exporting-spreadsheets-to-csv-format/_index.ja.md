---
title: スプレッドシートをCSV形式にエクスポートする際に先行する空白行と列をトリミングします
type: docs
weight: 50
url: /ja/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---

## **可能な使用シナリオ**

ExcelまたはCSVファイルには先行する空白の列または行が含まれている場合があります。 たとえば、この行を考えてみてください

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

ここでは、最初の3つのセルまたは列が空白です。 このようなCSVファイルをMicrosoft Excelで開くと、Microsoft Excelはこれらの先行する空白行と列を破棄します。

デフォルトでは、Aspose.Cellsは先行する空白の列と行を保存時に破棄しませんが、Microsoft Excelと同様にそれらを除去したい場合は、Aspose.Cellsが[**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)を提供します。 それを**true**に設定すると、すべての先行する空白行と列が保存時に破棄されます。

{{% alert color="primary" %}}

Aspose.Cells for .NET 20.4のリリース前は、[**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)のデフォルト値は**false**でした。 20.4リリース以降、[**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)のデフォルト値は**true**です。

{{% /alert %}}

## **スプレッドシートをCSV形式にエクスポートする際に先行する空白行と列をトリミングします。**

以下のサンプルコードは、2つの先行する空白の列を含むソースExcelファイルをロードし、まず何も変更せずにCSV形式で保存し、次に[**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)を**true**に設定して再保存します。 スクリーンショットには、[source excel file](sampleTrimBlankColumns.xlsx)、トリミングなしの[output CSV file without trimming](outputWithoutTrimBlankColumns.csv)、およびトリミングされた[output CSV file with trimming](outputTrimBlankColumns.csv)が表示されています。

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVFormat-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVForm.Java" >}}
{{< app/cells/assistant language="java" >}}
