---
title: Zugriff auf Arbeitsblattzelle
type: docs
weight: 10
url: /de/net/aspose-cells-gridweb/access-worksheet-cell/
keywords: GridWeb,cell,GridCell
description: Dieser Artikel zeigt, wie man die Zelle (GridCell) in GridWeb erhält.
---

{{% alert color="primary" %}} 

In diesem Artikel werden Zellen behandelt und die grundlegendste Funktion von Aspose.Cells.GridWeb betrachtet: der Zugriff auf Zellen.

{{% /alert %}} 
## **Zugriff auf Zellen in einem Arbeitsblatt**
Jedes Arbeitsblatt enthält eine Eigenschaft mit dem Namen Cells, die tatsächlich eine Sammlung von GridCell-Objekten darstellt, wobei ein GridCell-Objekt eine Zelle in Aspose.Cells.GridWeb darstellt. Es ist möglich, auf jede Zelle mithilfe von Aspose.Cells.GridWeb zuzugreifen. Es gibt zwei bevorzugte Methoden, die jeweils unten erläutert werden.


### **Verwendung des Zellnamens**
Alle Zellen haben einen eindeutigen Namen. Zum Beispiel A1, A2, B1, B2 usw. Aspose.Cells.GridWeb ermöglicht Entwicklern, auf jede gewünschte Zelle zuzugreifen, indem sie den Zellnamen (als Index) an die Zellsammlung des GridWorksheet übergeben.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByName.cs" >}}


**Bemerkung**

Der Zugriff auf GridCell über cells[cellName] kann mehr Speicher verbrauchen. Es erstellt immer ein neues Zell (GridCell)-Objekt, unabhängig davon, ob die Zelle null ist.


### **Verwendung von Zeilen- und Spaltenindizes**


Eine Zelle kann auch anhand ihrer Position in Bezug auf Zeilen- und Spaltenindizes identifiziert werden. Übergeben Sie einfach die Zeilen- und Spaltenindizes einer Zelle an die Zellsammlung des GridWorksheet. Dieser Ansatz ist schneller als der obige.

**Beste Praktiken**:

Wenn wir den Zellwert oder Zellstil abrufen möchten und die Aktualisierungsoperation nicht ausführen möchten, können wir die **CheckCell**-Methode verwenden, die null zurückgibt, wenn die Zelle nicht existiert. Dies spart **Speicher**.
~~~C#
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   GridCell cell = cells.CheckCell(1, 1);
   if(cell!=null)
   {
    Console.WriteLine(cell.ToString());
   }
~~~


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByRowColumnIndex.cs" >}}



**Beste Praktiken**:
### Iterieren über die Zellen
Wenn wir alle Zellen im Arbeitsblatt nacheinander abrufen möchten, können wir **Iterator** verwenden, um die vorhandenen Zellen zu durchlaufen. Dadurch wird **Arbeitsspeicher gespart**.
~~~C#
   GridCells cells = GridWeb1.ActiveSheet.Cells;
   foreach (GridCell c in cells)
  {
      Console.WriteLine(c.ToString());
   }
~~~
Vergleichen Sie den untenstehenden Code, der **schlecht** ist. Dieser erstellt alle Zellenobjekte, unabhängig davon, ob sie null sind, und führt daher zu Speicherproblemen. Bitte verwenden Sie **nicht** diesen Weg.
~~~C#
 GridCells cells = GridWeb1.ActiveSheet.Cells;
 for(int r=0;r< cells.MaxRow;r++)
 {
     for(int c=0;c< cells.MaxColumn; c++)
     {
         Console.WriteLine(cells[r,c].ToString());
     }
 }
~~~
