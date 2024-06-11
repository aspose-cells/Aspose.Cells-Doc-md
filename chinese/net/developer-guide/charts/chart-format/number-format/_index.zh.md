---
title: 设置图表系列的值格式代码
description: 学习如何设置Aspose.Cells for .NET中图表系列的值格式代码。我们的指南将帮助您了解如何使用适当的格式代码对图表系列数据进行格式化，从而可以准确、专业地呈现您的数据。
keywords: Aspose.Cells for .NET，图表系列，值格式代码，格式化，数据呈现，准确性，专业性。
linktitle: 数字格式
type: docs
weight: 100
url: /zh/net/set-the-values-format-code-of-chart-series/
---

## **可能的使用场景**
您可以使用[Series.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode)属性设置图表系列的值格式代码。此属性不仅对基于工作表内范围的系列有用，还可用于基于数值数组创建的系列。
## **设置图表系列的值格式代码**
以下示例代码在空图表中添加了一个系列，该图表之前没有系列。它使用数值数组添加了系列。添加系列后，它使用$#,##0代码进行格式化，使用[Series.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode)属性，数字10000变成$10,000。屏幕截图显示了代码在执行后对[sample Excel file](51740712.xlsx)和[output Excel file](51740713.xlsx)的影响。

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetValuesFormatCodeOfChartSeries.cs" >}}
