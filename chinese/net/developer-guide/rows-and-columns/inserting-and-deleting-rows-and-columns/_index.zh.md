---
title: 插入和删除Excel文件的行和列
linktitle: 插入和删除行和列
type: docs
weight: 70
url: /zh/net/inserting-and-deleting-rows-and-columns/
description: 本文章展示了如何通过 Aspose.Cells for .NET API 插入和删除行和列。
keywords: Aspose.Cells的C#版本可以管理行和列，插入和删除行和列。
---

## **介绍**

无论是从头开始创建新工作表还是在现有工作表上操作，我们可能需要添加额外的行或列来容纳更多数据。反之，我们可能还需要从工作表中的指定位置删除行或列。
为了满足这些需求，Aspose.Cells提供了一组非常简单的类和方法，下面将讨论其中一些。

### **管理行和列**

Aspose.Cells提供一个类[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合，表示工作表中的所有单元格。

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合提供了几种管理工作表中行和列的方法，下面将讨论其中一些。

{{% alert color="primary" %}}

当添加行或列时，工作表中的内容会向下或向右移动，如果删除行或列，则内容会向上或向左移动。

{{% /alert %}}


## **插入行和列**

### **如何插入行**

通过调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合的[**InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)方法，在工作表中的任何位置插入一行。[**InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)方法接受新行将被插入的行索引。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

### **如何插入多行**

要向工作表中插入多行，调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合的[**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)方法。[**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)方法接受两个参数：

- 行索引，新行将从该行插入。
- 行数，需要插入的总行数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

### **如何插入带有格式的行**

要插入带有格式选项的行，使用接受[**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions)参数的[**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)重载。将[**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions)类的[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)属性与[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)枚举设置。[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)枚举有以下三个成员。

- SameAsAbove: 格式与上方行相同。
- SameAsBelow: 格式与下方行相同。
- Clear: 清除格式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

### **如何插入列**

开发人员还可以通过调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合的[**InsertColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn)方法在工作表的任何位置插入列。[**InsertColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn)方法接受将插入新列的列的索引。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

## **删除行和列**

### **如何删除多行**

要从工作表删除多行，请调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合的[**DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows)方法。[**DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows)方法接受两个参数：

- 行索引，要删除行的索引。
- 行数，需要删除的总行数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


### **如何删除列**

要从工作表的任何位置删除列，请调用[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合的[**DeleteColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn)方法。[**DeleteColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn)方法接受要删除的列的索引。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
