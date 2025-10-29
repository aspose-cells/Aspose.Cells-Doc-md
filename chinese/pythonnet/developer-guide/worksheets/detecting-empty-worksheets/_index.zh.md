---
title: 检测空工作表
type: docs
weight: 410
url: /zh/python-net/detecting-empty-worksheets/
description: 本文提供了示例代码，说明如何使用 Aspose.Cells for Python via .NET 库程序化检测Excel工作簿中的空白工作表。
keywords: Python Excel 库，使用python检测空工作表，查找Python中的空Excel工作表。
---

## **检查已填充的单元格**

工作表中可以填充一个或多个单元格的值，其中值可以是简单的（文本、数字、日期/时间）或公式或基于公式的值。在这种情况下，很容易检测给定工作表是否为空。我们只需检查[**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/)或[**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/)属性。如果上述属性返回零或正值，那么表示一个或多个单元格已被填充，但如果其中任何一个属性返回-1，那就表示给定工作表中没有填充任何单元格。

{{% alert color="primary" %}}

行和列的集合具有从零开始的索引，因此行0和列0的单元格表示工作表中的第一个单元格，即A1。

{{% /alert %}}

## **检测空初始化单元格**

所有有值的单元格都会自动初始化，但也存在工作表中只有格式应用的单元格。在这种情况下，[**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/) 或 [**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/) 属性会返回 -1，表示没有已填充值，但由于单元格格式造成的已初始化单元格无法通过此方法检测。要检查工作表是否有空的已初始化单元格，建议使用从 [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合中获取的枚举器调用 IEnumerator.MoveNext 方法。如果方法返回 **true**，意味着工作表中存在一个或多个已初始化的单元格。

## **检查形状**

某个工作表可能没有任何已填充的单元格，但可能包含形状和对象，如控件、图表、图片等。如果需要检查工作表中是否包含任何形状，可以通过检查 [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) 元素来实现。任何正值都表示工作表中存在形状。

## **编程示例**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-DetectEmptyWorksheets.py" >}}
{{< app/cells/assistant language="python-net" >}}
