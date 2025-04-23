---
title: 将文本数值数据转换为数字
type: docs
weight: 900
url: /zh/nodejs-cpp/convert-text-numeric-data-to-number/
description: 学习如何使用Aspose.Cells for Node.js via C++ API将Excel中存储为文本的数字转换为数字。
keywords: Excel转换文本为数字，Node.js代码将文本数字数据转换为数字，使用Aspose.Cells for Node.js via C++ API可以将字符串转换为数字。
---

## **可能的使用场景**
有时，你想将以文本输入的数字数据转换为数字。你可以在Microsoft Excel中在数字前加上撇号，例如‘12345’，Excel会将其视为字符串。Aspose.Cells for Node.js via C++可以帮助你将字符串转换为数字。


## 如何将 Excel 中存储为文本的数字转换为数字
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

## 如何使用Aspose.Cells for Node.js via C++将存储为文本的数字转换为数字
Aspose.Cells for Node.js via C++提供了[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#convertStringToNumericValue--)方法，可以将所有字符串或文本数字数据转换为数字。

以下截图显示了单元格**A1:A17**中的字符串数字。字符串数字对齐到左边。
<br>
<img src="5.png" width=70% />

这些字符串数字已经使用[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#convertStringToNumericValue--) 转换为数字，如下面的截图所示。您可以看到，它们现在是右对齐的。
<br>
<img src="6.png" width=70% />

## Node.js代码将字符串数字数据转换为实际数字

以下示例代码说明了如何在所有工作表中将所有字符串数值数据转换为实际数值。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-ConvertTextNumericDatatoNumber.js" >}}
