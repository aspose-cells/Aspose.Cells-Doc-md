---
title: Zeilen und Spalten formatieren
linktitle: Zeilen und Spalten
type: docs
weight: 100
url: /de/net/adjusting-row-height-and-column-width/
description: Aspose.Cells for .NET unterstützt die Änderung der Zeilenhöhe oder Spaltenbreite sowie das Anwenden von Formatierungen auf Zeilen oder Spalten.
keywords: Zeilenhöhe und Spaltenbreite einstellen, Zeilenhöhe und Spaltenbreite anpassen, die Zeilenhöhe oder Spaltenbreite ändern, Zeilen und Spalten formatieren, wie man die Zeilenhöhe und Spaltenbreite einstellt
---


{{% alert color="primary" %}}

Wenn Sie mit Tabellenkalkulationen arbeiten und Daten zu Zeilen oder Spalten hinzufügen, müssen Sie möglicherweise die Höhe von Zeilen oder die Breite von Spalten ändern. Manchmal bedeutet das Anwenden von Formatierungen auf Zeilen oder Spalten, dass die aktuelle Höhe oder Breite geändert werden muss, um die Daten anzuzeigen. Normalerweise passen Benutzer die Zeilenhöhen und Spaltenbreiten in einer WYSIWYG-Umgebung mit Microsoft Excel an. Mit Aspose.Cells können Entwickler diese Operationen jedoch zur Laufzeit ausführen.

{{% /alert %}}

## **Arbeiten mit Zeilen**

### **Wie man die Zeilenhöhe anpasst**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-Klasse enthält eine [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection), die den Zugriff auf jede Arbeitsmappe in der Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Klasse repräsentiert. Die [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Klasse bietet eine [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung, die alle Zellen in der Arbeitsmappe repräsentiert.

Die [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung bietet verschiedene Methoden zum Verwalten von Zeilen oder Spalten in einem Arbeitsblatt. Einige davon werden unten genauer erläutert.

### **Wie man die Höhe einer Zeile festlegt**

Es ist möglich, die Höhe einer einzelnen Zeile durch Aufrufen der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlungsmethode [**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) festzulegen. Die [**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight)-Methode nimmt die folgenden Parameter wie folgt entgegen:

- **Zeilenindex**, der Index der Zeile, deren Höhe geändert wird.
- **Zeilenhöhe**, die auf die Zeile anzuwendende Zeilenhöhe.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightOfRow-1.cs" >}}

### **Wie man die Höhe aller Zeilen in einem Arbeitsblatt festlegt**

Wenn Entwickler die gleiche Zeilenhöhe für alle Zeilen im Arbeitsblatt festlegen müssen, können sie dies über die [**StandardHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardheight)-Eigenschaft der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung tun.

**Beispiel:**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightAllRows-1.cs" >}}

## **Arbeiten mit Spalten**

### **Wie man die Breite einer Spalte festlegt**

Die Breite einer Spalte wird durch Aufrufen der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlungsmethode [**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) festgelegt. Die [**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth)-Methode nimmt folgende Parameter entgegen:

- **Spaltenindex**, der Index der Spalte, deren Breite geändert wird.
- **Spaltenbreite**, die gewünschte Spaltenbreite.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.cs" >}}

### **Wie man die Spaltenbreite in Pixeln festlegt**

Legen Sie die Breite einer Spalte fest, indem Sie die Methode [**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel) der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung aufrufen. Die Methode [**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel) nimmt die folgenden Parameter an:

- **Spaltenindex**, der Index der Spalte, deren Breite geändert wird.
- **Spaltenbreite**, die gewünschte Spaltenbreite in Pixel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.cs" >}}

### **Wie man die Breite aller Spalten in einem Arbeitsblatt festlegt**

Um dieselbe Spaltenbreite für alle Spalten im Arbeitsblatt festzulegen, verwenden Sie die Eigenschaft [**StandardWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardwidth) der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.cs" >}}

## **Erweiterte Themen**
- [Automatische Anpassung von Zeilen und Spalten](/cells/de/net/autofit-rows-and-columns/)
- [Text in Spalten konvertieren mit Aspose.Cells](/cells/de/net/convert-text-to-columns-using-aspose-cells/)
- [Kopieren von Zeilen und Spalten](/cells/de/net/copying-rows-and-columns/)
- [Leere Zeilen und Spalten in einem Arbeitsblatt löschen](/cells/de/net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Gruppieren und Aufheben der Gruppierung von Zeilen und Spalten](/cells/de/net/grouping-and-ungrouping-rows-and-columns/)
- [Zeilen und Spalten ausblenden und anzeigen](/cells/de/net/hiding-and-showing-rows-and-columns/)
- [Zeilen in einem Excel-Arbeitsblatt einfügen oder löschen](/cells/de/net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Einfügen und Löschen von Zeilen und Spalten einer Excel-Datei](/cells/de/net/inserting-and-deleting-rows-and-columns/)
- [Duplikate Zeilen in einem Arbeitsblatt entfernen](/cells/de/net/remove-duplicate-rows-in-a-worksheet/)
- [Aktualisieren Sie Verweise in anderen Arbeitsblättern, während Sie leere Spalten und Zeilen in einem Arbeitsblatt löschen](/cells/de/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
{{< app/cells/assistant language="csharp" >}}
