---
title: Accesso a GridRow in un foglio di lavoro
type: docs
weight: 10
url: /it/net/aspose-cells-griddesktop/access-row-in-a-worksheet/
keywords: GridDesktop, GridRow, ottieni riga
description: Questo articolo introduce come ottenere l oggetto riga (GridRow) nel foglio di lavoro in GridDesktop.
---
### Iterare sulle righe
**Buone Pratiche**:
se vogliamo accedere a tutte le righe nel foglio di lavoro una per una, possiamo utilizzare **iteratori** per attraversare le righe esistenti. questo **risparmierà memoria**.
~~~C#
   Worksheet sheet = gridDesktop1.GetActiveWorksheet();
// Accesso a una riga usando gli iteratori
   GridCells cells = sheet.Cells;
   foreach (GridRow row in cells.Rows)
  {
      Console.WriteLine(row.Index+" "+row.Height);
   }
~~~
confronta il codice sottostante , questo creerà tutti gli oggetti riga indipendentemente che sia nullo, quindi causerà problemi di memoria, quindi per favore **non** usare questo modo
~~~C#
 Worksheet sheet = gridDesktop1.GetActiveWorksheet();
 GridCells cells = sheet.Cells;
 for(int r=0;r< sheet.RowsCount;r++)
 {
     GridRow row=cells.Rows[r];
     Console.WriteLine(row.Index+" "+row.Height);
 }
~~~
tuttavia è possibile utilizzare il metodo CheckRow, per verificare se la riga è vuota
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
