---
title : "Managing Cell Controls in Worksheets" 
description : "" 
weight : 16617 
toc : false
type: docs
url: /net/developerguide/griddesktop/worksheet/managing+cell+controls+in+worksheets/
---

# Aspose.Cells for .NET : Managing Cell Controls in Worksheets


This topic discusses some important concepts about managing cell controls using the API of Aspose.Cells.GridDesktop. We will explain that how can developer access, modify and remove cell controls from their worksheets. Let's have a look into it.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Accessing Cell Controls](#accessing-cell-controls)
*   2 [Removing Cell Controls](#removing-cell-controls)
{{< /panel >}}
 

 

## Accessing Cell Controls

To access and modify an existing cell control in the worksheet, developers can access a specific cell control from the **Controls** collection of the **Worksheet** by specifying the cell (using cell name or its location in terms of row and column numbers) in which the cell control is being displayed. Once a cell control is accessed, developers can modify its properties at runtime. For an instance, in the example given below, we have accessed an existing **CheckBox** cell control from the **Worksheet** and modified its Checked property.

**IMPORTANT:** **Controls** collection contains all types of cell controls in the form of **CellControl** objects. So, if you need to access a specific type of cell control, say **CheckBox** then you will have to typecast the **CellControl** object to **CheckBox** class.

## Removing Cell Controls

To remove an existing cell control, developers can simply access a desired worksheet and then **Remove** the cell control from the **Controls** collection of the **Worksheet** by specifying the cell (using its name or row & column number) containing cell control.

