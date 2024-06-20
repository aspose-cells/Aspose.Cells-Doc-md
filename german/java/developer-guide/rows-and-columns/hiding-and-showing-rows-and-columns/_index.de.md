---
title: Zeilen und Spalten ausblenden und anzeigen
type: docs
weight: 50
url: /de/java/hiding-and-showing-rows-and-columns/
---

## **Einführung**
Manchmal ist es auch möglich, dass Benutzer bestimmte Zeilen oder Spalten des Arbeitsblatts ausblenden und später anzeigen möchten. Microsoft Excel bietet diese Funktion und auch Aspose.Cells.
## **Steuerung der Sichtbarkeit von Zeilen & Spalten**
Aspose.Cells bietet eine Klasse, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Microsoft Excel-Datei darstellt. Die Klasse [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) enthält eine [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) dargestellt. Die Klasse [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) bietet eine [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung, die alle Zellen im Arbeitsblatt darstellt. Die [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)[ ](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung bietet mehrere Methoden zur Verwaltung von Zeilen oder Spalten in einem Arbeitsblatt. Einige davon werden unten diskutiert.
### **Verstecken von Zeilen oder Spalten**
Entwickler können eine Zeile oder Spalte verstecken, indem sie die Methoden [HideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideRow\(int\)) und [HideColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideColumn\(int\)) der [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung aufrufen. Beide Methoden nehmen den Zeilen-/Spaltenindex als Parameter, um die spezifische Zeile oder Spalte zu verstecken.

{{% alert color="primary" %}} 

Hinweis: Es ist auch möglich, eine Zeile oder Spalte zu verstecken, wenn die Zeilenhöhe bzw. die Spaltenbreite auf 0 gesetzt wird.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-HidingRowsandColumns-HidingRowsandColumns.java" >}}
### **Anzeigen von Zeilen und Spalten**
Entwickler können eine versteckte Zeile oder Spalte wieder sichtbar machen, indem sie die Methoden [UnhideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideRow\(int,%20double\)) und [UnhideColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideColumn\(int,%20double\)) der [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung aufrufen. Beide Methoden nehmen zwei Parameter:

- **Zeilen- oder Spaltenindex** - der Index einer Zeile oder Spalte, der verwendet wird, um die spezifische Zeile oder Spalte anzuzeigen.
- **Zeilenhöhe oder Spaltenbreite** - die der Zeile oder Spalte nach dem Zeigen zugewiesene Zeilenhöhe oder Spaltenbreite.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UnhidingRowsandColumns-UnhidingRowsandColumns.java" >}}

{{% alert color="primary" %}} 

Beim Wiederherstellen einer versteckten Spalte/Zeile zu einer zuvor zugewiesenen Breite oder Höhe, oder zu ihrer ursprünglichen Breite oder Höhe, entfernen Sie bitte die Spalte oder Zeile mit negativer Breite oder Höhe. Zum Beispiel: `worksheet.getCells().unhideColumn(5, -1)`

{{% /alert %}}
