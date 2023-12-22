---
title: 如何旋转Cell的文本
type: docs
weight: 80
url: /zh/net/how-to-rotate-text-of-cell/
description: C# 代码将 Cell 的文本旋转为 Aspose.Cells for .NET API
keywords: c# rotate text of Cell, c# programmatically rotate text of Cell in workbook, programmatically set cell rotation angle in workbook, c# how to rotate text of Cell in excel
---
##  **在 Aspose.Cells 中旋转 Cell 的文本**

Aspose.Cells 是功能强大的 .NET 和 Java 组件，使开发人员能够以编程方式使用 Excel 电子表格。 Aspose.Cells 提供的功能之一是旋转单元格的能力，允许您自定义文本的方向并改进数据的视觉呈现。在本文档中，我们将探讨如何使用 Aspose.Cells 旋转单元格。

##  **如何在Excel中旋转Cell的文本**
要旋转 Excel 中的单元格，可以使用以下步骤：
1. 打开 Excel 并选择要旋转的单元格或单元格区域。
1. 右键单击选定的单元格，然后从上下文菜单中选择“格式 Cells”。或者，您可以转到 Excel 功能区中的“主页”选项卡，单击“Cells”组中的“格式”下拉列表，然后选择“格式 Cells”。
1. 在“格式 Cells”对话框中，导航至“对齐”选项卡。
1. 在“方向”部分下，您将看到旋转文本的选项。您可以直接在“度”框中输入所需的旋转角度（以度为单位）。正值逆时针旋转文本，负值顺时针旋转文本。
<br>
![待办事项：图像_替代_文本](alignment.png)
1. 选择所需的旋转后，单击“确定”应用更改。现在，所选单元格将根据您选择的旋转角度或方向进行旋转。

##  **如何使用 Aspose.Cells API 旋转 Cell 的文本**

[**样式.旋转角度**](https://reference.aspose.com/cells/net/aspose.cells/style/rotationangle/)属性使得旋转单元格变得很方便。要旋转 Aspose.Cells 中的单元格，您需要执行以下步骤：
1. 加载 Excel 工作簿
<br>
首先，您需要使用 Aspose.Cells 加载 Excel 工作簿。您可以使用 Workbook 类打开现有 Excel 文件或创建新文件。

1. 访问工作表
<br>
加载工作簿后，您需要访问要旋转单元格的工作表。您可以通过索引或名称访问工作表。

1. 旋转Cell的文字
<br>
现在您已经可以访问工作表了，您可以通过修改所需单元格的 Style 对象来旋转单元格。 Style 对象允许您设置各种格式选项，包括旋转。

1. 保存工作簿
<br>
旋转单元格后，您可以使用 Save 方法将修改后的工作簿保存回文件或流。

##  **C# 示例代码**

请看下面的代码，它创建一个工作簿对象并为多个单元格设置不同的旋转角度。屏幕截图显示了示例代码执行后的结果。
<br>
<img src="rotation.png" width=80% />



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-rotate-text.cs" >}}
