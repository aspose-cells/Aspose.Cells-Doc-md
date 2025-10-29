---
title: 设置图表系列的值格式代码
description: 学习如何设置图表系列的数值格式代码在 Aspose.Cells for Python via .NET。我们的指南将帮助你理解如何使用合适的格式代码格式化图表系列数据，从而准确、专业地展示你的数据。
keywords: Aspose.Cells for Python via .NET，图表系列，数值格式代码，格式化，数据呈现，准确性，专业性。
linktitle: 数字格式
type: docs
weight: 100
url: /zh/python-net/set-the-values-format-code-of-chart-series/
---

## **可能的使用场景**
你可以使用 [Series.values_format_code](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series/values_format_code) 属性设置图表系列的数值格式代码。此属性不仅适用于基于工作表范围的系列，也适用于使用数值数组创建的系列。

## **设置图表系列的值格式代码**
以下示例代码在一个之前没有系列的空图表中添加了一个系列。它通过数值数组添加系列。添加后，使用 [Series.values_format_code](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series/values_format_code) 属性将其格式化为 $#,##0，数字10000变为$10,000。截图显示了代码对[示例Excel文件](51740712.xlsx)和[输出Excel文件](51740713.xlsx)的效果。

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **示例代码**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SetValuesFormatCodeOfChartSeries.py" >}}
{{< app/cells/assistant language="python-net" >}}
