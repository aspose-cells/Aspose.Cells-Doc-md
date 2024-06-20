---
title: Anpassen der Zeilenhöhe und Spaltenbreite
type: docs
weight: 10
url: /de/java/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}} 

Wenn Sie mit Tabellenkalkulationen arbeiten und Daten zu Zeilen oder Spalten hinzufügen, müssen Sie möglicherweise die Höhe der Zeilen oder die Breite der Spalten ändern. Manchmal muss die aktuelle Höhe oder Breite geändert werden, um Daten anzuzeigen, wenn Formatierungen auf Zeilen oder Spalten angewendet werden. Normalerweise passen Benutzer die Zeilenhöhen und Spaltenbreiten in einer WYSIWYG-Umgebung mit Microsoft Excel an. Mit Aspose.Cells können Entwickler diese Operationen jedoch zur Laufzeit durchführen. Die Indizes von Zeilen und Spalten beginnen bei 0.

{{% /alert %}} 
## **Arbeiten mit Zeilen**
### **Anpassen der Zeilenhöhe**
Aspose.Cells bietet eine Klasse, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Microsoft Excel-Datei darstellt. Die [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält eine [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), die den Zugriff auf jede Arbeitsmappe in der Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-Klasse repräsentiert. Die [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-Klasse stellt eine [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung dar, die alle Zellen in der Arbeitsmappe repräsentiert.

Die [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung bietet verschiedene Methoden zur Verwaltung von Zeilen oder Spalten in einer Arbeitsmappe. Einige davon werden unten detaillierter besprochen.
### **Einstellen der Zeilenhöhe**
Es ist möglich, die Höhe einer einzelnen Zeile durch Aufruf der [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlungsmethode [setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\)) festzulegen. Die [setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\))-Methode hat die folgenden Parameter:

- **Zeilenindex**, der Index der Zeile, deren Höhe geändert wird.
- **Zeilenhöhe**, die auf die Zeile anzuwendende Zeilenhöhe.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightOfRow-SettingHeightOfRow.java" >}}
### **Einstellen der Höhe aller Zeilen**
Um die gleiche Zeilenhöhe für alle Zeilen in einer Arbeitsmappe festzulegen, verwenden Sie die [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlungsmethode [setStandardHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardHeight).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightAllRows-SettingHeightAllRows.java" >}}
## **Arbeiten mit Spalten**
### **Einstellen der Breite einer Spalte**
Legen Sie die Breite einer Spalte fest, indem Sie die [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlungsmethode [setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\)) aufrufen. Die [setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\))-Methode hat die folgenden Parameter:

- **Spaltenindex**, der Index der Spalte, deren Breite geändert wird.
- **Spaltenbreite**, die gewünschte Spaltenbreite.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfColumn-SettingWidthOfColumn.java" >}}
### **Einstellen der Breite aller Spalten**
Um die gleiche Spaltenbreite für alle Spalten in einer Arbeitsmappe festzulegen, verwenden Sie die [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlungsmethode [setStandardWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardWidth).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfAllColumns-SettingWidthOfAllColumns.java" >}}
