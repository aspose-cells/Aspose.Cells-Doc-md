---
title: 将文本数值数据转换为数字
type: docs
weight: 900
url: /zh/python-net/convert-text-numeric-data-to-number/
description: 通过 .NET 的 Aspose.Cells for Python API 学习如何将 Excel 中存储为文本的数字转换为数字。
keywords: Python Excel 将文本转换为数字，使用 Python Excel 将文本转换为数字，使用 Python Excel 将文本数值数据转换为数字，使用 Python Excel 将文本数值数据转换为数字，使用 Python Excel 将数值文本转换为数字，使用 Python Excel 将数值文本转换为数字，使用 Python Excel 将数值文本转换为数字，在 Excel 中使用 Python 将数值文本转换为数字，使用 Python Excel 将文本数值数据转换为数字，使用 Python Excel 将数值字符串转换为数字。
---

## **可能的使用场景**
有时候，您希望将以文本形式输入的数值数据转换为数字。您可以在 Microsoft Excel 中以文本形式输入数字，方法是在数字前加上撇号，例如 **'12345**。Excel 将该数字作为字符串处理。通过 .NET 的 Aspose.Cells for Python 可以让您将字符串转换为数字。


## **如何将 Excel 中存储为文本的数字转换为数字**
您可以通过几个简单的步骤将存储为文本的数字转换为数字。
1. 选择具有错误指示器的任何单个单元格或单元格范围。
1. 在所选单元格或单元格范围旁边，单击出现的错误按钮。在菜单上，单击转换为数字。 
<br>
<img src="4.png" width=70% />
1. 如果警报按钮不可用，请选择具有此问题的列。如果您不想转换整个列，可以选择一个或多个单元格。只需确保您选择的单元格位于同一列，否则该过程将无法正常工作。文本到列按钮通常用于拆分列，但也可用于将单列文本转换为数字。在“数据”选项卡上，单击“文本到列”。
<br>
<img src="1.png" width=70% />
1. 单击弹出框中的完成按钮。
<br>
<img src="2.png" width=70% />
1. 存储为文本的数字将被转换为数字。
<br>
<img src="3.png" width=70% />

## **如何使用 Aspose.Cells for Python Excel 库将存储为文本的数字转换为数字**
通过 .NET 的 Aspose.Cells for Python 提供 [**Cells.convert_string_to_numeric_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/convert_string_to_numeric_value/) 方法，可用于将所有文本数值数据转换为数字。

以下截图显示了单元格**A1:A17**中的字符串数字。 字符串数字左对齐。
<br>
<img src="5.png" width=70% />

这些字符串数字已经在以下截图中使用[**Cells.convert_string_to_numeric_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/convert_string_to_numeric_value/) 转换为数字。 如您所见，它们现在已右对齐。
<br>
<img src="6.png" width=70% />

## **Python 代码将字符串数值数据转换为实际数字**

以下示例代码说明了如何将所有工作表中的字符串数值数据转换为实际数值。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.py" >}}
