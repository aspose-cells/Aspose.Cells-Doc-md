---
title: 创建自定义命令按钮
type: docs
weight: 100
url: /zh/net/aspose-cells-gridweb/create-custom-command-buttons/
keywords: GridWeb,命令,命令按钮,自定义
description: 本文介绍了如何在 GridWeb 中自定义命令按钮。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb 包含特殊按钮，如 **提交**、**保存** 和 **撤消**。所有这些按钮为 Aspose.Cells.GridWeb 执行特定任务。
还可以添加执行自定义任务的自定义按钮。本主题解释了如何使用此功能。

{{% /alert %}} 
## **创建自定义命令按钮**
要在 Aspose.Cells.GridWeb 中创建自定义命令按钮：

1. 在 Web 表单中添加 Aspose.Cells.GridWeb 控件。
1. 访问工作表。
1. 创建 CustomCommandButton 类的实例。
1. 将按钮的 Command 设置为某个值。此值在按钮的事件处理程序中使用。
1. 设置按钮的文本。
1. 设置按钮的图像 URL。
1. 最后，将 CustomCommandButton 对象添加到 GridWeb 控件的 CustomCommandButtons 集合中。

{{% alert color="primary" %}} 

也可以使用 Visual Studio 的属性对话框在 WYSIWYG 模式下添加自定义命令按钮。

{{% /alert %}} 

代码片段的输出如下所示：

**向 GridWeb 控件添加自定义命令按钮** 

![todo:image_alt_text](create-custom-command-buttons_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitCustomCommandButton.aspx-InitCustomCommandButton.cs" >}}
### **自定义命令按钮的事件处理**
自定义命令按钮最重要的方面是点击时执行的操作。要设置操作，请为 GridWeb 控件的 CustomCommand 事件创建一个事件处理程序。

CustomCommand 事件总是在单击自定义命令按钮时触发。因此，事件处理程序必须通过将按钮添加到 GridWeb 控件时设置的 Command 来识别要应用到的特定自定义命令按钮。最后，添加在按钮被点击时执行的自定义代码。

在下面的代码示例中，单击按钮时向单元格 A1 添加了文本消息。

**单击自定义命令按钮时向 A1 单元格添加文本** 

![todo:image_alt_text](create-custom-command-buttons_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleCustomCommandEvent.aspx-HandleCustomCommandEvent.cs" >}}
