---
title: Gruppieren und Aufheben der Gruppierung von Zeilen und Spalten
type: docs
weight: 40
url: /de/java/grouping-and-ungrouping-rows-and-columns/
---

## **Einführung**
In einer Microsoft Excel-Datei können Sie eine Gliederung für die Daten erstellen, um mit einem einzigen Mausklick Ebenen von Details anzuzeigen und auszublenden.

Klicken Sie auf die **Gliederungssymbole**, 1,2,3, + und -, um nur die Zeilen oder Spalten anzuzeigen, die Zusammenfassungen oder Überschriften für Abschnitte in einem Arbeitsblatt bereitstellen, oder verwenden Sie die Symbole, um Details unter einer einzelnen Zusammenfassung oder Überschrift anzuzeigen, wie unten in der Abbildung gezeigt:

Gruppierung von Zeilen und Spalten 

![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)
## **Gruppenverwaltung von Zeilen und Spalten**
Aspose.Cells bietet eine Klasse, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) enthält eine [Worksheets](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) repräsentiert. Die Klasse [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) bietet eine [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung, die alle Zellen im Arbeitsblatt repräsentiert.

Die [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung bietet mehrere Methoden zur Verwaltung von Zeilen oder Spalten in einem Arbeitsblatt, einige davon sind unten genauer erläutert.
### **Gruppierung von Zeilen & Spalten**
Es ist möglich, Zeilen oder Spalten durch Aufrufen der Methoden [groupRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupRows-int-int-boolean-) und [groupColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupColumns-int-int-boolean-) der [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung zu gruppieren. Beide Methoden nehmen folgende Parameter entgegen:

- Erster Zeilen-/Spaltenindex, die erste Zeile oder Spalte in der Gruppe.
- Letzter Zeilen-/Spaltenindex, die letzte Zeile oder Spalte in der Gruppe.
- Ist versteckt, ein boolescher Parameter, der angibt, ob Zeilen/Spalten nach dem Gruppieren ausgeblendet werden sollen oder nicht.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-GroupingRowsandColumns-1.java" >}}
## **Gruppeneinstellungen**
Microsoft Excel erlaubt auch die Konfiguration von Gruppeneinstellungen zur Anzeige:

- Zusammenfassungszeilen unterhalb von Details.
- Zusammenfassungsspalten rechts vom Detail.

**Gruppeneinstellungen** 

![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_2.png)

Es ist möglich, diese Gruppeneinstellungen mithilfe der Outline-Eigenschaft der Worksheet-Klasse zu konfigurieren.
### **Zusammenfassungszeilen unterhalb des Details**
Entwickler können die Anzeige von Zusammenfassungszeilen unterhalb des Details mithilfe der [Outline](https://reference.aspose.com/cells/java/com.aspose.cells/Outline)-Klasse und der Methode [SummaryRowBelow](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow) steuern.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowBelow-1.java" >}}
### **Zusammenfassungsspalten rechts von den Details**
Es ist möglich zu steuern, ob Zusammenfassungsspalten rechts vom Detail angezeigt werden, mithilfe der [Outline](https://reference.aspose.com/cells/java/com.aspose.cells/Outline)-Klasse und der Methode [SummaryColumnRight](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryColumnRight).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowRight-1.java" >}}
### **Zeilen & Spalten aufheben**
Ungruppieren Sie gruppierte Zeilen oder Spalten durch Aufrufen der [UngroupRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupRows-int-int-) und [UngroupColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupColumns-int-int-) Methoden der [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung. Beide Methoden verwenden die gleichen Parameter:

- Erster Zeilen- oder Spaltenindex, die erste Zeile/Spalte, die aufgehoben werden soll.
- Letzter Zeilen- oder Spaltenindex, die letzte Zeile/Spalte, die aufgehoben werden soll.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UngroupingRowsandColumns-UngroupingRowsandColumns.java" >}}
{{< app/cells/assistant language="java" >}}
