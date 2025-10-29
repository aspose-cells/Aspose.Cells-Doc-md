---
title: 使用Golang通过C++设置图表系列的值格式代码
linktitle: 数字格式
type: docs
weight: 100
url: /zh/go-cpp/set-the-values-format-code-of-chart-series/
description: 学习如何在Aspose.Cells for C++中设置图表系列的值格式代码。我们的指南将帮助您理解如何使用适当的格式代码格式化图表系列数据，以便准确专业地呈现您的数据。
keywords: Aspose.Cells for C++，图表系列，值格式代码，格式，数据展示，准确性，专业性。
---

## **可能的使用场景**
 您可以使用[Series.GetValuesFormatCode()](https://reference.aspose.com/cells/go-cpp/series/getvaluesformatcode/)属性设置图表系列的值格式代码。该属性不仅适用于基于工作表范围的系列，还适用于使用值数组创建的系列。

## **设置图表系列的值格式代码**
 以下示例代码向之前没有系列的空白图表添加了一个系列。它使用值数组添加系列。一旦添加系列后，它会使用[Series.GetValuesFormatCode()](https://reference.aspose.com/cells/go-cpp/series/getvaluesformatcode/)属性将其格式化为$#,##0，数字10000变为$10,000。截图显示了代码在[示例Excel文件](51740712.xlsx)和[输出Excel文件](51740713.xlsx)中的效果。

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **示例代码**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NumberFormat.go" >}}
