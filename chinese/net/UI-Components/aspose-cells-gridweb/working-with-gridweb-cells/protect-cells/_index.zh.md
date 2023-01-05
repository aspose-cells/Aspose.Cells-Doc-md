---
title: 保护 Cells
type: docs
weight: 50
url: /zh/net/protect-cells/
---
{{% alert color="primary" %}} 

本主题介绍了一些用于保护单元格的技术。使用这些技术允许开发人员限制用户编辑工作表中的所有或选定范围的单元格。

{{% /alert %}} 
## **保护 Cells**
 Aspose.Cells.GridWeb 提供了几种不同的技术来控制单元格的保护级别，当控件处于[编辑模式](/cells/zh/net/enable-different-gridweb-modes/#edit-mode)（默认模式）。这可以保护单元不被最终用户修改。
### **使所有 Cells 只读**
要将工作表中的所有单元格设置为只读，请调用工作表的 SetAllCellsReadonly 方法。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsReadOnly.cs" >}}
### **使所有 Cells 可编辑**
要取消对所有单元格的保护，请调用工作表的 SetAllCellsEditable 方法。此方法与 SetAllCellsReadonly 方法具有相反的效果。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsEditable.cs" >}}
### **使选定的 Cells 只读**
仅保护一定范围的单元格：

1. 首先通过调用 SetAllCellsEditable 方法使所有单元格都可编辑。
1. 通过调用工作表的 SetReadonlyRange 方法指定要保护的单元格范围。此方法采用行数和列数来指定单元格范围。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsReadOnly.cs" >}}
### **使选定的 Cells 可编辑**
要取消对一系列单元格的保护：

1. 通过调用 SetAllCellsReadonly 方法使所有单元格只读。
1. 通过调用工作表的 SetEditableRange 方法指定可编辑的单元格范围。此方法采用行数和列数来指定单元格范围。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsEditable.cs" >}}
