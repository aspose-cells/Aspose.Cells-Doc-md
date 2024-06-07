---
title: 设置图表系列的值格式代码
description: 学习如何在Aspose.Cells for Java中设置图表系列的值格式代码。我们的指南将帮助您了解如何使用适当的格式代码格式化图表系列数据，从而能够准确、专业地呈现数据。
keywords: Aspose.Cells for Java, 图表系列, 值格式代码, 格式化, 数据呈现, 准确性, 专业性。
linktitle: 数字格式
type: docs
weight: 100
url: /zh/java/set-the-values-format-code-of-chart-series/
---

## **可能的使用场景**
您可以使用[Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-)方法设置图表系列的值格式代码。此方法不仅适用于基于工作表内范围的系列，还适用于使用值数组创建的系列。
## **设置图表系列的值格式代码**
以下示例代码在没有系列的空图表中添加了一个系列。它使用值数组添加了系列。添加系列后，使用[Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-)方法以代码$#,##0进行格式化，数字10000将变为$10,000。屏幕截图显示了代码在执行后的[示例Excel文件](51740712.xlsx)和[输出Excel文件](51740713.xlsx)上的效果。

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SetValuesFormatCodeOfChartSeries.java" >}}
