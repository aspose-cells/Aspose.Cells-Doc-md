---
title: 在包含自定义排序列表的列中排序数据
type: docs
weight: 210
url: /zh/java/sort-data-in-column-with-custom-sort-list/
---

## **可能的使用场景**

你可以使用[DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey-int-int-java.lang.String-)方法，在列中使用自定义列表进行排序。不过，该方法只适用于自定义列表中的项目没有逗号的情况；如果有，比如"美国，美国"，"中国，中国"，必须使用同样的方法，但最后一个参数类型为字符串数组而非字符串。

## **使用自定义排序列表对列中的数据进行排序**

以下示例代码解释了如何使用 DataSorter.AddKey(int key, SortOrder order, String[] customList) 方法使用自定义排序列表对数据进行排序。请参阅在此代码中使用的 [sample Excel file](50528359.xlsx) 和由此生成的 [output Excel file](50528358.xlsx)。下面的屏幕截图显示了在执行代码时对样本Excel文件产生的效果。

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SortDataInColumnWithCustomSortList.java" >}}
{{< app/cells/assistant language="java" >}}
