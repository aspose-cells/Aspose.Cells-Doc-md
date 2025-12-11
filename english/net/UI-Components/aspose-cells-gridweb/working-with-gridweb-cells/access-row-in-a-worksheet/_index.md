---
title: Access GridRow in a Worksheet
type: docs
weight: 10
url: /net/aspose-cells-gridweb/access-row-in-a-worksheet/
keywords: GridWeb,GridRow,get row
description: This article introduces how to get row object (GridRow) in the worksheet in GridWeb.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
### Iterate over the rows
**Best Practices**:
If we want to access all the rows in the worksheet one by one, we can use **iterators** to traverse the existing rows. This will **save memory**.
```csharp
   
// Accessing a row using iterators
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   foreach (GridRow row in cells.Rows)
  {
      Console.WriteLine(row.Index+" "+row.Height);
   }
```
Compare the code below; this will create all the row objects regardless of whether they are null, thus causing memory issues, so please **do not** use this approach.
```csharp
 GridCells cells = GridWeb1.ActiveSheet.Cells;
 for(int r=0;r<=cells.MaxRow;r++)
 {
     GridRow row=cells.Rows[r];
     Console.WriteLine(row.Index+" "+row.Height);
 }
```
However, you can use the `CheckRow` method to check if a row is empty.
```csharp
 GridCells cells = GridWeb1.ActiveSheet.Cells;
 for(int r=0;r<=cells.MaxRow;r++)
 {
     GridRow row=cells.CheckRow(r);
     if(row==null){
       Console.WriteLine("the row is empty:"+r);
     }else{
       Console.WriteLine(row.Index+" "+row.Height);
     }
 }
```
