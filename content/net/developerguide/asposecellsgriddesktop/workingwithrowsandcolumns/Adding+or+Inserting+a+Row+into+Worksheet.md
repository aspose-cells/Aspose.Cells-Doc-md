+++
title = "Adding or Inserting a Row into Worksheet" 
description = "" 
weight = 16626 
+++

Aspose.Cells for .NET : Adding or Inserting a Row into Worksheet  

# Aspose.Cells for .NET : Adding or Inserting a Row into Worksheet


Similar to one of our previous topics, this topic describes the feature of adding and inserting rows to the worksheets at runtime using the API of Aspose.Cells.GridDesktop. The basic difference between addition and insertion is that in addition, a row is added at the end of the rows collection of the worksheet where as in insertion, a row can be added to any specified position in the worksheet.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Adding a Row to Worksheet](#AddingorInsertingaRowintoWorksheet-AddingaRowtoWorksheet)
*   2 [Inserting a Row into Worksheet](#AddingorInsertingaRowintoWorksheet-InsertingaRowintoWorksheet)
{{< /panel >}}
 

 

## Adding a Row to Worksheet

To add a new row to the worksheet, please follow the steps below:

*   Add Aspose.Cells.GridDesktop control to your **Form**
*   Access any desired **Worksheet**
*   Add **Row** to the **Worksheet**

## Inserting a Row into Worksheet

To insert a new row into worksheet at a specified position, please follow the steps below:

*   Add Aspose.Cells.GridDesktop control to your **Form**
*   Access any desired **Worksheet**
*   Insert **Row** into **Worksheet** (at a specific position by specifying the index of the row where to insert it)

{{< code lang="cs" >}}
// Accessing first worksheet of the Grid
Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];

// Inserting row to the worksheet to the first position.
sheet.Cells.InsertRow(0);
{{< /code >}}

