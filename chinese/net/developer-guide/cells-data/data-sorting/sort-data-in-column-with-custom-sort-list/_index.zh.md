---
title: 在包含自定义排序列表的列中排序数据
type: docs
weight: 290
url: /zh/net/sort-data-in-column-with-custom-sort-list/
description: 使用Aspose.Cells for .NET API学习如何使用自定义列表按列对数据进行排序。
keywords: 使用自定义排序列表对列中的数据进行排序，使用自定义列表对数据进行排序。
---

## **可能的使用场景**

您可以使用[**DataSorter.AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2)方法对列中的数据使用自定义列表进行排序。然而，该方法仅在自定义列表中的项目不包含逗号时才有效。如果它们包含逗号，如"美国,US"，"中国,CN"等，则必须使用[**DataSorter.AddKey Method(Int32, SortOrder, String[])](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3)方法。在这里，最后一个参数不是String，而是字符串数组。

## **使用自定义排序列表对列中的数据进行排序**

以下示例代码解释了如何使用[**DataSorter.AddKey Method(Int32, SortOrder, String[])](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3)方法对数据使用自定义排序列表进行排序。请参阅此代码中使用的[示例Excel文件](50528327.xlsx)和其生成的[输出Excel文件](50528328.xlsx)。以下截图展示了代码对示例Excel文件执行后的效果。

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}
{{< app/cells/assistant language="csharp" >}}
