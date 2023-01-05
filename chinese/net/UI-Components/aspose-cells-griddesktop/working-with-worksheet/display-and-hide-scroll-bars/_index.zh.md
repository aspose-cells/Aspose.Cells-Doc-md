---
title: 显示和隐藏滚动条
type: docs
weight: 140
url: /zh/net/display-and-hide-scroll-bars/
---
{{% alert color="primary" %}}

滚动条对于导航电子表格的内容非常有用，这些电子表格又宽又深，也就是说，有很多行和列。大多数应用程序支持两种类型的滚动条：

- 垂直滚动条
- 水平滚动条

这两个都可以在 Microsoft Excel 中找到。

Aspose.Cell 的 GridDesktop API 提供水平和垂直滚动条，用于滚动工作表的内容。使用 Aspose.Cells.GridDesktop API，开发人员可以控制这两个滚动条的可见性。

{{% /alert %}}

## **控制滚动条可见性**

要控制滚动条在 GridDesktop 中的可见性，请使用 IsVerticalScrollBarVisible 和 IsHorizontalScrollBarVisible 属性。下面的例子展示了如何隐藏和显示滚动条。

### **编程示例：隐藏滚动条**

要隐藏滚动条，请将控制可见性的属性设置为 false。

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-DisplayHideScrolBars-HideScrollbars.cs" >}}

### **编程示例：使滚动条可见**

要使滚动条可见，请将控制可见性的属性设置为 true。

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-DisplayHideScrolBars-ShowScrollbars.cs" >}}
