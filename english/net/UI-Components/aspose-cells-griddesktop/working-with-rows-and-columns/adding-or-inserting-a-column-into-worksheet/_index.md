---
title: Adding or Inserting a Column into Worksheet
type: docs
weight: 10
url: /net/aspose-cells-griddesktop/add-or-insert-a-column-into-worksheet/
keywords: GridDesktop,insert,add,column,insert column,insert row
description: This article introduces how to insert or add column in GridDesktop.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

In this topic, we will describe the basic feature of adding and inserting columns to the worksheets at runtime using the API of Aspose.Cells.GridDesktop. The basic difference between addition and insertion is that, in addition, the column is added at the end of the columns collection of the worksheet, whereas in insertion, a column can be added to any specified position in the worksheet.

{{% /alert %}} 
## **Adding a Column to Worksheet**
To add a new column to the worksheet, please follow the steps below:

- Add Aspose.Cells.GridDesktop control to your **Form**
- Access any desired **Worksheet**
- Add **Column** to the **Worksheet**



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertColumn-AddColumn.cs" >}}
## **Inserting a Column into Worksheet**
To insert a new column into a worksheet at a specified position, please follow the steps below:

- Add Aspose.Cells.GridDesktop control to your **Form**
- Access any desired **Worksheet**
- Insert **Column** into [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) (at a specific position by specifying the index of the column where to insert it)

{{< highlight java >}}

 // Accessing the first worksheet of the Grid

Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting column to the worksheet at the first position.

sheet.Cells.InsertColumn(0);

{{< /highlight >}}
