---
title: 刷新自动筛选后获取所有隐藏行索引
type: docs
weight: 240
url: /zh/java/get-all-hidden-rows-indices-after-refreshing-autofilter/
---
## **可能的使用场景**

当您在工作表单元格上应用自动筛选器时，某些行会自动隐藏。但可能某些行已被 Excel 最终用户手动隐藏，并且未被自动筛选器隐藏。因此，很难知道哪些行被自动筛选器隐藏，哪些行被 Excel 最终用户手动隐藏。 Aspose.Cells 使用 int[] 处理这个问题[**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh(boolean)） 方法。此方法返回自动过滤器隐藏的所有行的行索引，而不是 Excel 最终用户手动隐藏的行索引。

## **刷新自动筛选后获取所有隐藏行索引**

请参阅以下加载的示例代码[示例 Excel 文件](64716913.xlsx)其中包含一些由 Excel 最终用户手动隐藏的行。该代码应用自动过滤器并使用 int[] 刷新它[**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh(boolean)方法返回自动筛选器隐藏的所有行的行索引。然后它在控制台上打印隐藏行的索引以及单元格名称和值。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.java" >}}

## **控制台输出**

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
