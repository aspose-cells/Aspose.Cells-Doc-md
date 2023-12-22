---
title: 使用自定义排序列表对列中的数据进行排序
type: docs
weight: 290
url: /zh/net/sort-data-in-column-with-custom-sort-list/
description: 了解如何使用自定义列表对列中的数据进行排序 Aspose.Cells for .NET API。
keywords: Sort Data in Column with Custom Sort List, Sort data by custom list.
---
##  **可能的使用场景**

您可以使用自定义列表对列中的数据进行排序。这可以使用以下方法完成[**DataSorter.AddKey(int key, SortOrder 顺序, String customList)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2)方法。但是，仅当自定义列表中的项目内部不包含逗号时，此方法才有效。如果它们包含“USA,US”、“China,CN”等逗号，则必须使用 [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference. aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) 方法。这里，最后一个参数不是字符串而是字符串数组。

##  **使用自定义排序列表对列中的数据进行排序**

以下示例代码说明了如何使用 [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey /methods/3) 使用自定义排序列表对数据进行排序的方法。请参阅[Excel 文件示例](50528327.xlsx)在此代码中使用和[输出Excel文件](50528328.xlsx)由它产生的。以下屏幕截图显示了示例 Excel 文件上的代码执行后的效果。

![待办事项：图像_替代_文本](sort-data-in-column-with-custom-sort-list_1.png)

##  **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}
