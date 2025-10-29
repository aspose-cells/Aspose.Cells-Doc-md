---
title: Как сделать серию невидимой с помощью Python.NET
linktitle: Как сделать серию невидимой
type: docs
weight: 74
url: /ru/python-net/how-to-set-series-invisible/
description: Узнайте, как скрыть серию на графике в Excel с помощью Aspose.Cells для Python via .NET, следуя этому пошаговому руководству.
keywords: python excel график, скрыть серию, свойство is_filtered, Aspose.Cells Python
---

## **Как сделать серию невидимой на графике Excel**

В графике Excel вы можете щелкнуть правой кнопкой мыши по графику, выбрать "Выбрать данные" и в появившемся окне установить видимость серии, поставив или сняв галочку.
Вы можете скачать следующий [пример файла](SeriesFiltered.xlsx) и работать с ним в Excel, как показано на рисунке, чтобы достичь этой функции. Далее мы покажем, как выполнить это с помощью библиотеки Aspose.Cells для Python via .NET.

![todo:image_alt_text](series-invisible.png)

## **Как сделать серию невидимой с помощью Aspose.Cells**

 Используйте следующий код для установки серии как невидимой с помощью Aspose.Cells для Python via .NET:

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

Вы можете получить следующий [входной файл](SeriesFiltered.xlsx) и [выходной файл](output.xlsx).

На рисунке ниже видно, что первые две серии, которые были изначально видимы, стали невидимыми в итоговом файле.
![todo:image_alt_text](output.png)
{{< app/cells/assistant language="python-net" >}}
