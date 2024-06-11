---
title: 对具有自定义排序列表的列进行排序数据
type: docs
weight: 290
url: /zh/python-net/sort-data-in-column-with-custom-sort-list/
description: 了解如何使用Aspose.Cells for Python通过.NET API使用自定义列表对列中的数据进行排序。
keywords: Python Excel库，Python使用自定义排序列表对列中的数据进行排序，Python按自定义列表对数据进行排序。
---

## **可能的使用场景**

您可以使用自定义列表对列中的数据进行排序。这可以使用[**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list)方法完成。但是，如果自定义列表中的项目中带有逗号，如“USA，US”，“China，CN”等，则必须使用[**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list)方法。在此，最后一个参数不是字符串，而是一个字符串数组。

## **对具有自定义排序列表的列进行排序数据**

以下示例代码解释了如何使用[**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list)方法使用自定义排序列表对数据进行排序。请查看此代码中使用的[示例Excel文件](50528327.xlsx)以及由其生成的[输出Excel文件](50528328.xlsx)。以下屏幕截图显示了执行代码对样本Excel文件的影响。

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SortDataInColumnWithCustomSortList.py" >}}
