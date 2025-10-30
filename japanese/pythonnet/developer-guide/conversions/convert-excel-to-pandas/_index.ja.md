---
title: ExcelをPandas DataFrameに変換
type: docs
weight: 30
url: /ja/python-net/convert-excel-to-pandas-dataframe/
description: Aspose.Cells for Python via .NET API を使用して Pandas を Excel に変換します。
keywords: PythonでExcelをPandas DataFrameに変換し、PythonでExcelをPandas DataFrameにエクスポートする方法via NET、PythonでxlsxをPandas DataFrameに変換し、ExcelをPandas DataFrameに保存します。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET APIを使用すると、Excel、TSV、CSV、Jsonなど、さまざまな形式をpandas DataFrameに変換できます。

{{% /alert %}}

## **ExcelをPandas DataFrameに変換（最初から作成）**
Aspose.Cells for Python via .NETを使用して、ExcelデータをPandas DataFrameに直接エクスポートする方法を示すコードスニペットの例です。
1. Workbookを作成していくつかの値を追加します。
1. ExcelデータをトラバースしてAspose.Cells for Python via .NETを使用してPandas DataFrameにデータをエクスポートします。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Pandas-export-excel-to-pandas-dataframe-directly.py" >}}

## **既存のExcelファイルをPandas DataFrameに変換**
以下は、Aspose.Cells for Python via .NETを使用して既存の.xlsxファイルを開き、ExcelデータをPandas DataFrameにエクスポートする方法を示す例のコードスニペットです：
1. 既存の[Excelファイル](PandasTest.xlsx)を開く。
1. 各行と列のセルデータをPandas DataFrameに変換する。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Pandas-export-excel-to-pandas-dataframe-by-openning-file.py" >}}

## **ExcelをJSONデータを介してPandas DataFrameに変換する**
Aspose.Cells for Python via .NETを使用して、ExcelデータをJSONデータを介してPandas DataFrameにエクスポートする方法を示すコードスニペットの例です。
1. Workbookを作成していくつかの値を追加します。
1. ExcelデータをJSON文字列にエクスポートします。
1. pandasライブラリを使用してJSONデータを読み込みます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Pandas-export-excel-to-pandas-dataframe-by-json.py" >}}

## **CSVファイルを介したExcelからPandas DataFrameへの変換**
CSVファイル形式の特性により、.xlsxファイルをCSVファイルに変換し、その後Pandas DataFrameに読み込むことは自然で簡単なプロセスです：
1. 既存のxlsx([ProductDatatoCSV.xlsx])をCSVファイルに変換。
1. CSVファイルをPandas DataFrameに変換。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Pandas-export-excel-to-pandas-dataframe-via-CSV.py" >}}
{{< app/cells/assistant language="python-net" >}}
