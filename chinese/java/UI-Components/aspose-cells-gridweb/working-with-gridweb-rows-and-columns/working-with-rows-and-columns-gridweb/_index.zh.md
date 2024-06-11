---
title: 与行和列一起使用GridWeb
type: docs
weight: 20
url: /zh/java/working-with-rows-and-columns-gridweb/
---

## **插入行和列**
本主题解释了如何使用Aspose.Cells.GridWeb API将新行和列插入工作表。可以在工作表的任何位置插入行或列。
### **插入行**
在工作表的任何位置插入行：

1. 将Aspose.Cells.GridWeb控件添加到Web表单或页面。
2. 访问要添加行的工作表。
3. 通过指定要插入行的行索引来插入行。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingRows-InsertingRows.jsp" >}}
### **插入列**
在工作表的任何位置插入列：

1. 将Aspose.Cells.GridWeb控件添加到Web表单或页面。
1. 访问要添加列的工作表。
1. 通过指定要插入列的列索引来插入列。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingColumns-InsertingColumns.jsp" >}}

{{% alert color="primary" %}} 

您还可以使用insertRows()/insertColumns()方法相应地在工作表中插入多行/列。

{{% /alert %}} 
## **删除行和列**
本主题演示了如何使用Aspose.Cells.GridWeb API从工作表中删除行和列。借助此功能，开发人员可以在运行时删除行或列。
### **删除行**
要从工作表中删除行：

1. 将Aspose.Cells.GridWeb控件添加到Web表单或页面。
1. 访问您想要从中删除行的工作表。
1. 通过指定其行索引来从工作表中删除行。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingRows-DeletingRows.jsp" >}}
### **删除列**
要从工作表中删除列：

1. 将Aspose.Cells.GridWeb控件添加到Web表单或页面。
1. 访问您想要从中删除列的工作表。
1. 通过指定其列索引来从工作表中删除列。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingColumns-DeletingColumns.jsp" >}}
## **设置行高度和列宽度**
有时单元格的值比它们所在的单元格宽，或者跨越多行。这种值对用户来说不完全可见，除非他们改变行和列的高度和宽度。Aspose.Cells.GridWeb完全支持设置行高和列宽。本主题详细讨论了这些功能，并提供了示例。
### **操作行高度和列宽度**
#### **设置行高度**
设置行的高度：

1. 在您的Web表单/页面中添加Aspose.Cells.GridWeb控件。
1. 访问工作表的GridCells集合。
1. 设置任意指定行中所有单元格的高度。

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb接受以点、英寸、像素等为单位的行高和列宽度测量。

{{% /alert %}} 

**输出：第1行的高度已设置为50个点** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingRowHeight-SettingRowHeight.jsp" >}}
#### **设置列宽度**
要设置列的宽度：

1. 在您的Web表单/页面中添加Aspose.Cells.GridWeb控件。
1. 访问工作表的GridCells集合。
1. 设置任意指定列中所有单元格的宽度。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingColumnWidth-SettingColumnWidth.jsp" >}}
## **自定义行和列标题**
与Microsoft Excel类似，Aspose.Cells.GridWeb也使用标准行标题或列标题（例如1、2、3等数字和A、B、C等字母）。Aspose.Cells.GridWeb还可以按照需要进行自定义。本主题讨论了如何使用Aspose.Cells.GridWeb API在运行时自定义行和列标题。
### **自定义行标题**
要自定义行的标题或标注：

1. 将Aspose.Cells.GridWeb控件添加到Web表单/页面。
1. 访问GridWorksheetCollection中的工作表。
1. 设置任意指定行的标题。

**自定义了第1行和第2行的标题** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingRowHeader-CustomizingRowHeader.jsp" >}}
### **自定义列标题**
要自定义列的标题或标注：

1. 将Aspose.Cells.GridWeb控件添加到Web表单/页面。
1. 访问GridWorksheetCollection中的工作表。
1. 设置任何指定列的标题。

**已自定义列1和2的标题** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingColumnHeader-CustomizingColumnHeader.jsp" >}}
## **冻结和解冻行和列**
本主题解释了如何冻结和解冻行和列。冻结列或行允许用户在滚动到工作表的其他部分时保持列标题或行标题可见。在处理包含大量数据的工作表时，此功能非常有帮助。当用户滚动时，只有数据被向下滚动，标题保持在原位，使数据更易于阅读。分栏冻结功能仅支持Internet Explorer 6.0以上版本。
### **冻结行和列**
要冻结指定数量的行和列：

1. 将Aspose.Cells.GridWeb控件添加到Web表单/页面。
1. 访问工作表。
1. 冻结若干行和列。

{{% alert color="primary" %}} 

还可以使用界面冻结特定数量的行和列。右键单击要冻结行和列的单元格，然后从列表中选择**冻结**。

{{% /alert %}} 

**冻结状态的行和列** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-FreezingRowsandColumns-FreezingRowsandColumns.jsp" >}}
### **取消冻结行和列**
要取消冻结行和列：

1. 将Aspose.Cells.GridWeb控件添加到Web表单/页面。
1. 访问工作表。
1. 取消冻结行和列。

**取消冻结后的工作表** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-UnfreezingRowsandColumns-UnfreezingRowsandColumns.jsp" >}}
## **保护行和列**
本主题讨论了保护行和列中的单元格不受最终用户执行的任何操作的几种技术。开发人员可以使用两种技术实现此保护：使行和列中的单元格只读，或限制GridWeb的上下文菜单选项。
### **限制上下文菜单选项**
GridWeb提供了一个上下文菜单，用户可以使用它来在控件上执行操作。菜单提供了许多选项，用于操纵单元格、行和列。

**完整的上下文选项** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_6.png)

可以通过将GridWeb控件的EnableClientColumnOperations和EnableClientRowOperations属性设置为false来限制在行和列上的任何客户端操作。还可以通过将GridWeb控件的EnableClientFreeze属性设置为false来限制用户冻结行和列。

**限制行和列选项后的上下文菜单** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_7.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-ProtectingCellsinRowsandColumns-ProtectingCellsinRowsandColumns.jsp" >}}
