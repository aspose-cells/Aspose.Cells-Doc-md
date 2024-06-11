---
title: 在排序数据时指定排序警告
type: docs
weight: 140
url: /zh/python-net/specifying-sort-warning-while-sorting-data/
description: 通过Aspose.Cells for Python通过.NET API学习如何在对数据进行排序时指定排序警告。
keywords: Python Excel库，Python对数据进行排序时添加排序警告，Python在对数据进行排序时设置排序警告，Python在对数据进行排序时选择排序警告。
---

## **可能的使用场景**

请考虑以下文本数据即{11, 111, 22}。 这些文本数据被排序，因为从文本的角度来看，111在22之前。 但是，如果您希望将此数据与数字一样而不是文本进行排序，则结果将为{11, 22, 111}，因为在数字上，111在22之后。 Aspose.Cells for Python通过.NET提供了{0}属性来解决此问题。 请将此属性设置为**true**，您的文本数据将被排序为数值数据。 以下屏幕截图显示了在文本数据（看起来像数值数据）排序时，Microsoft Excel显示的排序警告。

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **示例代码**

下面的示例代码演示了如前面所述使用[**DataSorter.sort_as_number**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort_as_number/)属性。请检查其[示例Excel文件](43352075.xlsx)和[输出Excel文件](43352076.xlsx)以获得更多帮助。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SpecifyingSortWarningWhileSortingData.py" >}}
