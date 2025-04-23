---
title: 在排序数据时指定排序警告
type: docs
weight: 100
url: /zh/java/specifying-sort-warning-while-sorting-data/
---

## **可能的使用场景**
请考虑这个文本数据，例如 {11, 111, 22}。这个文本数据以这种方式排序是因为按照文本，111在22之前。但是，如果您想将这些数据按照数字而不是文本排序，则会变成 {11, 22, 111}，因为从数字上来看，111在22之后。Aspose.Cells提供了[DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber)属性来处理这个问题。请将此属性设置为**true**，您的文本数据将被视为数字数据排序。以下截图显示了当类似于数字数据的文本数据被排序时，Microsoft Excel显示的排序警告。

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)
## **示例代码**
以下示例代码说明了如前述所述使用[DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber)属性。请查看其[示例Excel文件](43352077.xlsx)和[输出Excel文件](43352078.xlsx)以获得更多帮助。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SpecifyingSortWarningWhileSortingData.java" >}}
{{< app/cells/assistant language="java" >}}
