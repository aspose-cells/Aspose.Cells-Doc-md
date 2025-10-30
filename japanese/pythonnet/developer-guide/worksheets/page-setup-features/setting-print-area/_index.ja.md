---
title: Python.NETを使った印刷範囲の設定方法
linktitle: 印刷範囲の設定方法
type: docs
weight: 200
url: /ja/python-net/how-to-set-print-area/
description: Aspose.Cells for Python via .NET を使ってExcelファイルの印刷範囲を設定・クリアする方法を学びます。
keywords: Pythonで印刷範囲を設定し、印刷範囲をクリアし、Python Excelの印刷設定、Aspose.cellsのPythonでの印刷範囲設定、Pythonでの印刷範囲制限
---

## **可能な使用シナリオ**

ドキュメントに印刷範囲を設定することは、印刷内容を制御するのに役立ちます。主な理由は次のとおりです：

1. 特定のデータに焦点を当てる：関連部分のみを印刷
1. レイアウトの改善：ページ全体をきれいに整理します
1. リソースの節約：用紙とインクの消費を削減
1. プロフェッショナルなプレゼンテーション：洗練された出力を確保
1. 一貫性：統一された印刷結果を維持

## **Excelで印刷範囲を設定する方法**

プログラムで印刷範囲を設定するには：

1. ワークシートのページ設定プロパティにアクセス
1. セル範囲表記を使用して印刷範囲を定義
1. 変更したワークブックを保存

```python
# Sample image reference remains unchanged
<img src="3.png" width=60% />
```

## **Excelで印刷範囲をクリアする方法**

印刷範囲の制約を解除するには：

1. ページ設定プロパティにアクセス
1. 印刷範囲を空の文字列にリセット
1. 変更を保存

```python
# Sample image reference remains unchanged
<img src="4.png" width=60% />
```

## **印刷範囲をクリアした後に何が起こるか**

印刷範囲をクリアすると次のようになります：

1. ワークシート全体のデフォルト印刷
1. 以前の範囲制約の除去
1. すべての書式設定されたセルを含む

## **Aspose.Cellsを使用した印刷範囲の設定方法**

ワークシートのページ設定を通じて印刷範囲を設定：

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("input.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Set print area to A1:D10
worksheet.page_setup.print_area = "A1:D10"

# Save modified workbook
workbook.save("output_set_print_area.xlsx")
```

```python
# Output image reference
<img src="1.png" width=60% />
```

## **Aspose.Cellsを使用した印刷範囲のクリア方法**

既存の印刷範囲の定義を解除：

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("input.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Clear print area
worksheet.page_setup.print_area = ""

# Save modified workbook
workbook.save("output_clear_print_area.xlsx")
```

```python
# Output image reference
<img src="2.png" width=60% />
```

```python
from aspose.cells import Workbook

# Load the workbook
workbook = Workbook("input.xlsx")

# Access the desired worksheet
worksheet = workbook.worksheets[0]

# Set the print area - specify the range you want to print
worksheet.page_setup.print_area = "A1:D10"

# Save the workbook
workbook.save("set_print_area.pdf")
```
```python
from aspose.cells import Workbook

# Load the workbook
workbook = Workbook("input.xlsx")

# Access the desired worksheet
worksheet = workbook.worksheets[0]

# Clear the print area
worksheet.page_setup.print_area = ""

# Save the workbook
workbook.save("clear_print_area.pdf")
```
{{< app/cells/assistant language="python-net" >}}
