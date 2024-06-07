---
title: 在排序数据时指定排序警告
type: docs
weight: 100
url: /zh/java/specifying-sort-warning-while-sorting-data/
---

## **可能的使用场景**
请考虑以下文本数据即 {11, 111, 22}。这些文本数据被排序为 {11, 111, 22} ，因为在文本方面，111在22之前。但，如果你要将这些数据不按文本而按数字来排序，那么它将变成{11, 22, 111} ，因为从数字上讲，111在22之后。Aspose.Cells提供了[DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber) 属性来解决这个问题。请将该属性设置为**true**，您的文本数据将按数字数据进行排序。以下截图显示了当将类似数值数据的文本数据排序时，Microsoft Excel显示的排序警告。

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)
## **示例代码**
以下示例代码说明了如何使用[DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber) 属性，如前述所述。请查看其 [样本Excel文件](43352077.xlsx) 和 [输出Excel文件](43352078.xlsx) 以获取更多帮助。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SpecifyingSortWarningWhileSortingData.java" >}}
