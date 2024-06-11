---
title: 在浏览器窗口中调整GridWeb的大小
type: docs
weight: 40
url: /zh/net/aspose-cells-gridweb/resize-gridweb-in-the-browser-window/
keywords: GridWeb,调整大小
description: 本文介绍了如何在GridWeb中调整大小。
---

## **可能的使用场景**
有时您希望Aspose.Cells.GridWeb能够根据浏览器窗口进行调整。您可能需要GridWeb始终调整其大小（高度、宽度）并与浏览器窗口的大小兼容。Aspose.Cells.GridWeb提供客户端 *resize()* 功能以实现此目的。此外，您甚至可以使GridWeb控件可以在浏览器窗口中调整大小。例如，您可以使用鼠标通过右下角的手柄自定义其在窗口中的宽度/高度。您还需要在项目的页面源中引入/指定jquery Javascript文件以使其工作。
## **使用GridWeb的resize方法**
以下代码将每100毫秒检查是否有调整大小的操作发生。当没有更多调整大小操作时，它认为调整大小操作已经完成。我们使用一个被导入到GridWeb中的示例模板文件。我们使用客户端代码来调整GridWeb的大小。截图显示了GridWeb在调整浏览器窗口大小时相应地调整了自身大小。

![todo:image_alt_text](resize-gridweb-in-the-browser-window_1.png)
### **示例代码**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-ResizeGridWebUsingResizeMethod" >}}


## **使用Jquery UI功能使GridWeb可调整大小**
以下代码将使GridWeb控件可以在浏览器窗口中调整大小。例如，您可以使用右下角的手柄来自定义GridWeb在窗口中的大小。我们首先使用相同的模板文件将其导入到GridWeb中。我们使用jquery脚本来使GridWeb可以调整大小。截图显示了GridWeb在浏览器窗口中使用其右下角手柄进行了调整。

![todo:image_alt_text](resize-gridweb-in-the-browser-window_2.png)
### **示例代码**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-MakingGridWebResizableUsingResizablejQueryUiFeature" >}}
