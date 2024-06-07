---
title: 对具有自定义排序列表的列进行排序数据
type: docs
weight: 210
url: /zh/java/sort-data-in-column-with-custom-sort-list/
---

## **可能的使用场景**

您可以使用自定义列表对列中的数据进行排序。这可以通过 [DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)) 方法来实现。但是，此方法只适用于自定义列表中的项目不包含逗号。如果它们包含逗号，比如"USA, US"，"China, CN"等，则必须使用 [DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)) 方法。这里，最后一个参数不是String，而是字符串数组。

## **对具有自定义排序列表的列进行排序数据**

以下示例代码说明了如何使用DataSorter.AddKey(int key, SortOrder order, String[] customList)方法对数据进行自定义排序。请查看此代码中使用的 [样本Excel文件](50528359.xlsx) 和它所生成的 [输出Excel文件](50528358.xlsx)。以下截图显示了代码在执行中对样本Excel文件的效果。

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SortDataInColumnWithCustomSortList.java" >}}
