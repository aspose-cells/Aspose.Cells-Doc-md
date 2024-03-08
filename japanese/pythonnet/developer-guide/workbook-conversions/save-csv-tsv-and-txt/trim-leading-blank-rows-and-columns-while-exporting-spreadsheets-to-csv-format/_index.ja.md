---
title: スプレッドシートを CSV 形式にエクスポートする際に、先頭の空白の行と列をトリミングする
type: docs
weight: 100
url: /ja/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Aspose.Cells for Python via .NET API を使用して、スプレッドシートを CSV 形式にエクスポートするときに、先頭の空白の行と列をトリミングします。
keywords: Python Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format, Trim Leading Blank Rows and Columns while saving excel to CSV format in Python via NET, Python Trim Leading Blank Rows and Columns exporting excel to CSV format.
---
##  **考えられる使用シナリオ**

Excel または CSV ファイルの先頭に空白の列または行がある場合があります。たとえば、次の行を考えてみましょう

{{< highlight "java" >}}

 ,,,data1,data2

{{< /highlight >}}

ここでは、最初の 3 つのセルまたは列は空白です。このような CSV ファイルを Microsoft Excel で開くと、Microsoft Excel はこれらの先頭の空白の行と列を破棄します。

デフォルトでは、Aspose.Cells for Python via .NET は保存時に先頭の空白の列と行を破棄しませんが、Microsoft Excel と同じようにそれらを削除したい場合は、Aspose.Cells for Python via .NET が提供します。**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)**財産。に設定してください**真実**その後、先頭の空白の行と列は保存時にすべて破棄されます。

{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET 20.4 のリリースより前は、デフォルト値は**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)**だった**間違い**。 20.4 リリース以降、**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) のデフォルト値が使用されています。**は**真実。**

{{% /alert %}}

##  **スプレッドシートを CSV 形式にエクスポートする際に、先頭の空白の行と列をトリミングする**

次のサンプルコードは、[ソースエクセルファイル](sampleTrimBlankColumns.xlsx)先頭に 2 つの空白列があります。まず Excel ファイルを変更せずに CSV 形式で保存し、次に設定します。**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)**財産を**真実**そして再度保存します。スクリーンショットは、[ソースエクセルファイル](sampleTrimBlankColumns.xlsx), [CSV ファイルをトリミングせずに出力します](outputWithoutTrimBlankColumns.csv)、 そしてその[CSV ファイルをトリミングして出力](outputTrimBlankColumns.csv).

![todo:image_alt_text](result.png)

##  **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-TrimLeadingBlankRowsAndColumns.py" >}}
