---
title: Python.NETを使用してポイントを合計に設定する方法
linktitle: ポイントを合計に設定する方法
type: docs
weight: 72
url: /ja/python-net/how-to-set-point-as-total/
description: Aspose.Cells for Python via .NETを使用してExcelウォーターフォールチャートの合計ポイントを設定する方法について、ステップバイステップガイドで解説します。
---

## **Excelの "ポイントを合計に設定" とは何ですか？**

ウォーターフォールチャートの例では、いくつかのデータポイントがこれまでの値の合計を表します。この記事では、Aspose.Cellsを使用してこれらの合計ポイントをプログラムで設定する方法を示します。

## **合計ポイントを必要とするウォーターフォールチャート例**

![todo:image_alt_text](set-as-total1.png)

このウォーターフォールチャート例では、「合計2024」のポイントを含む4つの"合計"データポイントが、前の値を集約しています。オリジナルのファイルでは、未設定の合計状態を示すハイライトされたポイントが確認できます。サンプルのExcelファイル（SampleSheet.xlsx）をダウンロードして、操作を進めてください。

## **Aspose.Cells for Pythonを使用した合計ポイントの設定**

次のコードは適切な合計ポイントの設定を示しています：

```python
import aspose.cells as cells
from aspose.cells.charts import ChartType

# Load sample workbook
workbook = cells.Workbook("SampleSheet.xlsx")

try:
    # Access first worksheet and chart
    worksheet = workbook.worksheets[0]
    chart = worksheet.charts[0]

    # Verify chart type
    if chart.type == ChartType.WATERFALL:
        # Configure chart data range
        chart.set_data_range("A1:B8", True)

        # Customize series formatting
        chart.n_series.is_color_varied = True

        # Configure total points (0-based indices)
        total_points = [3, 5, 7]  # Points to mark as totals
        for i in total_points:
            point = chart.n_series.points[i]
            point.is_total = True

        # Save modified workbook
        workbook.save("output.xlsx")

except Exception as e:
    print(f"Error processing workbook: {str(e)}")
```

```python
import os
from aspose.cells import Workbook

file_path = ""
wb = Workbook(os.path.join(file_path, "SampleSheet.xlsx"))
worksheet = wb.worksheets[0]
chart = worksheet.charts.get("Graphiq5")

# Set some points as total column
# In this example, we set points 0, 4, 8, 12 as total
chart.n_series[0].layout_properties.subtotals = [0, 4, 8, 12]
wb.save(os.path.join(file_path, "output.xlsx"))
```

修正された[出力ファイル](output.xlsx)は、合計ポイントを正しく設定しています：

![todo:image_alt_text](set-as-total2.png)

主な実装詳細：
- データポイントには0ベースのインデックスを使用
- `ChartPoint`オブジェクトに`is_total`プロパティを設定
- 適切なデータ範囲設定を確認
- チャートタイプの検証を行う

高度な設定オプションについては[ChartPointドキュメント](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/)を参照してください。
