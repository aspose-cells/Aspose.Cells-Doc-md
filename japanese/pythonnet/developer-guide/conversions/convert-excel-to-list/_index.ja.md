---
title: Excel を Python データに変換する
type: docs
weight: 30
url: /ja/python-net/convert-excel-to-list/
description: Aspose.Cells for Python via .NET API を使用して、Excel データをリストに変換します。
keywords: Python Excel ライブラリを使用して、Workbook を Dictionary に変換する方法、Worksheet を Dictionary に変換する方法、Row オブジェクトをリストに変換する、ListObject をリストに変換する、Column オブジェクトをリストに変換する方法、Range をリストに変換する方法、Worksheet をリストに変換する方法。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET API を使用すると、Workbook、Worksheet、Range、Row、Column などの Excel データを Python リストに変換できます。

{{% /alert %}}

## **Excel ワークブックを Dictionary に変換する方法**
Aspose.Cells for Python via .NET を使用して、Excel データを Dictionary にエクスポートする方法を示す例のコードスニペットです:
1. [サンプルファイル](sample_data.xlsx)をロードします。
1. すべてのワークシートをトラバースし、Aspose.Cells for Python Excel ライブラリを使用して Workbook を Dictionary に変換します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-Dictionary.py" >}}

出力結果：
```
{'Sheet1': [['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]], 'Sheet2': [['City2', 'Region2', 'Store3'], ['Seattle', 'West', 3000], ['philadelph', 'East', 3082], ['Detroit', 'Central', 3074]], 'Sheet3': [['City3', 'Region3', 'Store3'], ['Seattle', 'West', 3166], ['New York', 'East', 3090], ['Chicago', 'Central', 3055]]}
```

## **Excel ワークブックをリストに変換する方法**
Aspose.Cells for Python via .NET を使用して、Excel データをリストにエクスポートする方法を示す例のコードスニペットです:
1. [サンプルファイル](sample_data.xlsx)をロードします。
1. Aspose.Cells for Python Excel ライブラリを使用して、すべてのワークシートを走査し、ワークブックをリストに変換します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-List.py" >}}

出力結果：
```
[[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]], 
[['City2', 'Region2', 'Store3'], ['Seattle', 'West', 3000], ['philadelph', 'East', 3082], ['Detroit', 'Central', 3074]], [['City3', 'Region3', 'Store3'], ['Seattle', 'West', 3166], ['New York', 'East', 3090], ['Chicago', 'Central', 3055]]] 
```

## **ワークシートをリストに変換する方法**
以下は、Aspose.Cells for Python via .NET を使用してワークシートデータをリストにエクスポートする方法を示すコードスニペットの例です。
1. [サンプルファイル](sample_data.xlsx)をロードします。
1. 最初のワークシートを取得します。
1. Aspose.Cells for Python Excel ライブラリを使用して、ワークシートデータをリストに変換します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Worksheet-to-List.py" >}}

出力結果：
```
[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]]
```

## **Excel の ListObject をリストに変換する方法**
以下は、Aspose.Cells for Python via .NET を使用して ListObject データをリストにエクスポートする方法を示すコードスニペットの例です。
1. [サンプルファイル](sample_data.xlsx)をロードします。
1. 最初のワークシートを取得します。
1. ListObjectオブジェクトを作成します。
1. Aspose.Cells for Python Excel ライブラリを使用して、ListObject データをリストに変換します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-ListObject-to-List.py" >}}

出力結果：
```
[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]]
```


## **Excel の行をリストに変換する方法**
以下は、Aspose.Cells for Python via .NET を使用して行データをリストにエクスポートする方法を示すコードスニペットの例です。
1. [サンプルファイル](sample_data.xlsx)をロードします。
1. 最初のワークシートを取得します。
1. 行インデックスで行オブジェクトを取得します。
1. Aspose.Cells for Python Excel ライブラリを使用して、行データをリストに変換します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Row-to-List.py" >}}

出力結果：
```
['Detroit', 'Central', 3074]
```

## **Excel の列をリストに変換する方法**
以下は、Aspose.Cells for Python via .NET を使用して列データをリストにエクスポートする方法を示すコードスニペットの例です。
1. [サンプルファイル](sample_data.xlsx)をロードします。
1. 最初のワークシートを取得します。
1. 列インデックスで列オブジェクトを取得します。
1. Aspose.Cells for Python Excel ライブラリを使用して、列データをリストに変換します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Column-to-List.py" >}}

出力結果：
```
['Store', 3055, 3036, 3074]
```

## **Excel の範囲をリストに変換する方法**
以下はAspose.Cells for Python via .NETを使用して範囲データをリストにエクスポートする方法を示すコードスニペットの例です。
1. [サンプルファイル](sample_data.xlsx)をロードします。
1. 最初のワークシートを取得します。
1. 範囲を作成します。
1. Aspose.Cells for Python Excelライブラリを使用して範囲データをリストに変換します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Range-to-List.py" >}}

出力結果：
```
[['Region', 'Store'], ['Central', 3055], ['East', 3036]]
```
{{< app/cells/assistant language="python-net" >}}
