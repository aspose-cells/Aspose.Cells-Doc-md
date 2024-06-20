---
title: Tillgång till GridRow i ett Arbetsblad
type: docs
weight: 10
url: /sv/net/aspose-cells-gridweb/access-row-in-a-worksheet/
keywords: GridWeb, GridRow, få rad
description: Denna artikel introducerar hur man kan få radobjekt (GridRow) i arbetsbladet i GridWeb.
---
### Iterera över raderna
**Bästa praxis**:
Om vi vill komma åt alla rader i arbetsbladet en efter en kan vi använda **iterativt** för att navigera genom befintliga rader. Detta kommer att **spara minne**.
~~~C#

// Att komma åt en rad med hjälp av iterativt
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   foreach (GridRow row in cells.Rows)
  {
      Console.WriteLine(row.Index+" "+row.Height);
   }
~~~
jämför nedanstående kod, detta kommer att skapa alla radobjekt oavsett om de är null, vilket kommer att orsaka minnesproblem, så **använd inte** på detta sätt
~~~C#
 GridCells cells = GridWeb1.ActiveSheet.Cells;
 for(int r=0;r<=cells.MaxRow;r++)
 {
     GridRow row=cells.Rows[r];
     Console.WriteLine(row.Index+" "+row.Height);
 }
~~~
du kan dock använda CheckRow-metoden för att kontrollera om raden är tom
~~~C#
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
~~~
