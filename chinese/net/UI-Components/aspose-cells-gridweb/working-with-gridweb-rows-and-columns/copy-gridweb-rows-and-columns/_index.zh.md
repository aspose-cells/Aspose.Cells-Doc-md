---
title: 复制GridWeb行和列
type: docs
weight: 80
url: /zh/net/aspose-cells-gridweb/copy-gridweb-rows-and-columns/
keywords: GridWeb,复制
description: 本文介绍如何在GridWeb中复制行和列。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb组件在使用GridCells类时提供了复制行和列的手段。本文演示了通过Aspose.Cells.GridWeb公开的API的用法，以在GridWeb界面上复制行和列。 

GridCells.CopyRow、GridCells.CopyColumn、GridCells.CopyRows和GridCells.CopyColumns方法将从源行和列复制内容、样式和公式到目标位置。

{{% /alert %}} 
## **复制行和列**
如果您还不熟悉Aspose.Cells.GridWeb组件，我们强烈建议您查看[介绍Aspose.Cells.GridWeb](https://docs.aspose.com/cells/net/aspose-cells-gridweb/browsers-capabilities/)和[如何在WebForms应用程序中添加Aspose.Cells.GridWeb组件的详细文章](https://docs.aspose.com/cells/net/aspose-cells-gridweb/add-gridweb-to-web-form/)。
### **复制单行**
为了保持示例简单，文章使用一个包含一行和一个简单公式（对该行中所有值求和）的现有电子表格。以下是在复制该行之前，电子表格在Aspose.Cells.GridWeb界面中的显示方式。

![todo:image_alt_text](copy-gridweb-rows-and-columns_1.png)

如下所示，代码片段很简单。它访问活动工作表的GridCells对象，以将第一行复制到后续行。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyRow.cs" >}}


在复制行操作之后，Aspose.Cells.GridWeb的外观如何。

![todo:image_alt_text](copy-gridweb-rows-and-columns_2.png)
### **复制单列**
以下示例使用包含一列和一个简单公式（对该列中所有值求和）的现有电子表格。以下是在复制该列之前，电子表格在Aspose.Cells.GridWeb界面中的显示方式。

![todo:image_alt_text](copy-gridweb-rows-and-columns_3.png)

与上面的示例类似，以下代码段访问活动工作表的GridCells对象，将第一列复制到后续列。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyColumn.cs" >}}



在复制列操作之后，Aspose.Cells.GridWeb的外观如何。

![todo:image_alt_text](copy-gridweb-rows-and-columns_4.png)

{{% alert color="primary" %}} 

您可以在循环中使用GridCells.CopyRow和GridCells.CopyColumn方法来分别将源行和列复制到多行和多列。

{{% /alert %}} 
### **复制多行**
在使用GridCells.CopyRows方法复制多行到新目标时，还可以额外提供一个整数类型的参数，以指定要复制的源行数。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleRows.cs" >}}



在复制行操作之前和之后，查看Aspose.Cells.GridWeb的外观。

![todo:image_alt_text](copy-gridweb-rows-and-columns_5.png)

![todo:image_alt_text](copy-gridweb-rows-and-columns_6.png)
### **复制多个列**
GridCells类还提供CopyColumns方法，额外提供一个整数类型的参数，以指定要复制的源列数。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleColumns.cs" >}}



在复制行操作之前和之后，查看Aspose.Cells.GridWeb的外观。

![todo:image_alt_text](copy-gridweb-rows-and-columns_7.png)

![todo:image_alt_text](copy-gridweb-rows-and-columns_8.png)
