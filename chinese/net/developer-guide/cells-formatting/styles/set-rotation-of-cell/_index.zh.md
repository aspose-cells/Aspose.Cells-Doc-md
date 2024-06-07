---
title: 如何旋转单元格中的文本
type: docs
weight: 80
url: /zh/net/how-to-rotate-text-of-cell/
description: 使用Aspose.Cells for .NET API旋转单元格的C#代码
keywords: c#旋转单元格的文本，在工作簿中以编程方式旋转单元格的文本，在工作簿中以编程方式设置单元格旋转角度，c#如何在Excel中旋转单元格中的文本
---

## **在Aspose.Cells中旋转单元格中的文本**

Aspose.Cells是一个强大的.NET和Java组件，使开发人员能够通过编程方式处理Excel电子表格。Aspose.Cells提供的功能之一是旋转单元格的能力，允许您自定义文本的方向并改善数据的视觉呈现。在本文档中，我们将探讨如何使用Aspose.Cells旋转单元格。

## **如何在Excel中旋转单元格中的文本**
要在Excel中旋转单元格，可以按照以下步骤进行:
1. 打开Excel并选择要旋转的单元格或单元格范围。
1. 在所选单元格上右键单击并从上下文菜单中选择“设置单元格格式”。或者，您可以打开Excel功能区中的“主页”选项卡，单击“单元格”组中的“设置”下拉菜单，然后选择“设置单元格”。
1. 在“设置单元格格式”对话框中，导航至“对齐”选项卡。
1. 在“方向”部分下，您将看到旋转文本的选项。您可以在“度数”框中直接输入所需的旋转角度。正值将逆时针旋转文本，负值将顺时针旋转文本。
<br>
![todo:image_alt_text](alignment.png)
1. 选择所需的旋转后，单击“确定”应用更改。所选单元格将根据您选择的旋转角度或方向进行旋转。

## **使用Aspose.Cells API旋转单元格中的文本**

[**Style.RotationAngle**](https://reference.aspose.com/cells/net/aspose.cells/style/rotationangle/)属性使得旋转单元格变得方便。要在Aspose.Cells中旋转单元格，您需要按照以下步骤操作:
1. 加载Excel工作簿
<br>
首先，您需要使用Aspose.Cells加载Excel工作簿。您可以使用Workbook类打开现有的Excel文件或创建一个新的Excel文件。 

1. 访问工作表
<br>
加载工作簿后，您需要访问要旋转单元格的工作表。您可以通过索引或名称访问工作表。 

1. 旋转单元格的文本
<br>
现在，您可以访问工作表，并通过修改所需单元格的Style对象来旋转单元格。Style对象允许您设置各种格式选项，包括旋转。 

1. 保存工作簿
<br>
旋转单元格后，您可以使用Save方法将修改后的工作簿保存回文件或流中。

## **C# 示例代码**

请查看以下代码，它创建了一个工作簿对象，并为几个单元格设置了不同的旋转角度。下面的截图展示了执行示例代码后的结果。
<br>
<img src="rotation.png" width=80% />



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-rotate-text.cs" >}}
