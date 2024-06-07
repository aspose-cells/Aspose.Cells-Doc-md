---
title: 插入，删除行和列
type: docs
weight: 40
url: /zh/cpp/inserting-deleting-rows-and-columns/
---

## **介绍**
无论是从头开始创建新的工作表，还是在现有工作表上工作，我们可能需要添加额外的行或列以容纳更多数据。 相反，我们可能还需要从工作表中的指定位置删除行或列。 为了满足这些需求，Aspose.Cells提供了一套非常简单的类和方法，下面进行讨论。
### **管理行和列**
Aspose.Cells提供一个类，[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)，代表一个Microsoft Excel文件。 [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类包含一个 [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) 集合，允许访问Excel文件中的每个工作表。 工作表由 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类表示。 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类提供一个 [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合，代表工作表中的所有单元格。

[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合提供了几种管理工作表中行和列的方法。 其中一些方法如下所述。

{{% alert color="primary" %}} 

当添加行或列时，工作表中的内容会向下或向右移动，如果删除行或列，则内容会向上或向左移动。

{{% /alert %}} 
#### **插入行**
通过调用 [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合的 [InsertRow](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) 方法，在工作表的任何位置插入一行。 [InsertRow](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) 方法接受将插入新行的行索引。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow-new.cpp" >}}


#### **插入多行**
要在工作表中插入多行，请调用 [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合的 [InsertRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) 方法。 [InsertRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) 方法需要两个参数：

- 行索引，新行将插入的起始行的索引。
- 行数，需要插入的总行数。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows-new.cpp" >}}


#### **删除多行**
要从工作表中删除多行，请调用 [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合的 [DeleteRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) 方法。 [DeleteRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) 方法需要两个参数：

- 行索引，要删除的行的索引。
- 行数，要删除的总行数。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows-new.cpp" >}}


#### **插入列**
开发人员还可以通过调用[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合的[InsertColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/)方法，在工作表中任何位置插入列。[InsertColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/)方法接受要插入新列的列索引。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn-new.cpp" >}}


#### **删除列**
要从工作表的任何位置删除列，请调用[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合的[DeleteColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/)方法。[DeleteColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/)方法接受要删除的列的索引。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn-new.cpp" >}}
