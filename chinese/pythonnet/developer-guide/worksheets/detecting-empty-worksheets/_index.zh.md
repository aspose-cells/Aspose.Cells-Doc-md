---
title: 检测空工作表
type: docs
weight: 410
url: /zh/python-net/detecting-empty-worksheets/
description: 本文向您展示了如何使用Aspose.Cells for Python via .NET库以编程方式检测Excel工作簿中的空工作表的代码。
keywords: Python Excel库，使用Python检测空工作表，在Python中找到空的Excel工作表。
---

## **检查已填充的单元格**

工作表中可以填充一个或多个单元格的值，其中值可以是简单的（文本、数字、日期/时间）或公式或基于公式的值。在这种情况下，很容易检测给定工作表是否为空。我们只需检查[**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/)或[**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/)属性。如果上述属性返回零或正值，那么表示一个或多个单元格已被填充，但如果其中任何一个属性返回-1，那就表示给定工作表中没有填充任何单元格。

{{% alert color="primary" %}}

行和列的集合具有从零开始的索引，因此行0和列0的单元格表示工作表中的第一个单元格，即A1。

{{% /alert %}}

## **检测空初始化单元格**

所有具有值的单元格都会自动初始化，但是可能某个工作表只有应用格式的单元格。在这种情况下，[**Cells.max_data_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_row/)或[**Cells.max_data_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_data_column/)属性将返回-1，指示没有任何填充值但已初始化的单元格，因此无法使用此方法检测到具有空初始化的单元格。为了检查工作表是否有空初始化的单元格，建议使用从[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)集合获得的枚举器上的IEnumerator.MoveNext方法。如果IEnumerator.MoveNext方法返回true，则表示给定工作表中有一个或多个已初始化的单元格。

## **检查形状**

有可能某个给定的工作表没有任何填充的单元格，但可能包含形状和对象，例如控件、图表、图像等。如果我们需要检查工作表是否包含任何形状，可以通过检查[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)元素进行。任何正值都表示工作表中存在形状。

## **编程示例**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-DetectEmptyWorksheets.py" >}}
