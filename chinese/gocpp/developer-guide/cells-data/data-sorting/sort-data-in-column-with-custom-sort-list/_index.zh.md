---
title: 用Golang via C++在列中用自定义排序列表对数据进行排序
linktitle: 在包含自定义排序列表的列中排序数据
type: docs
weight: 290
url: /zh/go-cpp/sort-data-in-column-with-custom-sort-list/
description: 学习如何使用Aspose.Cells for C++ API，将列中的数据根据自定义列表排序。
keywords: 使用自定义排序列表对列中的数据进行排序，使用自定义列表对数据进行排序。
---

## **可能的使用场景**

你可以使用自定义列表对列中的数据进行排序。这可以通过 [**DataSorter::AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/) 方法完成。然而，此方法仅在自定义列表中的项目没有逗号时有效。如果项目中有逗号，比如 "USA,US"、"中国,CN" 等，则必须使用 [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/) 方法。这里，最后一个参数不是字符串，而是字符串数组。

## **使用自定义排序列表对列中的数据进行排序**

以下示例代码说明了如何使用 [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/) 方法通过自定义排序列表对数据进行排序。请查看此代码所用的 [示例Excel文件](50528327.xlsx) 和由其生成的 [输出Excel文件](50528328.xlsx)。下图显示了代码执行后对样本Excel文件的效果。

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SortDataInColumnWithCustomSortList.go" >}}
