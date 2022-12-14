---
title: 使用 GridWeb 双击事件
type: docs
weight: 80
url: /zh/net/working-with-gridweb-double-click-events/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb包含三种类型的双击事件：

- CellDoubleClick，双击单元格时触发。
- ColumnDoubleClick，双击列标题时触发。
- RowDoubleClick，双击行标题时触发。

本主题讨论如何在 Aspose.Cells.GridWeb 中启用双击事件。它还讨论了为这些事件创建事件处理程序。

{{% /alert %}} 
## **启用双击事件**
通过将 GridWeb 控件的 EnableDoubleClickEvent 属性设置为 true，可以在客户端启用所有类型的双击事件。

{{% alert color="primary" %}} 

默认情况下，EnableDoubleClickEvent 属性设置为 false。这意味着默认情况下不启用双击事件。要实施此类事件，请首先启用该功能。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-EnableDoubleClickEvents.cs" >}}



一旦启用了双击事件，就可以为任何双击事件创建事件处理程序。当给定的双击事件被触发时，这些事件处理程序执行特定的任务。
## **处理双击事件**
要在 Visual Studio 中创建事件处理程序：

1. 双击**事件**在“属性”窗格中列出。

对于此示例，我们为各种双击事件实现了事件处理程序。
### **双击 Cell**
CellDoubleClick 事件的事件处理程序提供了一个 CellEventArgs 类型的参数，它提供了被双击的单元格的完整信息。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-CellDoubleClickEvent.cs" >}}
### **双击列标题**
ColumnDoubleClick 事件的事件处理程序提供 RowColumnEventArgs 类型的参数，该参数提供被双击的标题的列索引号和其他信息。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-ColumnDoubleClickEvent.cs" >}}
### **双击行标题**
RowDoubleClick 事件的事件处理程序提供了一个 RowColumnEventArgs 类型的参数，该参数提供了被双击的标题行的索引号和其他相关信息。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-RowDoubleClickEvent.cs" >}}
