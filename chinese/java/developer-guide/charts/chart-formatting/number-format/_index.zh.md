---
title: 设置图表系列的值格式代码
description: 学习如何设置Aspose.Cells for Java图表系列的值格式代码。我们的指南将帮助您了解如何使用适当的格式代码格式化您的图表系列数据，使您能够准确和专业地呈现您的数据。
keywords: Aspose.Cells for Java, 图表系列, 值格式代码, 格式化, 数据呈现, 准确性, 专业性。
linktitle: 数字格式
type: docs
weight: 100
url: /zh/java/set-the-values-format-code-of-chart-series/
---

## **可能的使用场景**
您可以使用[Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-) 方法设置图表系列的值格式代码。此方法不仅适用于基于工作表内范围的系列，而且适用于使用值数组创建的系列。
## **设置图表系列的值格式代码**
以下示例代码在之前没有系列的空图表中添加了一个系列。它使用值数组添加系列。一旦添加系列，它会使用代码$#,##0 使用[Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-) 方法格式化它，数字10000 变为$10,000。屏幕截图显示了代码在执行后对[sample Excel file](51740712.xlsx) 和[output Excel file](51740713.xlsx) 的影响。

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SetValuesFormatCodeOfChartSeries.java" >}}
{{< app/cells/assistant language="java" >}}
