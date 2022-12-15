---
title: 调整 GridWeb 及其标题栏的大小
type: docs
weight: 30
url: /zh/net/resize-gridweb-and-its-header-bar/
---
{{% alert color="primary" %}} 

[将 GridWeb 添加到 Web 窗体](/cells/zh/net/add-gridweb-to-web-form/)，讨论了使用所见即所得调整 Aspose.Cells.GridWeb 控件的大小。本文解释了如何在运行时使用 Aspose.Cells.GridWeb API 执行相同的操作。它还解释了如何调整 Aspose.Cells.GridWeb 控件的标题栏的大小以使其数据更易于阅读。

{{% /alert %}} 
## **改变 Aspose.Cells.GridWeb 的宽度和高度**
更改 Aspose.Cells.GridWeb 控件的宽度和高度是一个简单但重要的功能。 Aspose.Cells.GridWeb 控件由 API 中的 GridWeb 类表示。要调整 GridWeb 控件的宽度和高度，只需使用其宽度和高度属性即可。

{{% alert color="primary" %}} 

控件的宽度和高度可以以像素或点为单位定义。

{{% /alert %}} 

以下代码片段的输出如下所示。

**更改了 GridWeb 控件的宽度和高度** 

![待办事项：图像_替代_文本](resize-gridweb-and-its-header-bar_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeGridWeb.aspx-ResizeGridWeb.cs" >}}
### **改变标题栏的宽度和高度**
Aspose.Cells.GridWeb 控件包含两个标题栏，如下所示：

- 顶部标题栏，此标题栏将列表示为 A 、 B 、 C 、 D 等。
- 左标题栏，此标题栏将行表示为 1 、 2 、 3 、 4 等。

这两个标题栏如下所示。

**标题栏** 

![待办事项：图像_替代_文本](resize-gridweb-and-its-header-bar_2.png)

分别使用 GridWeb 控件的 HeaderBarHeight 和 HeaderBarWidth 属性更改顶部标题栏的高度和左侧标题栏的宽度。下图显示了后面的代码示例的输出。

**更改了标题栏的宽度和高度** 

![待办事项：图像_替代_文本](resize-gridweb-and-its-header-bar_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeHeaderBar.aspx-ResizeHeaderBar.cs" >}}
