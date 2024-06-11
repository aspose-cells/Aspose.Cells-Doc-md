---
title: 保护单元格
type: docs
weight: 50
url: /zh/net/aspose-cells-gridweb/protect-cells/
keywords: GridWeb,保护,只读,可编辑
description: 本文介绍了如何在GridWeb中保护单元格。
---

{{% alert color="primary" %}} 

本主题描述了保护单元格的几种技术。使用这些技术可让开发人员限制用户对工作表中所有或选定范围的单元格进行编辑。

{{% /alert %}} 
## **保护单元格**
当控件处于[编辑模式](/cells/zh/net/aspose-cells-gridweb/enable-different-gridweb-modes/#edit-mode)（默认模式）时，Aspose.Cells.GridWeb提供了几种不同的技术来控制单元格的保护级别。这样可以防止最终用户修改单元格。
### **设置所有单元格为只读**
要将工作表中的所有单元格设置为只读，请调用工作表的SetAllCellsReadonly方法。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsReadOnly.cs" >}}
### **设置所有单元格为可编辑**
要取消所有单元格的保护，请调用工作表的SetAllCellsEditable方法。该方法与SetAllCellsReadonly方法具有相反的效果。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsEditable.cs" >}}
### **将选定的单元格设置为只读**
仅保护一系列单元格:

1. 首先通过调用SetAllCellsEditable方法使所有单元格可编辑。
1. 通过调用工作表的SetReadonlyRange方法指定需保护的单元格范围。此方法采用行数和列数来指定单元格范围。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsReadOnly.cs" >}}
### **使选定的单元格可编辑**
取消保护一系列单元格:

1. 通过调用SetAllCellsReadonly方法使所有单元格只读。
1. 通过调用工作表的SetEditableRange方法指定可编辑的单元格范围。此方法采用行数和列数来指定单元格范围。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsEditable.cs" >}}
