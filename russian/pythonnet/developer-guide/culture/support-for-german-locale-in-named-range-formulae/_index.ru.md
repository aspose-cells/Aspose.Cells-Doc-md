---
title: Поддержка немецкой локализации для формул с именными диапазонами с использованием Python.NET
linktitle: Поддержка немецкой локали в формулах для именованных диапазонов
type: docs
weight: 60
url: /ru/python-net/support-for-german-locale-in-named-range-formulae/
description: Узнайте, как обрабатывать настройки немецкой локали для формул с именованными диапазонами в Excel с помощью Aspose.Cells для Python via .NET.
---

Английские формулы записываются в именованные области. Этот файл Excel можно открыть в среде, настроенной на немецкую локаль, и английская формула будет переведена на немецкий язык. Для этого примера необходимо установить Excel с настройками немецкого языка и системой, настроенной на немецкую локаль.

Образец файла для тестирования этой функции можно скачать с:  
[sampleNamedRangeTest.xlsm](73990165.xlsm)

```python
import os
from aspose.cells import Workbook

source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "source")
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")

name = "HasFormula"
value = "=GET.CELL(48, INDIRECT(\"ZS\",FALSE))"

wb_source = Workbook(os.path.join(source_dir, "sampleNamedRangeTest.xlsm"))
ws_col = wb_source.worksheets

name_index = ws_col.names.add(name)
named_range = ws_col.names[name_index]
named_range.refers_to = value

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

wb_source.save(os.path.join(output_dir, "sampleOutputNamedRangeTest.xlsm"))
```
