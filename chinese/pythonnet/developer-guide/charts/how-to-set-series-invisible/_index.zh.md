---
title: 如何用 Python.NET 设置系列隐藏
linktitle: 如何设置系列不可见
type: docs
weight: 74
url: /zh/python-net/how-to-set-series-invisible/
description: 学习如何使用 Aspose.Cells for Python via .NET 隐藏 Excel 中的图表系列，这里有详细的步骤指南。
keywords: python excel 图表，隐藏系列，is_filtered 属性，Aspose.Cells Python
---

## **如何在 Excel 图表中设置系列为隐藏状态**

在 Excel 图表中，您可以右键点击图表，然后选择“选择数据”，在弹出窗口中，勾选或取消勾选系列以控制其是否显示。
您可以下载以下[示例文件](SeriesFiltered.xlsx)，并在 Excel 中按照图示操作实现该功能。接下来，我们将展示如何使用 Aspose.Cells for Python via .NET 实现此操作。

![todo:image_alt_text](series-invisible.png)

## **如何使用 Aspose.Cells 设置系列不可见**

使用以下代码，用 Aspose.Cells for Python via .NET 设置系列不可见：

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

你可以获取以下[输入文件](SeriesFiltered.xlsx)和[输出文件](output.xlsx)。

如下图所示，原本可见的前两个系列在输出文件中变为不可见。
![todo:image_alt_text](output.png)
{{< app/cells/assistant language="python-net" >}}
