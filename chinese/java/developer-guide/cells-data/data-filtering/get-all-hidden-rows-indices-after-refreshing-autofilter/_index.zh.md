---
title: 在刷新AutoFilter后获取所有隐藏行索引
type: docs
weight: 240
url: /zh/java/get-all-hidden-rows-indices-after-refreshing-autofilter/
---

## **可能的使用场景**

当在工作表单元上应用自动筛选时，一些行会自动隐藏。但可能存在一种情况，有些行已由Excel最终用户手动隐藏，而不是由自动筛选进行隐藏。因此，很难知道哪些行是由自动筛选隐藏的，哪些是由Excel最终用户手动隐藏的。Aspose.Cells使用[**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh(boolean))方法解决了这个问题。此方法返回由自动筛选隐藏而不是由Excel最终用户手动隐藏的所有行的行索引。

## **在刷新自动筛选后获取所有隐藏行索引**

请参阅以下加载包含一些由Excel最终用户手动隐藏的行的[sample Excel文件](64716913.xlsx)的示例代码。该代码应用自动筛选并刷新它，使用[**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh(boolean))方法返回所有由自动筛选隐藏的行的行索引。然后在控制台上打印隐藏行的索引以及单元格名称和值。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.java" >}}

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
