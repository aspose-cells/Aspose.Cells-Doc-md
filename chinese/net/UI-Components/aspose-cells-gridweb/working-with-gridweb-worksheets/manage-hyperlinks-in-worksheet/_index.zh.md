---
title: 在工作表中管理超链接
type: docs
weight: 100
url: /zh/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/
keywords: GridWeb, 超链接
description: 本文介绍了如何在GridWeb中处理超链接。
---

{{% alert color="primary" %}} 

本主题讨论了Aspose.Cells.GridWeb支持哪些类型的超链接以及如何通过编程方式管理它们。超链接可用于创建指向Web URL或执行服务器端回发的链接。

{{% /alert %}} 
## **使用超链接**
### **超链接类型**
通常，Aspose.Cells.GridWeb支持以下超链接：

- [URL超链接](/cells/zh/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/)，可链接到Web URL的超链接。
- [文本超链接](/cells/zh/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/)，应用于文本的URL超链接。
- [图像超链接](/cells/zh/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/)，应用于图像的URL超链接。
- [单元格命令超链接](/cells/zh/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/)，将数据发送到服务器的超链接。此类超链接在单击时触发服务器端事件，更像是触发服务器端事件的按钮。

下面的部分详细描述了所有类型的超链接的使用。还讨论了如何访问或删除超链接。
### **添加超链接**

#### **URL超链接**
URL超链接看起来更像是您在网站上通常看到的简单超链接。URL超链接的作用类似于单元格中的锚点。每当单击它时，它会导航到一个网页或打开一个新的浏览器窗口。

有不同类型的URL超链接:

- 文本超链接。
- 图片超链接。

开发人员可以为超链接指定一个图像。如果未指定图像，则创建一个文本超链接；否则创建一个图像超链接。


##### **文本超链接**
要在工作表中添加文本超链接:

1. 将Aspose.Cells.GridWeb控件添加到您的Web表单中。
1. 访问工作表。
1. 在工作表的单元格中添加超链接。
1. 设置在单元格中显示的文本。
1. 设置超链接的URL。
1. 如果需要，设置超链接的目标。
1. 如果需要的话，设置工具提示。

{{% alert color="primary" %}} 

注意: 可以将超链接目标设置为_self、_top或_parent，以在新窗口、当前窗口或顶层窗口中打开Web URL。

{{% /alert %}} 

下面的示例向工作表添加了两个超链接。一个没有目标，另一个设置为_parent。

**输出：工作表中添加的文本超链接** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddTextHyperlinks.cs" >}}


##### **图像超链接**
要添加图像超链接:

1. 将Aspose.Cells.GridWeb控件添加到您的Web表单中。
1. 访问工作表。
1. 在单元格中添加超链接。
1. 设置要显示为超链接的图像的URL。
1. 设置超链接的URL。
1. 如果需要的话，设置工具提示。
1. 如果需要，设置超链接文本。

**输出: 将图像超链接添加到工作表** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_2.png)

{{% alert color="primary" %}} 

Setting the image hyperlink's AltText fills a similar function as setting an <ALT> tag in HTML. The text is displayed only if the hyperlinked image is not displayed. (For example, if the image isn't at the specified location.) If the image of the second hyperlink is not found, the output of the code snippet below would look as follows.

**找不到图像URL的图像** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_3.png)

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddImageHyperlinks.cs" >}}


#### **单元格命令超链接**
单元格命令超链接是一种特殊类型的超链接，它触发服务器端事件而不是打开网页。开发人员可以向服务器端事件添加代码，并在单击超链接时执行任何任务。此功能使开发人员能够创建更多交互式应用程序。

要添加单元格命令超链接:

1. 将Aspose.Cells.GridWeb控件添加到您的Web表单中。
1. 访问工作表。
1. 在单元格中添加超链接。
1. 将超链接的命令设置为所需的任何值。
   该值用于超链接的事件处理程序识别它。
1. 如果需要的话，设置工具提示。
1. 设置图像的URL，该图像将显示为超链接。

**已向工作表添加了单元格命令超链接** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddCellCommandHyperlinks.cs" >}}
##### **处理单元格命令超链接的事件**
开发人员需要为GridWeb控件的CellCommand事件创建事件处理程序，以便在单击特定单元格命令超链接时执行特定任务。CellCommand事件的事件处理程序提供了CellEventArgs类型的对象，该对象提供Argument属性。使用Argument属性来通过比较其CellCommand值来识别特定超链接。

下面的示例创建了一个事件处理程序，用于处理上面代码中创建的单元格命令超链接。超链接的CellCommand设置为Click。因此，在事件处理程序中，首先检查它，然后添加代码以在A6单元格中显示消息。

超链接被单击时调用事件处理程序。

**输出：单击超链接时添加到A6单元格的文本** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_5.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-HandleCellCommandHyperlinkEvent.cs" >}}
### **访问超链接**
要访问现有的超链接：

1. 访问包含它的单元格。
1. 获取单元格引用。
1. 将引用传递给超链接集合的GetHyperlink方法，以访问超链接。
1. 修改超链接的属性。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-AccessHyperlinks.cs" >}}
### **删除超链接**
要移除超链接：

1. 访问活动工作表。
1. 使用超链接集合的Remove方法移除超链接。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-RemoveHyperlink.cs" >}}
