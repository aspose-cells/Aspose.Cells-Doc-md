---
title: 排序数据时指定排序警告
type: docs
weight: 140
url: /zh/net/specifying-sort-warning-while-sorting-data/
---
## **可能的使用场景**

请考虑此文本数据，即 {11, 111, 22}。此文本数据已排序，因为就文本而言，111 在 22 之前。但是，如果您不想将此数据排序为文本而是数字，那么它将变为 {11, 22, 111} 因为数字上 111 在 22 之后. Aspose.Cells 规定[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber)财产来处理这个问题。请设置此属性**真的**并且您的文本数据将被排序为数字数据。以下屏幕截图显示了 Microsoft Excel 在对看起来像数字数据的文本数据进行排序时显示的排序警告。

![待办事项：图片_替代_文本](specifying-sort-warning-while-sorting-data_1.png)

## **示例代码**

下面的示例代码说明了[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber)属性如前所述。请检查其[示例 Excel 文件](43352075.xlsx)和[输出Excel文件](43352076.xlsx)寻求更多帮助。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SpecifyingSortWarningWhileSortingData.cs" >}}
