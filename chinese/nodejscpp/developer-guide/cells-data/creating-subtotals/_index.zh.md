---
title: 创建分类汇总
type: docs
weight: 800
url: /zh/nodejs-cpp/creating-subtotals/
description: 学习如何使用Aspose.Cells for Node.js via C++ API为电子表格中的任何重复值创建小计。
keywords: 应用小计、设置小计、添加小计、创建小计、如何向工作表添加小计 
---

{{% alert color="primary" %}}

你可以自动为电子表格中的任何重复值创建小计。Aspose.Cells for Node.js via C++提供API功能，帮助你以编程方式在电子表格中添加小计。

{{% /alert %}}

## **使用Microsoft Excel**

在Microsoft Excel中添加小计：

1. 在工作簿的第一个工作表中创建一个简单的数据列表（如下图所示），并将文件保存为 Book1.xls。
1. 选择列表中的任何单元格。
1. 从**数据**菜单中选择**小计**。将显示小计对话框。定义要使用的函数和放置小计的位置。

## **使用Aspose.Cells for Node.js via C++ API**

Aspose.Cells for Node.js via C++提供一个类[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)，表示一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)集合，允许访问Excel文件中的每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类表示。该类提供了广泛的属性和方法来管理工作表和其他对象。每个工作表都包含一个[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)集合。要向工作表添加小计，请使用[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)类的[**subtotal**](https://reference.aspose.com/cells/nodejs-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-)方法。向该方法提供参数值以指定如何计算和放置小计。

以下示例中，我们使用Aspose.Cells for Node.js via C++ API在[模板文件](book1.xlsx)的第一个工作表中添加了小计。当代码执行时，会创建一个带有小计的工作表。

以下代码片段展示了如何使用Aspose.Cells for Node.js via C++为工作表添加小计。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CreatingSubtotals-1.js" >}}

