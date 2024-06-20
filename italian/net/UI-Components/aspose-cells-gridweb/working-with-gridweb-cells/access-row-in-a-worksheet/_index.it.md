---
title: Accesso a GridRow in un foglio di lavoro
type: docs
weight: 10
url: /it/net/aspose-cells-gridweb/access-row-in-a-worksheet/
keywords: GridWeb, GridRow, ottenere riga
description: Questo articolo introduce come ottenere l oggetto riga (GridRow) nel foglio di lavoro in GridWeb.
---
### Iterare sulle righe
**Buone Pratiche**:
se vogliamo accedere a tutte le righe nel foglio di lavoro una per una, possiamo utilizzare **iteratori** per attraversare le righe esistenti. questo **risparmierà memoria**.
~~~C#

// Accesso a una riga usando gli iteratori
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   foreach (GridRow row in cells.Rows)
  {
      Console.WriteLine(row.Index+" "+row.Height);
   }
~~~
confronta il codice sottostante , questo creerà tutti gli oggetti riga indipendentemente che sia nullo, quindi causerà problemi di memoria, quindi per favore **non** usare questo modo
~~~C#
 GridCells cells = GridWeb1.ActiveSheet.Cells;
 for(int r=0;r<=cells.MaxRow;r++)
 {
     GridRow row=cells.Rows[r];
     Console.WriteLine(row.Index+" "+row.Height);
 }
~~~
tuttavia è possibile utilizzare il metodo CheckRow, per verificare se la riga è vuota
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
