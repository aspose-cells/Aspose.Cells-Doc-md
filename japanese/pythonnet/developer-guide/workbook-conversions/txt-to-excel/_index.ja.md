---
title: CSV、TSV、TXT を Excel に変換
type: docs
weight: 30
url: /ja/python-net/convert-csv-tsv-and-txt-to-excel/
description: CSV、TSV、TXT を Aspose.Cells for Python via .NET API を使用して Excel に変換します。
keywords: Python Convert CSV, TSV and TXT to Excel, Resave CSV, TSV and TXT to Excel in Python via NET, Python Convert CSV, TSV and TXT to xlsx, Load for import CSV, TSV and TXT to Excel.
---
{{% alert color="primary" %}}

Aspose.Cells を使用すると、CSV ファイルを Excel 、OpenOffice、Pdf、Json およびさまざまな形式に変換できます。

{{% /alert %}}


##  **CSV ファイルを開く**

カンマ区切り値 (CSV) ファイルには、値がカンマで区切られたレコードが含まれています。データはテーブルとして保存され、各列はカンマ文字で区切られ、二重引用符で囲まれます。フィールド値に二重引用符が含まれている場合は、二重引用符のペアでエスケープされます。 Microsoft Excel を使用してスプレッドシート データを CSV にエクスポートすることもできます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-OpeningCSVFiles-1.py" >}}

##  **CSV ファイルを開いて無効な文字を置換する**

Excel では、特殊文字を含む CSV ファイルを開くと、文字が自動的に置き換えられます。以下のコード例で示すように、Aspose.Cells API によっても同じことが行われます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-OpeningCSVFilesAndReplacingInvalidCharacters-1.py" >}}

##  **タブ区切りファイルを開く**

タブ区切り (テキスト) ファイルにはスプレッドシート データが含まれていますが、書式設定はされていません。データは、表やスプレッドシートと同様に行と列に配置されます。基本的に、タブ区切りファイルは、各列の間にタブがある特別な種類のプレーン テキスト ファイルです。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-OpeningTabDelimitedFiles-1.py" >}}

##  **タブ区切り値 (TSV) ファイルを開く**

タブ区切り値 (TSV) ファイルにはスプレッドシート データが含まれていますが、書式設定は行われていません。表やスプレッドシートのようにデータが行と列に配置されるタブ区切りファイルも同様です。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-OpeningTSVFiles-1.py" >}}


##  **アドバンストトピック**
- [数式を含む CSV ファイルをロードまたはインポートする](/cells/ja/python-net/load-or-import-csv-file-with-formulas/)
- [複数のエンコーディングを持つ CSV ファイルの読み取り](/cells/ja/python-net/reading-csv-file-with-multiple-encodings/)

