---
title: Как установить точку как Общее с помощью Python.NET
linktitle: Как установить точку как Общее
type: docs
weight: 72
url: /ru/python-net/how-to-set-point-as-total/
description: Узнайте, как настраивать общие точки в водопадных диаграммах Excel с помощью Aspose.Cells для Python via .NET, следуя этому пошаговому руководству.
---

## **Что такое "Установка точки как Общее" в диаграмме Excel**

В некоторых диаграммах Excel, таких как водопадные диаграммы, некоторые точки данных представляют собой суммарное значение предыдущих. Эта статья показывает, как программно настроить эти итоговые точки с помощью Aspose.Cells.

## **Водопадная диаграмма с требованием общего пункта**

![todo:image_alt_text](set-as-total1.png)

Этот пример водопадной диаграммы показывает четыре пункта "Итого", которые должны агрегировать предыдущие значения. Выделенная точка "Итого 2024" демонстрирует не настроенное состояние итога в исходном файле. Скачать [пробный Excel файл](SampleSheet.xlsx), чтобы ознакомиться.

## **Настройка общих пунктов с помощью Aspose.Cells для Python**

Следующий код демонстрирует правильную настройку общего пункта:

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

Исправленный [выходной файл](output.xlsx) теперь правильно настраивает общие пункты:

![todo:image_alt_text](set-as-total2.png)

Ключевые детали реализации:
- Используйте индексы, начинающиеся с 0, для точек данных
- Устанавливайте свойство `is_total` у объектов `ChartPoint`
- Обеспечьте правильную настройку диапазона данных
- Проверка типа графика

Смотрите [документацию ChartPoint](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/) для расширенных настроек.
