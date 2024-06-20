---
title: CSV、TSV、TXTをExcelに変換する
type: docs
weight: 50
url: /ja/java/convert-csv-tsv-and-txt-to-excel/
---

## **CSV ファイルを開く**

コンマ区切り値（CSV）ファイルには、値がコンマで区切られ、二重引用符で引用されたレコードが含まれています。 CSVファイルでは、データはコンマ文字で区切られ、二重引用符によって引用されたフィールドで保管されています。フィールドの値に二重引用符文字が含まれている場合は、一対の二重引用符文字でエスケープされます。また、Microsoft Excelを使用して、スプレッドシートのデータをCSVファイルにエクスポートすることもできます。

CSVファイルを開くには、[**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)クラスを使用して、[**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) 列挙体で定義された[**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV)値を選択してください。

## **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **CSV ファイルを開くと無効な文字を置換する**

ExcelでCSVファイルを開くと、特殊文字が自動的に置き換えられます。Aspose.CellsのAPIも同様に、以下のコード例に示されているように自動的に置き換えます。

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

## **優先されるパーサを使用してCSVファイルを開く**

CSVファイルを開く際にはデフォルトのパーサ設定を使用する必要はありません。時々、CSVファイルのインポートが期待通りの出力を作成しないことがあります。たとえば、日付形式が期待通りでない、または空のフィールドが異なる方法で扱われるなどです。そのために、要件に応じて異なるデータ型を解析するための優先されるパーサを提供するために[**TxtLoadOptions.PreferredParsers**](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)が利用できます。以下のサンプルコードは、優先されるパーサの使用方法を示しています。  

この機能をテストするために、サンプルのソースファイルと出力ファイルを以下のリンクからダウンロードできます。

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

## **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **TSV（タブ区切り）ファイルを開く**

タブ区切りファイルには、書式はありませんが、表やスプレッドシートのような行と列でデータが配置されています。要するに、タブ区切りファイルは、各列の間にタブがある通常のテキストファイルの特別な種類です。

タブ区切りファイルを開くには、開発者は[**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)クラスを使用し、[**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV)値を選択し、[**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)列挙型で事前定義する必要があります。

## **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

## **高度なトピック**
- [数式を持つCSVファイルを読み込むまたはインポートする](/cells/ja/java/load-or-import-csv-file-with-formulas/)
- [スプレッドシートをCSV形式にエクスポートする際に先行する空白行と列をトリミングします。](/cells/ja/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)

