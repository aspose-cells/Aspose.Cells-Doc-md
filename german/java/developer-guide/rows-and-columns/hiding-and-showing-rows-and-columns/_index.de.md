---
title: Zeilen und Spalten ein- und ausblenden
type: docs
weight: 50
url: /de/java/hiding-and-showing-rows-and-columns/
---
## **Einführung**
Manchmal kann es auch erforderlich sein, dass Benutzer bestimmte Zeilen oder Spalten des Arbeitsblatts ausblenden und später wieder anzeigen. Microsoft Excel bietet diese Funktion und so wie Aspose.Cells.
## **Steuern der Sichtbarkeit von Zeilen und Spalten**
 Aspose.Cells bietet eine Klasse,[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält a[Arbeitsblattsammlung](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse. Das[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse bietet a[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Auflistung, die alle Zellen im Arbeitsblatt darstellt. Das[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)[](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung bietet mehrere Methoden zum Verwalten von Zeilen oder Spalten in einem Arbeitsblatt. Einige davon werden unten besprochen.
### **Ausblenden von Zeilen oder Spalten**
 Entwickler können eine Zeile oder Spalte ausblenden, indem sie die aufrufen[Zeile ausblenden](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideRow\(int\) ) und[Spalte ausblenden](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideColumn\(int\) ) Methoden der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Sammlung bzw. Beide Methoden verwenden den Zeilen-/Spaltenindex als Parameter, um die bestimmte Zeile oder Spalte auszublenden.

{{% alert color="primary" %}} 

Hinweis: Es ist auch möglich, eine Zeile oder Spalte auszublenden, wenn wir die Zeilenhöhe bzw. Spaltenbreite auf 0 setzen.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-HidingRowsandColumns-HidingRowsandColumns.java" >}}
### **Zeilen und Spalten anzeigen**
 Entwickler können jede ausgeblendete Zeile oder Spalte einblenden, indem sie die aufrufen[Zeile einblenden](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideRow\(int,%20double\) ) und[Spalte einblenden](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideColumn\(int,%20double\) ) Methoden der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Sammlung bzw. Beide Methoden nehmen zwei Parameter:

- **Zeilen- oder Spaltenindex** - der Index einer Zeile oder Spalte, der verwendet wird, um die bestimmte Zeile oder Spalte anzuzeigen.
- **Zeilenhöhe oder Spaltenbreite** - die Zeilenhöhe oder Spaltenbreite, die der Zeile oder Spalte zugewiesen wird, nachdem sie angezeigt wurde.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UnhidingRowsandColumns-UnhidingRowsandColumns.java" >}}

{{% alert color="primary" %}} 

Wenn Sie beim Sichtbarmachen einer ausgeblendeten Spalte/Zeile die zuvor zugewiesene Breite oder Höhe oder die ursprüngliche Breite oder Höhe wiederherstellen müssen, blenden Sie die Spalte oder Zeile mit negativer Breite oder Höhe ein. Beispiel: worksheet.getCells().unhideColumn(5, -1)

{{% /alert %}}
