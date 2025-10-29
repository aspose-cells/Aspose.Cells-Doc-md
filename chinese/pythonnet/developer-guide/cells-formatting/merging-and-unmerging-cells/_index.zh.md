---
title: 合并和分割单元格
description: Aspose.Cells 是一个用于处理电子表格文件的 Python 库，支持合并与拆分单元格。本文将介绍如何使用 Aspose.Cells for Python via .NET 合并与拆分单元格，以及如何自定义合并单元格样式。
keywords: Aspose.Cells for Python via .NET，NET 库，电子表格，合并单元格，取消合并单元格，样式设置，自定义样式
type: docs
weight: 190
url: /zh/python-net/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells for Python via .NET 支持此功能，还可以合并工作表中的单元格。你也可以取消合并，或者拆分已合并的单元格。合并单元格的单元格引用是指原始选择范围中左上角单元格的引用。

{{% /alert %}} 
## **介绍**
并非总是希望每行或每列中都有相同数量的单元格。例如，您可能希望在一个跨越多个列的单元格中放置标题。或者，如果创建发票，则可能希望总计列中的列数较少。将两个或多个单元格合并成一个单元格，以实现此目的。Microsoft Excel允许用户选择文件并将其合并以按照自己的方式构造电子表格。

{{% alert color="primary" %}} 

请注意，当单元格合并时，只有范围中左上角单元格中的数据被保留。如果范围中的其他单元格中有数据，则此数据将被删除。
同样，格式基于参考单元格，因此当合并单元格时，范围中左上角单元格的格式设置将应用于合并单元格。当单元格拆分时，新单元格将保留其原始格式设置。

{{% /alert %}} 
## **在工作表中合并单元格**
### **在Microsoft Excel中合并单元格**
以下步骤描述如何在MS Excel中合并工作表中的单元格。

1. 将要复制的数据复制到范围内左上角的单元格中。
1. 选择要合并的单元格。
1. 要合并行或列中的单元格并将单元格内容居中，点击**合并和居中**图标上的**格式**工具栏。

### **使用 Aspose.Cells for Python via .NET 进行单元格合并**
Aspose.Cells.Cells类具有一些用于此任务的有用方法。例如，方法Merge()将单元格合并到指定范围内的单个单元格中。

以下示例显示了如何在工作表中合并单元格（C6:E7）。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-MergingCellsInWorksheet.-1.py" >}}

## **取消合并（拆分）合并的单元格**
### **使用Microsoft Excel**
以下是使用Microsoft Excel拆分合并单元格的步骤。

1. 选择已合并的单元格。当单元格被合并时，在“格式”工具栏上会选中**合并和居中**。
1. 在**格式**工具栏上点击**合并和居中**。

### **使用Aspose.Cells for Python via .NET**
Aspose.Cells.Cells类具有一个名为UnMerge()的方法，该方法将单元格拆分为其原始状态。该方法使用合并单元格范围中的单元格引用进行拆分。

以下示例显示了如何拆分合并的单元格（C6）。该示例使用上一个示例中创建的文件，并拆分了合并的单元格。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UnMergingtheMergedCells-1.py" >}}


## **高级主题**
- [在工作表中检测合并的单元格](/cells/zh/python-net/detect-merged-cells-in-a-worksheet/)

{{< app/cells/assistant language="python-net" >}}
