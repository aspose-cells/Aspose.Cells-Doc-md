---
title: 在排序数据时指定排序警告
type: docs
weight: 140
url: /zh/nodejs-cpp/specifying-sort-warning-while-sorting-data/
description: 学习如何在排序数据时指定排序警告，使用Aspose.Cells for Node.js via C++ API。
keywords: 在对数据进行排序时添加排序警告，设置排序警告，在对数据进行排序时选择排序警告。
---

## **可能的使用场景**

请考虑此文本数据，即{11, 111, 22}。此文本数据会被排序，因为就文本而言，111排在22之前。但如果你希望以数字方式排序，而不是文本，则排序结果将是{11, 22, 111}，因为从数字角度看，111在22之后。Aspose.Cells for Node.js via C++提供了{0}属性来处理此问题。请将此属性设置为**true**，这样你的文本数据就会作为数字数据进行排序。以下截图显示了当以数字方式排序类似数字的文本数据时，Microsoft Excel提示的排序警告。

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **示例代码**

下面的示例代码说明了如何使用前面解释的[**DataSorter.setSortAsNumber**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#setSortAsNumber-boolean-)属性。有关更多帮助，请查看其[示例Excel文件](43352075.xlsx)和[输出Excel文件](43352076.xlsx)。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SpecifyingSortWarningWhileSortingData.js" >}}

