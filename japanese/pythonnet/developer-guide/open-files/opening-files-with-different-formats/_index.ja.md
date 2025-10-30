---
title: さまざまな形式のファイルを開く
type: docs
weight: 30
url: /ja/python-net/opening-files-with-different-formats/
description: Aspose.Cells for Python via .NET APIは、XLSX、HTML、CSV、ODS、TSV、SXC、FODSなどの異なるフォーマットのファイルを開いて読み取ることができます。
keywords: xlsx ファイルを開く、html ファイルを開く、fods ファイルを読む、ods ファイルを読む、sxc ファイルを読む、csv ファイルを開く、タブ区切り、SpreadsheetML、tsv、mhtml
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NETを使用すると、さまざまなフォーマットのファイルを開くことができます。例えば、Microsoft Excelのスプレッドシート（XLS、XLSX、XLSM、XLSB）、SpreadsheetML、カンマ区切り値（CSV）、タブ区切りまたはTSVファイルなどです。

すべてのサポートされるファイル形式を知りたい場合は、次のページを参照してください:
[サポートされているファイルフォーマット](https://docs.aspose.com/cells/python-net/supported-file-formats/)

{{% /alert %}}

## **異なるフォーマットのファイルを開く**

Aspose.Cells for Python via .NETは、異なるフォーマットのスプレッドシートファイル（SpreadsheetML、CSV、TSV、ODSなど）を開くことを可能にします。これらのファイルを開くには、Microsoft Excelの異なるバージョンのファイルを開くときと同じ方法を使用できます。

### **SpreadsheetML ファイルを開く**

SpreadsheetML ファイルは、書式設定、数式など、スプレッドシートに関するすべての情報を含む XML 表現です。Microsoft Excel XP 以降、XML エクスポートオプションが追加され、スプレッドシートを SpreadsheetML ファイルにエクスポートできます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningSpreadsheetMLFiles-1.py" >}}

### **HTML ファイルを開く**

Aspose.Cells for Python via .NETは、HTMLファイルをWorkbookオブジェクトに開くことができます。HTMLファイルはMicrosoft Excelに適したものである必要があります。つまり、MS-Excelが開くことができる必要があります。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningHTMLFile-1.py" >}}

### **CSV ファイルを開く**

コンマ区切り値（CSV）ファイルには、値がコンマで区切られたレコードが含まれています。データは、各列がコンマ文字で区切られ、二重引用符で引用された表として保存されます。フィールド値に二重引用符文字が含まれる場合は、それを二重引用符文字のペアでエスケープします。Microsoft Excel を使用してスプレッドシートデータを CSV にエクスポートすることもできます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningCSVFiles-1.py" >}}

#### **CSV ファイルを開くと無効な文字を置換する**

Excelで、特殊文字を含むCSVファイルを開くと、文字が自動的に置き換えられます。これと同じ処理をAspose.Cells for Python via .NET APIも行い、以下のコード例で示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningCSVFilesAndReplacingInvalidCharacters-1.py" >}}



### **タブ区切りファイルを開く**

タブ区切り（テキスト）ファイルには、スプレッドシートデータが含まれていますが、フォーマットはありません。データは表やスプレッドシートのように行と列で配置されています。基本的に、タブ区切りファイルは各列の間にタブがある特別な種類のプレーンテキストファイルです。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningTabDelimitedFiles-1.py" >}}

### **タブ区切り値（TSV）ファイルを開く**

タブ区切り値（TSV）ファイルには、スプレッドシートデータが含まれていますが、フォーマットはありません。データは表やスプレッドシートのように行と列で配置されています。データはタブ区切りファイルと同様であり、各列の間にタブがあります。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningTSVFiles-1.py" >}}

### **SXCファイルを開く**

StarOffice CalcはMicrosoft Excelに似ており、数式、グラフ、関数、マクロをサポートしています。このソフトウェアで作成したスプレッドシートはSXC拡張子で保存されます。SXCファイルはOpenOffice.org Calcのスプレッドシートファイルにも使用されます。Aspose.Cells for Python via .NETは、以下のコードサンプルに示すようにSXCファイルを読み取ることができます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningSXCFiles-1.py" >}}

### **FODSファイルを開く**

FODSファイルは、圧縮なしのOpenDocument XMLとして保存されたスプレッドシートです。Aspose.Cells for Python via .NETは、以下のコードサンプルに示すようにFODSファイルを読み取ることができます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFODSFiles-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
