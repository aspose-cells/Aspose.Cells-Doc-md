---
title: Greifen Sie auf das Arbeitsblatt Cells zu
type: docs
weight: 10
url: /de/net/access-worksheet-cells/
---
{{% alert color="primary" %}} 

In diesem Thema werden Zellen behandelt, wobei die grundlegendste Funktion von Aspose.Cells.GridWeb betrachtet wird: der Zugriff auf Zellen.

{{% /alert %}} 
## **Zugriff auf Cells in einem Arbeitsblatt**
Jedes Arbeitsblatt enthält eine Eigenschaft mit dem Namen Cells, die eigentlich eine Sammlung von GridCell-Objekten ist, wobei ein GridCell-Objekt eine Zelle in Aspose.Cells.GridWeb darstellt. Mit Aspose.Cells.GridWeb kann auf jede Zelle zugegriffen werden. Es gibt zwei bevorzugte Verfahren, von denen jedes unten diskutiert wird.


### **Verwendung des Namens Cell**
Alle Zellen haben einen eindeutigen Namen. Zum Beispiel A1, A2, B1, B2 usw. Aspose.Cells.GridWeb ermöglicht Entwicklern den Zugriff auf jede gewünschte Zelle, indem sie den Zellennamen verwenden. Übergeben Sie einfach den Zellennamen (als Index) an die Sammlung Cells des GridWorksheet.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByName.cs" >}}


### **Verwenden von Zeilen- und Spaltenindizes**
Eine Zelle kann auch anhand ihrer Position in Bezug auf Zeilen- und Spaltenindizes erkannt werden. Übergeben Sie einfach die Zeilen- und Spaltenindizes einer Zelle an die Sammlung Cells des GridWorksheet. Dieser Ansatz ist schneller als der obige.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByRowColumnIndex.cs" >}}
