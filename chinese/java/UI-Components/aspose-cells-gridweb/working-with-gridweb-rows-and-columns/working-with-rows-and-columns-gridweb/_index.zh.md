---
title: 与GridWeb的行和列一起使用
type: docs
weight: 20
url: /zh/java/working-with-rows-and-columns-gridweb/
---

## **插入行和列**
本主题解释了如何使用 Aspose.Cells.GridWeb API 在工作表中插入新行和列。可以在工作表的任何位置插入行或列。
### **插入行**
要在工作表的任何位置插入行：

1. 在Web表单或页面中添加Aspose.Cells.GridWeb控件。
1. 访问要添加行的工作表。
1. 通过指定要插入行的行索引来插入行。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingRows-InsertingRows.jsp" >}}
### **插入列**
要在工作表的任何位置插入列：

1. 将Aspose.Cells.GridWeb控件添加到Web表单或页面中。
1. 访问要添加列的工作表。
1. 通过指定要插入列的列索引来插入列。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingColumns-InsertingColumns.jsp" >}}

{{% alert color="primary" %}} 

您还可以使用insertRows()/insertColumns()方法将多行/列插入到工作表中。

{{% /alert %}} 
## **删除行和列**
本主题演示了如何使用Aspose.Cells.GridWeb API从工作表中删除行和列。开发人员可以在运行时删除行或列。
### **删除行**
要从工作表中删除行：

1. 将Aspose.Cells.GridWeb控件添加到Web表单或页面中。
1. 访问要从中删除行的工作表。
1. 通过指定行索引从工作表中删除行。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingRows-DeletingRows.jsp" >}}
### **删除列**
要从工作表中删除列：

1. 将Aspose.Cells.GridWeb控件添加到Web表单或页面中。
1. 访问要删除列的工作表。
1. 通过指定列索引从工作表中删除列。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingColumns-DeletingColumns.jsp" >}}
## **设置行高和列宽**
有时单元格值比其所在的单元格更宽，或者分布在几行中。这样的值对用户而言不是完全可见，除非他们更改行和列的高度和宽度。Aspose.Cells.GridWeb完全支持设置行高和列宽。本主题通过示例详细讨论了这些功能。
### **处理行高和列宽**
#### **设置行高**
要设置行高：

1. 将Aspose.Cells.GridWeb控件添加到您的Web表单/页面中。
1. 访问工作表的GridCells集合。
1. 设置指定行中所有单元格的高度。

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb接受以点、英寸、像素等作为单位的行高和列宽度测量。

{{% /alert %}} 

**输出：第一个行的高度已设置为50个点** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingRowHeight-SettingRowHeight.jsp" >}}
#### **设置列宽**
要设置列宽：

1. 将Aspose.Cells.GridWeb控件添加到您的Web表单/页面中。
1. 访问工作表的GridCells集合。
1. 设置指定列中所有单元格的宽度。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingColumnWidth-SettingColumnWidth.jsp" >}}
## **自定义行和列标题**
与Microsoft Excel一样，Aspose.Cells.GridWeb还使用标准的行标题和列标题（行号如1、2、3等，列号如A、B、C等）。Aspose.Cells.GridWeb还可以自定义标题。本主题讨论了使用Aspose.Cells.GridWeb API在运行时自定义行和列标题的方法。
### **自定义行标题**
要自定义行的标题或说明：

1. 将Aspose.Cells.GridWeb控件添加到Web表单/页面中。
1. 访问 GridWorksheetCollection 中的工作表。
1. 设置任何指定行的标题。

**第1行和第2行的标题已自定义** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingRowHeader-CustomizingRowHeader.jsp" >}}
### **自定义列标题**
要自定义列的标题或说明：

1. 将Aspose.Cells.GridWeb控件添加到Web表单/页面中。
1. 访问 GridWorksheetCollection 中的工作表。
1. 设置任何指定列的标题。

**第1列和第2列的标题已自定义** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingColumnHeader-CustomizingColumnHeader.jsp" >}}
## **冻结和解冻行和列**
本主题解决了如何冻结和取消冻结行和列。冻结列或行可以让用户在滚动到工作表的其他部分时保持列标题或行标题可见。在处理包含大量数据的工作表时，此功能非常有用。当用户滚动时，只有数据会向下滚动，标题保持在原位，使数据更易阅读。冻结窗格功能仅受支持于 Internet Explorer 6.0 或更高版本。
### **冻结行和列**
要冻结指定数量的行和列：

1. 将Aspose.Cells.GridWeb控件添加到Web表单/页面中。
1. 访问工作表。
1. 冻结指定数量的行和列。

{{% alert color="primary" %}} 

您也可以使用界面冻结指定数量的行和列。右键单击您想要冻结行和列的单元格，然后从列表中选择**冻结**。

{{% /alert %}} 

**被冻结的行和列** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-FreezingRowsandColumns-FreezingRowsandColumns.jsp" >}}
### **取消冻结行和列**
要解除行和列的冻结状态：

1. 将Aspose.Cells.GridWeb控件添加到Web表单/页面中。
1. 访问工作表。
1. 解除行和列的冻结。

**解冻后的工作表** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-UnfreezingRowsandColumns-UnfreezingRowsandColumns.jsp" >}}
## **保护行和列**
本主题讨论了保护行和列中的单元格，以防止最终用户执行任何操作。开发人员可以使用两种技术来实现此保护：将行和列中的单元格设置为只读，或限制GridWeb的上下文菜单选项。
### **限制上下文菜单选项**
GridWeb提供了一个上下文菜单，最终用户可以使用它来对控件执行操作。菜单提供许多选项来操作单元格、行和列。

**完整的上下文选项** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_6.png)

可以通过将GridWeb控件的EnableClientColumnOperations和EnableClientRowOperations属性设置为false来限制对行和列的任何客户端操作。还可以通过将GridWeb控件的EnableClientFreeze属性设置为false来阻止用户冻结行和列。

**限制行列选项后的上下文菜单** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_7.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-ProtectingCellsinRowsandColumns-ProtectingCellsinRowsandColumns.jsp" >}}
