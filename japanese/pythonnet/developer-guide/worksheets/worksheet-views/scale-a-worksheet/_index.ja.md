---
title: Python.NETを使用したワークシートの縮尺方法
linktitle: ワークシートを縮尺する方法
type: docs
weight: 130
url: /ja/python-net/how-to-scale-a-worksheet/
description: この資料は、Aspose.Cells for Python.NETを使用したワークシートの縮尺方法について説明します。
keywords: Pythonでのワークシートの縮尺、Python.NETでワークシートを縮尺、Pythonでページに合わせる、Pythonでワークシートの縮尺率、Aspose.Cells Pythonのワークシート縮尺
---

## **可能な使用シナリオ**
ワークシートの縮尺は、作業するコンテキストによってさまざまな理由で便利です。一般的な理由をいくつか挙げます：
1. **ページに合わせる**：印刷時にすべての内容が単一ページまたは特定のページ数に収まるようにするため。
1. **プレゼンテーション**：整理されていてプロフェッショナルな見た目にして共有を容易にするため。
1. **読みやすさ**：視覚的アクセシビリティを向上させるためにテキストや要素のサイズを調整する。
1. **空間管理**：ワークシートのレイアウトを最適化し、不必要な白スペースを最小限に抑える。
1. **データ可視化**：チャートやグラフのサイズを利用可能なスペースに合わせて適切に調整する。
1. **一貫性**：複数のワークシートやドキュメント間で統一された外観を維持するため。

## **Excelでワークシートを縮尺する方法**
Excelでワークシートを縮尺すると、印刷時に内容を指定されたページに収めることができます。以下の手順に従ってください：

1. Excelでワークシートを開きます
1. **ページレイアウト** > **縮尺調整**グループに移動
1. ページ数の要件に合わせて[幅]と[高さ]を調整
1. 必要に応じてカスタムスケーリングパーセンテージを設定
<br>
<img src="1.png" width=60% />

## **Python.NETを使用したワークシートのスケール方法**
Aspose.Cells for Python.NETは包括的なワークシートスケーリング機能を提供します。これらの方法を使用して、プログラム的にワークシートをスケールします：

### **ページに合わせてフィット例**
指定したページに内容をフィットさせるために印刷設定を調整：
```python
from aspose.cells import Workbook

# Load the Excel file
workbook = Workbook("sample.xlsx")

# Access the first worksheet
sheet = workbook.worksheets[0]

# Access the PageSetup object
page_setup = sheet.page_setup

# Set the worksheet to fit to 1 page wide and 1 page tall
page_setup.fit_to_pages_wide = 1
page_setup.fit_to_pages_tall = 1

# Save the modified workbook
workbook.save("output_fit_to_page.xlsx")
```
<br>
<img src="3.png" width=60% />

### **パーセンテージに合わせてスケール例**
ワークシートの内容にカスタムスケーリングパーセンテージを適用：
```python
from aspose.cells import Workbook

# Load the Excel file
workbook = Workbook("sample.xlsx")

# Access the first worksheet
sheet = workbook.worksheets[0]

# Access the PageSetup object
page_setup = sheet.page_setup

# Set the scaling to a specific percentage (e.g., 75%)
page_setup.zoom = 75

# Save the modified workbook
workbook.save("output_scaled_percentage.xlsx")
```
<br>
<img src="2.png" width=60% />

**主要APIリファレンス:**
- [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) クラス
- [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) クラス
- [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/) 構成
