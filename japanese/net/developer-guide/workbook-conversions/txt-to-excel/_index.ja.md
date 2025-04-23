---
title: CSV、TSV、TXTをExcelに変換する
type: docs
weight: 30
url: /ja/net/convert-csv-tsv-and-txt-to-excel/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用して、CSVファイルをExcel、OpenOffice、Pdf、Jsonなど多くの異なる形式に変換することができます。

{{% /alert %}}


## **CSV ファイルを開く**

コンマ区切り値（CSV）ファイルには、値がコンマで区切られたレコードが含まれています。データは、各列がコンマ文字で区切られ、二重引用符で引用された表として保存されます。フィールド値に二重引用符文字が含まれる場合は、それを二重引用符文字のペアでエスケープします。Microsoft Excel を使用してスプレッドシートデータを CSV にエクスポートすることもできます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

## **CSV ファイルを開くと無効な文字を置換する**

Excel では、特殊文字が含まれる CSV ファイルを開くと、文字が自動的に置換されます。Aspose.Cells API でも同様に行います。これは以下のコード例で示されています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

## **好みのパーサーの使用**

CSVファイルを開くためにデフォルトのパーサー設定を使用する必要があるわけではないことがあります。場合によっては、CSVファイルをインポートしても日付形式が期待通りでない、または空のフィールドが異なる方法で処理されることがあります。そのために、**TxtLoadOptions.PreferredParsers**は、異なるデータ型を要件に応じて解析するために独自の好みのパーサーを提供するために利用できます。以下のサンプルコードは、好みのパーサーの使用法を示しています。  

この機能をテストするために、サンプルのソースファイルと出力ファイルを以下のリンクからダウンロードできます。

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesWithPreferredParser-1.cs" >}}

### **カスタム区切り記号を使用してテキストファイルを開く**

テキストファイルは、書式なしでスプレッドシートデータを保持するために使用されます。この種のファイルは、カスタマイズされた区切り記号を持つプレーンテキストファイルです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTextFilewithCustomSeparator-1.cs" >}}

### **タブ区切りファイルを開く**

タブ区切り（テキスト）ファイルには、スプレッドシートデータが含まれていますが、フォーマットはありません。データは表やスプレッドシートのように行と列で配置されています。基本的に、タブ区切りファイルは各列の間にタブがある特別な種類のプレーンテキストファイルです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTabDelimitedFiles-1.cs" >}}

### **タブ区切り値（TSV）ファイルを開く**

タブ区切り値（TSV）ファイルには、スプレッドシートデータが含まれていますが、フォーマットはありません。データは表やスプレッドシートのように行と列で配置されています。データはタブ区切りファイルと同様であり、各列の間にタブがあります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTSVFiles-1.cs" >}}


## **高度なトピック**
- [数式を持つCSVファイルを読み込むまたはインポートする](/cells/ja/net/load-or-import-csv-file-with-formulas/)
- [複数のエンコーディングを持つCSVファイルの読み込み](/cells/ja/net/reading-csv-file-with-multiple-encodings/)

{{< app/cells/assistant language="csharp" >}}
