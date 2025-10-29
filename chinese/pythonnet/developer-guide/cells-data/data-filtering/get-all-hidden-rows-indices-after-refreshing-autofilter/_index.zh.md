---
title: 在刷新AutoFilter后获取所有隐藏行索引
type: docs
weight: 320
url: /zh/python-net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: 学习如何使用Aspose.Cells for Python via .NET API在刷新AutoFilter后获取所有隐藏行索引。
keywords: Python Excel库，Python在刷新AutoFilter后获取所有隐藏行索引，Python在刷新AutoFilter后获取所有隐藏行索引，Python在刷新AutoFilter后检索所有隐藏行索引
---

## **可能的使用场景**

当您在工作表单元格上应用自动筛选时，一些行会自动隐藏。但可能情况是，一些行已经被Excel最终用户手动隐藏了，并不是由自动筛选自动隐藏的。因此，很难知道哪些行是由自动筛选隐藏的，哪些是由Excel最终用户手动隐藏的。Aspose.Cells for Python via .NET 使用[**AutoFilter.refresh(hide_rows)**](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/refresh/#bool)方法解决了这个问题。该方法返回所有由自动筛选隐藏而不是由Excel最终用户手动隐藏的行索引。

## **在刷新自动筛选后获取所有隐藏行索引**

请参阅以下示例代码，该代码加载包含一些由Excel最终用户手动隐藏的行的[示例Excel文件](64716909.xlsx)。该代码应用自动筛选并使用[**AutoFilter.refresh(hide_rows)**](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/refresh/#bool)方法刷新自动筛选，返回自动筛选隐藏的所有行的行索引。然后在控制台上打印出隐藏行的索引、单元格名称和值。

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.py" >}}

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
{{< app/cells/assistant language="python-net" >}}
