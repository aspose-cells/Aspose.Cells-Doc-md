---
title: Zeilen und Spalten ausblenden und anzeigen
type: docs
weight: 60
url: /de/net/hiding-and-showing-rows-and-columns/
---

{{% alert color="primary" %}}

Manchmal macht es Sinn, bestimmte Zeilen oder Spalten in einem Arbeitsblatt zu verstecken und später anzuzeigen. Microsoft Excel bietet diese Funktion und auch Aspose.Cells.

{{% /alert %}}

## **Steuerung der Sichtbarkeit von Zeilen und Spalten**

Aspose.Cells bietet eine Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält eine [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection), die es Entwicklern ermöglicht, auf jedes Arbeitsblatt in der Excel-Datei zuzugreifen. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) bietet eine [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung, die alle Zellen im Arbeitsblatt repräsentiert. Die Sammlung [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) bietet mehrere Methoden zum Verwalten von Zeilen oder Spalten in einem Arbeitsblatt. Einige davon werden unten diskutiert.

### **Verbergen von Zeilen und Spalten**

Entwickler können eine Zeile oder Spalte ausblenden, indem sie die [**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow)- und [**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn)-Methoden der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung aufrufen. Beide Methoden nehmen den Zeilen- und Spaltenindex als Parameter an, um die spezifische Zeile oder Spalte auszublenden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Es ist auch möglich, eine Zeile oder Spalte auszublenden, indem die Zeilenhöhe oder Spaltenbreite auf 0 gesetzt wird.

{{% /alert %}}

### **Anzeigen von Zeilen und Spalten**

Entwickler können eine versteckte Zeile oder Spalte anzeigen, indem sie die [**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow)- und [**UnhideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn)-Methoden der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung aufrufen. Beide Methoden nehmen zwei Parameter an:

- **Zeilen- oder Spaltenindex** - der Index einer Zeile oder Spalte, der verwendet wird, um die spezifische Zeile oder Spalte anzuzeigen.
- **Zeilenhöhe oder Spaltenbreite** - die Zeilenhöhe oder Spaltenbreite, die der Zeile oder Spalte nach dem Ausblenden zugewiesen wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Wenn Sie eine versteckte Spalte sichtbar machen, müssen Sie sie bei Bedarf auf die zuvor zugewiesene Breite oder ursprüngliche Breite wiederherstellen, indem Sie die Spalte mit einer negativen Breite ausblenden. Zum Beispiel: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Mehrere Zeilen und Spalten verstecken**

Entwickler können mehrere Zeilen oder Spalten auf einmal ausblenden, indem sie die [**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows)- und [**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns)-Methoden der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung aufrufen. Beide Methoden nehmen den Startindex der Zeile oder Spalte und die Anzahl der auszublendenden Zeilen oder Spalten als Parameter an.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Es ist auch möglich, die [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)- und [**UnhideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows)-Methoden der Klasse [**UnhideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns) zu verwenden, um mehrere Zeilen und Spalten sichtbar zu machen.

{{% /alert %}}
