---
title: 刷新自动筛选后，获取所有隐藏行的索引（使用C++实现的Golang）
linktitle: 在刷新AutoFilter后获取所有隐藏行索引
type: docs
weight: 320
url: /zh/go-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: 学习如何使用Aspose.Cells for C++ API在刷新AutoFilter后获取所有隐藏行的索引。
keywords: 刷新AutoFilter后获取所有隐藏行的索引，刷新AutoFilter后获得所有隐藏行的索引，检索刷新AutoFilter后所有隐藏行的索引
---

## **可能的使用场景**

当您在工作表单元格上应用自动筛选时，一些行会自动隐藏。但是可能会出现这种情况，一些行已经被Excel终端用户手动隐藏，它们不是由自动筛选隐藏的。这使得难以知道哪些行是由自动筛选隐藏的，哪些是由Excel终端用户手动隐藏的。Aspose.Cells使用int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/go-cpp/autofilter/refresh/)方法来解决这个问题。该方法返回所有由自动筛选隐藏而不是由Excel终端用户手动隐藏的行的行索引。

## **在刷新自动筛选后获取所有隐藏行索引**

请参阅以下示例代码，加载包含一些由Excel终端用户手动隐藏的行的[示例Excel文件](64716909.xlsx)。代码应用自动筛选并使用int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/go-cpp/autofilter/refresh/)方法来刷新它，该方法返回由自动筛选隐藏的所有行的行索引。然后将隐藏行的索引与单元格名称和值一起打印在控制台上。

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetAllHiddenRowsIndicesAfterRefreshingAutofilter.go" >}}
## **控制台输出**

{{< highlight java >}}

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.

\--------------------------

1       A2      Apple

2       A3      Apple

3       A4      Apple

6       A7      Apple

7       A8      Apple

11      A12     Pear

12      A13     Pear

{{< /highlight >}}
