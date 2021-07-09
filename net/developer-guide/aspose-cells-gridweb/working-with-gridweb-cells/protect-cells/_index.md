---
title: Protect Cells
type: docs
weight: 50
url: /net/protect-cells/
---

{{% alert color="primary" %}} 

This topic describes a few techniques for protecting cells. Using these techniques allows developers to restrict users from editing all or a selected range of cells in a worksheet.

{{% /alert %}} 
## **Protecting Cells**
Aspose.Cells.GridWeb provides a few different techniques for controlling the protection level on cells when the control is in [Edit mode](http://www.aspose.com/docs/display/cellsnet/Enable+Different+GridWeb+Modes#EnableDifferentGridWebModes-EditMode) (the default mode). This protects cells from being modified by end users.
### **Making All Cells Read Only**
To set all cells in a worksheet to read only, call the worksheet's SetAllCellsReadonly method.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsReadOnly.cs" >}}
### **Making All Cells Editable**
To remove protection from all cells, call the worksheet's SetAllCellsEditable method. This method has the opposite effect to the SetAllCellsReadonly method.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsEditable.cs" >}}
### **Making Selected Cells Read Only**
To protect only a range of cells:

1. First make all cells editable by calling the SetAllCellsEditable method.
1. Specify the range of cells that to protect by calling the worksheet's SetReadonlyRange method. This method takes the number of rows and columns to specify the range of cells.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsReadOnly.cs" >}}
### **Making Selected Cells Editable**
To un-protect a range of cells:

1. Make all cells read only by calling the SetAllCellsReadonly method.
1. Specify the range of cells that to be editable by calling the worksheet's SetEditableRange method. This method takes the number of rows and columns to specify the range of cells.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsEditable.cs" >}}
