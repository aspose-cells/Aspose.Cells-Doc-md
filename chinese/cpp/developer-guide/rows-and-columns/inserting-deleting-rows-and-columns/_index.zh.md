---
title: 插入、删除行和列
type: docs
weight: 40
url: /zh/cpp/inserting-deleting-rows-and-columns/
---
## **介绍**
无论是从头开始创建新工作表还是处理现有工作表，我们都可能需要添加额外的行或列以容纳更多数据。反之，我们可能还需要删除工作表中指定位置的行或列。为满足这些要求，Aspose.Cells 提供了一组非常简单的类和方法，如下所述。
### **管理行和列**
Aspose.Cells提供了一个类，[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)，代表一个 Microsoft Excel 文件。这[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)类包含一个[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)允许访问 Excel 文件中每个工作表的集合。工作表由[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)班级。这[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)类提供了一个[细胞](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)代表工作表中所有单元格的集合。

这[细胞](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collection 提供了多种方法来管理工作表中的行和列。下面讨论其中一些。

{{% alert color="primary" %}} 

添加行或列时，工作表中的内容向下或向右移动，如果删除行或列，则内容向上或向左移动。

{{% /alert %}} 
#### **插入一行**
通过调用[插入行](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad9c067ccb5f34a7740f5d1cc3dbefbe7)的方法[细胞](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)收藏。这[插入行](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad9c067ccb5f34a7740f5d1cc3dbefbe7)方法采用将插入新行的行的索引。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow.cpp" >}}


#### **插入多行**
要将多行插入到工作表中，请调用[插入行](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a61e4cd6dcaeeb0d11afd54616df75ee0)的方法[细胞](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)收藏。这[插入行](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a61e4cd6dcaeeb0d11afd54616df75ee0)方法有两个参数：

- 行索引，将插入新行的行的索引。
- Number of rows，需要插入的总行数。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows.cpp" >}}


#### **删除多行**
要从工作表中删除多行，请调用[删除行](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a251261027b564ebdf27c2c6d5149c0e1)的方法[细胞](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)收藏。这[删除行](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a251261027b564ebdf27c2c6d5149c0e1)方法有两个参数：

- 行索引，将从中删除行的行的索引。
- 行数，需要删除的总行数。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows.cpp" >}}


#### **插入一列**
开发人员还可以通过调用[插入列](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a8e8cb6d0812129669258378649b3fd55)的方法[细胞](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)收藏。[插入列](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a8e8cb6d0812129669258378649b3fd55)方法采用将插入新列的列的索引。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn.cpp" >}}


#### **删除列**
要从工作表的任何位置删除列，请调用[删除列](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ae00721fd2be220e7b73b2cab6a70e89b)的方法[细胞](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)收藏。这[删除列](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ae00721fd2be220e7b73b2cab6a70e89b)方法采用要删除的列的索引。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn.cpp" >}}
