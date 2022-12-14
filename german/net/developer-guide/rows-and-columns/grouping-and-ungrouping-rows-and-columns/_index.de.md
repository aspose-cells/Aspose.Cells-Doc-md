---
title: Gruppieren und Aufheben der Gruppierung von Zeilen und Spalten
type: docs
weight: 50
url: /de/net/grouping-and-ungrouping-rows-and-columns/
---
## **Einführung**

In einer Microsoft Excel-Datei können Sie eine Gliederung der Daten erstellen, um Detailebenen mit einem einzigen Mausklick ein- und auszublenden.

 Drücke den**Gliederungssymbole**, 1,2,3, + und -, um schnell nur die Zeilen oder Spalten anzuzeigen, die Zusammenfassungen oder Überschriften für Abschnitte in einem Arbeitsblatt enthalten, oder Sie können die Symbole verwenden, um Details unter einer einzelnen Zusammenfassung oder Überschrift anzuzeigen, wie unten in der Abbildung gezeigt :

|**Zeilen und Spalten gruppieren.**|
|:- |
|![todo: Bild_alt_Text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Gruppenverwaltung von Zeilen und Spalten**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblattsammlung**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Auflistung, die alle Zellen im Arbeitsblatt darstellt.

 Das[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection bietet mehrere Methoden zum Verwalten von Zeilen oder Spalten in einem Arbeitsblatt, einige davon werden im Folgenden ausführlicher besprochen.

### **Zeilen und Spalten gruppieren**

 Es ist möglich, Zeilen oder Spalten zu gruppieren, indem Sie die aufrufen[**GroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/grouprows/index) und[**GruppierenSpalten**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/groupcolumns/index) Methoden der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung. Beide Methoden nehmen die folgenden Parameter:

- Index der ersten Zeile/Spalte, die erste Zeile oder Spalte in der Gruppe.
- Letzter Zeilen-/Spaltenindex, die letzte Zeile oder Spalte in der Gruppe.
- Ist ausgeblendet, ein boolescher Parameter, der angibt, ob Zeilen/Spalten nach der Gruppierung ausgeblendet werden sollen oder nicht.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-GroupingRowsAndColumns-1.cs" >}}

#### **Gruppeneinstellungen**

Microsoft Mit Excel können Sie Gruppeneinstellungen für die Anzeige konfigurieren:

- Zusammenfassungszeilen unter Detail.
- Zusammenfassungsspalten rechts vom Detail.

 Entwickler können diese Gruppeneinstellungen mithilfe von konfigurieren[**Umriss**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/outline) Eigentum der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Klasse.

### **Zusammenfassungszeilen unterhalb von Details**

 Es ist möglich, zu steuern, ob Übersichtszeilen unter den Details angezeigt werden, indem Sie festlegen[**Umriss**](https://reference.aspose.com/cells/net/aspose.cells/outline) Klasse'[**SummaryRowBelow**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summaryrowbelow) Eigentum zu**Stimmt** oder**FALSCH**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowBelow-1.cs" >}}

### **Zusammenfassungsspalten rechts vom Detail**

 Entwickler können auch die Anzeige von Zusammenfassungsspalten rechts neben den Details steuern, indem sie das festlegen[**SummaryColumnRight**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summarycolumnright) Eigentum von[**Umriss**](https://reference.aspose.com/cells/net/aspose.cells/outline) Klasse zu**Stimmt** oder**FALSCH**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowRight-1.cs" >}}

## **Gruppierung von Zeilen und Spalten aufheben**

 Um die Gruppierung gruppierter Zeilen oder Spalten aufzuheben, rufen Sie die auf[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Sammlung[**Gruppierung aufheben**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) und[**Gruppierung von Spalten aufheben**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungroupcolumns)Methoden. Beide Methoden nehmen zwei Parameter:

- Index der ersten Zeile oder Spalte, die erste Zeile/Spalte, deren Gruppierung aufgehoben werden soll.
- Letzter Zeilen- oder Spaltenindex, die letzte Zeile/Spalte, deren Gruppierung aufgehoben werden soll.

[**Gruppierung aufheben**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) hat eine Überladung, die einen booleschen dritten Parameter akzeptiert. Einstellen auf**Stimmt**entfernt alle gruppierten Informationen. Andernfalls werden nur die äußeren Gruppeninformationen entfernt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-UngroupingRowsAndColumns-1.cs" >}}
