---
title: Managing Cell Controls in Columns
type: docs
weight: 100
url: /net/aspose-cells-griddesktop/manage-cell-controls-in-columns/
keywords: GridDesktop,controls,control
description: This article introduces how to set control in column GridDesktop.
---

{{% alert color="primary" %}} 

This topic discusses some important concepts about managing cell controls in columns using Aspose.Cells.GridDesktop API. We will explain that how can developer access, modify and remove cell controls from the columns of their worksheets. Let's have a look into it.

{{% /alert %}} 
## **Accessing Cell Controls**
To access and modify an existing cell control in the column, developers can use the CellControl property of a **Aspose.Cells.GridDesktop.Data.GridColumn**. Once a cell control is accessed, developers can modify its properties at runtime. For an instance, in the example given below, we have accessed an existing **CheckBox** cell control from a specific **Aspose.Cells.GridDesktop.Data.GridColumn** and modified its Checked property.

**IMPORTANT:** CellControl property provides a cell control in the form of **CellControl** object. So, if you need to access a specific type of cell control, say **CheckBox** then you will have to typecast the **CellControl** object to **CheckBox** class.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-AccessCheckbox.cs" >}}
## **Removing Cell Controls**
To remove an existing cell control, developers can simply access a desired worksheet and then **Remove** the cell control from the specific column by using the **RemoveCellControl** method of **Aspose.Cells.GridDesktop.Data.GridColumn**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-RemoveCheckbox.cs" >}}

{{% alert color="primary" %}} 

Each column in the **Columns** collection of the **Worksheet** is represented by an instance of **Aspose.Cells.GridDesktop.Data.GridColumn** class.

{{% /alert %}}
