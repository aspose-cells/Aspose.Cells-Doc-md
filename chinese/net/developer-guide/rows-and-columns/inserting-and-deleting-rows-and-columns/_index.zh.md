---
title: 插入和删除Excel文件的行和列
linktitle: 插入和删除行和列
type: docs
weight: 70
url: /zh/net/inserting-and-deleting-rows-and-columns/
description: 本文展示了如何通过Aspose.Cells for .NET API插入和删除行和列。
keywords: Aspose.Cells C# 管理行和列，插入行和列，删除行和列
---

## **介绍**

无论是从头开始创建新工作表还是在现有工作表上工作，我们可能需要添加额外的行或列以容纳更多数据。反之，我们可能还需要从工作表中指定的位置删除行或列。
为了满足这些要求，Aspose.Cells提供了一套非常简单的类和方法，如下所述。

### **管理行和列**

Aspose.Cells提供了一个类，它代表了一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含了一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合，代表工作表中的所有单元格。

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合提供了几种方法来管理工作表中的行和列。以下讨论了其中一些。

{{% alert color="primary" %}}

当添加行或列时，工作表中的内容会向下或向右移动，如果删除行或列，则内容会向上或向左移动。

{{% /alert %}}


## **插入行和列**

### **如何插入一行**

通过调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合的[**InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)方法，在工作表中的任何位置插入一行。[**InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)方法获取新行将被插入的行索引。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

### **如何插入多行**

要在工作表中插入多行，请调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合的[**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)方法。[**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)方法带有两个参数：

- 行索引，新行将插入的起始行的索引。
- 行数，需要插入的总行数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

### **如何插入具有格式的行**

要插入带有格式选项的行，请使用以[**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions)为参数的[**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)重载。使用[**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions)类的[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)属性设置[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)枚举值。[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)枚举有以下三个成员。

- SameAsAbove：与上面的行格式相同。
- SameAsBelow：与下面的行格式相同。
- Clear：清除格式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

### **如何插入一列**

开发人员还可以通过调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合的[**InsertColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn)方法，在工作表中的任何位置插入一列。[**InsertColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn)方法获取新列将被插入的列索引。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

## **删除行和列**

### **如何删除多行**

要从工作表中删除多行，请调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合的[**DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows)方法。[**DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows)方法带有两个参数：

- 行索引，要删除的行的索引。
- 行数，要删除的总行数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


### **如何删除一列**

要从工作表中任何位置删除一列，请调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合的[**DeleteColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn)方法。[**DeleteColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn)方法获取要删除的列的索引。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
