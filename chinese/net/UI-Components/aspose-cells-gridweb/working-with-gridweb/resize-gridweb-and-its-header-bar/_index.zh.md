---
title: 调整GridWeb及其标题栏大小
type: docs
weight: 30
url: /zh/net/aspose-cells-gridweb/resize-gridweb-and-its-header-bar/
keywords: GridWeb,调整大小
description: 本文介绍了如何在GridWeb中调整大小。
---

{{% alert color="primary" %}} 

[将GridWeb添加到Web表单](/cells/zh/net/aspose-cells-gridweb/add-gridweb-to-web-form/)，讨论使用所见即所得图形界面调整Aspose.Cells.GridWeb控件。本文解释了如何使用Aspose.Cells.GridWeb API在运行时执行相同操作。还解释了如何调整Aspose.Cells.GridWeb控件的标题栏大小，使其数据易于阅读。

{{% /alert %}} 
## **更改Aspose.Cells.GridWeb的宽度和高度**
更改Aspose.Cells.GridWeb控件的宽度和高度是一个简单但重要的功能。Aspose.Cells.GridWeb控件在API中由GridWeb类表示。要调整GridWeb控件的宽度和高度，只需使用其width和height属性。

{{% alert color="primary" %}} 

控件的宽度和高度可以以像素或点的形式定义。

{{% /alert %}} 

以下是代码片段的输出结果。

**更改了GridWeb控件的宽度和高度** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeGridWeb.aspx-ResizeGridWeb.cs" >}}
### **更改标题栏的宽度和高度**
Aspose.Cells.GridWeb控件包含以下两个标题栏:

- 顶部标题栏，该标题栏表示A，B，C，D等列。
- 左侧标题栏，该标题栏表示1，2，3，4等行。

下面显示了这两个标题栏。

**标题栏** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_2.png)

使用GridWeb控件的HeaderBarHeight和HeaderBarWidth属性分别更改顶部标题栏和左侧标题栏的高度和宽度。下图显示了以下代码示例的输出。

**更改了标题栏的宽度和高度** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeHeaderBar.aspx-ResizeHeaderBar.cs" >}}
