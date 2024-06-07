---
title: 对具有自定义排序列表的列进行排序数据
type: docs
weight: 290
url: /zh/net/sort-data-in-column-with-custom-sort-list/
description: 学习如何使用Aspose.Cells for .NET API通过自定义列表对列中的数据进行排序。
keywords: 对具有自定义排序列表的列进行排序数据，使用自定义列表对数据进行排序。
---

## **可能的使用场景**

您可以使用[**DataSorter.AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2)方法对列中的数据使用自定义列表进行排序。但是，如果自定义列表中的项目内部包含逗号，如"USA,US"，"China,CN"等，则必须使用[**DataSorter.AddKey方法(Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) 方法。在这里，最后一个参数不是String，而是字符串数组。

## **对具有自定义排序列表的列进行排序数据**

以下示例代码解释了如何使用[**DataSorter.AddKey方法(Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) 方法在自定义排序列表中对数据进行排序。请查看在此代码中使用的[示例Excel文件](50528327.xlsx)以及生成的[输出的Excel文件](50528328.xlsx)。以下屏幕截图显示了在执行示例Excel文件上的代码后效果。

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}
