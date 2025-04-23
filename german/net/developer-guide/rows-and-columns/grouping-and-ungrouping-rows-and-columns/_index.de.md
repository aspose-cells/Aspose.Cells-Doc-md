---
title: Gruppieren und Aufheben der Gruppierung von Zeilen und Spalten
type: docs
weight: 50
url: /de/net/grouping-and-ungrouping-rows-and-columns/
---

## **Einführung**

In einer Microsoft Excel-Datei können Sie eine Gliederung für die Daten erstellen, um mit einem einzigen Mausklick Ebenen von Details anzuzeigen und auszublenden.

Klicken Sie auf die **Gliederungssymbole**, 1,2,3, + und -, um nur die Zeilen oder Spalten anzuzeigen, die Zusammenfassungen oder Überschriften für Abschnitte in einem Arbeitsblatt bereitstellen, oder verwenden Sie die Symbole, um Details unter einer einzelnen Zusammenfassung oder Überschrift anzuzeigen, wie unten in der Abbildung gezeigt:

|**Gruppieren von Zeilen und Spalten.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Gruppenverwaltung von Zeilen und Spalten**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel-Datei darstellt. Die [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-Klasse enthält eine [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection), die den Zugriff auf jede Arbeitsmappe in der Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Klasse stellt eine [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung dar, die alle Zellen in der Arbeitsmappe repräsentiert.

Die [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung bietet mehrere Methoden zum Verwalten von Zeilen oder Spalten in einer Arbeitsmappe, einige davon werden unten genauer erläutert.

### **Zeilen und Spalten gruppieren**

Es ist möglich, Zeilen oder Spalten zu gruppieren, indem man die [**GroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/grouprows/index)- und [**GroupColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/groupcolumns/index)-Methoden der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung aufruft. Beide Methoden nehmen folgende Parameter an:

- Erster Zeilen-/Spaltenindex, die erste Zeile oder Spalte in der Gruppe.
- Letzter Zeilen-/Spaltenindex, die letzte Zeile oder Spalte in der Gruppe.
- Ist versteckt, ein boolescher Parameter, der angibt, ob Zeilen/Spalten nach dem Gruppieren ausgeblendet werden sollen oder nicht.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-GroupingRowsAndColumns-1.cs" >}}

#### **Gruppeneinstellungen**

Microsoft Excel ermöglicht es Ihnen, Gruppeneinstellungen für die Anzeige zu konfigurieren:

- Zusammenfassungszeilen unterhalb von Details.
- Zusammenfassungsspalten rechts neben dem Detail.

Entwickler können diese Gruppeneinstellungen mithilfe der [**Outline**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/outline)-Eigenschaft der [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Klasse konfigurieren.

### **Zusammenfassungszeilen unterhalb der Details**

Es ist möglich zu steuern, ob Zusammenfassungszeilen unterhalb des Details angezeigt werden, indem man die [**Outline**](https://reference.aspose.com/cells/net/aspose.cells/outline)-Eigenschaft der [**SummaryRowBelow**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summaryrowbelow)-Klasse auf **true** oder **false** setzt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowBelow-1.cs" >}}

### **Zusammenfassungsspalten rechts von den Details**

Entwickler können auch steuern, ob Zusammenfassungsspalten rechts neben dem Detail angezeigt werden, indem sie die [**SummaryColumnRight**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summarycolumnright)-Eigenschaft der [**Outline**](https://reference.aspose.com/cells/net/aspose.cells/outline)-Klasse auf **true** oder **false** setzen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowRight-1.cs" >}}

## **Zeilen und Spalten entgruppieren**

Um gruppierte Zeilen oder Spalten aufzuheben, rufen Sie die [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlungsmethoden [**UngroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) und [**UngroupColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungroupcolumns) auf. Beide Methoden nehmen zwei Parameter an:

- Erster Zeilen- oder Spaltenindex, die erste Zeile/Spalte, die aufgehoben werden soll.
- Letzter Zeilen- oder Spaltenindex, die letzte Zeile/Spalte, die aufgehoben werden soll.

[**UngroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) hat eine Überladung, die einen dritten booleschen Parameter akzeptiert. Wenn dieser auf **true** gesetzt wird, werden alle gruppierten Informationen entfernt. Andernfalls wird nur die äußere Gruppeninformation entfernt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-UngroupingRowsAndColumns-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
