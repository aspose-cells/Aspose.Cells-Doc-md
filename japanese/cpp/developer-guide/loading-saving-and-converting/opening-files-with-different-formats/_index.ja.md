---
title: 異なる形式のファイルを開く
type: docs
weight: 30
url: /ja/cpp/opening-files-with-different-formats/
description: Aspose.Cells for .NET API を使用すると、XLSX、HTML、CSV、ODS、TSV、SXC、FODS などのさまざまな形式を開いたり読み取ったりできます。
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
---
{{% alert color="primary" %}}

 Aspose.Cells を使用すると、さまざまな形式のファイルを開くことができます。**Aspose.Cells** Microsoft Excel スプレッドシート (XLS、XLSX、XLSM、XLSB)、SpreadsheetML、カンマ区切り値 (CSV)、タブ区切りまたはタブ区切り値 (TSV) ファイルなど、さまざまなファイル形式を開くことができます。

サポートされているすべてのファイル形式を知る必要がある場合は、次のページを参照してください。
[サポートされているファイル形式](https://docs.aspose.com/cells/cpp/supported-file-formats/)

{{% /alert %}}

##  **異なる形式のファイルを開く**

Aspose.Cells を使用すると、開発者は、SpreadsheetML、カンマ区切り値 (CSV)、タブ区切りまたはタブ区切り値 (TSV)、ODS ファイルなどのさまざまな形式のスプレッドシート ファイルを開くことができます。このようなファイルを開くには、開発者は、異なる Microsoft Excel バージョンのファイルを開く場合と同じ方法を使用できます。

###  **SpreadsheetML ファイルを開く**

SpreadsheetML ファイルは、書式設定や数式など、スプレッドシートに関するすべての情報を含むスプレッドシートの XML 表現です。 Microsoft Excel XP 以降、スプレッドシートを SpreadsheetML ファイルにエクスポートする XML エクスポート オプションが Microsoft Excel に追加されています。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSpreadsheetMLFile-new.cpp" >}}

###  **HTML ファイルを開く**

Aspose.Cells を使用すると、HTML ファイルを Workbook オブジェクトで開くことができます。 HTML ファイルは Microsoft Excel 指向、つまり MS-Excel で開くことができる必要があります。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenHTMLFile-new.cpp" >}}

###  **CSV ファイルを開く**

カンマ区切り値 (CSV) ファイルには、値がカンマで区切られたレコードが含まれています。データはテーブルとして保存され、各列はカンマ文字で区切られ、二重引用符で囲まれます。フィールド値に二重引用符が含まれている場合は、二重引用符のペアでエスケープされます。 Microsoft Excel を使用してスプレッドシート データを CSV にエクスポートすることもできます。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFile-new.cpp" >}}

####  **CSV ファイルを開いて無効な文字を置換する**

Excel では、特殊文字を含む CSV ファイルを開くと、文字が自動的に置き換えられます。以下のコード例で示すように、Aspose.Cells API によっても同じことが行われます。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFileAndReplaceInvalidCharacters-new.cpp" >}}

この機能をテストするために、サンプル ソース ファイルを次のリンクからダウンロードできます。

[無効な文字.csv](InvalidCharacters.csv)

###  **カスタムセパレータを使用してテキストファイルを開く**

テキスト ファイルは、スプレッドシート データを書式設定せずに保持するために使用されます。このファイルは、カスタマイズされた区切り文字を含むことができる一種のプレーン テキスト ファイルです。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTextFilewithCustomSeparator-new.cpp" >}}

この機能をテストするために、サンプル ソース ファイルを次のリンクからダウンロードできます。

[カスタムセパレーター.txt](CustomSeparator.txt)

###  **タブ区切りファイルを開く**

タブ区切り (テキスト) ファイルにはスプレッドシート データが含まれていますが、書式設定はされていません。データは、表やスプレッドシートと同様に行と列に配置されます。基本的に、タブ区切りファイルは、各列の間にタブがある特別な種類のプレーン テキスト ファイルです。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTabDelimitedFile-new.cpp" >}}

###  **タブ区切り値 (TSV) ファイルを開く**

タブ区切り値 (TSV) ファイルにはスプレッドシート データが含まれていますが、書式設定は行われていません。表やスプレッドシートのようにデータが行と列に配置されるタブ区切りファイルも同様です。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTSVFile-new.cpp" >}}

###  **SXC ファイルを開く**

StarOffice Calc は Microsoft Excel に似ており、数式、グラフ、関数、マクロをサポートしています。このソフトウェアで作成したスプレッドシートは、拡張子SXCで保存されます。 SXC ファイルは、OpenOffice.org Calc スプレッドシート ファイルにも使用されます。次のコードサンプルで示すように、Aspose.Cells は SXC ファイルを読み取ることができます。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSXCFile-new.cpp" >}}

###  **FODS ファイルを開く**

FODS ファイルは、圧縮なしで OpenDocument XML で保存されたスプレッドシートです。次のコードサンプルで示すように、Aspose.Cells は FODS ファイルを読み取ることができます。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenFODSFile-new.cpp" >}}
