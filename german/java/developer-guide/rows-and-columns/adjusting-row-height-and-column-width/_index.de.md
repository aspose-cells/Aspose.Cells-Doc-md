---
title: Zeilenhöhe und Spaltenbreite anpassen
type: docs
weight: 10
url: /de/java/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

Wenn Sie mit Tabellenkalkulationen arbeiten und Daten zu Zeilen oder Spalten hinzufügen, müssen Sie möglicherweise die Zeilenhöhe oder Spaltenbreite ändern. Manchmal bedeutet das Anwenden von Formatierungen auf Zeilen oder Spalten, dass die aktuelle Höhe oder Breite geändert werden muss, um die Daten anzuzeigen. Normalerweise passen Benutzer Zeilenhöhen und Spaltenbreiten in einer WYSIWYG-Umgebung mit Microsoft Excel an. Aber mit Aspose.Cells können Entwickler diese Operationen zur Laufzeit ausführen. Indizes von Zeilen und Spalten beginnen bei 0.

{{% /alert %}} 
## **Arbeiten mit Zeilen**
### **Anpassen der Zeilenhöhe**
 Aspose.Cells bietet eine Klasse,[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält a[Arbeitsblattsammlung](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse. Das[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse bietet a[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Auflistung, die alle Zellen im Arbeitsblatt darstellt.

 Das[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung bietet mehrere Methoden zum Verwalten von Zeilen oder Spalten in einem Arbeitsblatt. Einige davon werden weiter unten ausführlicher besprochen.
### **Einstellen der Zeilenhöhe**
 Es ist möglich, die Höhe einer einzelnen Zeile durch Aufrufen von festzulegen[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung[setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\) ) Methode. Das[setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\))-Methode nimmt die folgenden Parameter an:

- **Zeilenindex**, der Index der Zeile, deren Höhe Sie ändern.
- **Zeilenhöhe**, die Zeilenhöhe, die auf die Zeile angewendet werden soll.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightOfRow-SettingHeightOfRow.java" >}}
### **Einstellen der Höhe aller Zeilen**
 Um dieselbe Zeilenhöhe für alle Zeilen in einem Arbeitsblatt festzulegen, verwenden Sie die[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung[setStandardHöhe](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardHeight)Methode.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightAllRows-SettingHeightAllRows.java" >}}
## **Arbeiten mit Spalten**
### **Einstellen der Breite einer Spalte**
 Legen Sie die Breite einer Spalte fest, indem Sie die aufrufen[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung[setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\) ) Methode. Das[setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\))-Methode nimmt die folgenden Parameter an:

- **Spaltenindex**, der Index der Spalte, deren Breite Sie ändern.
- **Spaltenbreite**, die gewünschte Spaltenbreite.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfColumn-SettingWidthOfColumn.java" >}}
### **Einstellen der Breite aller Spalten**
 Um dieselbe Spaltenbreite für alle Spalten in einem Arbeitsblatt festzulegen, verwenden Sie die[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung[setStandardWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardWidth)Methode.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfAllColumns-SettingWidthOfAllColumns.java" >}}
