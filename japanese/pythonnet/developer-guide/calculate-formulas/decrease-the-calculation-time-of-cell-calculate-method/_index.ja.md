---
title: Python.NETを使用したセル.Calculateメソッドの計算時間短縮
linktitle: セル.Calculateの計算時間短縮
type: docs
weight: 100
url: /ja/python-net/decrease-the-calculation-time-of-cell-calculate-method/
description: Aspose.Cells for Python via .NETを使用してExcelセルの計算パフォーマンスを最適化する方法を学ぶ。CalculationOptions設定で計算時間を短縮。
keywords: Python Excel計算、セル計算の最適化、Aspose.Cells Python、計算パフォーマンス、再帰的計算オプション
---

## **可能な使用シナリオ**

通常、ユーザーには[**workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/)メソッドを一度呼び出し、その後個々のセルの値を取得することをお勧めします。単一セルの計算作業では、[**calculation_options.recursive**](https://reference.aspose.com/cells/python-net/aspose.cells/calculationoptions/recursive/)プロパティを使用することで計算時間を大幅に短縮できます。このプロパティを`False`に設定すると、後続の呼び出し時に依存セルの再計算を防ぎます。

## **セル計算パフォーマンスの最適化**

以下のサンプルは再帰プロパティの使用例を示します。[サンプルExcelファイル](5113710.xlsx)を使用してパフォーマンスの違いをテストしてください。コードは`recursive=False`に設定することで冗長な依存セルの再計算を避け、計算時間を短縮する方法を示しています。

```python
# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# Test calculation time after setting recursive true
test_calc_time_recursive(True)

# Test calculation time after setting recursive false
test_calc_time_recursive(False)
```

```python
import os
import time
from aspose.cells import Workbook, CalculationOptions

def test_calc_time_recursive(rec):
    """
    Tests calculation time with recursive option and prints elapsed seconds
    """
    # The path to the documents directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "data")

    # Load sample workbook
    wb = Workbook(os.path.join(data_dir, "sample.xlsx"))

    # Access first worksheet
    ws = wb.worksheets[0]

    # Set calculation options
    opts = CalculationOptions()
    opts.recursive = rec

    # Start timing
    start_time = time.perf_counter()

    # Calculate cell A1 one million times
    for _ in range(1000000):
        ws.cells.get("A1").calculate(opts)

    # Calculate elapsed time
    elapsed_time = int(time.perf_counter() - start_time)

    # Print results
    print(f"Recursive {rec}: {elapsed_time} seconds")
```

## **パフォーマンスベンチマーク結果**

サンプルファイルを使用した最適化コードの実行例では、時間短縮が顕著に示されます：

{{< highlight text >}}
Recursive True: 96 seconds
Recursive False: 42 seconds
{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
