---
title: 通过Python.NET降低单元格Calculate方法的计算时间
linktitle: 降低单元格Calculate的计算时间
type: docs
weight: 100
url: /zh/python-net/decrease-the-calculation-time-of-cell-calculate-method/
description: 了解如何使用Aspose.Cells for Python via .NET优化Excel单元格计算性能。通过设置CalculationOptions，减少计算时间。
keywords: python excel计算，优化单元格计算，Aspose.Cells Python，计算性能，递归计算选项
---

## **可能的使用场景**

通常，我们建议用户调用[**workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/)方法一次，然后获取个别单元格的计算值。在处理单一单元格计算时，你可以使用[**calculation_options.recursive**](https://reference.aspose.com/cells/python-net/aspose.cells/calculationoptions/recursive/)属性显著减少计算时间。将此属性设置为`False`可以阻止后续调用时重新计算依赖的单元格。

## **优化单元格计算性能**

以下示例演示了使用递归属性。使用提供的[示例Excel文件](5113710.xlsx)测试性能差异。代码显示了设置`recursive=False`如何通过避免冗余依赖单元格重新计算来减少计算时间。

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

## **性能基准测试结果**

运行带有示例文件的优化代码时的典型输出显示显著的时间缩短：

{{< highlight text >}}
Recursive True: 96 seconds
Recursive False: 42 seconds
{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
