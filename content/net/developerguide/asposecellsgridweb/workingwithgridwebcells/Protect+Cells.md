+++
title = "Protect Cells" 
description = "" 
weight = 16714 
+++

Aspose.Cells for .NET : Protect Cells  

# Aspose.Cells for .NET : Protect Cells


This topic describes a few techniques for protecting cells. Using these techniques allows developers to restrict users from editing all or a selected range of cells in a worksheet.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Protecting Cells](#ProtectCells-ProtectingCells)
    *   1.1 [Making All Cells Read Only](#ProtectCells-MakingAllCellsReadOnly)
    *   1.2 [Making All Cells Editable](#ProtectCells-MakingAllCellsEditable)
    *   1.3 [Making Selected Cells Read Only](#ProtectCells-MakingSelectedCellsReadOnly)
    *   1.4 [Making Selected Cells Editable](#ProtectCells-MakingSelectedCellsEditable)
{{< /panel >}}
 

## Protecting Cells

Aspose.Cells.GridWeb provides a few different techniques for controlling the protection level on cells when the control is in [Edit mode](http://www.aspose.com/docs/display/cellsnet/Enable+Different+GridWeb+Modes#EnableDifferentGridWebModes-EditMode) (the default mode). This protects cells from being modified by end users.

### Making All Cells Read Only

To set all cells in a worksheet to read only, call the worksheet's `SetAllCellsReadonly` method.

### Making All Cells Editable

To remove protection from all cells, call the worksheet's `SetAllCellsEditable` method. This method has the opposite effect to the `SetAllCellsReadonly` method.

### Making Selected Cells Read Only

To protect only a range of cells:

1.  First make all cells editable by calling the `SetAllCellsEditable` method.
2.  Specify the range of cells that to protect by calling the worksheet's `SetReadonlyRange` method. This method takes the number of rows and columns to specify the range of cells.

### Making Selected Cells Editable

To un-protect a range of cells:

1.  Make all cells read only by calling the `SetAllCellsReadonly` method.
2.  Specify the range of cells that to be editable by calling the worksheet's `SetEditableRange` method. This method takes the number of rows and columns to specify the range of cells.

