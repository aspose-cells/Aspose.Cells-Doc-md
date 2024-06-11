---
title: 将文本数值数据转换为数字
type: docs
weight: 900
url: /zh/python-net/convert-text-numeric-data-to-number/
description: 学习如何使用Aspose.Cells for Python via .NET API将在Excel中存储为文本的数字转换为数字。
keywords: python excel将文本转换为数字，python excel将文本转换为数字，python excel将文本数字数据转换为数字，python excel将文本数字数据转换为数字，python excel将数值文本转换为数字，python excel将数值文本转换为数字，使用python将excel中的数值文本转换为数字，使用python将excel中的数值文本转换为数字，在excel中使用python将数值文本转换为数字，python excel库将文本数字数据转换为数字，python excel将数值文本转换为数字。
---

## **可能的使用场景**
有时，您希望将以文本形式输入的数值数据转换为数字。您可以在Microsoft Excel中通过在数字前放置撇号来将数字输入为文本，例如**'12345**。然后，Excel将该数字视为字符串。Aspose.Cells for Python via .NET允许您将字符串转换为数字。


## **如何将在文本中存储的数字转换为Excel中的数字**
您可以按照以下几个简单步骤将存储为文本的数字转换为数字。
1. 选择任何一个具有左上角错误指示器的单元格或单元格范围。
1. 在所选单元格或单元格范围旁边，单击出现的错误按钮。在菜单上，单击转换为数字。 
<br>
<img src="4.png" width=70% />
1. 如果警报按钮不可用，请选择具有此问题的列。如果您不想转换整个列，可以选择一个或多个单元格。只需确保您选择的单元格在同一列中，否则此过程将无法工作。文本到列按钮通常用于拆分列，但也可以用于将单个文本列转换为数字。在数据选项卡上，单击文本到列。
<br>
<img src="1.png" width=70% />
1. 在弹出框中单击完成按钮。
<br>
<img src="2.png" width=70% />
1. 存储为文本的数字已转换为数字。
<br>
<img src="3.png" width=70% />

## **使用Aspose.Cells for Python Excel库将存储为文本的数字转换为数字**
Aspose.Cells for Python via .NET提供了可以将所有字符串或文本数值数据转换为数字的[**Cells.convert_string_to_numeric_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/convert_string_to_numeric_value/)方法。

以下截图显示了单元格**A1:A17**中的字符串数字。字符串数字对齐到左边。
<br>
<img src="5.png" width=70% />

这些字符串数字已经使用[**Cells.convert_string_to_numeric_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/convert_string_to_numeric_value/) 转换为数字，如下面的截图所示。您可以看到，它们现在是右对齐的。
<br>
<img src="6.png" width=70% />

## **将字符串数字数据转换为实际数字的Python代码**

以下示例代码说明了如何在所有工作表中将所有字符串数值数据转换为实际数值。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.py" >}}
