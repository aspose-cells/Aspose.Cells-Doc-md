---
title: 设置图表系列的数值格式代码
description: 了解如何设置图表系列的值格式代码 Aspose.Cells for Java。我们的指南将帮助您了解如何使用适当的格式代码来格式化图表系列数据，使您能够准确、专业地呈现您的数据。
keywords: Aspose.Cells for Java, chart series, values format code, formatting, data presentation, accuracy, professionalism.
linktitle: 数字格式
type: docs
weight: 100
url: /zh/java/set-the-values-format-code-of-chart-series/
---
##  **可能的使用场景**
您可以使用以下命令设置图表系列的值格式代码[系列.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-)方法。此方法不仅适用于基于工作表内范围的系列，而且也适用于使用值数组创建的系列。
##  **设置图表系列的数值格式代码**
以下示例代码在之前没有系列的空图表中添加一个系列。它使用值数组添加系列。一旦添加了系列，它就会使用代码 $#,##0 对其进行格式化[系列.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-)方法，数字 10000 变为 $10,000。截图显示了代码的效果[Excel 文件示例](51740712.xlsx)和[输出Excel文件](51740713.xlsx)执行后。

![待办事项：图像_替代_文本](set-the-values-format-code-of-chart-series_1.png)
##  **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SetValuesFormatCodeOfChartSeries.java" >}}
