---
title: ExcelをCSV、TSV、およびTxtに変換する
linktitle: CSV、TSV、およびTxtとして保存
type: docs
weight: 40
url: /ja/net/convert-excel-to-csv-tsv-and-txt/
---

{{% alert color="primary" %}}

Aspose.CellsでExcel、ods、jsonなどの形式ファイルをCSV、TSV、TXTに変換することが可能になります。

{{% /alert %}}

## **ワークブックをテキストまたはCSV形式で保存**

時々、複数のワークシートを含むワークブックをテキスト形式に変換または保存したい場合があります。テキスト形式（たとえば、TXT、TabDelim、CSVなど）の場合、デフォルトでMicrosoft ExcelおよびAspose.Cellsの両方はアクティブなワークシートの内容のみを保存します。

以下のコード例では、ワークブック全体をテキスト形式で保存する方法について説明しています。任意のMicrosoft ExcelまたはOpenOfficeスプレッドシートファイル（XLS、XLSX、XLSM、XLSB、ODSなど）を読み込み、任意の数のワークシートを含めることができます。

コードを実行すると、ワークブックのすべてのシートのデータがTXT形式に変換されます。

同じ例を修正してファイルをCSV形式で保存することもできます。デフォルトでは、[**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)はコンマなので、CSV形式に保存する場合は区切り文字を指定しないでください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **カスタム区切り文字でテキストファイルを保存**

テキストファイルには書式がないスプレッドシートデータが含まれます。ファイルは、データ間にいくつかのカスタマイズされた区切り記号があるプレーンテキストファイルの種類です。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}


## **高度なトピック**
- [CSV形式へのスプレッドシートのエクスポート時に空行の区切り記号を保持する](/cells/ja/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [スプレッドシートをCSV形式にエクスポートする際に先行する空白行と列をトリミングします。](/cells/ja/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
