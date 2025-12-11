---  
title: Adding or Inserting a Row into Worksheet  
type: docs  
weight: 30  
url: /net/aspose-cells-griddesktop/add-or-insert-a-row-into-worksheet/  
keywords: GridDesktop,insert,add,row,insert row,add row  
description: This article introduces how to add or insert row in GridDesktop.  
ai_search_scope: cells_net  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  

Similar to one of our previous topics, this topic describes the feature of adding and inserting rows to the worksheets at runtime using the API of Aspose.Cells.GridDesktop. The basic difference between addition and insertion is that, in addition, a row is added at the end of the rows collection of the worksheet, whereas in insertion, a row can be added to any specified position in the worksheet.  

{{% /alert %}}  

## **Adding a Row to Worksheet**  
To add a new row to the worksheet, please follow the steps below:

- Add Aspose.Cells.GridDesktop control to your **Form**  
- Access any desired **Worksheet**  
- Add **Row** to the **Worksheet**  

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-AddInsertRow-AddRow.cs" >}}  

## **Inserting a Row into Worksheet**  
To insert a new row into a worksheet at a specified position, please follow the steps below:

- Add Aspose.Cells.GridDesktop control to your **Form**  
- Access any desired **Worksheet**  
- Insert **Row** into **Worksheet** (at a specific position by specifying the index of the row where to insert it)  

{{< highlight java >}}  

 // Accessing the first worksheet of the Grid  
 Aspose.Cells.GridDesktop.Worksheet sheet = gridDesktop1.Worksheets[0];  

 // Inserting a row into the worksheet at the first position  
 sheet.Cells.InsertRow(0);  

{{< /highlight >}}
