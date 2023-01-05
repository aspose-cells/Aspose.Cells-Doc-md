---
title: 插入和删除Excel文件的行和列
linktitle: 插入和删除行和列
type: docs
weight: 70
url: /zh/net/inserting-and-deleting-rows-and-columns/
---
## **介绍**

无论是从头开始创建新工作表还是处理现有工作表，我们都可能需要添加额外的行或列以容纳更多数据。反之，我们可能还需要删除工作表中指定位置的行或列。
为满足这些要求，Aspose.Cells 提供了一组非常简单的类和方法，如下所述。

### **管理行和列**

Aspose.Cells提供类[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)允许访问 Excel 文件中每个工作表的集合。工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)代表工作表中所有单元格的集合。

这[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection 提供了多种方法来管理工作表中的行和列。下面讨论其中一些。

{{% alert color="primary" %}}

添加行或列时，工作表中的内容向下或向右移动，如果删除行或列，则内容向上或向左移动。

{{% /alert %}}


## **插入行和列**

### **插入一行**

通过调用[**插入行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)的方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏。这[**插入行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)方法采用将插入新行的行的索引。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

### **插入多行**

要将多行插入到工作表中，请调用[**插入行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)的方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏。这[**插入行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)方法有两个参数：

- 行索引，将插入新行的行的索引。
- Number of rows，需要插入的总行数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

### **插入带格式的行**

要插入带有格式选项的行，请使用[**插入行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)超载需要[**插入选项**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions)作为参数。设置[**复制格式类型**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)的财产[**插入选项**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions)类[**复制格式类型**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)枚举。这[**复制格式类型**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)枚举具有三个成员，如下所列。

- SameAsAbove：格式化与上一行相同的行。
- SameAsBelow：格式化与下一行相同的行。
- 清除：清除格式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

### **插入一列**

开发人员还可以通过调用[**插入列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn)的方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏。这[**插入列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn)方法采用将插入新列的列的索引。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

## **删除行和列**

### **删除多行**

要从工作表中删除多行，请调用[**删除行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows)的方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏。这[**删除行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows)方法有两个参数：

- 行索引，将从中删除行的行的索引。
- 行数，需要删除的总行数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


### **删除列**

要从工作表的任何位置删除列，请调用[**删除列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn)的方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏。这[**删除列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn)方法采用要删除的列的索引。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
