---
title: 合并和拆分单元格
type: docs
weight: 140
url: /zh/java/merging-and-unmerging-cells/
---

{{% alert color="primary" %}}

您并不总是希望每行或每列中的单元格数相同。例如，您可能希望在跨越多个列的单元格中放入一个标题。或者，如果创建发票，您可能希望总计少一些列。要将两个或更多个单元格合并为一个单元格，请将它们合并。Microsoft Excel 允许用户选择单元格并将它们合并，以便按照他们想要的方式构造电子表格。

**在 Microsoft Excel 中左侧单元格格式化的范围合并然后拆分的结果** 

![todo:image_alt_text](merging-and-unmerging-cells_1.png)

Aspose.Cells支持此功能，并且还可以在工作表中合并单元格。您还可以取消合并或拆分合并的单元格。合并单元格的单元格引用是最初选择的范围中左上角单元格的引用。

请注意，当单元格合并时，只保留左上角单元格中的数据。如果其他单元格中有数据，则该数据将被删除。

同样，格式取决于引用单元格，因此当您合并单元格时，会将范围中左上角单元格的格式设置应用于合并后的单元格。当单元格拆分时，新单元格会保留其原始格式设置。

{{% /alert %}}

## **合并工作表中的单元格。**

### **使用Microsoft Excel**

以下步骤描述了如何使用 Microsoft Excel 合并工作表中的单元格。

1. 将要复制的数据复制到范围内最左上角的单元格中。
1. 选择要合并的单元格。
1. 要合并一行或一列的单元格并使单元格内容居中，单击**合并和居中**工具栏上的**合并和居中**图标。

### **使用Aspose.Cells**

[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) 类有一些用于此任务的实用方法。例如，方法 [**merge()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)）将单元格合并为指定单元格范围内的单个单元格。

执行下面的代码后生成以下输出。

**已合并单元格 (C6:E7)** 

![todo:image_alt_text](merging-and-unmerging-cells_2.png)

#### **代码示例**

以下示例显示了如何在工作表中合并单元格(C6:E7)。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}

## **取消合并（拆分）合并的单元格**

### **使用Microsoft Excel**

以下步骤描述了如何使用Microsoft Excel拆分合并的单元格。

1. 选择合并的单元格。 
   当单元格已合并时，**合并和居中**在**格式**工具栏上被选中。
1. 单击**格式**工具栏上的**合并和居中**。

#### **使用Aspose.Cells**

[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) 类有一个名为 [**unMerge()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unMerge(int,%20int,%20int,%20int)）的方法，将单元格拆分为其原始状态。该方法使用合并单元格范围中的单元格引用来取消合并单元格。

#### **代码示例**

以下示例显示了如何拆分合并的单元格（C6）。该示例使用前一个示例中创建的文件，并拆分了合并的单元格。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UnMergingCellsInWorksheet-UnMergingCellsInWorksheet.java" >}}

## **相关文章**

- [查找和拆分合并单元格](/cells/zh/java/detect-merged-cells-in-a-worksheet/)。
- [使用 Range.merge() 和 Range.unMerge() 方法合并和拆分单元格范围](/cells/zh/java/merge-or-unmerge-range-of-cells/)。

