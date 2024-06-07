---
title: 保护行和列
type: docs
weight: 60
url: /zh/net/aspose-cells-gridweb/protect-rows-and-columns/
keywords: GridWeb,protect
description: 本文介绍如何保护 GridWeb 中的行和列。
---

{{% alert color="primary" %}} 

本主题讨论了保护行和列中单元格免受终端用户执行的任何操作的几种技术。开发人员可以使用两种技术实现此保护：使行和列中的单元格只读，或限制 Aspose.Cells.GridWeb 的上下文菜单选项。下面通过示例讨论了这两种技术。

{{% /alert %}} 
## **保护行和列中的单元格**
### **使行和列成为只读**
保护工作表中的行和列的一种方法是将单元格设置为只读。这样，终端用户就无法删除这些单元格。

要将行和列设置为只读：

1. 将Aspose.Cells.GridWeb控件添加到Web表单中。
1. 访问集合中的GridWorksheet。
1. 将您希望设置为只读的单元格设置为只读。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-MakeRowsColumnsReadOnly.aspx-MakeCellReadOnly.cs" >}}
### **限制上下文菜单选项**
Aspose.Cells.GridWeb提供了一个上下文菜单，用户可以使用它来对控件执行操作。该菜单提供许多操作单元格、行和列的选项。

**完整的上下文选项** 

![todo:image_alt_text](protect-rows-and-columns_1.png)

通过限制上下文菜单中可用的选项，可以限制任何一种类型的客户端端操作。可以通过将GridWeb控件的EnableClientColumnOperations和EnableClientRowOperations属性设置为false来实现。也可以通过将GridWeb控件的EnableClientFreeze属性设置为false来限制用户冻结行和列的操作。

**限制行列选项后的上下文菜单** 

![todo:image_alt_text](protect-rows-and-columns_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-RestrictContextMenu.aspx-RestrictContextMenu.cs" >}}
