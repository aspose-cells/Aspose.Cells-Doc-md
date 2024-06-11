---
title: 保护行和列
type: docs
weight: 60
url: /zh/net/aspose-cells-gridweb/protect-rows-and-columns/
keywords: GridWeb，保护
description: 本文介绍了如何保护GridWeb中的行和列。
---

{{% alert color="primary" %}} 

此主题讨论了保护行和列中单元格不受最终用户执行的任何操作的几种技术。开发人员可以使用两种技术来实现此保护：通过使行和列中的单元格只读，或者通过限制Aspose.Cells.GridWeb的上下文菜单选项。下面将通过示例讨论这两种技术。

{{% /alert %}} 
## **保护行和列中的单元格**
### **使行和列只读**
保护工作表中行和列的一种方法是使单元格只读。然后最终用户无法删除它们。

使行和列只读：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 表单中。
1. 访问集合中的GridWorksheet。
1. 设置你所需要的行或列中的单元格为只读。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-MakeRowsColumnsReadOnly.aspx-MakeCellReadOnly.cs" >}}
### **限制上下文菜单选项**
Aspose.Cells.GridWeb提供了一个上下文菜单，最终用户可以使用它对控件执行操作。菜单提供了许多用于操作单元格、行和列的选项。

**完整的上下文选项** 

![todo:image_alt_text](protect-rows-and-columns_1.png)

可以通过限制上下文菜单中的可用选项来限制行和列上的任何一种客户端操作。可以通过将GridWeb控件的EnableClientColumnOperations和EnableClientRowOperations属性设置为false来实现。还可以通过将GridWeb控件的EnableClientFreeze属性设置为false来限制用户冻结行和列。

**限制行和列选项后的上下文菜单** 

![todo:image_alt_text](protect-rows-and-columns_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-RestrictContextMenu.aspx-RestrictContextMenu.cs" >}}
