---
title: تقليل وقت حساب طريقة Cell.Calculate باستخدام Python.NET
linktitle: تقليل وقت حساب Cell.Calculate
type: docs
weight: 100
url: /ar/python-net/decrease-the-calculation-time-of-cell-calculate-method/
description: تعلم كيف تقوم بتحسين أداء حساب خلايا إكسل باستخدام Aspose.Cells لبايثون via .NET. قلل وقت العمليات الحسابية بضبط إعدادات CalculationOptions.
keywords: حساب إكسل بايثون، تحسين حساب الخلايا، Aspose.Cells بايثون، أداء الحساب، خيارات الحساب التكراري
---

## **سيناريوهات الاستخدام المحتملة**

 عادةً، نوصي المستخدمين باستدعاء طريقة [**workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) مرة واحدة ثم الحصول على القيم المحسوبة للخلايا الفردية. عند العمل مع حساب خلايا فردية، يمكنك استخدام الخاصية [**calculation_options.recursive**](https://reference.aspose.com/cells/python-net/aspose.cells/calculationoptions/recursive/) لتقليل زمن الحساب بشكل كبير. ضبط هذه الخاصية إلى `False` يمنع إعادة حساب الخلايا المعتمدة في الاستدعاءات التالية.

## **تحسين أداء حساب الخلايا**

يعرض المثال التالي استخدام الخاصية التكرارية. يمكنك استخدام ملف إكسل النموذجي المقدم للاختبار لمقارنة الأداء. يوضح الكود كيف أن ضبط `recursive=False` يقلل من وقت الحساب بتجنب إعادة حساب الخلايا المعتمدة بشكل مكرر.

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

## **نتائج قياس الأداء**

النتيجة النموذجية عند تشغيل الكود المُحسن مع الملف النموذجي تُظهر تقليلًا كبيرًا في الوقت:

{{< highlight text >}}
Recursive True: 96 seconds
Recursive False: 42 seconds
{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
