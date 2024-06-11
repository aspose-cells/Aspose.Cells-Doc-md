---
title: 在包含自定义排序列表的列中排序数据
type: docs
weight: 290
url: /zh/python-net/sort-data-in-column-with-custom-sort-list/
description: 学习如何使用Aspose.Cells for Python via .NET API使用自定义列表对列中的数据进行排序。
keywords: Python Excel库，Python使用自定义排序列表对列中的数据进行排序，Python按自定义列表对数据进行排序。
---

## **可能的使用场景**

您可以使用自定义列表对列中的数据进行排序。可以使用[**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list)方法来实现。但是，仅当自定义列表中的项目不含有逗号时，此方法才可用。如果它们包含逗号，比如"USA,US"，"China,CN"等，那么您必须使用[**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list)方法。在这里，最后一个参数不是字符串，而是字符串数组。

## **使用自定义排序列表对列中的数据进行排序**

下面的示例代码解释了如何使用[**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list)方法根据自定义排序列表对数据进行排序。请查看此代码中使用的[示例Excel文件](50528327.xlsx)以及其生成的[输出Excel文件](50528328.xlsx)。以下屏幕截图显示了在执行此代码后对示例Excel文件的影响。

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SortDataInColumnWithCustomSortList.py" >}}
