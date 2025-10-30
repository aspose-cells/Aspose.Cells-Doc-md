---
title: C++を経由してGolangでCSV、TSV、TXTをExcelに変換
linktitle: CSV、TSV、TXTをExcelに変換
type: docs
weight: 30
url: /ja/go-cpp/convert-csv-tsv-and-txt-to-excel/
description: Aspose.Cells for C++を使用してCSV、TSV、TXTファイルをExcelに変換する方法を学ぶ
---

{{% alert color="primary" %}}

Aspose.Cells for C++を使えば、CSVファイルをExcel、OpenOffice、PDF、JSON、その他多くの形式に変換できます。

{{% /alert %}}

## **CSV ファイルを開く**

カンマ区切り値（CSV）ファイルは、値がカンマで区切られたレコードを含みます。データは表として保存され、各列はカンマ文字で区切られ、二重引用符で囲まれています。フィールド値に二重引用符が含まれる場合、それは二重引用符のペアでエスケープされます。Microsoft Excelを使用してスプレッドシートデータをCSVにエクスポートすることもできます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel.go" >}}
## **CSVファイルを開き、無効な文字を置換する**

Excelで特殊文字を含むCSVファイルを開くと、文字は自動的に置換されます。Aspose.Cells APIも同様に処理し、以下のコード例で示します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-1.go" >}}
## **推奨パーサーの使用**

CSVファイルを開く際に常にデフォルトのパーサー設定を使用する必要はありません。時には、CSVファイルのインポートが期待した出力を生成しない場合があります。例えば、日付形式が期待通りでない場合や空のフィールドが異なる扱いをされる場合です。このため、**TxtLoadOptions.PreferredParsers**を利用して必要に応じたパーサーを指定できます。以下は推奨パーサーの使用例です。

この機能をテストするために、サンプルのソースファイルと出力ファイルを以下のリンクからダウンロードできます。

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-2.go" >}}
### **カスタム区切り記号を使用してテキストファイルを開く**

テキストファイルは、書式なしでスプレッドシートデータを保持するために使用されます。この種のファイルは、カスタマイズされた区切り記号を持つプレーンテキストファイルです。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-3.go" >}}
### **タブ区切りファイルの開き方**

タブ区切り（テキスト）ファイルはスプレッドシートデータを含みますが、フォーマットはありません。データは表やスプレッドシートのように行と列に配置されます。基本的に、タブ区切りファイルは各列間にタブがあるプレーンテキストファイルの一種です。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-4.go" >}}
### **タブ区切り値（TSV）ファイルを開く**

TSV（タブ区切り値）ファイルはスプレッドシートデータを含みますが、フォーマットはありません。これは、行と列にデータが配置される点で、タブ区切りファイルと同じです。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-5.go" >}}
## **上級トピック**
- [数式を含むCSVファイルのロードまたはインポート](/cells/ja/cpp/load-or-import-csv-file-with-formulas/)
- [複数のエンコーディングを持つCSVファイルの読み込み](/cells/ja/cpp/reading-csv-file-with-multiple-encodings/)
