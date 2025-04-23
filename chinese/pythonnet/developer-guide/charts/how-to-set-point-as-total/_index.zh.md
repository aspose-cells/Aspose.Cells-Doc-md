---
title: 如何用 Python.NET 将点设置为总和
linktitle: 如何设置点为总和
type: docs
weight: 72
url: /zh/python-net/how-to-set-point-as-total/
description: 学习如何使用 Aspose.Cells for Python via .NET 逐步配置Excel瀑布图中的总点。
---

## **Excel图表中的“设置点为总和”是什么意思**

在某些Excel图表如瀑布图中，某些数据点代表之前值的累计总和。本文演示如何使用 Aspose.Cells 编程配置这些总点。

## **需要总点的瀑布图**

![todo:image_alt_text](set-as-total1.png)

此瀑布图示例显示了四个“总计”数据点，应汇总先前的值。突出显示的“Total 2024”点演示了未配置的总和状态。下载[示例Excel文件](SampleSheet.xlsx)以便跟随操作。

## **使用 Aspose.Cells for Python 配置总分数**

以下代码演示了正确的总分数配置：

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

已修正的[输出文件](output.xlsx) 现已正确配置总分数：

![todo:image_alt_text](set-as-total2.png)

关键实现细节：
- 使用0为起点的索引表示数据点
- 在 `ChartPoint` 对象上设置 `is_total` 属性
- 确保正确的数据范围配置
- 处理图表类型验证

查看 [ChartPoint 文档](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/) 获取高级配置选项。
