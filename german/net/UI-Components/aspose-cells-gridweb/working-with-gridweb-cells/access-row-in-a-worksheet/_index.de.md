---
title: Zugriff auf GridRow in einem Arbeitsblatt
type: docs
weight: 10
url: /de/net/aspose-cells-gridweb/access-row-in-a-worksheet/
keywords: GridWeb,GridRow,erhalten Zeile
description: Dieser Artikel zeigt, wie man das Zeilenobjekt (GridRow) im Arbeitsblatt in GridWeb abruft.
---
### Iterieren über die Zeilen
**Beste Praktiken**:
Wenn wir nacheinander auf alle Zeilen im Arbeitsblatt zugreifen möchten, können wir **Iteratoren** verwenden, um die vorhandenen Zeilen zu durchlaufen. Dies spart **Speicher**.
~~~C#

// Zugriff auf eine Zeile mithilfe von Iteratoren
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   foreach (GridRow row in cells.Rows)
  {
      Console.WriteLine(row.Index+" "+row.Height);
   }
~~~
Vergleichen Sie den untenstehenden Code  ,dieser wird alle Zeilenobjekte erstellen, unabhängig davon, ob sie null sind, was zu Speicherproblemen führen wird. Bitte verwenden Sie daher **nicht** auf diese Weise
~~~C#
 GridCells cells = GridWeb1.ActiveSheet.Cells;
 for(int r=0;r<=cells.MaxRow;r++)
 {
     GridRow row=cells.Rows[r];
     Console.WriteLine(row.Index+" "+row.Height);
 }
~~~
Sie können jedoch die CheckRow-Methode verwenden, um zu überprüfen, ob die Zeile leer ist
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
