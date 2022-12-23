---
title: Excel を CSV,TSV および Txt に変換します
linktitle: CSV,TSV および Txt として保存
type: docs
weight: 40
url: /ja/net/convert-excel-to-csv-tsv-and-txt/
---
{{% alert color="primary" %}}

Aspose.Cells は、Excel、ods、json およびその他の形式のファイルを CSV、TSV、および TXT に変換することを可能にします。

{{% /alert %}}

## **ワークブックをテキストまたは CSV 形式で保存する**

場合によっては、複数のワークシートを含むワークブックをテキスト形式に変換または保存する必要があります。テキスト形式 (例: TXT、TabDelim、CSV など) の場合、既定では、Microsoft Excel と Aspose.Cells の両方で、アクティブなワークシートの内容のみが保存されます。

次のコード例は、ブック全体をテキスト形式で保存する方法を示しています。 Microsoft Excel または OpenOffice スプレッドシート ファイル (XLS、XLSX、XLSM、XLSB、ODS など) のソース ワークブックを任意の数のワークシートと共に読み込みます。

コードが実行されると、ブック内のすべてのシートのデータが TXT 形式に変換されます。

同じ例を変更して、ファイルを CSV に保存できます。デフォルトでは、**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**はコンマなので、CSV 形式で保存する場合はセパレータを指定しないでください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **カスタム セパレータを使用したテキスト ファイルの保存**

テキスト ファイルには、書式設定されていないスプレッドシート データが含まれています。このファイルは、データ間にカスタマイズされた区切り文字を含めることができる一種のプレーン テキスト ファイルです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}


## **先行トピック**
- [スプレッドシートを CSV 形式にエクスポートする際に、空白行の区切り記号を保持する](/cells/ja/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [スプレッドシートを CSV 形式にエクスポートする際に、先頭の空白の行と列をトリミングする](/cells/ja/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
