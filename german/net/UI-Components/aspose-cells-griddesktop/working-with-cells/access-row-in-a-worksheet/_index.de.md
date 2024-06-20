---
title: Zugriff auf GridRow in einem Arbeitsblatt
type: docs
weight: 10
url: /de/net/aspose-cells-griddesktop/access-row-in-a-worksheet/
keywords: GridDesktop, GridRow, Zeile abrufen
description: Dieser Artikel stellt vor, wie man das Zeilenobjekt (GridRow) im Arbeitsblatt in GridDesktop erhält.
---
### Iterieren über die Zeilen
**Beste Praktiken**:
Wenn wir nacheinander auf alle Zeilen im Arbeitsblatt zugreifen möchten, können wir **Iteratoren** verwenden, um die vorhandenen Zeilen zu durchlaufen. Dies spart **Speicher**.
~~~C#
   Worksheet sheet = gridDesktop1.GetActiveWorksheet();
// Zugriff auf eine Zeile mithilfe von Iteratoren
   GridCells cells = sheet.Cells;
   foreach (GridRow row in cells.Rows)
  {
      Console.WriteLine(row.Index+" "+row.Height);
   }
~~~
Vergleichen Sie den untenstehenden Code  ,dieser wird alle Zeilenobjekte erstellen, unabhängig davon, ob sie null sind, was zu Speicherproblemen führen wird. Bitte verwenden Sie daher **nicht** auf diese Weise
~~~C#
 Worksheet sheet = gridDesktop1.GetActiveWorksheet();
 GridCells cells = sheet.Cells;
 for(int r=0;r< sheet.RowsCount;r++)
 {
     GridRow row=cells.Rows[r];
     Console.WriteLine(row.Index+" "+row.Height);
 }
~~~
Sie können jedoch die CheckRow-Methode verwenden, um zu überprüfen, ob die Zeile leer ist
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
