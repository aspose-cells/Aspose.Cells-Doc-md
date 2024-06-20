---
title: Tillgång till GridRow i ett Arbetsblad
type: docs
weight: 10
url: /sv/net/aspose-cells-griddesktop/access-row-in-a-worksheet/
keywords: GridDesktop, GridRow, få rad
description: Den här artikeln introducerar hur man får radobjektet (GridRow) i kalkylbladet i GridDesktop.
---
### Iterera över raderna
**Bästa praxis**:
Om vi vill komma åt alla rader i arbetsbladet en efter en kan vi använda **iterativt** för att navigera genom befintliga rader. Detta kommer att **spara minne**.
~~~C#
   Worksheet sheet = gridDesktop1.GetActiveWorksheet();
// Att komma åt en rad med hjälp av iterativt
   GridCells cells = sheet.Cells;
   foreach (GridRow row in cells.Rows)
  {
      Console.WriteLine(row.Index+" "+row.Height);
   }
~~~
jämför nedanstående kod, detta kommer att skapa alla radobjekt oavsett om de är null, vilket kommer att orsaka minnesproblem, så **använd inte** på detta sätt
~~~C#
 Worksheet sheet = gridDesktop1.GetActiveWorksheet();
 GridCells cells = sheet.Cells;
 for(int r=0;r< sheet.RowsCount;r++)
 {
     GridRow row=cells.Rows[r];
     Console.WriteLine(row.Index+" "+row.Height);
 }
~~~
du kan dock använda CheckRow-metoden för att kontrollera om raden är tom
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
