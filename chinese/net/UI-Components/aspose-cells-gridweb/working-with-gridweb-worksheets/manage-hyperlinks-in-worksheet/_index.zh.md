---
title: 管理工作表中的超链接
type: docs
weight: 100
url: /zh/net/manage-hyperlinks-in-worksheet/
---
{{% alert color="primary" %}} 

本主题讨论 Aspose.Cells.GridWeb 支持哪些类型的超链接以及如何以编程方式管理它们。超链接可用于创建指向 Web URL 的链接或执行回发到服务器。

{{% /alert %}} 
## **使用超链接**
### **超链接的类型**
通常，Aspose.Cells.GridWeb 支持以下超链接：

- [网址超链接](/cells/zh/net/manage-hyperlinks-in-worksheet/)可以链接到 Web URL 的超链接。
- [文本超链接](/cells/zh/net/manage-hyperlinks-in-worksheet/)应用于文本的 URL 超链接。
- [图片超链接](/cells/zh/net/manage-hyperlinks-in-worksheet/)应用于图像的 URL 超链接。
- [Cell 命令超链接](/cells/zh/net/manage-hyperlinks-in-worksheet/)将数据发布到服务器的超链接。这样的超链接更像是一个按钮，单击时会触发服务器端事件。

以下部分详细描述了所有类型的超链接的使用。它还讨论了如何访问或删除链接。
### **添加超链接**

#### **网址超链接**
URL 超链接看起来更像是您通常在网站上看到的简单超链接。 URL 超链接的作用类似于单元格中的锚点。无论何时单击它，它都会导航到网页或打开一个新的浏览器窗口。

有不同类型的 URL 超链接：

- 文本超链接。
- 图片超链接。

开发人员可以为超链接指定图像。如果未指定图像，则会创建文本超链接；否则会创建图像超链接。


##### **文本超链接**
要向工作表添加文本超链接：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体。
1. 访问工作表。
1. 将超链接添加到工作表中的单元格。
1. 设置将在单元格中显示的文本。
1. 设置超链接的 URL。
1. 如果需要，设置超链接的目标。
1. 如果需要，设置工具提示。

{{% alert color="primary" %}} 

注意：超链接目标可以设置为_自己，_top 或 _parent 分别用于在新窗口、当前窗口或顶部窗口中打开 Web URL。

{{% /alert %}} 

下面的示例将两个超链接添加到工作表。一个没有目标，而另一个设置为_parent。

**输出：添加到工作表的文本超链接** 

![待办事项：图片_替代_文本](manage-hyperlinks-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddTextHyperlinks.cs" >}}


##### **图像超链接**
要添加图像超链接：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体。
1. 访问工作表。
1. 向单元格添加超链接。
1. 设置将显示为超链接的图像的 URL。
1. 设置超链接 URL。
1. 如果需要，设置工具提示。
1. 如果需要，设置超链接文本。

**输出：添加到工作表的图像超链接** 

![待办事项：图片_替代_文本](manage-hyperlinks-in-worksheet_2.png)

{{% alert color="primary" %}} 

设置图像超链接的 AltText 与设置一个类似的功能<ALT>HTML 中的标记。仅当未显示超链接图像时才显示文本。 （例如，如果图像不在指定位置。）如果找不到第二个超链接的图像，下面代码片段的输出将如下所示。

**找不到图像 URL 的图像** 

![待办事项：图片_替代_文本](manage-hyperlinks-in-worksheet_3.png)

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddImageHyperlinks.cs" >}}


#### **Cell 命令超链接**
单元命令超链接是一种特殊类型的超链接，它会触发服务器端事件而不是打开网页。开发人员可以向服务器端事件添加代码，并在单击超链接时执行任何任务。此功能使开发人员能够创建更具交互性的应用程序。

要添加单元格命令超链接：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体。
1. 访问工作表。
1. 向单元格添加超链接。
1. 将超链接的命令设置为任何所需的值。
超链接的事件处理程序使用该值来识别它。
1. 如果需要，设置工具提示。
1. 设置将显示为超链接的图像的 URL。

**单元格命令超链接已添加到工作表** 

![待办事项：图片_替代_文本](manage-hyperlinks-in-worksheet_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddCellCommandHyperlinks.cs" >}}
##### **Cell 命令超链接的事件处理**
开发人员需要为 GridWeb 控件的 CellCommand 事件创建事件处理程序，以便在单击特定单元格命令超链接时执行特定任务。 CellCommand 事件的事件处理程序提供了一个 CellEventArgs 类型的对象，该对象具有 Argument 属性。使用 Argument 属性通过比较其 CellCommand 值来识别特定的超链接。

下面的示例为在上面的代码中创建的单元格命令超链接创建了一个事件处理程序。超链接的 CellCommand 设置为 Click。因此，在事件处理程序中，首先检查它，然后添加在 A6 单元格中显示消息的代码。

单击超链接时将调用事件处理程序。

**输出：单击超链接时添加到 A6 单元格的文本** 

![待办事项：图片_替代_文本](manage-hyperlinks-in-worksheet_5.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-HandleCellCommandHyperlinkEvent.cs" >}}
### **访问超链接**
要访问现有的超链接：

1. 访问包含它的单元格。
1. 获取单元格引用。
1. 将引用传递给 Hyperlinks 集合的 GetHyperlink 方法以访问超链接。
1. 修改超链接的属性。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-AccessHyperlinks.cs" >}}
### **删除超链接**
要删除超链接：

1. 访问活动工作表。
1. 使用 Hyperlinks 集合的 Remove 方法删除超链接。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-RemoveHyperlink.cs" >}}
