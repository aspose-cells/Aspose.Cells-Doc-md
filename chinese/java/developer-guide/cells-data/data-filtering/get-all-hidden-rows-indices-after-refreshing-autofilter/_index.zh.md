---
title: 刷新AutoFilter后获取所有隐藏行索引
type: docs
weight: 240
url: /zh/java/get-all-hidden-rows-indices-after-refreshing-autofilter/
---

## **可能的使用场景**

当您在工作表单元格上应用自动筛选时，有些行会自动隐藏。但可能情况是，一些行已经被Excel最终用户手动隐藏，它们并不是自动筛选隐藏的。因此，难以知道哪些行是自动筛选隐藏的，哪些是由Excel最终用户手动隐藏的。Aspose.Cells使用int[] [**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh(boolean))方法来解决这个问题。这个方法返回所有被自动筛选隐藏而不是由Excel最终用户手动隐藏的行的行索引。

## **刷新AutoFilter后获取所有隐藏行索引**

请参阅以下示例代码，该代码加载了包含一些由Excel最终用户手动隐藏的行的 [样本Excel文件](64716913.xlsx)。代码应用了自动筛选功能并使用int[] [**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh(boolean))方法来刷新它，该方法返回所有被自动筛选隐藏的行的行索引。然后在控制台上打印了隐藏行的索引以及单元格的名称和值。

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
