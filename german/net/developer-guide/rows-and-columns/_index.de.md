---
title: Zeilen und Spalten formatieren
linktitle: Reihen und Spalten
type: docs
weight: 100
url: /de/net/adjusting-row-height-and-column-width/
description: Aspose.Cells for .NET kann das Ändern der Zeilenhöhe oder Spaltenbreite sowie das Anwenden von Formatierungen auf Zeilen oder Spalten unterstützen.
keywords: Set row height and column width, Adjust row height and column width, change the row height or column width, format rows and columns, how to set row height and column width.
---
{{% alert color="primary" %}}

Wenn Sie mit Tabellenkalkulationen arbeiten und Daten zu Zeilen oder Spalten hinzufügen, müssen Sie möglicherweise die Höhe von Zeilen oder die Breite von Spalten ändern. Manchmal bedeutet das Anwenden von Formatierungen auf Zeilen oder Spalten, dass die aktuelle Höhe oder Breite geändert werden muss, um die Daten anzuzeigen. Normalerweise passen Benutzer Zeilenhöhen und Spaltenbreiten in einer WYSIWYG-Umgebung mit Microsoft Excel an. Mit Aspose.Cells können Entwickler diese Vorgänge jedoch zur Laufzeit ausführen.

{{% /alert %}}

##  **Arbeiten mit Zeilen**

###  **So passen Sie die Zeilenhöhe an**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , das eine Microsoft Excel-Datei darstellt. Der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)Dies ermöglicht den Zugriff auf jedes Arbeitsblatt in der Excel-Datei. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Sammlung, die alle Zellen im Arbeitsblatt darstellt.

 Der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Die Sammlung bietet verschiedene Methoden zum Verwalten von Zeilen oder Spalten in einem Arbeitsblatt. Einige davon werden im Folgenden ausführlicher besprochen.

###  **So legen Sie die Höhe einer Zeile fest**

 Es ist möglich, die Höhe einer einzelnen Zeile durch Aufrufen von festzulegen[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung[**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) Methode. Der[**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight)Die Methode übernimmt die folgenden Parameter wie folgt:

- *Zeilenindex**, der Index der Zeile, deren Höhe Sie ändern.
- *Zeilenhöhe**, die auf die Zeile anzuwendende Zeilenhöhe.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightOfRow-1.cs" >}}

###  **So legen Sie die Höhe aller Zeilen in einem Arbeitsblatt fest**

 Wenn Entwickler für alle Zeilen im Arbeitsblatt die gleiche Zeilenhöhe festlegen müssen, können sie dies mithilfe von tun[**Standardhöhe**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardheight) Eigentum der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Sammlung.

**Beispiel:**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightAllRows-1.cs" >}}

##  **Arbeiten mit Spalten**

###  **So legen Sie die Breite einer Spalte fest**

 Legen Sie die Breite einer Spalte fest, indem Sie die aufrufen[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung[**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) Methode. Der[**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth)Die Methode benötigt die folgenden Parameter:

- *Spaltenindex**, der Index der Spalte, deren Breite Sie ändern.
- *Spaltenbreite**, die gewünschte Spaltenbreite.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.cs" >}}

###  **So legen Sie die Spaltenbreite in Pixel fest**

Legen Sie die Breite einer Spalte fest, indem Sie die aufrufen[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Sammlung[**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)Methode. Der[**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)Die Methode benötigt die folgenden Parameter:

- *Spaltenindex**, der Index der Spalte, deren Breite Sie ändern.
- *Spaltenbreite**, die gewünschte Spaltenbreite in Pixel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.cs" >}}

###  **So legen Sie die Breite aller Spalten in einem Arbeitsblatt fest**

 Um für alle Spalten im Arbeitsblatt die gleiche Spaltenbreite festzulegen, verwenden Sie die[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung[**Standardbreite**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardwidth)Eigentum.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.cs" >}}

##  **Vorabthemen**
- [Zeilen und Spalten automatisch anpassen](/cells/de/net/autofit-rows-and-columns/)
- [Konvertieren Sie Text mit Aspose.Cells in Spalten](/cells/de/net/convert-text-to-columns-using-aspose-cells/)
- [Zeilen und Spalten kopieren](/cells/de/net/copying-rows-and-columns/)
- [Leere Zeilen und Spalten in einem Arbeitsblatt löschen](/cells/de/net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Gruppieren und Gruppieren von Zeilen und Spalten aufheben](/cells/de/net/grouping-and-ungrouping-rows-and-columns/)
- [Ein- und Ausblenden von Zeilen und Spalten](/cells/de/net/hiding-and-showing-rows-and-columns/)
- [Zeilen in ein Excel-Arbeitsblatt einfügen oder löschen](/cells/de/net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Einfügen und Löschen von Zeilen und Spalten einer Excel-Datei](/cells/de/net/inserting-and-deleting-rows-and-columns/)
- [Entfernen Sie doppelte Zeilen in einem Arbeitsblatt](/cells/de/net/remove-duplicate-rows-in-a-worksheet/)
- [Aktualisieren Sie Verweise in anderen Arbeitsblättern, während Sie leere Spalten und Zeilen in einem Arbeitsblatt löschen](/cells/de/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
