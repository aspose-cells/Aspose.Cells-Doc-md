---
title: Managing Cell Controls in Worksheets
type: docs
weight: 130
url: /net/aspose-cells-griddesktop/manage-cell-controls-in-worksheets/
keywords: GridDesktop,cell control,control,controls
description: This article introduces how to work with cell controls in GridDesktop.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This topic discusses some important concepts about managing cell controls using the API of Aspose.Cells.GridDesktop. We will explain how developers can access, modify, and remove cell controls from their worksheets. Let's have a look at it.

{{% /alert %}} 
## **Accessing Cell Controls**
To access and modify an existing cell control in the worksheet, developers can access a specific cell control from the **Controls** collection of the **Worksheet** by specifying the cell (using its name or its location in terms of row and column numbers) where the cell control is displayed. Once a cell control is accessed, developers can modify its properties at runtime. For instance, in the example given below, we have accessed an existing **CheckBox** cell control from the **Worksheet** and modified its Checked property.

**IMPORTANT:** **Controls** collection contains all types of cell controls in the form of **CellControl** objects. So, if you need to access a specific type of cell control, say **CheckBox**, then you will have to typecast the **CellControl** object to the **CheckBox** class.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-AccessCheckbox.cs" >}}
## **Removing Cell Controls**
To remove an existing cell control, developers can simply access a desired worksheet and then **remove** the cell control from the **Controls** collection of the **Worksheet** by specifying the cell (using its name or row & column number) containing the cell control.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-RemoveCheckbox.cs" >}}
