---
title: Kopieren Sie GridWeb-Zeilen und -Spalten
type: docs
weight: 80
url: /de/net/copy-gridweb-rows-and-columns/
---
{{% alert color="primary" %}} 

 Aspose.Cells. Die GridWeb-Komponente bietet die Möglichkeit, Zeilen und Spalten zu kopieren, während die GridCells-Klasse verwendet wird. Dieser Artikel demonstriert die Verwendung von APIs, die von Aspose.Cells.GridWeb bereitgestellt werden, um Zeilen und Spalten auf der GridWeb-Schnittstelle zu kopieren.

Die Methoden GridCells.CopyRow, GridCells.CopyColumn, GridCells.CopyRows und GridCells.CopyColumns kopieren den Inhalt, das Styling und die Formeln aus der Quellzeile und -spalte zum Ziel.

{{% /alert %}} 
## **Kopieren von Zeilen und Spalten**
 Wenn Sie mit der Komponente Aspose.Cells.GridWeb noch nicht vertraut sind, empfehlen wir Ihnen dringend, diese zu überprüfen[Einführung in Aspose.Cells.GridWeb](https://docs.aspose.com/cells/net/browsers-capabilities/) und ausführlicher Artikel auf[So fügen Sie die Komponente Aspose.Cells.GridWeb in einer WebForms-Anwendung hinzu](https://docs.aspose.com/cells/net/add-gridweb-to-web-form/).
### **Einzelne Zeile kopieren**
Um das Beispiel einfach zu halten, verwendet der Artikel eine vorhandene Tabelle mit einer Zeile und einer einfachen Formel, die alle Werte in der Zeile summiert. So wird die Tabelle in der Aspose.Cells.GridWeb-Oberfläche angezeigt, bevor die Zeile kopiert wird.

![todo: Bild_alt_Text](copy-gridweb-rows-and-columns_1.png)

Das Code-Snippet ist einfach, wie unten gezeigt. Es greift auf das GridCells-Objekt der aktiven Arbeitsblattreihenfolge zu, um eine Kopie der ersten Zeile in die nachfolgende Zeile zu erstellen.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyRow.cs" >}}


So sieht Aspose.Cells.GridWeb nach dem Kopieren von Zeilen aus.

![todo: Bild_alt_Text](copy-gridweb-rows-and-columns_2.png)
### **Einzelne Spalte kopieren**
Das folgende Beispiel verwendet eine vorhandene Tabelle mit einer Spalte und einer einfachen Formel, die alle Werte in der Spalte summiert. So wird die Tabelle in der Aspose.Cells.GridWeb-Oberfläche angezeigt, bevor die Spalte kopiert wird.

![todo: Bild_alt_Text](copy-gridweb-rows-and-columns_3.png)

Ähnlich wie im obigen Beispiel greift der folgende Codeausschnitt auf das GridCells-Objekt der aktiven Arbeitsblattreihenfolge zu, um eine Kopie der ersten Spalte in die nachfolgende Spalte zu erstellen.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyColumn.cs" >}}



So sieht Aspose.Cells.GridWeb nach dem Kopieren von Spalten aus.

![todo: Bild_alt_Text](copy-gridweb-rows-and-columns_4.png)

{{% alert color="primary" %}} 

Sie können die Methoden GridCells.CopyRow und GridCells.CopyColumn in einer Schleife verwenden, um die Quellzeile und -spalte jeweils in mehrere Zeilen und Spalten zu kopieren.

{{% /alert %}} 
### **Kopieren mehrerer Zeilen**
Es ist auch möglich, mehrere Zeilen an ein neues Ziel zu kopieren, während die GridCells.CopyRows-Methode verwendet wird, die einen zusätzlichen Parameter vom Typ Integer akzeptiert, um die Anzahl der zu kopierenden Quellzeilen anzugeben.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleRows.cs" >}}



So sieht Aspose.Cells.GridWeb vor und nach dem Kopieren von Zeilen aus.

![todo: Bild_alt_Text](copy-gridweb-rows-and-columns_5.png)

![todo: Bild_alt_Text](copy-gridweb-rows-and-columns_6.png)
### **Kopieren mehrerer Spalten**
Die GridCells-Klasse stellt auch die CopyColumns-Methode bereit, die einen zusätzlichen Parameter vom Typ Integer akzeptiert, um die Anzahl der zu kopierenden Quellspalten anzugeben.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleColumns.cs" >}}



So sieht Aspose.Cells.GridWeb vor und nach dem Kopieren von Zeilen aus.

![todo: Bild_alt_Text](copy-gridweb-rows-and-columns_7.png)

![todo: Bild_alt_Text](copy-gridweb-rows-and-columns_8.png)
