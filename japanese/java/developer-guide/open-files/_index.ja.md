---
title: 異なる形式のファイルを開く
linktitle: ファイルを開く
type: docs
weight: 10
url: /ja/java/opening-files-with-different-formats/
---
{{% alert color="primary" %}}

開発者は Aspose.Cells を使用して、さまざまな目的でファイルを開きます。たとえば、ファイルを開いてそこからデータを取得したり、定義済みのデザイナー スプレッドシート ファイルを使用して開発プロセスをスピードアップしたりできます。 Aspose.Cells を使用すると、開発者はさまざまな種類のソース ファイルを開くことができます。これらのソース ファイルは、Microsoft Excel レポート、SpreadsheetML、カンマ区切り値 (CSV)、タブ区切りまたはタブ区切り値 (TSV) ファイルです。この記事では、Aspose.Cells を使用してこれらの異なるソース ファイルを開く方法について説明します。

サポートされているすべてのファイル形式を知る必要がある場合は、次のページを参照してください。
[サポートされているファイル形式](https://docs.aspose.com/cells/java/supported-file-formats/)

{{% /alert %}}

## **Excel ファイルを開く簡単な方法**

### **パスを介して開く**

ファイル パスを使用して Microsoft Excel ファイルを開くには、インスタンスの作成中にファイルのパスをパラメーターとして渡します。**[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**クラス。次のサンプル コードは、ファイル パスを使用して Excel ファイルを開く方法を示しています。

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughPath-OpeningFilesThroughPath.java" >}}

### **ストリームを介して開く**

開こうとしている Excel ファイルがストリームとして保存されている場合があります。その場合、ファイル パスを使用してファイルを開くのと同様に、インスタンス化中にストリームをパラメータとして渡します。**[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**クラス。次のサンプル コードは、ストリームを使用して Excel ファイルを開く方法を示しています。

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughStream-OpeningFilesThroughStream.java" >}}

### **異なる Microsoft Excel バージョンのファイルを開く**

ユーザーは**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**クラスを使用して、Excel ファイルの形式を指定します。**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**列挙。

の**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**列挙には、事前に定義された多くのファイル形式が含まれており、その一部を以下に示します。

|**フォーマットの種類**|**説明**|
|:- |:- |
|CSV|CSV ファイルを表します|
|Excel97To2003|Excel 97 - 2003 ファイルを表します|
|xlsx|Excel 2007/2010/2013/2016/2019 および Office 365 XLSX ファイルを表します|
|Xlsm|Excel 2007/2010/2013/2016/2019 および Office 365 XLSM ファイルを表します|
|Xltx|Excel 2007/2010/2013/2016/2019 および Office 365 テンプレート XLTX ファイルを表します|
|Xltm|Excel 2007/2010/2013/2016/2019 および Office 365 マクロ有効 XLTM ファイルを表します|
|Xlsb|Excel 2007/2010/2013/2016/2019 および Office 365 バイナリ XLSB ファイルを表します|
|SpreadsheetML|SpreadsheetML ファイルを表します|
|Tsv|タブ区切り値ファイルを表します|
|TabDelimited|タブ区切りのテキスト ファイルを表します|
|オッズ|ODS ファイルを表します|
|HTML|HTML ファイルを表します|
|Mhtml|MHTML ファイルを表します|

### **Microsoft Excel 95/5.0 ファイルを開く**

 Microsoft Excel 95 ファイルを開くには、**[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**テンプレート ファイルのパスまたはストリームを持つインスタンス。コードをテストするためのサンプル ファイルは、次のリンクからダウンロードできます。

[Excel95_5.0.xls](Excel95_5.0.xls)

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningExcel95_5_0XLSFiles-1.java" >}}

### **Microsoft Excel 97 以降のバージョン XLS ファイルを開く**

Microsoft Excel XLS 97 以降のバージョンの XLS ファイルを開くには、**[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**テンプレート ファイルのパスまたはストリームを持つインスタンス。または、**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**メソッドを選択し、**[EXCEL_97_TO_2003](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#EXCEL_97_TO_2003)**の値**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**列挙。

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel972003Files-OpeningMicrosoftExcel972003Files.java" >}}

### **Microsoft Excel 2007 以降のバージョン XLSX ファイルを開く**

Microsoft Excel 2007 以降のバージョンの XLSX ファイルを開くには、**[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**テンプレート ファイルのパスまたはストリームを持つインスタンス。または、**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**クラスを選択し、**[XLSX](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#XLSX)**の値**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**列挙。

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel2007XlsxFiles-OpeningMicrosoftExcel2007XlsxFiles.java" >}}

### **異なる形式のファイルを開く**

Aspose.Cells を使用すると、開発者は、SpreadsheetML、CSV、タブ区切りファイルなど、さまざまな形式のスプレッドシート ファイルを開くことができます。このようなファイルを開くために、開発者は、異なる Microsoft Excel バージョンのファイルを開く場合と同じ方法を使用できます。

### **SpreadsheetML ファイルを開く**

SpreadsheetML ファイルは、書式設定、数式など、スプレッドシートに関するすべての情報を含む、スプレッドシートの XML 表現です。

SpreadsheetML ファイルを開くには、**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**クラスを選択し、**[SPREADSHEET_ML](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#SPREADSHEET_ML)**の値**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**列挙。

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningSpreadsheetMLFiles-OpeningSpreadsheetMLFiles.java" >}}

### **CSV ファイルを開く**

コンマ区切り値 (CSV) ファイルには、値がコンマで区切られているか、区切られているレコードが含まれています。 CSV ファイルでは、データは、フィールドがコンマ文字で区切られ、二重引用符で囲まれた表形式で保存されます。フィールドの値に二重引用符が含まれている場合は、二重引用符のペアでエスケープされます。 Microsoft Excel を使用して、スプレッドシート データを CSV ファイルにエクスポートすることもできます。

CSV ファイルを開くには、**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**クラスを選択し、**[CSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV)**で定義済みの値**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**列挙。

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **CSV ファイルを開いて無効な文字を置き換える**

Excel で、特殊文字を含む CSV ファイルを開くと、文字が自動的に置き換えられます。以下のコード例で示されている Aspose.Cells API でも同じことが行われます。

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

### **優先パーサーを使用して CSV ファイルを開く**

これは、CSV ファイルを開くためにデフォルトのパーサー設定を使用するために常に必要なわけではありません。 CSV ファイルをインポートしても、日付形式が期待どおりでない、または空のフィールドが異なる方法で処理されるなど、期待される出力が作成されないことがあります。この目的のために**[TxtLoadOptions.PreferredParsers](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)**要件に応じてさまざまなデータ型を解析するための独自の優先パーサーを提供することができます。次のサンプル コードは、優先パーサーの使用方法を示しています。

この機能をテストするためのサンプル ソース ファイルと出力ファイルは、次のリンクからダウンロードできます。

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **TSV(タブ区切り)ファイルを開く**

タブ区切りファイルにはスプレッドシート データが含まれますが、書式はありません。データは、テーブルやスプレッドシートなどの行と列に配置されます。簡単に言うと、タブ区切りファイルは、テキストの各列の間にタブがある特別な種類のプレーン テキスト ファイルです。

タブ区切りファイルを開くには、開発者は**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)**クラスを選択し、**[TSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV)**で定義済みの値**[LoadFormat](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**列挙。

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

### **暗号化された Excel ファイルを開く**

Microsoft Excel を使用して暗号化された Excel ファイルを作成できることがわかっています。このような暗号化されたファイルを開くには、開発者は特別なオーバーロードされた LoadOptions メソッドを呼び出し、FileFormatType 列挙で定義済みの DEFAULT 値を選択する必要があります。このメソッドは、以下の例に示すように、暗号化されたファイルのパスワードも取得します。

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningEncryptedExcelFiles-OpeningEncryptedExcelFiles.java" >}}

Aspose.Cells は、パスワードで保護された MS Excel 2013 ファイルを開くこともサポートしています。

{{% alert color="primary" %}}

大規模なスプレッドシートのロード中に Workbook コンストラクターが System.OutOfMemoryException をスローする可能性はかなりあります。この例外は、スプレッドシートをメモリに完全にロードするには使用可能なメモリが不足していることを示唆しています。[メモリ設定](/cells/ja/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}

### **SXC ファイルを開く**

StarOffice Calc は Microsoft Excel に似ており、数式、チャート、関数、およびマクロをサポートしています。このソフトウェアで作成されたスプレッドシートは、拡張子 SXC で保存されます。 SXC ファイルは、OpenOffice.org Calc スプレッドシート ファイルにも使用されます。次のコード サンプルで示すように、Aspose.Cells は SXC ファイルを読み取ることができます。

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningSXCFiles-1.java" >}}

### **FODS ファイルを開く**

FODS ファイルは、圧縮せずに OpenDocument XML で保存されたスプレッドシートです。次のコード サンプルで示すように、Aspose.Cells は FODS ファイルを読み取ることができます。

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningFODSFiles-1.java" >}}

## **先行トピック**
- [ワークブックの読み込み中に定義された名前をフィルター処理する](/cells/ja/java/filter-defined-names-while-loading-workbook/)
- [ワークブックまたはワークシートの読み込み中にオブジェクトをフィルタリングする](/cells/ja/java/filter-objects-while-loading-workbook-or-worksheet/)
- [Excel ファイルの読み込み中に警告を受け取る](/cells/ja/java/get-warnings-while-loading-excel-file/)
- [スプレッドシートを CSV 形式にエクスポートする際に、空白行の区切り記号を保持する](/cells/ja/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [指定したプリンター用紙サイズのワークブックを読み込む](/cells/ja/java/load-workbook-with-specified-printer-paper-size/)
- [異なる Microsoft Excel バージョンのファイルを開く](/cells/ja/java/opening-different-microsoft-excel-versions-files/)
- [大規模なデータセットを含む大きなファイルを操作する際のメモリ使用量の最適化](/cells/ja/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [読み取り Numbers スプレッドシート Apple Inc. が Aspose.Cells を使用して開発](/cells/ja/java/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [複数のエンコーディングを持つ CSV ファイルの読み取り](/cells/ja/java/reading-csv-file-with-multiple-encodings/)
- [時間がかかりすぎる場合は、InterruptMonitor を使用して変換またはロードを停止します](/cells/ja/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [LightCells の使用 API](/cells/ja/java/using-lightcells-api/)
