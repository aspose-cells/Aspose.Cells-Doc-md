---
title: 插入和删除Excel文件的行和列
linktitle: 插入和删除行和列
type: docs
weight: 70
url: /zh/python-net/inserting-and-deleting-rows-and-columns/
description: 本文展示了如何通过Aspose.Cells for Python通过.NET API插入和删除行和列。
keywords: Python Excel库，Aspose.Cells Python管理行和列，Python插入行和列，Python删除行和列，Python删除行和列。
---

## **介绍**

无论是从头开始创建新工作表还是在现有工作表上工作，我们可能需要添加额外的行或列以容纳更多数据。反之，我们可能还需要从工作表中指定的位置删除行或列。
为了满足这些需求，Aspose.Cells for Python通过.NET提供了一组非常简单的类和方法，下面将进行讨论。

### **管理行和列**

Aspose.Cells for Python通过.NET提供了一个类[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)，表示Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类包含一个[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类提供了一个[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)集合，表示工作表中的所有单元格。

[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)集合提供了几种方法来管理工作表中的行和列。以下讨论了其中一些。

{{% alert color="primary" %}}

当添加行或列时，工作表中的内容会向下或向右移动，如果删除行或列，则内容会向上或向左移动。

{{% /alert %}}


## **插入行和列**

### **如何插入一行**

通过调用[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)集合的[**insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row/)方法，在工作表中的任何位置插入一行。[**insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row/)方法获取新行将被插入的行索引。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingARow-1.py" >}}

### **如何插入多行**

要在工作表中插入多行，请调用[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)集合的[**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int)方法。[**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int)方法带有两个参数：

- 行索引，新行将插入的起始行的索引。
- 行数，需要插入的总行数。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.py" >}}

### **如何插入具有格式的行**

要插入带有格式选项的行，请使用以[**InsertOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions)为参数的[**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int-aspose.cells.InsertOptions)重载。使用[**InsertOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions)类的[**copy_format_type**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions/copy_format_type/)属性设置[**CopyFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/copyformattype/)枚举值。[**CopyFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/copyformattype/)枚举有以下三个成员。

- SAME_AS_ABOVE: 将行格式设置为与上一行相同。
- SAME_AS_BELOW: 将行格式设置为与下一行相同。
- CLEAR: 清除格式。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.py" >}}

### **如何插入一列**

开发人员还可以通过调用[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)集合的[**insert_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_column/#int)方法，在工作表中的任何位置插入一列。[**insert_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_column/#int)方法获取新列将被插入的列索引。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingAColumn-1.py" >}}

## **删除行和列**

### **如何删除多行**

要从工作表中删除多行，请调用[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)集合的[**delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/#int-int)方法。[**delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/#int-int)方法带有两个参数：

- 行索引，要删除的行的索引。
- 行数，要删除的总行数。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.py" >}}


### **如何删除一列**

要从工作表中任何位置删除一列，请调用[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)集合的[**delete_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_column/#int)方法。[**delete_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_column/#int)方法获取要删除的列的索引。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-DeletingAColumn-1.py" >}}
