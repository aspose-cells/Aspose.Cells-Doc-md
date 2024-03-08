---
title: Excel を CSV,TSV および Txt に変換
linktitle: CSV,TSV および Txt として保存
type: docs
weight: 40
url: /ja/python-net/convert-excel-to-csv-tsv-and-txt/
description: Aspose.Cells for Python via .NET API を使用して、Excel を CSV、TSV および Txt に変換します。
keywords: Python Convert Excel to CSV,TSV and Txt, Convert Excel to CSV,TSV and Txt in Python via NET, Python Convert Workbook to CSV,TSV and Txt.
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET を使用すると、excel、ods、json などの形式のファイルを CSV、TSV、TXT に変換できます。

{{% /alert %}}

##  **ワークブックをテキストまたは CSV 形式で保存する**

場合によっては、複数のワークシートを含むワークブックをテキスト形式に変換または保存したい場合があります。テキスト形式 (TXT、TabDelim、CSV など) の場合、デフォルトでは、Microsoft Excel と Aspose.Cells for Python via .NET の両方がアクティブなワークシートの内容のみを保存します。

次のコード例は、ブック全体をテキスト形式で保存する方法を説明します。任意の数のワークシートを含むソース ワークブック (Microsoft Excel または OpenOffice スプレッドシート ファイル (つまり、XLS、XLSX、XLSM、XLSB、ODS など)) を読み込みます。

コードが実行されると、ブック内のすべてのシートのデータが TXT 形式に変換されます。

同じ例を変更して、ファイルを CSV に保存できます。デフォルトでは、**[TxtSaveOptions.separator](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator/)**はカンマなので、CSV 形式で保存する場合は区切り文字を指定しないでください。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SaveWorkbookToTextCSVFormat-1.py" >}}

##  **カスタムセパレータを使用してテキストファイルを保存する**

テキスト ファイルには、書式設定されていないスプレッドシート データが含まれています。このファイルは、データ間にカスタマイズされた区切り文字を含めることができる一種のプレーン テキスト ファイルです。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SavingTextFilewithCustomSeparator-1.py" >}}


##  **アドバンストトピック**
- [スプレッドシートを CSV 形式にエクスポートする際に空白行の区切り文字を維持する](/cells/ja/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [スプレッドシートを CSV 形式にエクスポートする際に、先頭の空白の行と列をトリミングする](/cells/ja/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
