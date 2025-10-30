---
title: スプレッドシートをCSV形式にエクスポートする際に先行する空白行と列をトリミングします
type: docs
weight: 100
url: /ja/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Aspose.Cells for Python via .NET APIを使用して、スプレッドシートをCSV形式にエクスポートする際に先頭の空白行と列をトリムする方法。
keywords: PythonでスプレッドシートをCSV形式にエクスポートする際に、先頭の空行と列をトリミングする、PythonでExcelをCSV形式にエクスポートする際に先頭の空行と列をトリミングするvia NET、ExcelをCSV形式にエクスポートする際に、先頭の空行と列をトリミングする。
---

## **可能な使用シナリオ**

ExcelまたはCSVファイルには先行する空白の列または行が含まれている場合があります。 たとえば、この行を考えてみてください

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

ここでは、最初の3つのセルまたは列が空白です。 このようなCSVファイルをMicrosoft Excelで開くと、Microsoft Excelはこれらの先行する空白行と列を破棄します。

デフォルトでは、Aspose.Cells for Python via .NETは保存時に先頭の空白行と列を削除しませんが、Microsoft Excelのようにそれらを削除したい場合は、[**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)プロパティを提供します。**true**に設定すると、すべての先頭の空白行と列が削除されます。

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET 20.4リリースより前は、[**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)のデフォルト値は**false**でした。20.4リリース以降、[**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)のデフォルト値は**true**です。

{{% /alert %}}

## **スプレッドシートをCSV形式にエクスポートする際に先行する空白行と列をトリミングします。**

[ソースExcelファイル](sampleTrimBlankColumns.xlsx)をロードします。先に変更せずにExcelファイルをCSV形式で保存し、その後[**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)プロパティを**true**に設定して再度保存します。スクリーンショットには、[ソースExcelファイル](sampleTrimBlankColumns.xlsx)、トリミングを行わない[出力CSVファイル](outputWithoutTrimBlankColumns.csv)、およびトリミングを行った[出力CSVファイル](outputTrimBlankColumns.csv)が含まれています。

![todo:image_alt_text](result.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-TrimLeadingBlankRowsAndColumns.py" >}}
{{< app/cells/assistant language="python-net" >}}
