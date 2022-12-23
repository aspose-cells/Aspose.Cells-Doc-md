---
title: 复制 GridWeb 行和列
type: docs
weight: 80
url: /zh/net/copy-gridweb-rows-and-columns/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb 组件提供了在使用 GridCells 类时复制行和列的方法。本文演示了如何使用 Aspose.Cells.GridWeb 公开的 API 在 GridWeb 界面上复制行和列。

GridCells.CopyRow、GridCells.CopyColumn、GridCells.CopyRows 和 GridCells.CopyColumns 方法会将内容、样式和公式从源行和列复制到目标。

{{% /alert %}} 
## **复制行和列**
如果您还不熟悉 Aspose.Cells.GridWeb 组件，我们强烈建议您检查[Aspose.Cells.GridWeb简介](https://docs.aspose.com/cells/net/browsers-capabilities/)和详细的文章[如何在 WebForms 应用程序中添加 Aspose.Cells.GridWeb 组件](https://docs.aspose.com/cells/net/add-gridweb-to-web-form/).
### **复制单行**
为了使示例保持简单，本文使用了一个包含一行的现有电子表格和一个对行中所有值求和的简单公式。以下是复制行之前电子表格在 Aspose.Cells.GridWeb 界面中的显示方式。

![待办事项：图片_替代_文本](copy-gridweb-rows-and-columns_1.png)

代码片段很简单，如下所示。它访问活动工作表顺序的 GridCells 对象，以将第一行复制到后续行。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyRow.cs" >}}


这是 Aspose.Cells.GridWeb 在复制行操作后的样子。

![待办事项：图片_替代_文本](copy-gridweb-rows-and-columns_2.png)
### **复制单列**
以下示例使用一个包含一列的现有电子表格和一个对列中所有值求和的简单公式。以下是复制列之前电子表格在 Aspose.Cells.GridWeb 界面中的显示方式。

![待办事项：图片_替代_文本](copy-gridweb-rows-and-columns_3.png)

与上面的示例类似，以下代码片段访问活动工作表顺序的 GridCells 对象，以将第一列复制到后续列。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyColumn.cs" >}}



这是 Aspose.Cells.GridWeb 在复制列操作后的样子。

![待办事项：图片_替代_文本](copy-gridweb-rows-and-columns_4.png)

{{% alert color="primary" %}} 

您可以在循环中使用 GridCells.CopyRow 和 GridCells.CopyColumn 方法将源行和列分别复制到多个行和列。

{{% /alert %}} 
### **复制多行**
还可以在使用 GridCells.CopyRows 方法时将多行复制到新目标，该方法采用整数类型的附加参数来指定要复制的源行数。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleRows.cs" >}}



这是 Aspose.Cells.GridWeb 在复制行操作前后的样子。

![待办事项：图片_替代_文本](copy-gridweb-rows-and-columns_5.png)

![待办事项：图片_替代_文本](copy-gridweb-rows-and-columns_6.png)
### **复制多列**
GridCells 类还提供 CopyColumns 方法，该方法采用整数类型的附加参数来指定要复制的源列数。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleColumns.cs" >}}



这是 Aspose.Cells.GridWeb 在复制行操作前后的样子。

![待办事项：图片_替代_文本](copy-gridweb-rows-and-columns_7.png)

![待办事项：图片_替代_文本](copy-gridweb-rows-and-columns_8.png)
