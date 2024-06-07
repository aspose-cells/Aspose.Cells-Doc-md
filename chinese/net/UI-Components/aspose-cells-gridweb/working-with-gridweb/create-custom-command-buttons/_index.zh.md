---
title: 创建自定义命令按钮
type: docs
weight: 100
url: /zh/net/aspose-cells-gridweb/create-custom-command-buttons/
keywords: GridWeb,command,command buttons,custom
description: 本文介绍如何在GridWeb中自定义命令按钮。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb包含特殊按钮如**提交**、**保存**和**撤销**。所有这些按钮为Aspose.Cells.GridWeb执行特定任务。
还可以添加执行自定义任务的自定义按钮。本主题解释了如何使用此功能。

{{% /alert %}} 
## **创建自定义命令按钮**
要在Aspose.Cells.GridWeb中创建自定义命令按钮：

1. 将Aspose.Cells.GridWeb控件添加到Web表单中。
1. 访问工作表。
2. 创建CustomCommandButton类的实例。
3. 将按钮的Command设置为某个值。该值在按钮的事件处理程序中使用。
4. 设置按钮的文本。
5. 设置按钮的图像URL。
1. 最后，将CustomCommandButton对象添加到GridWeb控件的CustomCommandButtons集合中。

{{% alert color="primary" %}} 

在Visual Studio的属性对话框中，也可以使用所见即所得模式添加自定义命令按钮。

{{% /alert %}} 

代码片段的输出如下所示:

**将自定义命令按钮添加到GridWeb控件** 

![todo:image_alt_text](create-custom-command-buttons_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitCustomCommandButton.aspx-InitCustomCommandButton.cs" >}}
### **自定义命令按钮的事件处理**
自定义命令按钮最重要的方面是它们在点击时执行的操作。要设置操作，请为GridWeb控件的CustomCommand事件创建事件处理程序。

当单击自定义命令按钮时，总是触发CustomCommand事件。因此，事件处理程序必须通过将按钮添加到GridWeb控件时设置的Command集来识别适用于其的特定自定义命令按钮。最后，添加在按钮被点击时执行的自定义代码。

在下面的代码示例中，当按钮被点击时，将文本消息添加到单元格A1。

**单击自定义命令按钮时向A1单元格添加的文本** 

![todo:image_alt_text](create-custom-command-buttons_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleCustomCommandEvent.aspx-HandleCustomCommandEvent.cs" >}}
