---
title: 合并和拆分单元格
description: Aspose.Cells是一个用于处理电子表格文件的.NET库，支持合并和拆分单元格。本文将介绍如何使用Aspose.Cells库合并和拆分单元格，以及如何自定义合并单元格的样式。
keywords: Aspose.Cells, .NET库, 电子表格, 合并单元格, 拆分单元格, 样式设置, 自定义样式
type: docs
weight: 190
url: /zh/net/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells支持此功能，还可以在工作表中合并单元格。您也可以取消合并或拆分合并后的单元格。合并单元格的单元格引用是原始选定范围中左上角单元格的引用。

{{% /alert %}} 
## **介绍**
您并不总是希望每行或每列中有相同数量的单元格。例如，您可能希望在跨越多列的单元格中放置一个标题。或者，如果创建发票，您可能希望总计列中的列较少。要将两个或更多个单元格合并成一个单元格，请将它们合并。Microsoft Excel允许用户选择文件并将它们合并以按照他们希望的方式构造电子表格。

{{% alert color="primary" %}} 

请注意，当单元格合并时，只有左上角单元格中的数据会被保留。如果范围中其他单元格中有数据，则该数据将被删除。
同样，格式取决于引用单元格，因此当您合并单元格时，范围中左上角单元格的格式设置将应用于合并的单元格。当单元格拆分时，新单元格将保留其原始格式设置。

{{% /alert %}} 
## **在工作表中合并单元格**
### **在Microsoft Excel中合并单元格**
以下步骤描述了如何使用MS Excel在工作表中合并单元格。

1. 将要复制的数据复制到范围内最左上角的单元格中。
1. 选择要合并的单元格。
1. 要合并一行或一列的单元格并使单元格内容居中，单击**合并和居中**工具栏上的**合并和居中**图标。
### **使用Aspose.Cells合并单元格**
Aspose.Cells.Cells类具有一些有用的方法。例如，Merge()方法将单元格合并到指定范围内的单个单元格中。

以下示例显示了如何在工作表中合并单元格(C6:E7)。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}
## **取消合并（拆分）合并的单元格**
### **使用Microsoft Excel**
以下步骤描述了如何使用Microsoft Excel拆分合并的单元格。

1. 选择合并的单元格。
   当单元格已合并时，**合并和居中**在**格式**工具栏上被选中。
1. 单击**格式**工具栏上的**合并和居中**。
### **使用Aspose.Cells**
Aspose.Cells.Cells类有一个名为UnMerge()的方法，将单元格拆分回其原始状态。该方法使用合并单元格范围中的单元格引用拆分单元格。

以下示例显示了如何拆分合并的单元格（C6）。该示例使用前一个示例中创建的文件，并拆分了合并的单元格。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-UnMergingtheMergedCells-1.cs" >}}


## **高级主题**
- [检测工作表中的合并单元格](/cells/zh/net/detect-merged-cells-in-a-worksheet/)
