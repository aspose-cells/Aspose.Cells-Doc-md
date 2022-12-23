---
title: スプレッドシートを CSV 形式にエクスポートする際に、先頭の空白の行と列をトリミングする
type: docs
weight: 50
url: /ja/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---
## **考えられる使用シナリオ**

Excel または CSV ファイルの先頭に空白の列または行がある場合があります。たとえば、この行を考えてみましょう

{{< highlight "java" >}}

 ,,,data1,data2

{{< /highlight >}}

ここでは、最初の 3 つのセルまたは列が空白です。このような CSV ファイルを Microsoft Excel で開くと、Microsoft Excel はこれらの先頭の空白行と列を破棄します。

デフォルトでは、Aspose.Cells は保存時に先頭の空白の列と行を破棄しませんが、Microsoft Excel のようにそれらを削除したい場合は、Aspose.Cells が提供します**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)**財産。に設定してください**真実**保存時に先頭の空白の行と列はすべて破棄されます。

{{% alert color="primary" %}}

 Aspose.Cells for .NET 20.4 のリリース前は、デフォルト値の**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)**だった**間違い** 20.4 リリース以降、デフォルト値の**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)**は**真実。**

{{% /alert %}}

## **スプレッドシートを CSV 形式にエクスポートする際に、先頭の空白の行と列をトリミングする**

次のサンプル コードは、先頭に 2 つの空白列があるソース Excel ファイルを読み込みます。最初にExcelファイルを変更せずにCSV形式で保存してから設定します**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)**プロパティへ**真実**再度保存します。スクリーンショットは、[ソースエクセルファイル](sampleTrimBlankColumns.xlsx), [トリミングなしで CSV ファイルを出力](outputWithoutTrimBlankColumns.csv)、 そしてその[CSV ファイルをトリミングして出力](outputTrimBlankColumns.csv).

![todo:画像_代替_文章](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVFormat-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVForm.Java" >}}
