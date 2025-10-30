---
title: GolangとC++を使ってExcelをCSV、TSV、Txtに変換
linktitle: CSV、TSV、およびTxtとして保存
type: docs
weight: 40
url: /ja/go-cpp/convert-excel-to-csv-tsv-and-txt/
description: Aspose.Cellsを使い、GolangとC++経由でExcelファイルを簡単にCSV、TSV、TXT形式に変換する。
---

{{% alert color="primary" %}}

Aspose.Cellsは、Excel、ODS、JSONなどのさまざまなフォーマットのファイルをCSV、TSV、TXTに変換できます。

{{% /alert %}}

## **ワークブックをテキストまたはCSV形式で保存**

時々、複数のワークシートを含むワークブックをテキスト形式に変換または保存したい場合があります。テキスト形式（たとえば、TXT、TabDelim、CSVなど）の場合、デフォルトでMicrosoft ExcelおよびAspose.Cellsの両方はアクティブなワークシートの内容のみを保存します。

以下のコード例では、ワークブック全体をテキスト形式で保存する方法について説明しています。任意のMicrosoft ExcelまたはOpenOfficeスプレッドシートファイル（XLS、XLSX、XLSM、XLSB、ODSなど）を読み込み、任意の数のワークシートを含めることができます。

コードを実行すると、ワークブックのすべてのシートのデータがTXT形式に変換されます。

同じ例を修正して、ファイルをCSVに保存することもできます。デフォルトでは、[**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getseparator/)はカンマです。CSV形式に保存する場合は区切り文字を指定しないでください。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveCsvTsvAndTxt.go" >}}
## **カスタム区切り文字でテキストファイルを保存**

テキストファイルには書式がないスプレッドシートデータが含まれます。ファイルは、データ間にいくつかのカスタマイズされた区切り記号があるプレーンテキストファイルの種類です。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveCsvTsvAndTxt-1.go" >}}
## **高度なトピック**
- [CSV形式へのスプレッドシートのエクスポート時に空行の区切り記号を保持する](/cells/ja/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [スプレッドシートをCSV形式にエクスポートする際に先行する空白行と列をトリミングします。](/cells/ja/cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
