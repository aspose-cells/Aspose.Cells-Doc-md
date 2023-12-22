---
title: 使用行和列 GridWeb
type: docs
weight: 20
url: /zh/java/working-with-rows-and-columns-gridweb/
---
##  **插入行和列**
本主题说明如何使用 Aspose.Cells.GridWeb API 将新行和列插入到工作表中。行或列可以插入到工作表中的任何位置。
###  **插入行**
要在工作表中的任意位置插入行：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体或页面。
1. 访问您要添加行的工作表。
1. 通过指定要插入行的行索引来插入行。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingRows-InsertingRows.jsp" >}}
###  **插入列**
要在工作表中的任意位置插入列：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体或页面。
1. 访问您要添加列的工作表。
1. 通过指定要插入列的列索引来插入列。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingColumns-InsertingColumns.jsp" >}}

{{% alert color="primary" %}} 

您还可以使用 insertRows()/insertColumns() 方法相应地将多行/列插入到工作表中。

{{% /alert %}} 
##  **删除行和列**
本主题演示如何使用 Aspose.Cells.GridWeb API 从工作表中删除行和列。借助此功能，开发人员可以在运行时删除行或列。
###  **删除行**
要从工作表中删除一行：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体或页面。
1. 访问要从中删除行的工作表。
1. 通过指定行索引从工作表中删除行。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingRows-DeletingRows.jsp" >}}
###  **删除列**
要从工作表中删除列：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体或页面。
1. 访问要从中删除列的工作表。
1. 通过指定列索引从工作表中删除列。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingColumns-DeletingColumns.jsp" >}}
##  **设置行高和列宽**
有时，单元格值比它们所在的单元格或多行单元格更宽。这些值对用户来说并不完全可见，除非它们更改行和列的高度和宽度。 Aspose.Cells.GridWeb完全支持设置行高和列宽。本主题借助示例详细讨论这些功能。
###  **使用行高和列宽**
####  **设置行高**
设置行的高度：

1. 将 Aspose.Cells.GridWeb 控件添加到您的 Web 表单/页面。
1. 访问工作表的 GridCells 集合。
1. 设置任何指定行中所有单元格的高度。

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb 接受以点、英寸、像素等为单位的行高和列宽测量。

{{% /alert %}} 

**输出：第一行的高度已设置为 50 点** 

![待办事项：图像_替代_文本](working-with-rows-and-columns-gridweb_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingRowHeight-SettingRowHeight.jsp" >}}
####  **设置列宽**
设置列的宽度：

1. 将 Aspose.Cells.GridWeb 控件添加到您的 Web 表单/页面。
1. 访问工作表的 GridCells 集合。
1. 设置任何指定列中所有单元格的宽度。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingColumnWidth-SettingColumnWidth.jsp" >}}
##  **自定义行标题和列标题**
与 Microsoft Excel 一样，Aspose.Cells.GridWeb 也对行（如 1、2、3 等数字）和列（如 A、B、C 等字母）使用标准标题或标题。 Aspose.Cells.GridWeb 还可以自定义标题。本主题讨论使用 Aspose.Cells.GridWeb API 在运行时自定义行标题和列标题。
###  **自定义行标题**
要自定义行的标题或标题：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体/页面。
1. 访问 GridWorksheetCollection 中的工作表。
1. 设置任何指定行的标题。

**第 1 行和第 2 行的标题已自定义** 

![待办事项：图像_替代_文本](working-with-rows-and-columns-gridweb_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingRowHeader-CustomizingRowHeader.jsp" >}}
###  **自定义列标题**
要自定义列的标题或标题：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体/页面。
1. 访问 GridWorksheetCollection 中的工作表。
1. 设置任何指定列的标题。

**第 1 列和第 2 列的标题已自定义** 

![待办事项：图像_替代_文本](working-with-rows-and-columns-gridweb_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingColumnHeader-CustomizingColumnHeader.jsp" >}}
##  **冻结和解冻行和列**
本主题介绍如何冻结和解冻行和列。冻结列或行允许用户在滚动到工作表的其他部分时保持列标题或行标题可见。当处理包含大量数据的工作表时，此功能非常有用。当用户滚动时，仅数据向下滚动并且标题保持在原位，使日期更易于阅读。仅 Internet Explorer 6.0 或更高版本支持冻结窗格功能。
###  **冻结行和列**
要冻结特定数量的行和列：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体/页面。
1. 访问工作表。
1. 冻结一些行和列。

{{% alert color="primary" %}} 

还可以使用该界面冻结特定数量的行和列。右键单击要冻结行和列的单元格，然后选择**冻结**从列表中。

{{% /alert %}} 

**行和列处于冻结状态** 

![待办事项：图像_替代_文本](working-with-rows-and-columns-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-FreezingRowsandColumns-FreezingRowsandColumns.jsp" >}}
###  **解冻行和列**
要解冻行和列：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体/页面。
1. 访问工作表。
1. 解冻行和列。

**解冻后的工作表** 

![待办事项：图像_替代_文本](working-with-rows-and-columns-gridweb_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-UnfreezingRowsandColumns-UnfreezingRowsandColumns.jsp" >}}
##  **保护行和列**
本主题讨论一些保护行和列中的单元格免受最终用户执行的任何类型操作的技术。开发人员可以使用两种技术来实现这种保护：将行和列中的单元格设置为只读，或者限制 GridWeb 的上下文菜单选项。
###  **限制上下文菜单选项**
GridWeb 提供了一个上下文菜单，最终用户可以使用该菜单对控件执行操作。该菜单提供了许多用于操作单元格、行和列的选项。

**完整的上下文选项** 

![待办事项：图像_替代_文本](working-with-rows-and-columns-gridweb_6.png)

通过限制上下文菜单中的可用选项，可以限制对行和列的任何类型的客户端操作。可以通过将 GridWeb 控件的 EnableClientColumnOperations 和 EnableClientRowOperations 属性设置为 false 来完成。还可以通过将 GridWeb 控件的 EnableClientFreeze 属性设置为 false 来限制用户冻结行和列。

**限制行和列选项后的上下文菜单** 

![待办事项：图像_替代_文本](working-with-rows-and-columns-gridweb_7.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-ProtectingCellsinRowsandColumns-ProtectingCellsinRowsandColumns.jsp" >}}
