---
title: 在排序数据时指定排序警告
type: docs
weight: 140
url: /zh/python-net/specifying-sort-warning-while-sorting-data/
description: 学习如何使用Aspose.Cells for Python via .NET API指定排序数据时的排序警告。
keywords: Python Excel库，Python在排序数据时添加排序警告，Python在排序数据时设置排序警告，Python在排序数据时选择排序警告。
---

## **可能的使用场景**

请考虑以下文本数据，即{11, 111, 22}。这些文本数据是有序的，因为从文本角度看，111出现在22之前。但如果您想将此数据不作为文本，而是作为数字进行排序，那么它将变为{11, 22, 111}，因为从数字上看，111出现在22之后。Aspose.Cells for Python via .NET提供了{0}属性来解决这个问题。请将此属性设置为true，您的文本数据将被排序为数字数据。以下屏幕截图显示了在将类似数字数据的文本数据排序时Microsoft Excel显示的排序警告。

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **示例代码**

下面的示例代码说明了如何使用前面解释的[**DataSorter.sort_as_number**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort_as_number/)属性。有关更多帮助，请查看其[示例Excel文件](43352075.xlsx)和[输出Excel文件](43352076.xlsx)。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SpecifyingSortWarningWhileSortingData.py" >}}
{{< app/cells/assistant language="python-net" >}}
