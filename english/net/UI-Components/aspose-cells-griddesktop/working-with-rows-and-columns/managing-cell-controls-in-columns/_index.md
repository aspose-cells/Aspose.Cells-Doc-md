---
title: Managing Cell Controls in Columns
type: docs
weight: 100
url: /net/aspose-cells-griddesktop/manage-cell-controls-in-columns/
keywords: GridDesktop,controls,control
description: This article introduces how to set control in column GridDesktop.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This topic discusses some important concepts about managing cell controls in columns using the Aspose.Cells.GridDesktop API. We will explain how developers can access, modify, and remove cell controls from the columns of their worksheets. Let's have a look.

{{% /alert %}} 
## **Accessing Cell Controls**
To access and modify an existing cell control in the column, developers can use the **CellControl** property of an **Aspose.Cells.GridDesktop.Data.GridColumn**. Once a cell control is accessed, developers can modify its properties at runtime. For instance, in the example given below, we access an existing **CheckBox** cell control from a specific **Aspose.Cells.GridDesktop.Data.GridColumn** and modify its **Checked** property.

**IMPORTANT:** The **CellControl** property provides a cell control in the form of a **CellControl** object. So, if you need to access a specific type of cell control, say **CheckBox**, then you will have to type‑cast the **CellControl** object to the **CheckBox** class.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-AccessCheckbox.cs" >}}
## **Removing Cell Controls**
To remove an existing cell control, developers can simply access the desired worksheet and then **Remove** the cell control from the specific column by using the **RemoveCellControl** method of **Aspose.Cells.GridDesktop.Data.GridColumn**.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-RemoveCheckbox.cs" >}}

{{% alert color="primary" %}} 

Each column in the **Columns** collection of the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) is represented by an instance of the **Aspose.Cells.GridDesktop.Data.GridColumn** class.

{{% /alert %}}
