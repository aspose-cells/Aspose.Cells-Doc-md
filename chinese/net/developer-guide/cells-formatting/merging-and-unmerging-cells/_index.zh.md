---
title: 合并和取消合并 Cells
type: docs
weight: 190
url: /zh/net/merging-and-unmerging-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells 支持这个功能，也可以合并工作表中的单元格。您也可以取消合并或拆分合并的单元格。合并单元格的单元格引用是原始选定区域中左上角单元格的引用。

{{% /alert %}} 
## **介绍**
您并不总是希望每行或每列中的单元格数量相同。例如，您可能希望将一个标题放在一个跨多列的单元格中。或者，如果创建发票，您可能需要更少的总计列。要从两个或多个单元格生成一个单元格，请合并它们。 Microsoft Excel 允许用户选择文件并合并它们以按照他们想要的方式构建电子表格。

{{% alert color="primary" %}} 

请注意，合并单元格时，仅保留左上角单元格中的数据。如果该范围内的其他单元格中有数据，则删除该数据。
同样，格式设置基于引用单元格，因此当您合并单元格时，范围内左上角单元格的格式设置将应用于合并的单元格。拆分单元格时，新单元格会保留其原始格式设置。

{{% /alert %}} 
## **在工作表中合并 Cells**
### **在 Microsoft Excel 中合并 Cells**
以下步骤描述了如何使用 MS Excel 合并工作表中的单元格。

1. 将所需数据复制到范围内最左上角的单元格中。
1. 选择要合并的单元格。
1. 要合并行或列中的单元格并将单元格内容居中，请单击**合并和居中**上的图标**格式化**工具栏。
### **将 Cells 与 Aspose.Cells 合并**
Aspose.Cells.Cells 类有一些对任务有用的方法。例如，方法 Merge() 将单元格合并为指定范围内的单个单元格。

以下示例显示如何合并工作表中的单元格 (C6:E7)。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}
## **取消合并（拆分）合并 Cells**
### **使用 Microsoft Excel**
以下步骤描述了如何使用 Microsoft Excel 拆分合并的单元格。

1. 选择合并的单元格。
当单元格合并后，**合并和居中**被选中的**格式化**工具栏。
1. 点击**合并和居中**在**格式化**工具栏。
### **使用 Aspose.Cells**
类 Aspose.Cells.Cells 有一个名为 UnMerge() 的方法，它将单元格拆分为它们的原始状态。该方法使用合并的单元格区域中的单元格引用取消合并单元格。

以下示例显示如何拆分合并的单元格 (C6)。该示例使用在上一个示例中创建的文件并拆分合并的单元格。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-UnMergingtheMergedCells-1.cs" >}}


## **推进主题**
- [在工作表中检测合并的 Cells](/cells/zh/net/detect-merged-cells-in-a-worksheet/)
