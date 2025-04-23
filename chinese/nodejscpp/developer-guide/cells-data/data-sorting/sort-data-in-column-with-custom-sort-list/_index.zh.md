---
title: 在包含自定义排序列表的列中排序数据
type: docs
weight: 290
url: /zh/nodejs-cpp/sort-data-in-column-with-custom-sort-list/
description: 学习如何使用Aspose.Cells for Node.js via C++ API按自定义列表排序列中的数据。
keywords: 使用自定义排序列表对列中的数据进行排序，使用自定义列表对数据进行排序。
---

## **可能的使用场景**

你可以使用自定义列表对列中的数据进行排序。这可以通过[**DataSorter.addKey**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-string-)方法实现。但此方法仅适用于自定义列表中的项不含逗号的情况。如果项中含有逗号，比如"USA,US"、"China,CN"等，你必须使用[**DataSorter.addKey(number, SortOrder, string[])**)](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-stringarray-)方法。此方法的最后一个参数不是字符串，而是字符串数组。

## **使用自定义排序列表对列中的数据进行排序**

以下示例代码说明如何使用[**DataSorter.addKey(number, SortOrder, string[])**)](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-stringarray-)方法，通过自定义排序列表对数据进行排序。请查看此代码中使用的[示例Excel文件](50528327.xlsx)以及由此生成的[输出Excel文件](50528328.xlsx)。执行后，截图显示了此代码对示例Excel文件的效果。

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SortDataInColumnWithCustomSortList.js" >}}

