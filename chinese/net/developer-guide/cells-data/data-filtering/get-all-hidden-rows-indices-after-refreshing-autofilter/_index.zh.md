---
title: 刷新AutoFilter后获取所有隐藏行索引
type: docs
weight: 320
url: /zh/net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: 学习如何使用Aspose.Cells for .NET API在刷新AutoFilter后获取所有隐藏行索引。
keywords: 刷新AutoFilter后获取所有隐藏行索引，刷新AutoFilter后获取所有隐藏行索引，检索AutoFilter刷新后所有隐藏行索引
---

## **可能的使用场景**

当您在工作表单元格上应用自动筛选时，一些行会自动隐藏。但可能的情况是，一些行已经被Excel最终用户手动隐藏，而不是由自动筛选隐藏。因此，很难知道哪些行是由自动筛选隐藏，哪些是由Excel最终用户手动隐藏。Aspose.Cells使用int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1)方法来处理这个问题。此方法返回由自动筛选隐藏而不是由Excel最终用户手动隐藏的所有行的行索引。

## **刷新AutoFilter后获取所有隐藏行索引**

请查看以下加载包含一些由Excel最终用户手动隐藏的行的[示例Excel文件](64716909.xlsx)的样本代码。该代码应用自动筛选并刷新它，使用int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1)方法返回由自动筛选隐藏的所有行的行索引。然后在控制台上打印隐藏行的索引以及单元格名称和值。

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.cs" >}}

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
