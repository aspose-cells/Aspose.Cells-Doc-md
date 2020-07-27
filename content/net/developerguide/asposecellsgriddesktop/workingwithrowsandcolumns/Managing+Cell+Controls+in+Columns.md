+++
title = "Managing Cell Controls in Columns" 
description = "" 
weight = 16633 
+++

Aspose.Cells for .NET : Managing Cell Controls in Columns  

# Aspose.Cells for .NET : Managing Cell Controls in Columns


This topic discusses some important concepts about managing cell controls in columns using Aspose.Cells.GridDesktop API. We will explain that how can developer access, modify and remove cell controls from the columns of their worksheets. Let's have a look into it.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Accessing Cell Controls](#ManagingCellControlsinColumns-AccessingCellControls)
*   2 [Removing Cell Controls](#ManagingCellControlsinColumns-RemovingCellControls)
{{< /panel >}}
 

 

## Accessing Cell Controls

To access and modify an existing cell control in the column, developers can use the CellControl property of a **Aspose.Cells.GridDesktop.Data.GridColumn**. Once a cell control is accessed, developers can modify its properties at runtime. For an instance, in the example given below, we have accessed an existing **CheckBox** cell control from a specific **Aspose.Cells.GridDesktop.Data.GridColumn** and modified its Checked property.

**IMPORTANT:** CellControl property provides a cell control in the form of **CellControl** object. So, if you need to access a specific type of cell control, say **CheckBox** then you will have to typecast the **CellControl** object to **CheckBox** class.

## Removing Cell Controls

To remove an existing cell control, developers can simply access a desired worksheet and then **Remove** the cell control from the specific column by using the **RemoveCellControl** method of **Aspose.Cells.GridDesktop.Data.GridColumn**.

Each column in the **Columns** collection of the **Worksheet** is represented by an instance of **Aspose.Cells.GridDesktop.Data.GridColumn** class.

