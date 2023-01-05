---
title: 異なる形式のファイルを開く
type: docs
weight: 30
url: /ja/python-net/opening-files-with-different-formats/
description: Aspose.Cells for .NET API を使用すると、XLSX、HTML、CSV、ODS、TSV、SXC、FODS などのさまざまな形式を開く/読み取ることができます。
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
---
{{% alert color="primary" %}}

 Aspose.Cells を使用すると、さまざまな形式のファイルを開くことができます。**Aspose.Cells** Microsoft Excel スプレッドシート (XLS、XLSX、XLSM、XLSB)、SpreadsheetML、カンマ区切り値 (CSV)、タブ区切りまたはタブ区切り値 (TSV) ファイルなど、さまざまなファイル形式を開くことができます。

サポートされているすべてのファイル形式を知る必要がある場合は、次のページを参照してください。
[サポートされているファイル形式](https://docs.aspose.com/cells/python-net/supported-file-formats/)

{{% /alert %}}

## **異なる形式のファイルを開く**

Aspose.Cells を使用すると、開発者は、SpreadsheetML、カンマ区切り値 (CSV)、タブ区切りまたはタブ区切り値 (TSV)、ODS ファイルなど、さまざまな形式のスプレッドシート ファイルを開くことができます。このようなファイルを開くには、開発者は異なる Microsoft Excel バージョンのファイルを開く場合と同じ方法を使用できます。

### **SpreadsheetML ファイルを開く**

SpreadsheetML ファイルは、書式設定、数式など、スプレッドシートに関するすべての情報を含むスプレッドシートの XML 表現です。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenSpreadsheetMLFile.py" >}}

### **HTML ファイルを開く**

Aspose.Cells を使用すると、HTML ファイルを Workbook オブジェクトで開くことができます。 HTML ファイルは Microsoft Excel 向けである必要があります。つまり、MS-Excel で開くことができます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenHTMLFile.py" >}}

### **CSV ファイルを開く**

コンマ区切り値 (CSV) ファイルには、値がコンマで区切られたレコードが含まれています。データは、各列がコンマ文字で区切られ、二重引用符で囲まれたテーブルとして保存されます。フィールド値に二重引用符が含まれている場合は、二重引用符のペアでエスケープされます。 Microsoft Excel を使用して、スプレッドシート データを CSV にエクスポートすることもできます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenCSVFile.py" >}}

#### **CSV ファイルを開いて無効な文字を置き換える**

Excel で、特殊文字を含む CSV ファイルを開くと、文字が自動的に置き換えられます。以下のコード例で示されている Aspose.Cells API でも同じことが行われます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenCSVFileAndReplaceInvalidCharacters.py" >}}

この機能をテストするために、次のリンクからサンプル ソース ファイルをダウンロードできます。

[無効な文字.csv](InvalidCharacters.csv)

### **カスタム セパレータを使用してテキスト ファイルを開く**

テキスト ファイルは、書式設定なしでスプレッドシート データを保持するために使用されます。このファイルは、カスタマイズされた区切り文字を持つことができる一種のプレーン テキスト ファイルです。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenTextFilewithCustomSeparator.py" >}}

この機能をテストするために、次のリンクからサンプル ソース ファイルをダウンロードできます。

[CustomSeparator.txt](CustomSeparator.txt)

### **タブ区切りファイルを開く**

タブ区切り (テキスト) ファイルにはスプレッドシート データが含まれますが、書式設定はありません。データは、表やスプレッドシートのように行と列に配置されます。基本的に、タブ区切りファイルは、各列の間にタブがある特別な種類のプレーン テキスト ファイルです。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenTabDelimitedFile.py" >}}

### **タブ区切り値 (TSV) ファイルを開く**

タブ区切り値 (TSV) ファイルにはスプレッドシート データが含まれていますが、書式設定はありません。テーブルやスプレッドシートのように、データが行と列に配置されるタブ区切りファイルと同じです。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenTSVFile.py" >}}

### **SXC ファイルを開く**

StarOffice Calc は Microsoft Excel に似ており、数式、チャート、関数、およびマクロをサポートしています。このソフトウェアで作成されたスプレッドシートは、拡張子 SXC で保存されます。 SXC ファイルは、OpenOffice.org Calc スプレッドシート ファイルにも使用されます。次のコード サンプルで示すように、Aspose.Cells は SXC ファイルを読み取ることができます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenSXCFile.py" >}}

### **FODS ファイルを開く**

FODS ファイルは、圧縮せずに OpenDocument XML で保存されたスプレッドシートです。次のコード サンプルで示すように、Aspose.Cells は FODS ファイルを読み取ることができます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFODSFile.py" >}}
