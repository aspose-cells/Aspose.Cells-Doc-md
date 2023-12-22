---
title: 刷新自动筛选后获取所有隐藏行索引
type: docs
weight: 320
url: /zh/net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: 了解如何使用 Aspose.Cells for .NET API 刷新自动筛选后获取所有隐藏行索引。
keywords: Get All Hidden Rows Indices after Refreshing AutoFilter, Obtain All Hidden Rows Indices after Refreshing AutoFilter, Retrieve All Hidden Rows Indices after Refreshing AutoFilter
---
##  **可能的使用场景**

当您在工作表单元格上应用自动筛选器时，某些行会自动隐藏。但情况可能是某些行已被 Excel 最终用户手动隐藏，并且它们未被自动筛选器隐藏。因此，很难知道哪些行被自动筛选器隐藏，哪些行被 Excel 最终用户手动隐藏。 Aspose.Cells 使用 int[] 处理这个问题[**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1)方法。此方法返回由自动筛选器隐藏的所有行的行索引，而不是由 Excel 最终用户手动隐藏的行。

##  **刷新自动筛选后获取所有隐藏行索引**

请参阅以下加载示例代码[Excel 文件示例](64716909.xlsx)其中包含一些由 Excel 最终用户手动隐藏的行。该代码应用自动过滤器并使用 int[] 刷新它[**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1)方法，通过自动过滤器返回所有隐藏行的行索引。然后，它会在控制台上打印隐藏行的索引以及单元格名称和值。

##  **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.cs" >}}

##  **控制台输出**

{{< highlight "java" >}}

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
