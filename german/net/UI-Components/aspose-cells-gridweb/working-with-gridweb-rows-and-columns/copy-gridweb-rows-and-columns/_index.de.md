---
title: Kopieren von GridWeb Zeilen und Spalten
type: docs
weight: 80
url: /de/net/aspose-cells-gridweb/copy-gridweb-rows-and-columns/
keywords: GridWeb, kopieren
description: Dieser Artikel zeigt, wie Zeilen und Spalten in GridWeb kopiert werden.
---

{{% alert color="primary" %}} 

Das Aspose.Cells.GridWeb-Komponente bietet die Möglichkeit, Zeilen & Spalten zu kopieren, während die Klasse GridCells verwendet wird. Dieser Artikel demonstriert die Verwendung der von Aspose.Cells.GridWeb bereitgestellten APIs zum Kopieren von Zeilen & Spalten auf der GridWeb-Benutzeroberfläche. 

Die Methoden GridCells.CopyRow, GridCells.CopyColumn, GridCells.CopyRows & GridCells.CopyColumns kopieren den Inhalt, das Styling & die Formeln von der Quellzeile & Spalte zum Ziel.

{{% /alert %}} 
## **Kopieren von Zeilen & Spalten**
Wenn Sie noch nicht mit dem Aspose.Cells.GridWeb-Komponente vertraut sind, empfehlen wir Ihnen, den [Einführung in Aspose.Cells.GridWeb](https://docs.aspose.com/cells/net/aspose-cells-gridweb/browsers-capabilities/) und den ausführlichen Artikel zum [Hinzufügen der Aspose.Cells.GridWeb-Komponente in einer WebForms-Anwendung](https://docs.aspose.com/cells/net/aspose-cells-gridweb/add-gridweb-to-web-form/) zu lesen.
### **Kopieren einer einzelnen Zeile**
Um das Beispiel einfach zu halten, verwendet der Artikel eine vorhandene Tabelle mit einer Zeile und einer einfachen Formel, die alle Werte in der Zeile summiert. So wird die Tabelle in der Aspose.Cells.GridWeb-Oberfläche vor dem Kopieren der Zeile angezeigt.

![todo:image_alt_text](copy-gridweb-rows-and-columns_1.png)

Der den Code block ist wie folgt. Es greift auf das GridCells-Objekt des aktiven Tabellenblatts zu, um eine Kopie der ersten Zeile in die nachfolgende Zeile zu machen.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyRow.cs" >}}


So sieht die Aspose.Cells.GridWeb nach dem Kopieren der Zeile aus.

![todo:image_alt_text](copy-gridweb-rows-and-columns_2.png)
### **Einzelne Spalte kopieren**
Das folgende Beispiel verwendet eine vorhandene Tabelle mit einer Spalte und einer einfachen Formel, die alle Werte in der Spalte summiert. So wird die Tabelle in der Aspose.Cells.GridWeb-Oberfläche vor dem Kopieren der Spalte angezeigt.

![todo:image_alt_text](copy-gridweb-rows-and-columns_3.png)

Ähnlich wie im obigen Beispiel greift der folgende Code auf das GridCells-Objekt des aktiven Tabellenblatts zu, um eine Kopie der ersten Spalte in die nachfolgende Spalte zu machen.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyColumn.cs" >}}



So sieht die Aspose.Cells.GridWeb nach dem Kopieren der Spalte aus.

![todo:image_alt_text](copy-gridweb-rows-and-columns_4.png)

{{% alert color="primary" %}} 

Sie können die GridCells.CopyRow & GridCells.CopyColumn-Methoden in einer Schleife verwenden, um die Quellzeile & Spalte jeweils auf mehrere Zeilen & Spalten zu kopieren.

{{% /alert %}} 
### **Mehrere Zeilen kopieren**
Es ist auch möglich, mehrere Zeilen zu einem neuen Ziel zu kopieren, während die GridCells.CopyRows-Methode verwendet wird, die einen zusätzlichen Parameter vom Typ Integer benötigt, um die Anzahl der zu kopierenden Quellzeilen anzugeben.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleRows.cs" >}}



So sieht Aspose.Cells.GridWeb vor & nach dem Kopieren von Spalten aus.

![todo:image_alt_text](copy-gridweb-rows-and-columns_5.png)

![todo:image_alt_text](copy-gridweb-rows-and-columns_6.png)
### **Mehrere Spalten kopieren**
Die Klasse GridCells bietet auch die CopyColumns-Methode, die einen zusätzlichen Parameter vom Typ Integer benötigt, um die Anzahl der zu kopierenden Quellspalten anzugeben.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleColumns.cs" >}}



So sieht Aspose.Cells.GridWeb vor & nach dem Kopieren von Spalten aus.

![todo:image_alt_text](copy-gridweb-rows-and-columns_7.png)

![todo:image_alt_text](copy-gridweb-rows-and-columns_8.png)
