---
title: Расчет функций MINIFS и MAXIFS Excel 2016 с помощью Python.NET
linktitle: Вычисление функций MINIFS и MAXIFS Excel 2016
type: docs
weight: 300
url: /ru/python-net/calculation-of-excel-2016-minifs-and-maxifs-functions/
description: Научитесь рассчитывать функции MINIFS и MAXIFS Excel 2016 с помощью API Aspose.Cells для Python via .NET с примерами кода.
keywords: python excel, minifs maxifs, расчет формул, aspose.cells
---

## **Возможные сценарии использования**
Excel 2016 поддерживает функции MINIFS и MAXIFS. Эти функции не поддерживаются в Excel 2013 или более ранних версиях. Aspose.Cells также поддерживает расчет этих функций. Следующий скриншот иллюстрирует использование этих функций. Пожалуйста, читайте красные комментарии внутри скриншота, чтобы понять, как работают эти функции.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Расчет функций MINIFS и MAXIFS Excel 2016**
Следующий пример кода загружает [пример файла Excel](5115149.xlsx) и вызывает метод [workbook.calculate_formula()](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) для выполнения расчетов формул через Aspose.Cells, затем сохраняет результаты в [выходной PDF](5115154.pdf).


```python
import os
from aspose.cells import Workbook, PdfSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET

current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, "data")
output_dir = os.path.join(current_dir, "output")

# Load your source workbook containing MINIFS and MAXIFS functions
workbook = Workbook(os.path.join(source_dir, "sampleMINIFSAndMAXIFS.xlsx"))

# Perform Aspose.Cells formula calculation
workbook.calculate_formula()

# Save the calculations result in pdf format
options = PdfSaveOptions()
options.one_page_per_sheet = True

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

workbook.save(os.path.join(output_dir, "outputMINIFSAndMAXIFS.pdf"), options)
```
