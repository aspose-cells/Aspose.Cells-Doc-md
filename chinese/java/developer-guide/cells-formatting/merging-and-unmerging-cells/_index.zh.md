---
title: 合并和取消合并 Cells
type: docs
weight: 140
url: /zh/java/merging-and-unmerging-cells/
---
{{% alert color="primary" %}}

您并不总是希望每行或每列中的单元格数量相同。例如，您可能希望将一个标题放在一个跨多列的单元格中。或者，如果创建发票，您可能需要更少的总计列。要从两个或多个单元格生成一个单元格，请合并它们。 Microsoft Excel 允许用户选择单元格并合并它们以按照他们想要的方式构建电子表格。

**在 Microsoft Excel 中合并然后拆分格式化为左侧单元格的单元格范围的结果** 

![待办事项：图像_替代_文本](merging-and-unmerging-cells_1.png)

Aspose.Cells 支持这个功能，也可以合并工作表中的单元格。您也可以取消合并或拆分合并的单元格。合并单元格的单元格引用是对最初选定区域中左上角单元格的引用。

请注意，合并单元格时，只会保留左上角单元格中的数据。如果该范围内的其他单元格中有数据，则该数据将被删除。

同样，格式设置基于引用单元格，因此当您合并单元格时，范围中左上角单元格的格式设置将应用于合并的单元格。拆分单元格时，新单元格会保留其原始格式设置。

{{% /alert %}}

## **在工作表中合并 Cells。**

### **使用 Microsoft Excel**

以下步骤描述了如何使用 Microsoft Excel 合并工作表中的单元格。

1. 将所需数据复制到范围内最左上角的单元格中。
1. 选择要合并的单元格。
1. 要合并行或列中的单元格并将单元格内容居中，请单击**合并和居中**上的图标**格式化**工具栏。

### **使用 Aspose.Cells**

这[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)类有一些对任务有用的方法。例如，方法[**合并（）**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)) 将单元格合并为指定单元格范围内的单个单元格。

执行下面的代码后会生成以下输出。

**单元格 (C6:E7) 已合并** 

![待办事项：图像_替代_文本](merging-and-unmerging-cells_2.png)

#### **代码示例**

以下示例显示如何合并工作表中的单元格 (C6:E7)。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}

## **取消合并（拆分）合并 Cells**

### **使用 Microsoft Excel**

以下步骤描述了如何使用 Microsoft Excel 拆分合并的单元格。

1. 选择合并的单元格。
当单元格合并后，**合并和居中**被选中的**格式化**工具栏。
1. 点击**合并和居中**在**格式化**工具栏。

#### **使用 Aspose.Cells**

这[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)类有一个名为[**取消合并()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unMerge(int,%20int,%20int,%20int)) 将细胞分裂成它们的原始状态。该方法使用合并的单元格区域中的单元格引用取消合并单元格。

#### **代码示例**

以下示例显示如何拆分合并的单元格 (C6)。该示例使用在上一个示例中创建的文件并拆分合并的单元格。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UnMergingCellsInWorksheet-UnMergingCellsInWorksheet.java" >}}

## **相关文章**

- [查找和拆分合并的单元格](/cells/zh/java/detect-merged-cells-in-a-worksheet/).
- [使用 Range.merge() 和 Range.unMerge() 方法合并和拆分单元格区域](/cells/zh/java/merge-or-unmerge-range-of-cells/).

