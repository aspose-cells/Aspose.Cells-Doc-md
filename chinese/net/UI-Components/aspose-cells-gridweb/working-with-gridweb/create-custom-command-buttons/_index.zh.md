---
title: 创建自定义命令按钮
type: docs
weight: 100
url: /zh/net/create-custom-command-buttons/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb 包含特殊按钮，如**提交**, **救球**和**撤消**.所有这些按钮都为 Aspose.Cells.GridWeb 执行特定任务。
还可以添加执行自定义任务的自定义按钮。本主题说明如何使用此功能。

{{% /alert %}} 
## **创建自定义命令按钮**
在 Aspose.Cells.GridWeb 中创建自定义命令按钮：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体。
1. 访问工作表。
1. 创建 CustomCommandButton 类的实例。
1. 将按钮的命令设置为某个值。该值用于按钮的事件处理程序。
1. 设置按钮的文本。
1. 设置按钮的图像 URL。
1. 最后，将 CustomCommandButton 对象添加到 GridWeb 控件的 CustomCommandButtons 集合中。

{{% alert color="primary" %}} 

还可以使用 Visual Studio 的“属性”对话框以所见即所得模式添加自定义命令按钮。

{{% /alert %}} 

代码片段的输出如下所示：

**添加到 GridWeb 控件的自定义命令按钮** 

![待办事项：图片_替代_文本](create-custom-command-buttons_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitCustomCommandButton.aspx-InitCustomCommandButton.cs" >}}
### **自定义命令按钮的事件处理**
自定义命令按钮最重要的方面是它们在单击时执行的操作。要设置操作，请为 GridWeb 控件的 CustomCommand 事件创建一个事件处理程序。

单击自定义命令按钮时，始终会触发 CustomCommand 事件。因此，在将按钮添加到 GridWeb 控件时，事件处理程序必须识别命令集所应用的特定自定义命令按钮。最后，添加单击按钮时执行的自定义代码。

在下面的代码示例中，当单击按钮时，一条文本消息将添加到单元格 A1。

**单击自定义命令按钮时添加到 A1 单元格的文本** 

![待办事项：图片_替代_文本](create-custom-command-buttons_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleCustomCommandEvent.aspx-HandleCustomCommandEvent.cs" >}}
