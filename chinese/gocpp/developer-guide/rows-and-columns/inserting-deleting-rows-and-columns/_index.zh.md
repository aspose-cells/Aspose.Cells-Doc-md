---
title: 插入、删除行和列
type: docs
weight: 40
url: /zh/go-cpp/inserting-deleting-rows-and-columns/
---

## **介绍**

无论是从头开始创建新的工作表还是在现有工作表上工作，我们可能需要添加额外的行或列来容纳更多数据。相反，我们也可能需要从工作表中的指定位置删除行或列。为了满足这些要求，Aspose.Cells提供了一组非常简单的类和方法，如下所述。

### **管理行和列**

Aspose.Cells提供[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)类，它代表微软Excel文件。包含一个[Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/)集合，能访问Excel文件中的每个工作表。

[Cells](https://reference.aspose.com/cells/go-cpp/cells/)集合提供多种管理工作表中行和列的方法，部分如下：

{{% alert color="primary" %}}

当添加行或列时，工作表中的内容会向下或向右移动，如果删除行或列，则内容会向上或向左移动。

{{% /alert %}}

可以调用[Cells](https://reference.aspose.com/cells/go-cpp/cells/)集合的[InsertRow](https://reference.aspose.com/cells/go-cpp/cells/insertrow/)方法在工作表任意位置插入行。该方法的参数为即将插入行的索引。
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertRow.go" >}}

#### **插入多行**

要在工作表中插入多行，调用[Cells](https://reference.aspose.com/cells/go-cpp/cells/insertrows_int_int/)方法。该方法的两个参数如下：

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertingMultipleRows.go" >}}

#### **删除多行**

要从工作表中删除多行，调用[Cells](https://reference.aspose.com/cells/go-cpp/cells/deleterows_int_int_bool/)方法。该方法的两个参数如下：

- 行索引，要删除行的索引。
- 行数，需要删除的总行数。

#### **插入列**

开发者也可以调用[Cells](https://reference.aspose.com/cells/go-cpp/cells/)集合的[InsertColumn](https://reference.aspose.com/cells/go-cpp/cells/insertcolumn_int/)方法，在任意位置插入列。参数为新列的索引。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertColumn.go" >}}

要删除工作表中的列，调用[Cells](https://reference.aspose.com/cells/go-cpp/cells/)集合的[DeleteColumn](https://reference.aspose.com/cells/go-cpp/cells/deletecolumn_int/)方法。参数为要删除的列索引。
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteColumn.go" >}}
