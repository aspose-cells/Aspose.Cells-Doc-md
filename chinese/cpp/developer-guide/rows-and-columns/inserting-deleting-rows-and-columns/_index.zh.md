---
title: 插入、删除行和列
type: docs
weight: 40
url: /zh/cpp/inserting-deleting-rows-and-columns/
---
##  **介绍**
无论是从头开始创建新工作表还是处理现有工作表，我们可能需要添加额外的行或列以容纳更多数据。反过来，我们可能还需要删除工作表中指定位置的行或列。为了满足这些要求，Aspose.Cells 提供了一组非常简单的类和方法，如下所述。
###  **管理行和列**
Aspose.Cells提供一堂课，[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)，代表一个 Microsoft Excel 文件。这[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)允许访问 Excel 文件中的每个工作表的集合。工作表由以下形式表示[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)班级。这[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了一个[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)代表工作表中所有单元格的集合。

这[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合提供了多种管理工作表中的行和列的方法。下面讨论其中一些。

{{% alert color="primary" %}} 

添加行或列时，工作表中的内容会向下或向右移动，如果删除行或列，则工作表中的内容会向上或向左移动。

{{% /alert %}} 
####  **插入一行**
通过调用在工作表中的任意位置插入一行[插入行](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/)的方法[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)收藏。这[插入行](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/)方法获取将插入新行的行的索引。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow-new.cpp" >}}


####  **插入多行**
要将多行插入到工作表中，请调用[插入行](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/)的方法[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)收藏。这[插入行](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/)方法有两个参数：

- 行索引，将插入新行的行的索引。
- 行数，需要插入的总行数。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows-new.cpp" >}}


####  **删除多行**
要从工作表中删除多行，请调用[删除行](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/)的方法[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)收藏。这[删除行](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/)方法有两个参数：

- 行索引，将从其中删除行的行的索引。
- 行数，需要删除的总行数。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows-new.cpp" >}}


####  **插入一列**
开发人员还可以通过调用以下函数将列插入工作表中的任意位置[插入列](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/)的方法[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)收藏。[插入列](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/)方法获取将插入新列的列的索引。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn-new.cpp" >}}


####  **删除列**
要从工作表的任意位置删除列，请调用[删除列](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/)的方法[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)收藏。这[删除列](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/)方法获取要删除的列的索引。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn-new.cpp" >}}
