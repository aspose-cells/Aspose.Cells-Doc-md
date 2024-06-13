---
title: 合并和分割单元格
type: docs
weight: 140
url: /zh/java/merging-and-unmerging-cells/
---

{{% alert color="primary" %}}

您并非总是希望每行或每列中具有相同数量的单元格。例如，您可能希望将一个标题放在跨越多列的单元格中。或者，如果创建发票，您可能希望总计少量列。要将两个或多个单元格合并为一个单元格，请将它们合并。Microsoft Excel允许用户选择单元格并将它们合并以按照他们想要的方式构建电子表格。

合并一系列单元格，然后将其拆分为 Microsoft Excel 中左侧单元格的格式化结果。 

![todo:image_alt_text](merging-and-unmerging-cells_1.png)

Aspose.Cells支持此功能，还可以在工作表中合并单元格。您也可以取消合并或拆分已合并的单元格。合并单元格的单元格引用是最初选定范围中左上角单元格的引用。

请注意，当单元格合并时，仅保留左上角单元格中的数据。如果范围中的其他单元格中存在数据，则该数据将被删除。

同样，格式也基于引用单元格，因此当您合并单元格时，将应用范围中左上角单元格的格式设置到合并单元格上。当单元格拆分时，新单元格将保留其原始格式设置。

{{% /alert %}}

## **在工作表中合并单元格。**

### **使用Microsoft Excel**

以下是使用Microsoft Excel在工作表中合并单元格的步骤。

1. 将要复制的数据复制到范围内左上角的单元格中。
1. 选择要合并的单元格。
1. 要合并行或列中的单元格并将单元格内容居中，点击**合并和居中**图标上的**格式**工具栏。

### **使用Aspose.Cells**

[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)类具有一些有用的方法。例如，方法[**merge()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int))将在指定的单元格范围内将单元格合并为一个单元格。

执行以下代码后生成以下输出。

**已合并单元格（C6:E7）** 

![todo:image_alt_text](merging-and-unmerging-cells_2.png)

#### **代码示例**

以下示例显示了如何在工作表中合并单元格（C6:E7）。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}

## **取消合并（拆分）合并的单元格**

### **使用Microsoft Excel**

以下是使用Microsoft Excel拆分合并单元格的步骤。

1. 选择已合并的单元格。 
   当单元格已合并时，在**格式**工具栏上选择**合并和居中**。
1. 在**格式**工具栏上点击**合并和居中**。

#### **使用Aspose.Cells**

[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)类有一个名为[**unMerge()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unMerge(int,%20int,%20int,%20int))的方法，用于将单元格拆分为其原始状态。该方法使用合并单元格范围中的单元格引用来取消合并单元格。

#### **代码示例**

以下示例显示了如何拆分合并的单元格（C6）。该示例使用上一个示例中创建的文件，并拆分了合并的单元格。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UnMergingCellsInWorksheet-UnMergingCellsInWorksheet.java" >}}

## **相关文章**

- [查找并拆分合并单元格](/cells/zh/java/detect-merged-cells-in-a-worksheet/)
- [使用Range.merge()和Range.unMerge()方法合并和拆分单元格范围](/cells/zh/java/merge-or-unmerge-range-of-cells/)

