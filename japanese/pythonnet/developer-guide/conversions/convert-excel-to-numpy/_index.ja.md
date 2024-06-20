---
title: ExcelをNumPyに変換
type: docs
weight: 30
url: /ja/python-net/convert-excel-to-numpy/
description: Aspose.Cells for Python via .NET APIを使用してExcelをNumPy配列に変換し、PythonでワークブックをNumPy配列にエクスポートし、行をNumPy配列に変換し、NumPy配列にテーブルを変換し、ListObjectをNumPy配列にエクスポートし、範囲をNumPy配列に変換し、Pythonを使用した浮動小数点配列への列変換
keywords: PythonでExcelファイルをNumPy配列に変換し、PythonでワークブックをNumPy配列にエクスポートする方法を、以下のようなものがあります via NET、Pythonで行をNumPy配列に変換する方法、PythonでテーブルをNumPy配列に変換する方法、PythonでListObjectをNumPy配列にエクスポートする方法 via NET、Pythonで範囲をNumPy配列に変換する方法、Pythonを使用してColumnをNumPy配列に変換します。
---

## **NumPyの紹介**
NumPy（Numerical Python）はPythonのオープンソースの数値演算拡張です。このツールは大きな行列を保存および処理するために使用でき、Pythonの階層リスト構造よりも効率的です（行列を表すためにも使用できます）。多数の次元配列および行列演算をサポートし、また、配列操作のための多数の数学関数ライブラリを提供します。 

NumPyの主な機能：
1. Ndarrayは、高速で柔軟性があり、データ構造を節約する多次元配列オブジェクトです。
1. 行列乗算、転置、逆行列などの線形代数演算。
1. 高速フーリエ変換、配列上で高速フーリエ変換を行います。
1. 浮動小数点配列の高速操作。
1. C言語コードをPythonに統合し、より速く実行します。

Aspose.Cells for Python via .NET APIを使用すると、Excel、TSV、CSV、Jsonなどのさまざまな形式をNumPy ndarrayに変換できます。

## **ExcelワークブックをNumPy ndarrayに変換する方法**
Aspose.Cells for Python via .NETを使用してExcelデータをNumPy配列にエクスポートするコードスニペットの例を次に示します:
1. [サンプルファイル](sample_data.xlsx)をロードします。
1. Aspose.Cells for Python via .NETを使用してExcelデータをトラバースし、データをNumPy ndarrayにエクスポートします。


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-NDArray.py" >}}

出力結果：
```
[[['City' 'Region' 'Store']    
  ['Chicago' 'Central' '3055'] 
  ['New York' 'East' '3036']   
  ['Detroit' 'Central' '3074']]

 [['City2' 'Region2' 'Store3']
  ['Seattle' 'West' '3000']
  ['philadelph' 'East' '3082']
  ['Detroit' 'Central' '3074']]

 [['City3' 'Region3' 'Store3']
  ['Seattle' 'West' '3166']
  ['New York' 'East' '3090']
  ['Chicago' 'Central' '3055']]]
```

## **ワークシートをNumPy ndarrayに変換する方法**
Aspose.Cells for Python via .NETを使用してワークシートデータをNumpy ndarrayにエクスポートするコードスニペットの例を次に示します:
1. [サンプルファイル](sample_data.xlsx)をロードします。
1. 最初のワークシートを取得します。
1. Aspose.Cells for Python Excelライブラリを使用してワークシートデータをNumpy ndarrayに変換します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Worksheet-to-NDArray.py" >}}

出力結果：
```
[['City' 'Region' 'Store']    
 ['Chicago' 'Central' '3055'] 
 ['New York' 'East' '3036']   
 ['Detroit' 'Central' '3074']]
```
## **Excelの範囲をNumPy ndarrayに変換する方法**
Aspose.Cells for Pythonを使用して範囲データをNumPy ndarrayにエクスポートする方法を示すコードスニペットの例ですvia .NET。
1. [サンプルファイル](sample_data.xlsx)をロードします。
1. 最初のワークシートを取得します。
1. 範囲を作成します。
1. Aspose.Cells for Python Excelライブラリを使用して範囲データをNumPy ndarrayに変換します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Range-to-NDArray.py" >}}

出力結果：
```
[['Region' 'Store']
 ['Central' '3055']
 ['East' '3036']]
```

## **ExcelのListObjectをNumPy ndarrayに変換する方法**
Aspose.Cells for Pythonを使用してListObjectデータをNumPy ndarrayにエクスポートする方法を示すコードスニペットの例ですvia .NET。
1. [サンプルファイル](sample_data.xlsx)をロードします。
1. 最初のワークシートを取得します。
1. ListObjectオブジェクトを作成します。
1. Aspose.Cells for Python Excelライブラリを使用してListObjectデータをNumPy ndarrayに変換します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-ListObject-to-NDArray.py" >}}

出力結果：
```
[['City' 'Region' 'Store']
 ['Chicago' 'Central' '3055']
 ['New York' 'East' '3036']
 ['Detroit' 'Central' '3074']]
```

## **Excelの行をNumPy ndarrayに変換する方法**
Aspose.Cells for Pythonを使用して行データをNumPy ndarrayにエクスポートする方法を示すコードスニペットの例ですvia .NET。
1. [サンプルファイル](sample_data.xlsx)をロードします。
1. 最初のワークシートを取得します。
1. 行インデックスで行オブジェクトを取得します。
1. Aspose.Cells for Python Excelライブラリを使用して行データをNumPy ndarrayに変換します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Row-to-NDArray.py" >}}

出力結果：
```
['Detroit' 'Central' '3074']
```

## **Excelの列をNumPy ndarrayに変換する方法**
Aspose.Cells for Pythonを使用して列データをNumPy ndarrayにエクスポートする方法を示すコードスニペットの例ですvia .NET。
1. [サンプルファイル](sample_data.xlsx)をロードします。
1. 最初のワークシートを取得します。
1. 列インデックスで列オブジェクトを取得します。
1. Aspose.Cells for Python Excelライブラリを使用して列データをNumPy ndarrayに変換します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Column-to-NDArray.py" >}}

出力結果：
```
['Store' '3055' '3036' '3074']
```
