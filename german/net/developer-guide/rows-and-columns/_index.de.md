---
title: Zeilen und Spalten formatieren
linktitle: Reihen und Spalten
type: docs
weight: 100
url: /de/net/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}}

Wenn Sie mit Tabellenkalkulationen arbeiten und Daten zu Zeilen oder Spalten hinzufügen, müssen Sie möglicherweise die Zeilenhöhe oder Spaltenbreite ändern. Manchmal bedeutet das Anwenden von Formatierungen auf Zeilen oder Spalten, dass die aktuelle Höhe oder Breite geändert werden muss, um die Daten anzuzeigen. Normalerweise passen Benutzer Zeilenhöhen und Spaltenbreiten in einer WYSIWYG-Umgebung mit Microsoft Excel an. Aber mit Aspose.Cells können Entwickler diese Operationen zur Laufzeit ausführen.

{{% /alert %}}

## **Arbeiten mit Zeilen**

### **Anpassen der Zeilenhöhe**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblattsammlung**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Auflistung, die alle Zellen im Arbeitsblatt darstellt.

 Das[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung bietet mehrere Methoden zum Verwalten von Zeilen oder Spalten in einem Arbeitsblatt. Einige davon werden weiter unten ausführlicher besprochen.

### **Festlegen der Höhe einer Zeile**

 Es ist möglich, die Höhe einer einzelnen Zeile durch Aufrufen von festzulegen[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung[**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) Methode. Das[**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight)Die Methode nimmt die folgenden Parameter wie folgt:

- **Zeilenindex**, der Index der Zeile, deren Höhe Sie ändern.
- **Zeilenhöhe**, die Zeilenhöhe, die auf die Zeile angewendet werden soll.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightOfRow-1.cs" >}}

### **Festlegen der Höhe aller Zeilen in einem Arbeitsblatt**

 Wenn Entwickler für alle Zeilen im Arbeitsblatt dieselbe Zeilenhöhe festlegen müssen, können sie dies mithilfe von tun[**Standardhöhe**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardheight) Eigentum der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Sammlung.

**Beispiel:**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightAllRows-1.cs" >}}

## **Arbeiten mit Spalten**

### **Einstellen der Breite einer Spalte**

 Legen Sie die Breite einer Spalte fest, indem Sie die aufrufen[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung[**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) Methode. Das[**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth)Die Methode nimmt die folgenden Parameter an:

- **Spaltenindex**, der Index der Spalte, deren Breite Sie ändern.
- **Spaltenbreite**, die gewünschte Spaltenbreite.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.cs" >}}

### **Spaltenbreite in Pixel einstellen**

Legen Sie die Breite einer Spalte fest, indem Sie die aufrufen[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Sammlung[**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)Methode. Das[**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)Die Methode nimmt die folgenden Parameter an:

- **Spaltenindex**, der Index der Spalte, deren Breite Sie ändern.
- **Spaltenbreite**die gewünschte Spaltenbreite in Pixel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.cs" >}}

### **Festlegen der Breite aller Spalten in einem Arbeitsblatt**

 Um dieselbe Spaltenbreite für alle Spalten im Arbeitsblatt festzulegen, verwenden Sie die[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung[**Standardbreite**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardwidth)Eigentum.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.cs" >}}

## **Themen vorantreiben**
- [Zeilen und Spalten automatisch anpassen](/cells/de/net/autofit-rows-and-columns/)
- [Konvertieren Sie Text in Spalten mit Aspose.Cells](/cells/de/net/convert-text-to-columns-using-aspose-cells/)
- [Kopieren von Zeilen und Spalten](/cells/de/net/copying-rows-and-columns/)
- [Löschen Sie leere Zeilen und Spalten in einem Arbeitsblatt](/cells/de/net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Gruppieren und Aufheben der Gruppierung von Zeilen und Spalten](/cells/de/net/grouping-and-ungrouping-rows-and-columns/)
- [Zeilen und Spalten ein- und ausblenden](/cells/de/net/hiding-and-showing-rows-and-columns/)
- [Einfügen oder Löschen von Zeilen in einem Excel-Arbeitsblatt](/cells/de/net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Einfügen und Löschen von Zeilen und Spalten einer Excel-Datei](/cells/de/net/inserting-and-deleting-rows-and-columns/)
- [Entfernen Sie doppelte Zeilen in einem Arbeitsblatt](/cells/de/net/remove-duplicate-rows-in-a-worksheet/)
- [Aktualisieren Sie Verweise in anderen Arbeitsblättern, während Sie leere Spalten und Zeilen in einem Arbeitsblatt löschen](/cells/de/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
