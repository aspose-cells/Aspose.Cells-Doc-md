---
title: 如何旋转单元格文本
type: docs
weight: 80
url: /zh/python-net/how-to-rotate-text-of-cell/
description: 使用Aspose.Cells for Python via .NET API旋转单元格文本的C#代码
keywords: Python旋转单元格文本，Python程序化旋转工作簿中的单元格文本，程序设置单元格旋转角度，Python如何旋转Excel中的单元格文本
---

## **在Aspose.Cells for Python via .NET中旋转单元格文本**

Aspose.Cells for Python via .NET是一个强大的.NET和Java组件，允许开发人员以编程方式处理Excel电子表格。Aspose.Cells for Python via .NET提供的功能之一是旋转单元格，允许您自定义文本的方向，改善数据的视觉表现。在本文中，我们将探讨如何使用Aspose.Cells for Python via .NET旋转单元格。

## **如何在Excel中旋转单元格中的文本**
要在Excel中旋转单元格，您可以按照以下步骤操作：
1. 打开Excel并选择您要旋转的单元格或单元格范围。
1. 右键单击所选单元格，并从上下文菜单中选择“格式单元格”。或者，您还可以在Excel功能区中的“主页”选项卡中，单击“单元格”组中的“格式”下拉菜单，然后选择“格式单元格”。
1. 在“格式单元格”对话框中，转到“对齐”选项卡。
1. 在“方向”部分下，您将看到旋转文本的选项。您可以直接在“度数”框中输入所需的旋转角度。正值逆时针旋转文本，负值顺时针旋转文本。
<br>
![todo:image_alt_text](alignment.png)
1. 选择所需的旋转后，单击“确定”以应用更改。所选单元格现在将根据您选择的旋转角度或方向进行旋转。

## **如何使用Aspose.Cells for Python via .NET API旋转单元格文本**

[**Style.rotation_angle**](https://reference.aspose.com/cells/python-net/aspose.cells/style/rotation_angle)属性使旋转单元格变得方便。若要在Aspose.Cells for Python via .NET中旋转单元格，您需要按照以下步骤操作：
1. 加载Excel工作簿
<br>
首先，您需要使用Aspose.Cells for Python via .NET加载Excel工作簿。您可以使用Workbook类打开一个现有的Excel文件或创建一个新文件。 

1. 访问工作表
<br>
加载工作簿后，您需要访问要旋转单元格的工作表。您可以通过索引或名称访问工作表。 

1. 旋转单元格文本
<br>
现在您已经可以访问工作表，就可以通过修改所需单元格的样式对象来旋转单元格。样式对象允许您设置各种格式选项，包括旋转。 

1. 保存工作簿
<br>
旋转单元格后，您可以使用Save方法将修改后的工作簿保存回文件或流。

## **Python示例代码**

请参阅以下代码，它创建一个工作簿对象，并为几个单元格设置不同的旋转角度。屏幕截图显示了执行示例代码后的结果。
<br>
<img src="rotation.png" width=80% />



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Cells-rotate-text.py" >}}

{{< app/cells/assistant language="python-net" >}}
