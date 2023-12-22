---
title: 合并与取消合并 Cells
description: Aspose.Cells 是一个用于处理电子表格文件的 .NET 库，它支持合并和取消合并单元格。本文将介绍如何使用Aspose.Cells库合并和取消合并单元格，以及如何自定义合并单元格样式。
keywords: Aspose.Cells, NET library, spreadsheet, merge cells, unmerge cells, style settings, custom styles
type: docs
weight: 190
url: /zh/net/merging-and-unmerging-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells支持此功能，还可以合并工作表中的单元格。您也可以取消合并或拆分合并的单元格。合并单元格的单元格引用是原始选定区域中左上角单元格的引用。

{{% /alert %}} 
##  **介绍**
您并不总是希望每行或每列都有相同数量的单元格。例如，您可能希望将标题放入跨多列的单元格中。或者，如果创建发票，您可能需要更少的总计列。要将两个或多个单元格合并为一个单元格，请将它们合并。 Microsoft Excel 允许用户选择文件并合并它们以按照自己想要的方式构建电子表格。

{{% alert color="primary" %}} 

请注意，合并单元格时，仅保留左上角单元格中的数据。如果该范围内的其他单元格中有数据，则该数据将被删除。
同样，格式设置基于引用单元格，因此当您合并单元格时，区域中左上角单元格的格式设置将应用于合并的单元格。拆分单元格时，新单元格将保留其原始格式设置。

{{% /alert %}} 
##  **将 Cells 合并到工作表中**
###  **在 Microsoft Excel 中合并 Cells**
以下步骤描述如何使用 MS Excel 合并工作表中的单元格。

1. 将所需数据复制到范围内最左上角的单元格中。
1. 选择要合并的单元格。
1. 要合并行或列中的单元格并使单元格内容居中，请单击**合并并居中**上的图标**格式化**工具栏。
###  **合并 Cells 与 Aspose.Cells**
Aspose.Cells.Cells 类有一些有用的方法来完成该任务。例如，方法 Merge() 将指定范围内的单元格合并为单个单元格。

以下示例显示如何合并工作表中的单元格 (C6:E7)。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}
##  **取消合并（拆分）合并 Cells**
###  **使用 Microsoft Excel**
以下步骤介绍如何使用 Microsoft Excel 拆分合并的单元格。

1. 选择合并的单元格。
当细胞合并后，**合并并居中**被选择在**格式化**工具栏。
1. 点击**合并并居中**于**格式化**工具栏。
###  **使用Aspose.Cells**
类 Aspose.Cells.Cells 有一个名为 UnMerge() 的方法，该方法将单元格拆分为原始状态。该方法使用合并单元格区域中的单元格引用取消单元格的合并。

以下示例显示如何拆分合并的单元格 (C6)。该示例使用上一示例中创建的文件并拆分合并的单元格。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-UnMergingtheMergedCells-1.cs" >}}


##  **高级主题**
- [检测工作表中的合并 Cells](/cells/zh/net/detect-merged-cells-in-a-worksheet/)
