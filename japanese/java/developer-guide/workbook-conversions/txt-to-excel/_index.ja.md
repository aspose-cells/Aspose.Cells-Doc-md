---
title: CSV、TSV、TXT を Excel に変換
type: docs
weight: 50
url: /ja/java/convert-csv-tsv-and-txt-to-excel/
---
## **CSV ファイルを開く**

コンマ区切り値 (CSV) ファイルには、値がコンマで区切られているか、区切られているレコードが含まれています。 CSV ファイルでは、データは、フィールドがコンマ文字で区切られ、二重引用符で囲まれた表形式で保存されます。フィールドの値に二重引用符が含まれている場合は、二重引用符のペアでエスケープされます。 Microsoft Excel を使用して、スプレッドシート データを CSV ファイルにエクスポートすることもできます。

CSV ファイルを開くには、**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**クラスを選択し、**[CSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV)**で定義済みの値**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**列挙。

## **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **CSV ファイルを開いて無効な文字を置き換える**

Excel で、特殊文字を含む CSV ファイルを開くと、文字が自動的に置き換えられます。以下のコード例で示されている Aspose.Cells API でも同じことが行われます。

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

## **優先パーサーを使用して CSV ファイルを開く**

これは、CSV ファイルを開くためにデフォルトのパーサー設定を使用するために常に必要なわけではありません。 CSV ファイルをインポートしても、日付形式が期待どおりでない、または空のフィールドが異なる方法で処理されるなど、期待される出力が作成されないことがあります。この目的のために**[TxtLoadOptions.PreferredParsers](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)**要件に応じてさまざまなデータ型を解析するための独自の優先パーサーを提供することができます。次のサンプル コードは、優先パーサーの使用方法を示しています。

この機能をテストするためのサンプル ソース ファイルと出力ファイルは、次のリンクからダウンロードできます。

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

## **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **TSV(タブ区切り)ファイルを開く**

タブ区切りファイルにはスプレッドシート データが含まれますが、書式はありません。データは、テーブルやスプレッドシートなどの行と列に配置されます。簡単に言うと、タブ区切りファイルは、テキストの各列の間にタブがある特別な種類のプレーン テキスト ファイルです。

タブ区切りファイルを開くには、開発者は**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**クラスを選択し、**[TSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV)**で定義済みの値**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**列挙。

## **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

## **先行トピック**
- [数式を含む CSV ファイルのロードまたはインポート](/cells/ja/java/load-or-import-csv-file-with-formulas/)
- [スプレッドシートを CSV 形式にエクスポートする際に、先頭の空白の行と列をトリミングする](/cells/ja/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)

