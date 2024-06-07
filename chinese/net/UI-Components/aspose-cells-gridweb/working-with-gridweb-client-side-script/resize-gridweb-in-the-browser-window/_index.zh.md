---
title: 调整浏览器窗口中的GridWeb大小
type: docs
weight: 40
url: /zh/net/aspose-cells-gridweb/resize-gridweb-in-the-browser-window/
keywords: GridWeb，调整大小
description: 本文介绍了如何在GridWeb中调整大小。
---

## **可能的使用场景**
有时您希望Aspose.Cells.GridWeb应该根据浏览器窗口重新调整大小。您可能需要GridWeb始终调整其大小（高度、宽度）并与浏览器窗口的大小兼容。Aspose.Cells.GridWeb提供了用于此目的的客户端*resize()*函数。此外，您甚至可以使GridWeb控件在浏览器窗口中可调整大小。例如，您可以使用底部右侧手柄（通过鼠标）在窗口中自定义其宽度/高度。还需在项目的页面源中包含/指定jquery Javascript文件以使其生效。
## **使用GridWeb的resize方法**
以下代码将每100毫秒检查是否发生调整大小操作。当没有更多调整大小操作时，它认为调整大小操作现在已经完成。我们使用一个导入到GridWeb中的示例模板文件。我们使用客户端代码调整GridWeb的大小。屏幕截图显示了当调整浏览器窗口大小时，GridWeb相应地调整其大小。

![todo:image_alt_text](resize-gridweb-in-the-browser-window_1.png)
### **示例代码**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-ResizeGridWebUsingResizeMethod" >}}


## **使用可调整大小的jquery ui功能使GridWeb可调整大小**
以下代码将使GridWeb控件在浏览器窗口中可调整大小。例如，您可以使用底部右侧手柄在窗口中自定义GridWeb的大小。首先，我们使用导入到GridWeb中的相同模板文件。我们使用jquery脚本使GridWeb可调整大小。屏幕截图显示了在浏览器窗口中使用底部右侧手柄调整GridWeb的大小。

![todo:image_alt_text](resize-gridweb-in-the-browser-window_2.png)
### **示例代码**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-MakingGridWebResizableUsingResizablejQueryUiFeature" >}}
