---
title: 保护单元格
type: docs
weight: 50
url: /zh/net/aspose-cells-gridweb/protect-cells/
keywords: GridWeb,保护,只读,可编辑
description: 本文介绍了如何在GridWeb中保护单元格。
---

{{% alert color="primary" %}} 

本主题介绍了保护单元格的几种技术。使用这些技术可以使开发人员限制用户编辑工作表中的所有或选定范围的单元格。

{{% /alert %}} 
## **保护单元格**
Aspose.Cells.GridWeb在“编辑模式”（默认模式）下为控件上的单元格控制保护级别提供了几种不同的技术。这样可以保护终端用户不对单元格进行修改。
### **将所有单元格设置为只读**
要将工作表中的所有单元格设置为只读，请调用工作表的SetAllCellsReadonly方法。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsReadOnly.cs" >}}
### **将所有单元格设置为可编辑**
要从所有单元格中移除保护，请调用工作表的SetAllCellsEditable方法。该方法与SetAllCellsReadonly方法的效果相反。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsEditable.cs" >}}
### **将选定的单元格设置为只读**
只保护一定范围的单元格：

1. 首先调用SetAllCellsEditable方法，使所有单元格可编辑。
2. 调用工作表的SetReadonlyRange方法指定要保护的单元格范围。该方法接受行数和列数来指定单元格范围。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsReadOnly.cs" >}}
### **将选定的单元格设置为可编辑**
取消保护一定范围的单元格：

1. 调用SetAllCellsReadonly方法将所有单元格设置为只读。
2. 调用工作表的SetEditableRange方法指定要可编辑的单元格范围。该方法接受行数和列数来指定单元格范围。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsEditable.cs" >}}
