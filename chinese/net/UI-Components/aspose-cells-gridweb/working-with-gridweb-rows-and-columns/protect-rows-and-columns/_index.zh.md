---
title: 保护行和列
type: docs
weight: 60
url: /zh/net/protect-rows-and-columns/
---
{{% alert color="primary" %}} 

本主题讨论了一些技术，用于保护行和列中的单元格免受最终用户执行的任何类型的操作。开发人员可以使用两种技术来实现这种保护：将行和列中的单元格设置为只读，或者限制 Aspose.Cells.GridWeb 的上下文菜单选项。下面将借助示例讨论这两种技术。

{{% /alert %}} 
## **保护行和列中的 Cells**
### **使行和列只读**
保护工作表中的行和列的一种方法是将单元格设置为只读。然后它们不能被最终用户删除。

使行和列只读：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体。
1. 访问集合中的 GridWorksheet。
1. 将行或列中所需的单元格设置为只读。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-MakeRowsColumnsReadOnly.aspx-MakeCellReadOnly.cs" >}}
### **限制上下文菜单选项**
Aspose.Cells.GridWeb 提供了一个上下文菜单，最终用户可以使用该菜单对控件执行操作。该菜单提供了许多用于操作单元格、行和列的选项。

**完整的上下文选项** 

![待办事项：图像_替代_文本](protect-rows-and-columns_1.png)

通过限制上下文菜单中可用的选项，可以限制任何类型的客户端对行和列的操作。这可以通过将 GridWeb 控件的 EnableClientColumnOperations 和 EnableClientRowOperations 属性设置为 false 来完成。也可以通过将 GridWeb 控件的 EnableClientFreeze 属性设置为 false 来限制用户冻结行和列。

**限制行和列选项后的上下文菜单** 

![待办事项：图像_替代_文本](protect-rows-and-columns_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-RestrictContextMenu.aspx-RestrictContextMenu.cs" >}}
