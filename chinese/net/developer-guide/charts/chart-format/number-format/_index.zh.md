---
title: 设置图表系列的值格式代码
description: 了解如何在Aspose.Cells for .NET中设置图表系列数据的值格式代码。我们的指南将帮助您了解如何使用适当的格式代码格式化图表系列数据，使您能够准确、专业地展示您的数据。
keywords: Aspose.Cells for .NET，图表系列，值格式代码，格式化，数据呈现，准确性，专业性。
linktitle: 数字格式
type: docs
weight: 100
url: /zh/net/set-the-values-format-code-of-chart-series/
---

## **可能的使用场景**
您可以使用[Series.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode)属性设置图表系列的值格式代码。该属性不仅适用于基于工作表内范围的系列，而且对于使用值数组创建的系列也很有效。
## **设置图表系列的值格式代码**
以下示例代码向空图表中添加一个系列，该系列之前没有任何系列。它使用值数组添加系列。一旦添加了系列，就使用$#,##0代码格式化它，使用[Series.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode)属性，数字10000变为$10,000。截图展示了代码在执行后对[sample Excel file](51740712.xlsx)和[output Excel file](51740713.xlsx)的影响。

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetValuesFormatCodeOfChartSeries.cs" >}}
