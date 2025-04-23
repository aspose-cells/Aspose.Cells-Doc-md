---
title: さまざまな形式のファイルを開く
type: docs
weight: 30
url: /ja/net/opening-files-with-different-formats/
description: Aspose.Cells for .NET API は、XLSX、HTML、CSV、ODS、TSV、SXC、FODS などの異なる形式を開く/読み込むことができます。
keywords: xlsx ファイルを開く、html ファイルを開く、fods ファイルを読む、ods ファイルを読む、sxc ファイルを読む、csv ファイルを開く、タブ区切り、SpreadsheetML、tsv、mhtml
---

{{% alert color="primary" %}}

Aspose.Cells を使用すると、異なる形式のファイルを開くことができます。**Aspose.Cells** は、Microsoft Excel スプレッドシート（XLS、XLSX、XLSM、XLSB）、SpreadsheetML、コンマ区切り値（CSV）、タブ区切りまたはタブ区切り値（TSV）ファイルなど、さまざまなファイル形式を開くことができます。

すべてのサポートされるファイル形式を知りたい場合は、次のページを参照してください:
[サポートされているファイルフォーマット](https://docs.aspose.com/cells/net/supported-file-formats/)

{{% /alert %}}

## **異なるフォーマットのファイルを開く**

Aspose.Cells は、SpreadsheetML、コンマ区切り値（CSV）、タブ区切りまたはタブ区切り値（TSV）、ODS ファイルなどの異なる形式のスプレッドシートファイルを開くことができます。このようなファイルを開くには、開く異なる Microsoft Excel バージョンのファイルを開くときと同じ方法を使用できます。

### **SpreadsheetML ファイルを開く**

SpreadsheetML ファイルは、書式設定、数式など、スプレッドシートに関するすべての情報を含む XML 表現です。Microsoft Excel XP 以降、XML エクスポートオプションが追加され、スプレッドシートを SpreadsheetML ファイルにエクスポートできます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningSpreadsheetMLFiles-1.cs" >}}

### **HTML ファイルを開く**

Aspose.Cells は、HTML ファイルを Workbook オブジェクトに開くことを可能にします。HTML ファイルは Microsoft Excel 向けである必要があります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningHTMLFile-1.cs" >}}

### **CSV ファイルを開く**

コンマ区切り値（CSV）ファイルには、値がコンマで区切られたレコードが含まれています。データは、各列がコンマ文字で区切られ、二重引用符で引用された表として保存されます。フィールド値に二重引用符文字が含まれる場合は、それを二重引用符文字のペアでエスケープします。Microsoft Excel を使用してスプレッドシートデータを CSV にエクスポートすることもできます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

#### **CSV ファイルを開くと無効な文字を置換する**

Excel では、特殊文字が含まれる CSV ファイルを開くと、文字が自動的に置換されます。Aspose.Cells API でも同様に行います。これは以下のコード例で示されています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

#### **好みのパーサーの使用**

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

### **SXCファイルを開く**

StarOffice CalcはMicrosoft Excelに似ており、数式、グラフ、関数、およびマクロをサポートしています。このソフトウェアで作成されたスプレッドシートはSXC拡張子で保存されます。SXCファイルはOpenOffice.org Calcスプレッドシートファイルにも使用されます。Aspose.Cellsは、以下のコードサンプルで示されるように、SXCファイルを読み取ることができます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningSXCFiles-1.cs" >}}

### **FODSファイルを開く**

FODSファイルは、圧縮なしで保存されたOpenDocument XMLのスプレッドシートです。Aspose.Cellsは、以下のコードサンプルで示されるように、FODSファイルを読み取ることができます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFODSFiles-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
