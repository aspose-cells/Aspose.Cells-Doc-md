---
title: CSV、TSV、TXTをExcelに変換する
type: docs
weight: 30
url: /ja/python-net/convert-csv-tsv-and-txt-to-excel/
description: Aspose.Cells for Python via .NET APIを使用してCSV、TSV、およびTXTをExcelに変換します。
keywords: PythonでCSV、TSV、およびTXTをExcelに変換する, PythonでCSV、TSV、およびTXTをExcelに再保存するvia NET, PythonでCSV、TSV、およびTXTをxlsxに変換する、CSV、TSV、およびTXTをExcelにインポートするための読み込み。
---

{{% alert color="primary" %}}

Aspose.Cellsを使用して、CSVファイルをExcel、OpenOffice、Pdf、Jsonなど多くの異なる形式に変換することができます。

{{% /alert %}}


## **CSV ファイルを開く**

コンマ区切り値（CSV）ファイルには、値がコンマで区切られたレコードが含まれています。データは、各列がコンマ文字で区切られ、二重引用符で引用された表として保存されます。フィールド値に二重引用符文字が含まれる場合は、それを二重引用符文字のペアでエスケープします。Microsoft Excel を使用してスプレッドシートデータを CSV にエクスポートすることもできます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-OpeningCSVFiles-1.py" >}}

## **CSV ファイルを開くと無効な文字を置換する**

Excel では、特殊文字が含まれる CSV ファイルを開くと、文字が自動的に置換されます。Aspose.Cells API でも同様に行います。これは以下のコード例で示されています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-OpeningCSVFilesAndReplacingInvalidCharacters-1.py" >}}

## **タブ区切りファイルを開く**

タブ区切り（テキスト）ファイルには、スプレッドシートデータが含まれていますが、フォーマットはありません。データは表やスプレッドシートのように行と列で配置されています。基本的に、タブ区切りファイルは各列の間にタブがある特別な種類のプレーンテキストファイルです。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-OpeningTabDelimitedFiles-1.py" >}}

## **タブ区切り値（TSV）ファイルを開く**

タブ区切り値（TSV）ファイルには、スプレッドシートデータが含まれていますが、フォーマットはありません。データは表やスプレッドシートのように行と列で配置されています。データはタブ区切りファイルと同様であり、各列の間にタブがあります。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-OpeningTSVFiles-1.py" >}}


## **高度なトピック**
- [数式を持つCSVファイルを読み込むまたはインポートする](/cells/ja/python-net/load-or-import-csv-file-with-formulas/)
- [複数のエンコーディングを持つCSVファイルの読み込み](/cells/ja/python-net/reading-csv-file-with-multiple-encodings/)

