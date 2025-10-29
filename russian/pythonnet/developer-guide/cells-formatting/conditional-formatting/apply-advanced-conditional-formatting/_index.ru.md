---
title: Применение расширенного условного форматирования с помощью Python.NET
linktitle: Применение расширенного условного форматирования
type: docs
weight: 70
url: /ru/python-net/apply-advanced-conditional-formatting/
description: Изучите, как реализовать расширенные функции условного форматирования Excel, такие как полосы данных, цветовые шкалы и наборы значков, с помощью Aspose.Cells для Python via .NET.
keywords: Форматирование Excel в Python, условное форматирование Python, полосы данных Python, цветовые шкалы Python, наборы значков Python, Aspose.Cells Python
---

{{% alert color="primary" %}} 

Microsoft Excel 2007 и более поздние версии (2010/2013/2016) предоставляют расширенные возможности условного форматирования, включая затенение ячеек, градиенты, цветные значки, стрелки, флаги и форматирование шрифтов.

{{% /alert %}} 

## **Реализуйте расширенное условное форматирование в файлах Excel**
Aspose.Cells для Python via .NET поддерживает все расширенные функции условного форматирования, включая:

- Добавлять заштрихованные полосы данных для графического улучшения базовых чисел, вставляя простую столбчатую диаграмму в ячейки.
- Автоматически заливать ячейки цветовыми шкалами на основе их отношения к значениям в других ячейках в диапазоне. По умолчанию наименьшее значение закрашивается красным, постепенно переходя к наибольшему значению зеленым.
- Используйте наборы значков аналогично цветовым шкалам, но вместо заливки ячеек добавляйте маленькие значки, такие как стрелки и светофоры, в ячейки.

Aspose.Cells полностью поддерживает условное форматирование, предоставляемое Microsoft Excel 2007 и более поздние версии в формате XLSX в реальном времени. В этом примере демонстрируется упражнение для продвинутых типов условного форматирования, включая IconSets, DataBars, Color Scales, TimePeriods, Top/Bottom и другие правила с различными наборами свойств.

- [**Adding Color Scale Conditional Formattings**](/cells/ru/python-net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [**Adding Above Average Conditional Formattings**](/cells/ru/python-net/how-to-add-above-average-conditional-formatting/)
- [**Adding DataBars Conditional Formattings**](/cells/ru/python-net/how-to-add-databars-conditional-formatting/)
- [**Adding IonSets Conditional Formattings**](/cells/ru/python-net/how-to-add-icon-sets-conditional-formatting/)
- [**Adding Text Conditional Formattings**](/cells/ru/python-net/how-to-add-text-conditional-formatting/)
- [**Adding TimePeriods Conditional Formattings**](/cells/ru/python-net/how-to-add-time-periods-conditional-formatting/)
- [**Adding Top10 Conditional Formattings**](/cells/ru/python-net/how-to-add-top10-conditional-formatting/)



### **Рассчитайте выбор цвета Excel для форматирования с цветовой шкалой**
Этот код показывает, как определить цвет, выбранный Excel для правил условного форматирования с цветовой шкалой:

```python
import os
from aspose.cells import Workbook
from aspose.pydrawing import Color

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-Python
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Instantiate a workbook object and open the template file
workbook = Workbook(os.path.join(data_dir, "Book1.xlsx"))
# Get the first worksheet
worksheet = workbook.worksheets[0]
# Get the A1 cell
a1 = worksheet.cells.get("A1")

# Get the conditional formatting resultant object
cfr1 = a1.get_conditional_formatting_result()
# Get the ColorScale resultant color object
c = cfr1.color_scale_result

# Read and print the color values
print(c.to_argb())
print(c.name)
```
{{< app/cells/assistant language="python-net" >}}
