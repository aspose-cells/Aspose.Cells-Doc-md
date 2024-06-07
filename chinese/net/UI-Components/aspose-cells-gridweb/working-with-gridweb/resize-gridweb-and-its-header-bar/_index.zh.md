---
title: 调整GridWeb及其标题栏的大小
type: docs
weight: 30
url: /zh/net/aspose-cells-gridweb/resize-gridweb-and-its-header-bar/
keywords: GridWeb，调整大小
description: 本文介绍了如何在GridWeb中调整大小。
---

{{% alert color="primary" %}} 

[将GridWeb添加到Web表单](/cells/zh/net/aspose-cells-gridweb/add-gridweb-to-web-form/)，讨论了使用所见即所得进行调整的Aspose.Cells.GridWeb控件。本文解释了如何在运行时使用Aspose.Cells.GridWeb API执行相同操作。它还解释了如何调整Aspose.Cells.GridWeb控件的标题栏大小，以使其数据更易于阅读。

{{% /alert %}} 
## **更改Aspose.Cells.GridWeb的宽度和高度**
更改Aspose.Cells.GridWeb控件的宽度和高度是一项简单但重要的功能。Aspose.Cells.GridWeb控件在API中由GridWeb类表示。要调整GridWeb控件的宽度和高度，只需使用其宽度和高度属性。

{{% alert color="primary" %}} 

控件的宽度和高度可以以像素或点数定义。

{{% /alert %}} 

以下代码片段的输出如下所示。

**更改GridWeb控件的宽度和高度** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeGridWeb.aspx-ResizeGridWeb.cs" >}}
### **更改标题栏的宽度和高度**
Aspose.Cells.GridWeb控件包含两个标题栏，如下所示:

- 顶部标题栏，此标题栏代表列为A，B，C，D等。
- 左边标题栏，此标题栏代表行为1，2，3，4等。

这两个标题栏如下所示。

**标题栏** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_2.png)

使用GridWeb控件的HeaderBarHeight和HeaderBarWidth属性分别更改顶部标题栏和左侧标题栏的高度。下面的图片展示了接下来的代码示例的输出。

**已更改的标题栏宽度和高度** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeHeaderBar.aspx-ResizeHeaderBar.cs" >}}
