---
title: 管理工作表中的超链接
type: docs
weight: 100
url: /zh/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/
keywords: GridWeb，超链接
description: 本文介绍如何在 GridWeb 中处理超链接。
---

{{% alert color="primary" %}} 

本主题讨论 Aspose.Cells.GridWeb 支持的超链接类型以及如何以编程方式管理它们。超链接可用于创建指向 Web URL 或执行服务器端回发的链接。

{{% /alert %}} 
## **处理超链接**
### **超链接类型**
一般来说，Aspose.Cells.GridWeb 支持以下类型的超链接：

- [URL 超链接](/cells/zh/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/)，可以链接到 Web URL 的超链接。
- [文本超链接](/cells/zh/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/)，应用于文本的 URL 超链接。
- [图片超链接](/cells/zh/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/)，应用于图片的 URL 超链接。
- [单元格命令超链接](/cells/zh/net/aspose-cells-gridweb/manage-hyperlinks-in-worksheet/)，将数据发送到服务器的超链接。这样的超链接更像是单击后触发服务器端事件的按钮。

下面的部分详细描述了所有类型超链接的使用方式。还讨论了如何访问或移除链接。
### **添加超链接**

#### **URL 超链接**
URL 超链接看起来更像是通常在网站上看到的简单超链接。URL 超链接在单元格中起到类似锚点的作用。每当单击它时，它会导航到一个网页或打开一个新的浏览器窗口。

有不同类型的 URL 超链接：

- 文本超链接。
- 图片超链接。

开发人员可以为超链接指定一个图像。如果未指定图像，则创建文本超链接；否则创建图像超链接。


##### **文本超链接**
在工作表中添加文本超链接：

1. 将Aspose.Cells.GridWeb控件添加到您的Web表单中。
1. 访问工作表。
1. 在工作表中的单元格添加超链接。
1. 设置要在单元格中显示的文本。
1. 设置超链接的URL。
1. 设置超链接的目标，如果需要的话。
1. 如有需要，设置工具提示。

{{% alert color="primary" %}} 

注意：超链接目标可以设置为_self、_top或_parent，分别用于在新窗口、当前窗口或顶层窗口中打开Web URL。

{{% /alert %}} 

下面的示例向工作表添加了两个超链接。其中一个没有目标，而另一个设置为_parent。

**输出：向工作表添加文本超链接** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddTextHyperlinks.cs" >}}


##### **图像超链接**
添加图像超链接：

1. 将Aspose.Cells.GridWeb控件添加到您的Web表单中。
1. 访问工作表。
1. 向单元格添加超链接。
1. 设置要显示为超链接的图像的URL。
1. 设置超链接的URL。
1. 如有需要，设置工具提示。
1. 如有需要，设置超链接文本。

**输出：将图像超链接添加到工作表** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_2.png)

{{% alert color="primary" %}} 

Setting the image hyperlink's AltText fills a similar function as setting an <ALT> tag in HTML. The text is displayed only if the hyperlinked image is not displayed. (For example, if the image isn't at the specified location.) If the image of the second hyperlink is not found, the output of the code snippet below would look as follows.

**找不到图像的图像网址** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_3.png)

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddImageHyperlinks.cs" >}}


#### **单元格命令超链接**
单元格命令超链接是一种特殊类型的超链接，触发服务器端事件而不是打开网页。开发人员可以向服务器端事件添加代码，并在点击超链接时执行任何任务。此功能使开发人员能够创建更多交互式应用程序。

添加单元格命令超链接：

1. 将Aspose.Cells.GridWeb控件添加到您的Web表单中。
1. 访问工作表。
1. 向单元格添加超链接。
1. 将超链接的命令设置为所需的任何值。
   该值由超链接的事件处理程序使用以识别它。
1. 如有需要，设置工具提示。
1. 设置图像的 URL，该图像将显示为超链接。

**已向工作表添加了单元格命令超链接** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddCellCommandHyperlinks.cs" >}}
##### **单元格命令超链接的事件处理**
开发人员需要为 GridWeb 控件的 CellCommand 事件创建一个事件处理程序，以在单击特定单元格命令超链接时执行特定任务。CellCommand 事件的事件处理程序提供 CellEventArgs 类型的对象，该对象提供 Argument 属性。使用 Argument 属性通过比较其 CellCommand 值来标识特定超链接。

下面的示例为上面的代码创建了一个单元格命令超链接的事件处理程序。超链接的 CellCommand 设置为 Click。因此，在事件处理程序中，首先检查它，然后添加代码，使 A6 单元格中显示一条消息。

当单击超链接时激发事件处理程序。

**输出：单击超链接时将文本添加到 A6 单元格** 

![todo:image_alt_text](manage-hyperlinks-in-worksheet_5.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-HandleCellCommandHyperlinkEvent.cs" >}}
### **访问超链接**
要访问现有的超链接：

1. 访问包含它的单元格。
1. 获取单元格引用。
1. 传递引用到Hyperlinks集合的GetHyperlink方法来访问超链接。
1. 修改超链接的属性。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-AccessHyperlinks.cs" >}}
### **删除超链接**
要删除超链接：

1. 访问活动工作表。
1. 使用Hyperlinks集合的Remove方法移除超链接。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-RemoveHyperlink.cs" >}}
