---
title: 在排序数据时指定排序警告
type: docs
weight: 140
url: /zh/net/specifying-sort-warning-while-sorting-data/
description: 使用Aspose.Cells for .NET API学习如何在排序数据时指定排序警告。
keywords: 在对数据进行排序时添加排序警告，设置排序警告，在对数据进行排序时选择排序警告。
---

## **可能的使用场景**

请考虑这段文本数据，即{11, 111, 22}。此文本数据被排序，因为在文本方面，111排在22前面。但是，如果您想将这些数据不作为文本而作为数字进行排序，那么它将变为{11, 22, 111}，因为从数字角度看，111在22之后。Aspose.Cells提供了{0}属性来解决这个问题。请将此属性设置为**true**，您的文本数据将作为数值数据进行排序。以下截图展示了当类似数值数据的文本数据排序时，Microsoft Excel显示的排序警告。

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **示例代码**

下面的示例代码说明了如何使用前面解释的[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber)属性。有关更多帮助，请查看其[示例Excel文件](43352075.xlsx)和[输出Excel文件](43352076.xlsx)。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SpecifyingSortWarningWhileSortingData.cs" >}}
