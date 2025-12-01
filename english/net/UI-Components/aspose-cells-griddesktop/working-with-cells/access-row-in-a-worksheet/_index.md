---
title: Access GridRow in a Worksheet
type: docs
weight: 10
url: /net/aspose-cells-griddesktop/access-row-in-a-worksheet/
keywords: GridDesktop,GridRow,get row
description: This article introduces how to get row object (GridRow) in the Worksheet in GridDesktop.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
### Iterate over the rows
**Best Practices**:
if we want to access all the rows in the worksheet one by one, we can use **iterators** to  traverse the existed rows. this will **save memory**.
~~~C#
   Worksheet sheet = gridDesktop1.GetActiveWorksheet();
// Accessing a row using iterators
   GridCells cells = sheet.Cells;
   foreach (GridRow row in cells.Rows)
  {
      Console.WriteLine(row.Index+" "+row.Height);
   }
~~~
compare the below code  ,this will create all the row object no matter whether it is null,thus will cause memory issues,so please **do not** use this way
~~~C#
 Worksheet sheet = gridDesktop1.GetActiveWorksheet();
 GridCells cells = sheet.Cells;
 for(int r=0;r< sheet.RowsCount;r++)
 {
     GridRow row=cells.Rows[r];
     Console.WriteLine(row.Index+" "+row.Height);
 }
~~~
however you can use CheckRow method,to check if the row is empty
~~~C#
 Worksheet sheet = gridDesktop1.GetActiveWorksheet();
 GridCells cells = sheet.Cells;
 for(int r=0;r< sheet.RowsCount;r++)
 {
     GridRow row=cells.CheckRow(r);
     if(row==null){
       Console.WriteLine("the row is empty:"+r);
     }else{
       Console.WriteLine(row.Index+" "+row.Height);
     }
 }
~~~
