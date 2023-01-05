---
title: Gruppieren und Aufheben der Gruppierung von Zeilen und Spalten
type: docs
weight: 40
url: /de/java/grouping-and-ungrouping-rows-and-columns/
---
## **Einführung**
In einer Microsoft Excel-Datei können Sie eine Gliederung der Daten erstellen, um Detailebenen mit einem einzigen Mausklick ein- und auszublenden.

 Drücke den**Gliederungssymbole**, 1,2,3, + und -, um schnell nur die Zeilen oder Spalten anzuzeigen, die Zusammenfassungen oder Überschriften für Abschnitte in einem Arbeitsblatt enthalten, oder Sie können die Symbole verwenden, um Details unter einer einzelnen Zusammenfassung oder Überschrift anzuzeigen, wie unten in der Abbildung gezeigt :

 Gruppierung von Zeilen und Spalten

![todo: Bild_alt_Text](grouping-and-ungrouping-rows-and-columns_1.png)
## **Gruppenverwaltung von Zeilen und Spalten**
 Aspose.Cells bietet eine Klasse,[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Das[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält a[Arbeitsblätter](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse. Das[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse bietet a[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Auflistung, die alle Zellen im Arbeitsblatt darstellt.

 Das[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection bietet mehrere Methoden zum Verwalten von Zeilen oder Spalten in einem Arbeitsblatt, einige davon werden im Folgenden ausführlicher besprochen.
### **Gruppieren von Zeilen und Spalten**
 Es ist möglich, Zeilen oder Spalten zu gruppieren, indem Sie die aufrufen[GruppeZeilen](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupRows\(int,%20int,%20boolean\) ) und[GruppeSpalten](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupColumns\(int,%20int,%20boolean\) ) Methoden der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Sammlung. Beide Methoden nehmen die folgenden Parameter:

- Index der ersten Zeile/Spalte, die erste Zeile oder Spalte in der Gruppe.
- Letzter Zeilen-/Spaltenindex, die letzte Zeile oder Spalte in der Gruppe.
- Ist ausgeblendet, ein boolescher Parameter, der angibt, ob Zeilen/Spalten nach der Gruppierung ausgeblendet werden sollen oder nicht.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-GroupingRowsandColumns-1.java" >}}
## **Gruppeneinstellungen**
Microsoft Excel ermöglicht auch die Konfiguration von Gruppeneinstellungen für die Anzeige von:

- Zusammenfassungszeilen unter Detail.
- Zusammenfassungsspalten rechts vom Detail.

**Gruppeneinstellungen** 

![todo: Bild_alt_Text](grouping-and-ungrouping-rows-and-columns_2.png)

Es ist möglich, diese Gruppeneinstellungen mit der Outline-Eigenschaft der Worksheet-Klasse zu konfigurieren.
### **Zusammenfassungszeilen unter Detail**
 Entwickler können die Anzeige von Zusammenfassungszeilen unter den Details steuern, indem sie die verwenden[Umriss](https://reference.aspose.com/cells/java/com.aspose.cells/Outline) Klasse'[SummaryRowBelow](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow) Methode.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowBelow-1.java" >}}
### **Zusammenfassungsspalten rechts vom Detail**
Mit kann gesteuert werden, ob Zusammenfassungsspalten rechts neben den Details angezeigt werden[Umriss](https://reference.aspose.com/cells/java/com.aspose.cells/Outline) Klasse'[SummaryColumnRight](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryColumnRight)Methode.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowRight-1.java" >}}
### **Gruppierung von Zeilen und Spalten aufheben**
 Heben Sie die Gruppierung gruppierter Zeilen oder Spalten auf, indem Sie die aufrufen[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung[Gruppierung aufheben](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupRows\(int,%20int\) ) und[Gruppierung von Spalten aufheben](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupColumns\(int,%20int\)) Methoden. Beide Methoden verwenden die gleichen Parameter:

- Index der ersten Zeile oder Spalte, die erste Zeile/Spalte, deren Gruppierung aufgehoben werden soll.
- Letzter Zeilen- oder Spaltenindex, die letzte Zeile/Spalte, deren Gruppierung aufgehoben werden soll.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UngroupingRowsandColumns-UngroupingRowsandColumns.java" >}}
