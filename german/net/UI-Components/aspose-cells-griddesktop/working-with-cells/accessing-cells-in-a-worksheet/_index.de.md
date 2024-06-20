---
title: Zugriff auf GridCell in einem Arbeitsblatt
type: docs
weight: 10
url: /de/net/aspose-cells-griddesktop/access-cell-in-a-worksheet/
keywords: GridDesktop,GridCell,get cell
description: Dieser Artikel zeigt, wie das Zellenobjekt (GridCell) im Arbeitsblatt in GridDesktop abgerufen werden kann.
---

{{% alert color="primary" %}} 

Wir haben bisher über die Arbeit mit Arbeitsblättern, Zeilen und Spalten gesprochen, aber jetzt ist es an der Zeit, tiefer zu gehen und über Zellen zu sprechen. In diesem Thema würden wir unsere Diskussion über Zellen mit einem grundlegenden Feature zum Abrufen von Zellen beginnen.

{{% /alert %}} 
## **Zugriff auf Zelle in einem Arbeitsblatt**
Wir können über die API von Aspose.Cells.GridDesktop auf jede Zelle eines Arbeitsblatts zugreifen. Es gibt drei mögliche Wege, um auf eine Zelle zuzugreifen, wie folgt:

- **Verwendung des Zellnamens**
- **Verwendung von Zeilen- & Spaltenindizes**
- **Abrufen der fokussierten Zelle**

Lassen Sie uns alle oben genannten drei Ansätze nacheinander besprechen.
### **Verwendung des Zellnamens**
Alle Zellen in einem Arbeitsblatt haben einen eindeutigen Namen. Zum Beispiel A1, A2, B1, B2 usw. Aspose.Cells.GridDesktop ermöglicht Entwicklern, auf jede gewünschte Zelle zuzugreifen, indem sie ihren Zellnamen verwenden. Alles, was wir tun müssen, ist den Zellnamen (als Index) an die **Cells**-Sammlung des **Arbeitsblatts** zu übergeben.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByName.cs" >}}

**Bemerkung**

Der Zugriff auf GridCell über cells[cellName] kann mehr Speicher verbrauchen. Es erstellt immer ein neues Zell (GridCell)-Objekt, unabhängig davon, ob die Zelle null ist.

### **Verwendung von Zeilen- und Spaltenindizes der Zelle**

**Beste Praktiken**:

Wenn wir den Zellwert oder Zellstil abrufen möchten und die Aktualisierungsoperation nicht ausführen möchten, können wir die **CheckCell**-Methode verwenden, die null zurückgibt, wenn die Zelle nicht existiert. Dies spart **Speicher**.
~~~C#
Worksheet sheet = gridDesktop1.GetActiveWorksheet();
// Zugriff auf eine Zelle über ihre Zeilen- und Spaltenindizes
GridCell cell = sheet.Cells.CheckCell(1, 1);
   if(cell!=null)
   {
    Console.WriteLine(cell.ToString());
   }
~~~

Eine Zelle in einem Arbeitsblatt kann auch anhand ihres Standorts in Bezug auf ihre Zeilen- und Spaltenindizes erkannt werden. Alles, was wir tun müssen, ist, die Zeilen- und Spaltenindizes der Zelle an die **Cells**-Sammlung des **Arbeitsblatts** zu übergeben.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByIndices.cs" >}}

**Bemerkung**

Der Zugriff auf GridCell über cells[rowIndex, columnIndex] kann mehr Speicher verbrauchen. Es erstellt immer ein neues Zell (GridCell)-Objekt, unabhängig davon, ob die Zelle null ist.


### **Abruf der fokussierten Zelle**
Wenn Sie nicht genau wissen, auf welche Zelle zugegriffen werden soll, ermöglicht Aspose.Cells.GridDesktop auch den Zugriff auf eine Zelle, die sich derzeit im Fokus eines Benutzers befindet. Mit dieser Funktion können Sie einem Benutzer ermöglichen, eine beliebige Zelle auszuwählen und dann auf diese Zelle im Hintergrund zuzugreifen. Dies kann einfach durch Verwendung der Methode **GetFocusedCell** des **Arbeitsblatts** erreicht werden.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessFocusedCell.cs" >}}

**Beste Praktiken**:
### Iterieren über die Zellen
Wenn wir alle Zellen im Arbeitsblatt nacheinander abrufen möchten, können wir **Iterator** verwenden, um die vorhandenen Zellen zu durchlaufen. Dadurch wird **Arbeitsspeicher gespart**.
~~~C#
   Worksheet sheet = gridDesktop1.GetActiveWorksheet();

   GridCells cells = sheet.Cells;
   foreach (GridCell c in cells)
  {
      Console.WriteLine(c.ToString());
   }
~~~
Vergleichen Sie den untenstehenden Code, der **schlecht** ist. Dieser erstellt alle Zellenobjekte, unabhängig davon, ob sie null sind, und führt daher zu Speicherproblemen. Bitte verwenden Sie **nicht** diesen Weg.
~~~C#
 Worksheet sheet = gridDesktop1.GetActiveWorksheet();
 for(int r=0;r< sheet.RowsCount;r++)
 {
     for(int c=0;c< sheet.ColumnsCount; c++)
     {
         Console.WriteLine(sheet.Cells[r,c].ToString());
     }
 }
~~~

