---
title: 在浏览器窗口中调整 GridWeb 的大小
type: docs
weight: 40
url: /zh/net/resize-gridweb-in-the-browser-window/
---
## **可能的使用场景**
有时你想要 Aspose.Cells.GridWeb 应该根据浏览器窗口调整自己的大小。您可能需要 GridWeb 应始终调整其大小（高度、宽度）并与浏览器窗口的大小兼容。 Aspose.Cells.GridWeb提供客户端*调整大小()*为目的而发挥作用。此外，您甚至可以使 GridWeb 控件在浏览器窗口中调整大小。例如，您可以使用右下角的手柄（通过鼠标）来自定义其在窗口中的宽度/高度。您还需要包含/指定 jquery Javascript 文件，以使其在项目的页面源中工作。
## **使用 GridWeb 的调整大小方法**
以下代码将检查是否每 100 毫秒发生一次调整大小操作。当没有更多的调整大小动作时，它认为调整大小操作现在已经完成。我们使用导入到 GridWeb 中的示例模板文件。我们使用客户端代码来调整 GridWeb 的大小。屏幕截图显示 GridWeb 在调整浏览器窗口大小时相应地调整自身大小。

![待办事项：图片_替代_文本](resize-gridweb-in-the-browser-window_1.png)
### **示例代码**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-ResizeGridWebUsingResizeMethod" >}}


## **使用可调整大小的 jquery ui 功能使 GridWeb 可调整大小**
以下代码将使 GridWeb 控件在浏览器窗口中可调整大小。例如，您可以使用右下角的手柄来自定义窗口中 GridWeb 的大小。我们使用首先导入 GridWeb 的相同模板文件。我们使用 jquery 脚本使 GridWeb 可调整大小。屏幕截图显示 GridWeb 已使用其在浏览器窗口中右下角的手柄调整了大小。

![待办事项：图片_替代_文本](resize-gridweb-in-the-browser-window_2.png)
### **示例代码**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-MakingGridWebResizableUsingResizablejQueryUiFeature" >}}
