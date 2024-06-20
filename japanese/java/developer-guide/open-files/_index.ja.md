---
title: さまざまな形式のファイルを開く
linktitle: ファイルを開く
type: docs
weight: 10
url: /ja/java/opening-files-with-different-formats/
---

{{% alert color="primary" %}}

開発者はさまざまな目的でAspose.Cellsを使用してファイルを開きます。たとえば、データを取得するためにファイルを開いたり、事前定義されたデザイナースプレッドシートファイルを使用して開発プロセスを高速化します。Aspose.Cellsを使用すると、さまざまな種類のソースファイルを開くことができます。これらのソースファイルには、Microsoft Excelレポート、SpreadsheetML、カンマ区切り値（CSV）、タブ区切りまたはタブ区切り値（TSV）ファイルが含まれます。この記事では、Aspose.Cellsを使用してこれらの異なるソースファイルを開く方法について説明します。

すべてのサポートされるファイル形式を知りたい場合は、次のページを参照してください:
[サポートされているファイルフォーマット](https://docs.aspose.com/cells/java/supported-file-formats/)

{{% /alert %}}

## **Excelファイルを開く簡単な方法**

### **ファイルのパスを通じて開く**

ファイルパスを使用してMicrosoft Excelファイルを開くには、ファイルパスをパラメーターとして渡して[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)クラスのインスタンスを作成します。次のサンプルコードは、ファイルパスを使用してExcelファイルを開く方法を示しています。

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughPath-OpeningFilesThroughPath.java" >}}

### **ストリームを介した開く**

必要なExcelファイルがストリームとして保存されている場合、ファイルパスを使用してファイルを開く方法と同様に、[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)クラスのインスタンスを作成する際にストリームをパラメーターとして渡します。次のサンプルコードは、ストリームを使用してExcelファイルを開く方法を示しています。

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughStream-OpeningFilesThroughStream.java" >}}

### **異なるMicrosoft Excelバージョンのファイルを開く**

ユーザーは[**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)クラスを使用してExcelファイルのフォーマットを指定することができます。その際には[**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)列挙型を使用します。

[**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)列挙型には、多くの事前定義ファイル形式が含まれています。 以下にその一部を示します。

|**フォーマットの種類**|**説明**|
| :- | :- |
|Csv|はCSVファイルを表します
|Excel97To2003|はExcel 97-2003ファイルを表します
|Xlsx|はExcel 2007/2010/2013/2016/2019およびOffice 365 XLSXファイルを表します
|Xlsm|はExcel 2007/2010/2013/2016/2019およびOffice 365 XLSMファイルを表します
|Xltx|はExcel 2007/2010/2013/2016/2019およびOffice 365テンプレートXLTXファイルを表します
|Xltm|はExcel 2007/2010/2013/2016/2019およびOffice 365マクロ有効なXLTMファイルを表します
|Xlsb|はExcel 2007/2010/2013/2016/2019およびOffice 365バイナリXLSBファイルを表します
|SpreadsheetML|はSpreadsheetMLファイルを表します
|Tsv|はタブ区切りの値ファイルを表します
|TabDelimited|はタブ区切りのテキストファイルを表します
|Ods|はODSファイルを表します
|Html|はHTMLファイルを表します
|Mhtml|はMHTMLファイルを表します

### **Microsoft Excel 95/5.0 ファイルを開く**

Microsoft Excel 95ファイルを開くには、[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)インスタンスをパスまたはテンプレートファイルのストリームでインスタンス化します。コードのテストに使用するサンプルファイルは、次のリンクからダウンロードできます。

[Excel95_5.0.xls](Excel95_5.0.xls)

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningExcel95_5_0XLSFiles-1.java" >}}

### **Microsoft Excel 97またはそれ以降のバージョンXLSファイルの開閉**

Microsoft Excel XLS 97またはそれ以降のバージョンのXLSファイルを開くには、[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)インスタンスをパスまたはテンプレートファイルのストリームでインスタンス化します。または、[**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)メソッドを使用して[**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)列挙型の[**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#EXCEL_97_TO_2003)値を選択します。

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel972003Files-OpeningMicrosoftExcel972003Files.java" >}}

### **Microsoft Excel 2007またはそれ以降のバージョンXLSXファイルの開閉**

Microsoft Excel 2007またはそれ以降のバージョンのXLSXファイルを開くには、[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)インスタンスをパスまたはテンプレートファイルのストリームでインスタンス化します。または、[**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)クラスを使用して[**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)列挙型の[**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#XLSX)値を選択します。

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel2007XlsxFiles-OpeningMicrosoftExcel2007XlsxFiles.java" >}}

### **異なるフォーマットのファイルを開く**

Aspose.Cellsを使用すると、SpreadsheetML、CSV、タブ区切りファイルなど、さまざまなフォーマットのスプレッドシートファイルを開くことができます。このようなファイルを開くには、Microsoft Excelの異なるバージョンのファイルを開くときと同じ手法を使用できます。

### **SpreadsheetML ファイルを開く**

SpreadsheetMLファイルは、スプレッドシートのすべての情報（書式設定、数式など）を含むスプレッドシートのXML表現です。Microsoft Excel XP以降、Microsoft ExcelにXMLエクスポートオプションが追加され、スプレッドシートをSpreadsheetMLファイルにエクスポートできます。

SpreadsheetMLファイルを開くには、[**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)クラスを使用して[**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)列挙型の[**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#SPREADSHEET_ML)値を選択します。

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningSpreadsheetMLFiles-OpeningSpreadsheetMLFiles.java" >}}

### **CSV ファイルを開く**

コンマ区切り値（CSV）ファイルには、値がコンマで区切られ、二重引用符で引用されたレコードが含まれています。 CSVファイルでは、データはコンマ文字で区切られ、二重引用符によって引用されたフィールドで保管されています。フィールドの値に二重引用符文字が含まれている場合は、一対の二重引用符文字でエスケープされます。また、Microsoft Excelを使用して、スプレッドシートのデータをCSVファイルにエクスポートすることもできます。

CSVファイルを開くには、[**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)クラスを使用して、[**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) 列挙体で定義された[**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV)値を選択してください。

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **CSV ファイルを開くと無効な文字を置換する**

ExcelでCSVファイルを開くと、特殊文字が自動的に置き換えられます。Aspose.CellsのAPIも同様に、以下のコード例に示されているように自動的に置き換えます。

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

### **優先されるパーサを使用してCSVファイルを開く**

CSVファイルを開く際にはデフォルトのパーサ設定を使用する必要はありません。時々、CSVファイルのインポートが期待通りの出力を作成しないことがあります。たとえば、日付形式が期待通りでない、または空のフィールドが異なる方法で扱われるなどです。そのために、要件に応じて異なるデータ型を解析するための優先されるパーサを提供するために[**TxtLoadOptions.PreferredParsers**](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)が利用できます。以下のサンプルコードは、優先されるパーサの使用方法を示しています。  

この機能をテストするために、サンプルのソースファイルと出力ファイルを以下のリンクからダウンロードできます。

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **TSV（タブ区切り）ファイルを開く**

タブ区切りファイルには、書式はありませんが、表やスプレッドシートのような行と列でデータが配置されています。要するに、タブ区切りファイルは、各列の間にタブがある通常のテキストファイルの特別な種類です。

タブ区切りファイルを開くには、開発者は[**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)クラスを使用し、[**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV)値を選択し、[**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)列挙型で事前定義する必要があります。

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

### **暗号化されたExcelファイルを開く**

Microsoft Excelを使用して暗号化されたExcelファイルを作成することが可能であることはわかっています。このような暗号化されたファイルを開くためには、開発者は特別なオーバーロードされたLoadOptionsメソッドを呼び出し、FileFormatType列挙型で定義されたDEFAULT値を選択する必要があります。このメソッドは、以下の例に示すように、暗号化されたファイルのパスワードも受け取ります。

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningEncryptedExcelFiles-OpeningEncryptedExcelFiles.java" >}}

Aspose.Cellsはまた、パスワードで保護されたMS Excel 2013ファイルを開くのをサポートしています。

{{% alert color="primary" %}}

大きなスプレッドシートを読み込む際に、WorkbookコンストラクタがSystem.OutOfMemoryExceptionをスローする可能性がかなりある。この例外は、利用可能なメモリがスプレッドシートを完全にメモリに読み込むには不十分であることを示唆しており、したがって、[メモリの設定](/cells/ja/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)を有効にした状態でスプレッドシートを読み込む必要があります。

{{% /alert %}}

### **SXCファイルを開く**

StarOffice CalcはMicrosoft Excelに似ており、数式、グラフ、関数、およびマクロをサポートしています。このソフトウェアで作成されたスプレッドシートはSXC拡張子で保存されます。SXCファイルはOpenOffice.org Calcスプレッドシートファイルにも使用されます。Aspose.Cellsは、以下のコードサンプルで示されるように、SXCファイルを読み取ることができます。

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningSXCFiles-1.java" >}}

### **FODSファイルを開く**

FODSファイルは、圧縮なしのOpenDocument XML形式で保存されたスプレッドシートです。Aspose.Cellsは、以下のコード例に示すように、FODSファイルを読み取ることができます。

#### **例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningFODSFiles-1.java" >}}

## **高度なトピック**
- [ワークブックを読み込む際に定義名をフィルタリングする](/cells/ja/java/filter-defined-names-while-loading-workbook/)
- [ワークブックまたはワークシートをロードする際にオブジェクトをフィルタする](/cells/ja/java/filter-objects-while-loading-workbook-or-worksheet/)
- [Excelファイルの読み込み中に警告を受け取る](/cells/ja/java/get-warnings-while-loading-excel-file/)
- [CSV形式へのスプレッドシートのエクスポート時に空行の区切り記号を保持する](/cells/ja/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [指定されたプリンタ用紙サイズでワークブックを読み込む](/cells/ja/java/load-workbook-with-specified-printer-paper-size/)
- [異なるMicrosoft Excelバージョンのファイルを開く](/cells/ja/java/opening-different-microsoft-excel-versions-files/)
- [大規模なデータセットを持つ大きなファイルで作業する際のメモリ使用量を最適化する](/cells/ja/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Aspose.Cellsを使用してApple Inc.が開発したNumbersスプレッドシートを読む](/cells/ja/java/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [複数のエンコーディングを持つCSVファイルの読み込み](/cells/ja/java/reading-csv-file-with-multiple-encodings/)
- [時間がかかりすぎる場合はInterruptMonitorを使用して変換または読み込みを停止してください](/cells/ja/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [LightCells APIの使用](/cells/ja/java/using-lightcells-api/)
