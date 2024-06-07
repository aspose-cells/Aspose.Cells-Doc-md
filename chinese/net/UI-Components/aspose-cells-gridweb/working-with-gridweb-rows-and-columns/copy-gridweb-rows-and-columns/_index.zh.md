---
title: 复制GridWeb行和列
type: docs
weight: 80
url: /zh/net/aspose-cells-gridweb/copy-gridweb-rows-and-columns/
keywords: GridWeb，复制
description: 本文介绍如何在GridWeb中复制行和列。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb组件在使用GridCells类时提供了复制行和列的手段。本文演示了Aspose.Cells.GridWeb公开的API的使用，以在GridWeb界面上复制行和列。 

GridCells.CopyRow、GridCells.CopyColumn、GridCells.CopyRows和GridCells.CopyColumns方法将从源行和列复制内容、样式和公式到目标行和列。

{{% /alert %}} 
## **复制行和列**
如果您还不熟悉Aspose.Cells.GridWeb组件，我们强烈建议您查看[Aspose.Cells.GridWeb简介](https://docs.aspose.com/cells/net/aspose-cells-gridweb/browsers-capabilities/)和详细文章[如何在WebForms应用程序中添加Aspose.Cells.GridWeb组件](https://docs.aspose.com/cells/net/aspose-cells-gridweb/add-gridweb-to-web-form/)。
### **复制单行**
为了让示例尽可能简单，本文使用了一个包含一行数据和一个简单公式的现有电子表格。该公式对该行中的所有数值求和。以下是在Aspose.Cells.GridWeb接口中复制行之前的电子表格显示方式。

![todo:image_alt_text](copy-gridweb-rows-and-columns_1.png)

如下所示，代码片段简单明了。它访问了活动工作表顺序的GridCells对象，以便将第一行复制到后续行。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyRow.cs" >}}


以下是在复制行操作后，Aspose.Cells.GridWeb的显示方式。

![todo:image_alt_text](copy-gridweb-rows-and-columns_2.png)
### **复制单列**
以下示例使用了一个包含一列数据和一个简单公式的现有电子表格。以下是在Aspose.Cells.GridWeb接口中复制列之前的电子表格显示方式。

![todo:image_alt_text](copy-gridweb-rows-and-columns_3.png)

与上面的示例类似，以下代码片段访问活动工作表顺序的GridCells对象，以便将第一列复制到后续列。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyColumn.cs" >}}



以下是在复制列操作后，Aspose.Cells.GridWeb的显示方式。

![todo:image_alt_text](copy-gridweb-rows-and-columns_4.png)

{{% alert color="primary" %}} 

您可以在循环中使用GridCells.CopyRow和GridCells.CopyColumn方法来复制源行和列到多行和列。

{{% /alert %}} 
### **复制多行**
在使用GridCells.CopyRows方法复制多行到新目标时，还可以传入一个整数类型的额外参数来指定要复制的源行数。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleRows.cs" >}}



这是Aspose.Cells.GridWeb在复制行操作之前和之后的显示方式。

![todo:image_alt_text](copy-gridweb-rows-and-columns_5.png)

![todo:image_alt_text](copy-gridweb-rows-and-columns_6.png)
### **复制多列**
GridCells类还提供了CopyColumns方法，它可以传入一个整数类型的额外参数来指定要复制的源列数。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleColumns.cs" >}}



这是Aspose.Cells.GridWeb在复制行操作之前和之后的显示方式。

![todo:image_alt_text](copy-gridweb-rows-and-columns_7.png)

![todo:image_alt_text](copy-gridweb-rows-and-columns_8.png)
