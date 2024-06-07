---
title: 在排序数据时指定排序警告
type: docs
weight: 140
url: /zh/net/specifying-sort-warning-while-sorting-data/
description: 学习如何使用Aspose.Cells for .NET API在排序数据时指定排序警告。
keywords: 在排序数据时添加排序警告，排序数据时设置排序警告，排序数据时选择排序警告。
---

## **可能的使用场景**

请考虑这些文本数据，即{11, 111, 22}。这些文本数据被排序，因为在文本方面，111在22之前。但是，如果你想将这些数据排序为数字而不是文本，那么它将变成{11, 22, 111}，因为在数字上，111在22之后。 Aspose.Cells提供{0}属性来解决这个问题。请将此属性设置为**true**，您的文本数据将被排序为数字数据。以下截图显示了当像数值数据一样排序看起来像数字数据的文本数据时，Microsoft Excel显示的排序警告。

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **示例代码**

下面的示例代码演示了如前面所述使用[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber)属性。请检查其[示例Excel文件](43352075.xlsx)和[输出Excel文件](43352076.xlsx)以获得更多帮助。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SpecifyingSortWarningWhileSortingData.cs" >}}
