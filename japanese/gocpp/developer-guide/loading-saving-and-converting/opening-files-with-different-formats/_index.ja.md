---
title: さまざまな形式のファイルを開く
type: docs
weight: 30
url: /ja/go-cpp/opening-files-with-different-formats/

description: Aspose.Cells for Go via C++ APIは、XLSX、HTML、CSV、ODS、TSV、SXC、FODSなどのさまざまなフォーマットを開く/読み取ることができます。
keywords: xlsx ファイルを開く、html ファイルを開く、fods ファイルを読む、ods ファイルを読む、sxc ファイルを読む、csv ファイルを開く、タブ区切り、SpreadsheetML、tsv、mhtml
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すると、さまざまなフォーマットのファイルを開くことができます。**Aspose.Cells**は、Microsoft Excelスプレッドシート（XLS、XLSX、XLSM、XLSB）、SpreadsheetML、カンマ区切り値（CSV）、タブ区切りまたはTSVファイルなど、さまざまなファイルフォーマットを開くことが可能です。

すべてのサポートされるファイル形式を知りたい場合は、次のページを参照してください:
[サポートされているファイルフォーマット](https://docs.aspose.com/cells/go-cpp/supported-file-formats/)

{{% /alert %}}

## **異なるフォーマットのファイルを開く**

Aspose.Cellsは、開発者がSpreadsheetML、カンマ区切り値（CSV）、タブ区切りまたはTSV、そしてODSファイルなど、異なるフォーマットのスプレッドシートファイルを開くことを可能にします。これらのファイルを開くには、Microsoft Excelの異なるバージョンのファイルを開くときと同じ方法論を使用できます。

### **SpreadsheetML ファイルを開く**

SpreadsheetMLファイルは、書式設定や数式など、その情報をすべて含むスプレッドシートのXML表現です。Microsoft Excel XP以降、Microsoft ExcelにはスプレッドシートをSpreadsheetMLファイルにエクスポートするXMLエクスポートオプションが追加されました。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenSpreadsheetMLFile.go" >}}

### **HTML ファイルを開く**

Aspose.Cells は、HTML ファイルを Workbook オブジェクトに開くことを可能にします。HTML ファイルは Microsoft Excel 向けである必要があります。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenHTMLFile.go" >}}

### **CSV ファイルを開く**

コンマ区切り値（CSV）ファイルには、値がコンマで区切られたレコードが含まれています。データは、各列がコンマ文字で区切られ、二重引用符で引用された表として保存されます。フィールド値に二重引用符文字が含まれる場合は、それを二重引用符文字のペアでエスケープします。Microsoft Excel を使用してスプレッドシートデータを CSV にエクスポートすることもできます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenCSVFile.go" >}}

### **カスタム区切り記号を使用してテキストファイルを開く**

テキストファイルは、書式なしでスプレッドシートデータを保持するために使用されます。この種のファイルは、カスタマイズされた区切り記号を持つプレーンテキストファイルです。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTextFilewithCustomSeparator.go" >}}

テスト用のサンプルソースファイルは、以下のリンクからダウンロードできます。

[CustomSeparator.txt](CustomSeparator.txt)

### **タブ区切りファイルを開く**

タブ区切り（テキスト）ファイルはスプレッドシートデータを含みますが、書式設定はありません。データは表やスプレッドシートのように行と列に整理されています。基本的に、タブ区切りファイルは、各列の間にタブがあるプレーンテキストファイルの一種です。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTabDelimitedFile.go" >}}

### **タブ区切り値（TSV）ファイルを開く**

タブ区切り値（TSV）ファイルは、書式設定のないスプレッドシートデータを含みます。これは、表やスプレッドシートのように、行と列に整理されたデータを持つタブ区切りファイルと同じです。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTSVFile.go" >}}

### **SXCファイルを開く**

StarOffice CalcはMicrosoft Excelに似ており、式、チャート、関数、マクロをサポートします。このソフトウェアで作成されたスプレッドシートはSXC拡張子で保存されます。SXCファイルは、OpenOffice.org Calcのスプレッドシートファイルにも使用されます。Aspose.CellsはSXCファイルを読み取ることができ、以下のコードサンプルで示します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenSXCFile.go" >}}

### **FODSファイルを開く**

FODSファイルは、OpenDocument XML形式で保存された圧縮されていないスプレッドシートです。Aspose.CellsはFODSファイルの読み取りも可能で、以下のコード例で示します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenFODSFile.go" >}}
