---
title: CSV、TSV、TXT を Excel に変換
type: docs
weight: 30
url: /ja/net/convert-csv-tsv-and-txt-to-excel/
---
{{% alert color="primary" %}}

Aspose.Cells を使用すると、CSV ファイルを Excel 、OpenOffice、Pdf、Json、およびさまざまな形式に変換できます。

{{% /alert %}}


## **CSV ファイルを開く**

コンマ区切り値 (CSV) ファイルには、値がコンマで区切られたレコードが含まれています。データは、各列がコンマ文字で区切られ、二重引用符で囲まれたテーブルとして保存されます。フィールド値に二重引用符が含まれている場合は、二重引用符のペアでエスケープされます。 Microsoft Excel を使用して、スプレッドシート データを CSV にエクスポートすることもできます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

## **CSV ファイルを開いて無効な文字を置き換える**

Excel で、特殊文字を含む CSV ファイルを開くと、文字が自動的に置き換えられます。以下のコード例で示されている Aspose.Cells API でも同じことが行われます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

## **優先パーサーの使用**

これは、CSV ファイルを開くためにデフォルトのパーサー設定を使用するために常に必要なわけではありません。 CSV ファイルをインポートしても、日付形式が期待どおりでない、または空のフィールドが異なる方法で処理されるなど、期待される出力が作成されないことがあります。この目的のために**TxtLoadOptions.PreferredParsers**要件に応じてさまざまなデータ型を解析するための独自の優先パーサーを提供することができます。次のサンプル コードは、優先パーサーの使用方法を示しています。

この機能をテストするためのサンプル ソース ファイルと出力ファイルは、次のリンクからダウンロードできます。

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesWithPreferredParser-1.cs" >}}

### **カスタム セパレータを使用してテキスト ファイルを開く**

テキスト ファイルは、書式設定なしでスプレッドシート データを保持するために使用されます。このファイルは、カスタマイズされた区切り文字を持つことができる一種のプレーン テキスト ファイルです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTextFilewithCustomSeparator-1.cs" >}}

### **タブ区切りファイルを開く**

タブ区切り (テキスト) ファイルにはスプレッドシート データが含まれますが、書式設定はありません。データは、表やスプレッドシートのように行と列に配置されます。基本的に、タブ区切りファイルは、各列の間にタブがある特別な種類のプレーン テキスト ファイルです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTabDelimitedFiles-1.cs" >}}

### **タブ区切り値 (TSV) ファイルを開く**

タブ区切り値 (TSV) ファイルにはスプレッドシート データが含まれていますが、書式設定はありません。テーブルやスプレッドシートのように、データが行と列に配置されるタブ区切りファイルと同じです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTSVFiles-1.cs" >}}


## **先行トピック**
- [数式を含む CSV ファイルのロードまたはインポート](/cells/ja/net/load-or-import-csv-file-with-formulas/)
- [複数のエンコーディングを持つ CSV ファイルの読み取り](/cells/ja/net/reading-csv-file-with-multiple-encodings/)

