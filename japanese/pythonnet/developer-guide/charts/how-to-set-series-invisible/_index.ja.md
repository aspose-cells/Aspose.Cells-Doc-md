---
title: Python.NETを使ったシリーズの非表示設定方法
linktitle: シリーズを非表示にする方法
type: docs
weight: 74
url: /ja/python-net/how-to-set-series-invisible/
description: Aspose.Cells for Python via .NETを使用してExcelのチャートシリーズを非表示にするステップバイステップガイドです。
keywords: Python Excelチャート、シリーズ非表示、is_filteredプロパティ、Aspose.Cells Python
---

## **Excelチャートでシリーズを非表示に設定する方法**

Excelのチャートで右クリックし、「データの選択」をクリックすると、ポップアップウィンドウでシリーズの表示・非表示を設定できます。
以下の[サンプルファイル](SeriesFiltered.xlsx)をダウンロードし、図のように操作してこの機能を実現できます。次に、Aspose.Cells for Python via .NETライブラリを使ってこれを達成する方法を説明します。

![todo:image_alt_text](series-invisible.png)

## **Aspose.Cellsを使ったシリーズの非表示設定方法**

Aspose.Cells for Python via .NETを使ってシリーズを非表示にするには、以下のコードを使用します：

```python
import os
from aspose.cells import Workbook

current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Load sample workbook
workbook = Workbook(os.path.join(data_dir, "SeriesFiltered.xlsx"))

# Access charts from first worksheet
charts = workbook.worksheets[0].charts
chart = charts.get("Chart 1")

# Get series collections
n_series_filtered = chart.filtered_n_series
n_series = chart.n_series

# Filter series by marking them as filtered
n_series[1].is_filtered = True
n_series[0].is_filtered = True

# Save modified workbook
workbook.save(os.path.join(data_dir, "output.xlsx"))
```

以下の[入力ファイル](SeriesFiltered.xlsx)と[出力ファイル](output.xlsx)を取得できます。

下図に示すように、もともと表示されていた最初の2つのシリーズが出力ファイルで非表示になっています。
![todo:image_alt_text](output.png)
{{< app/cells/assistant language="python-net" >}}
