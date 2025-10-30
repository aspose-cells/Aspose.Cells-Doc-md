---
title: Zeilen und Spalten formatieren
linktitle: Zeilen und Spalten
type: docs
weight: 100
url: /de/python-net/adjusting-row-height-and-column-width/
description: Aspose.Cells für Python via .NET kann die Höhe von Zeilen oder die Breite von Spalten ändern sowie Formatierungen auf Zeilen oder Spalten anwenden.
keywords: Python Excel Bibliothek, Python Set Row Höhe und Column Breite, Python Adjust Row Höhe und Column Breite, Python Ändern der Rohen Höhe oder Column Breite, Python Formatierung von Zeilen und Spalten, Python wie man Zeilen Höhe und Spalten Breite setzt.
---


{{% alert color="primary" %}}

Wenn Sie mit Tabellenkalkulationen arbeiten und Daten zu Zeilen oder Spalten hinzufügen, müssen Sie möglicherweise die Höhe von Zeilen oder die Breite von Spalten ändern. Manchmal bedeutet die Anwendung von Formatierungen auf Zeilen oder Spalten, dass die aktuelle Höhe oder Breite geändert werden muss, um die Daten anzuzeigen. Normalerweise passen Benutzer die Zeilenhöhen und Spaltenbreiten in einer WYSIWYG-Umgebung mit Microsoft Excel an. Aber mit Aspose.Cells für Python via .NET können Entwickler diese Operationen zur Laufzeit durchführen.

{{% /alert %}}

## **Arbeiten mit Zeilen**

### **Wie man die Zeilenhöhe anpasst**

Aspose.Cells für Python via .NET bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-Klasse enthält eine [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection), die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-Klasse repräsentiert. Die [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-Klasse bietet eine [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung, die alle Zellen im Arbeitsblatt repräsentiert.

Die [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung bietet verschiedene Methoden zum Verwalten von Zeilen oder Spalten in einem Arbeitsblatt. Einige davon werden unten genauer erläutert.

### **Wie man die Höhe einer Zeile festlegt**

Es ist möglich, die Höhe einer einzelnen Zeile durch Aufrufen der [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlungsmethode [**set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) festzulegen. Die [**set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float)-Methode nimmt die folgenden Parameter wie folgt entgegen:

- **row**, der Index der Zeile, deren Höhe geändert werden soll.
- **height**, die Höhe der Zeile, die auf die Zeile angewendet werden soll.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingHeightOfRow-1.py" >}}

### **Wie man die Höhe aller Zeilen in einem Arbeitsblatt festlegt**

Wenn Entwickler die gleiche Zeilenhöhe für alle Zeilen im Arbeitsblatt festlegen müssen, können sie dies über die [**standard_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/standard_height)-Eigenschaft der [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung tun.

**Beispiel:**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingHeightAllRows-1.py" >}}

## **Arbeiten mit Spalten**

### **Wie man die Breite einer Spalte festlegt**

Die Breite einer Spalte wird durch Aufrufen der [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlungsmethode [**set_column_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width/#int-float) festgelegt. Die [**set_column_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width/#int-float)-Methode nimmt folgende Parameter entgegen:

- **Spalte**, der Index der Spalte, deren Breite Sie ändern.
- **width**, die gewünschte Spaltenbreite.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.py" >}}

### **Wie man die Spaltenbreite in Pixeln festlegt**

Legen Sie die Breite einer Spalte fest, indem Sie die Methode [**set_column_width_pixel**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width_pixel/#int-int) der [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung aufrufen. Die Methode [**set_column_width_pixel**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width_pixel/#int-int) nimmt die folgenden Parameter an:

- **Spalte**, der Index der Spalte, deren Breite Sie ändern.
- **Pixel**, die gewünschte Spaltenbreite in Pixeln.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.py" >}}

### **Wie man die Breite aller Spalten in einem Arbeitsblatt festlegt**

Um dieselbe Spaltenbreite für alle Spalten im Arbeitsblatt festzulegen, verwenden Sie die Eigenschaft [**standard_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/standard_width) der [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.py" >}}

## **Erweiterte Themen**
- [Automatische Anpassung von Zeilen und Spalten](/cells/de/python-net/autofit-rows-and-columns/)
- [Text in Spalten konvertieren mit Aspose.Cells](/cells/de/python-net/convert-text-to-columns-using-aspose-cells/)
- [Kopieren von Zeilen und Spalten](/cells/de/python-net/copying-rows-and-columns/)
- [Leere Zeilen und Spalten in einem Arbeitsblatt löschen](/cells/de/python-net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Gruppieren und Aufheben der Gruppierung von Zeilen und Spalten](/cells/de/python-net/grouping-and-ungrouping-rows-and-columns/)
- [Zeilen und Spalten ausblenden und anzeigen](/cells/de/python-net/hiding-and-showing-rows-and-columns/)
- [Zeilen in einem Excel-Arbeitsblatt einfügen oder löschen](/cells/de/python-net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Einfügen und Löschen von Zeilen und Spalten einer Excel-Datei](/cells/de/python-net/inserting-and-deleting-rows-and-columns/)
- [Duplikate Zeilen in einem Arbeitsblatt entfernen](/cells/de/python-net/remove-duplicate-rows-in-a-worksheet/)
- [Aktualisieren Sie Verweise in anderen Arbeitsblättern, während Sie leere Spalten und Zeilen in einem Arbeitsblatt löschen](/cells/de/python-net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
{{< app/cells/assistant language="python-net" >}}
