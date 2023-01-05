---
title: 使用自定义排序列表对列中的数据进行排序
type: docs
weight: 210
url: /zh/java/sort-data-in-column-with-custom-sort-list/
---
## **可能的使用场景**

您可以使用自定义列表对列中的数据进行排序。这可以使用[DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)） 方法。但是，只有当自定义列表中的项目内部没有逗号时，此方法才有效。如果他们有像“USA, US”, “China, CN”等逗号，那么你必须使用[DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)） 方法。在这里，最后一个参数不是字符串而是字符串数组。

## **使用自定义排序列表对列中的数据进行排序**

以下示例代码解释了如何使用 DataSorter.AddKey(int key, SortOrder order, String[]customList) 方法使用自定义排序列表对数据进行排序。请参阅[示例 Excel 文件](50528359.xlsx)在此代码中使用和[输出Excel文件](50528358.xlsx)由它产生。下面的屏幕截图显示了示例 Excel 文件中的代码在执行时的效果。

![待办事项：图片_替代_文本](sort-data-in-column-with-custom-sort-list_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SortDataInColumnWithCustomSortList.java" >}}
