---
title: Ускорьте время расчетов метода Cell.Calculate с помощью Python.NET
linktitle: Ускорьте расчет времени Cell.Calculate
type: docs
weight: 100
url: /ru/python-net/decrease-the-calculation-time-of-cell-calculate-method/
description: Узнайте, как улучшить производительность расчетов ячеек Excel, используя Aspose.Cells для Python via .NET. Уменьшите время вычислений с помощью настроек CalculationOptions.
keywords: расчет Excel на Python, оптимизация расчетов ячеек, Aspose.Cells Python, производительность расчетов, рекурсивные опции расчета
---

## **Возможные сценарии использования**

Обычно рекомендуется вызывать метод [**workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) один раз и затем получать вычисленные значения отдельных ячеек. При работе с расчетами для одной ячейки можно использовать свойство [**calculation_options.recursive**](https://reference.aspose.com/cells/python-net/aspose.cells/calculationoptions/recursive/), чтобы значительно сократить время вычислений. Установка этого свойства в значение `False` предотвращает перерасчет зависимых ячеек при последующих вызовах.

## **Оптимизация производительности расчетов ячеек**

Следующий пример демонстрирует использование рекурсивного свойства. Используйте предоставленный [пример файла Excel](5113710.xlsx) для тестирования разницы в производительности. Код показывает, как установка `recursive=False` уменьшает время расчетов, избегая избыточных перерасчетов зависимых ячеек.

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

## **Результаты тестирования производительности**

Типичный результат при запуске оптимизированного кода с использованием примерного файла показывает значительное сокращение времени:

{{< highlight text >}}
Recursive True: 96 seconds
Recursive False: 42 seconds
{{< /highlight >}}
