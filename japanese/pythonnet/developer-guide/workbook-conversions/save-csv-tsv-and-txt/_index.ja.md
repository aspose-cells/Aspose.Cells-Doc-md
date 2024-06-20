---
title: ExcelをCSV、TSV、およびTxtに変換する
linktitle: CSV、TSV、およびTxtとして保存
type: docs
weight: 40
url: /ja/python-net/convert-excel-to-csv-tsv-and-txt/
description: Aspose.Cells for Python via .NET APIを使用してExcelをCSV、TSV、Txtに変換する方法を学ぶ。
keywords: PythonでExcelをCSV、TSV、およびTxtに変換する, PythonでExcelをCSV、TSV、およびTxtに変換する via NET, PythonでワークブックをCSV、TSV、およびTxtに変換する。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NETを使用して、Excel、ods、jsonなどのファイルをCSV、TSV、およびTXTに変換できます。

{{% /alert %}}

## **ワークブックをテキストまたはCSV形式で保存**

時には、複数のワークシートが含まれたワークブックをテキスト形式に変換または保存したいと思うことがあります。テキスト形式（たとえば、TXT、TabDelim、CSVなど）の場合、デフォルトでは、Microsoft ExcelとAspose.Cells for Python via .NETの両方がアクティブなワークシートの内容のみを保存します。

以下のコード例では、ワークブック全体をテキスト形式で保存する方法について説明しています。任意のMicrosoft ExcelまたはOpenOfficeスプレッドシートファイル（XLS、XLSX、XLSM、XLSB、ODSなど）を読み込み、任意の数のワークシートを含めることができます。

コードを実行すると、ワークブックのすべてのシートのデータがTXT形式に変換されます。

同じ例を修正してファイルをCSV形式で保存することもできます。デフォルトでは、[**TxtSaveOptions.separator**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator/)はコンマなので、CSV形式に保存する場合は区切り文字を指定しないでください。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SaveWorkbookToTextCSVFormat-1.py" >}}

## **カスタム区切り文字でテキストファイルを保存**

テキストファイルには書式がないスプレッドシートデータが含まれます。ファイルは、データ間にいくつかのカスタマイズされた区切り記号があるプレーンテキストファイルの種類です。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SavingTextFilewithCustomSeparator-1.py" >}}


## **高度なトピック**
- [CSV形式へのスプレッドシートのエクスポート時に空行の区切り記号を保持する](/cells/ja/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [スプレッドシートをCSV形式にエクスポートする際に先行する空白行と列をトリミングします。](/cells/ja/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
