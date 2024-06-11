---
title: 处理GridWeb双击事件
type: docs
weight: 80
url: /zh/net/aspose-cells-gridweb/gridweb-double-click-event/
keywords: GridWeb,双击,点击事件,事件
description: 本文介绍了如何在GridWeb中使用双击事件。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb包含三种类型的双击事件:

- CellDoubleClick，当双击单元格时触发。
- ColumnDoubleClick，当双击列标题时触发。
- RowDoubleClick，当双击行标题时触发。

本主题讨论如何在Aspose.Cells.GridWeb中启用双击事件。它还讨论了为这些事件创建事件处理程序。

{{% /alert %}} 
## **启用双击事件**
通过将GridWeb控件的EnableDoubleClickEvent属性设置为true可以在客户端启用所有类型的双击事件。

{{% alert color="primary" %}} 

默认情况下，EnableDoubleClickEvent属性设置为false。这意味着默认情况下未启用双击事件。要实现这些事件，首先要启用该功能。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-EnableDoubleClickEvents.cs" >}}



一旦启用双击事件，就可以为任何双击事件创建事件处理程序。这些事件处理程序在触发给定的双击事件时执行特定任务。
## **处理双击事件**
在Visual Studio中创建事件处理程序：

1. 在属性窗格的**事件**列表中双击一个事件。

在本示例中，我们为各种双击事件实现了事件处理程序。
### **双击单元格**
CellDoubleClick事件处理程序提供CellEventArgs类型的参数，该参数提供双击的单元格的完整信息。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-CellDoubleClickEvent.cs" >}}
### **双击列标题**
ColumnDoubleClick事件处理程序提供RowColumnEventArgs类型的参数，该参数提供双击列标题的列的索引号和其他信息。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-ColumnDoubleClickEvent.cs" >}}
### **双击行标题**
RowDoubleClick事件的事件处理程序提供了RowColumnEventArgs类型的参数，该参数提供了双击的标题行的索引号和其他相关信息。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-RowDoubleClickEvent.cs" >}}
