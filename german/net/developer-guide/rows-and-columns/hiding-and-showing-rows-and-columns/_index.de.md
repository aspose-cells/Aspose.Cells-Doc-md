---
title: Zeilen und Spalten ein- und ausblenden
type: docs
weight: 60
url: /de/net/hiding-and-showing-rows-and-columns/
---
{{% alert color="primary" %}}

Manchmal ist es sinnvoll, bestimmte Zeilen oder Spalten in einem Arbeitsblatt auszublenden und später anzuzeigen. Microsoft Excel bietet diese Funktion ebenso wie Aspose.Cells.

{{% /alert %}}

## **Steuern der Sichtbarkeit von Zeilen und Spalten**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblattsammlung**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) Dadurch können Entwickler auf jedes Arbeitsblatt in der Excel-Datei zugreifen. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Auflistung, die alle Zellen im Arbeitsblatt darstellt. Das[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Sammlung bietet mehrere Methoden zum Verwalten von Zeilen oder Spalten in einem Arbeitsblatt. Einige davon werden unten besprochen.

### **Zeilen und Spalten ausblenden**

 Entwickler können eine Zeile oder Spalte ausblenden, indem sie die aufrufen[**Zeile ausblenden**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) und[**Spalte ausblenden**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) Methoden der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Sammlung bzw. Beide Methoden verwenden den Zeilen- und Spaltenindex als Parameter, um die bestimmte Zeile oder Spalte auszublenden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Es ist auch möglich, eine Zeile oder Spalte auszublenden, indem Sie die Zeilenhöhe bzw. Spaltenbreite auf 0 setzen.

{{% /alert %}}

### **Zeilen und Spalten anzeigen**

 Entwickler können jede ausgeblendete Zeile oder Spalte anzeigen, indem sie die aufrufen[**Zeile einblenden**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) und[**Spalte einblenden**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) Methoden der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Sammlung bzw. Beide Methoden nehmen zwei Parameter:

- **Zeilen- oder Spaltenindex** - der Index einer Zeile oder Spalte, der verwendet wird, um die bestimmte Zeile oder Spalte anzuzeigen.
- **Zeilenhöhe oder Spaltenbreite** - die Zeilenhöhe oder Spaltenbreite, die der Zeile oder Spalte nach dem Einblenden zugewiesen wurde.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Wenn Sie beim Sichtbarmachen einer ausgeblendeten Spalte die zuvor zugewiesene Breite oder die ursprüngliche Breite wiederherstellen müssen, blenden Sie die Spalte bitte mit einer negativen Breite ein. Beispiel: Arbeitsblatt.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Ausblenden mehrerer Zeilen und Spalten**

 Entwickler können mehrere Zeilen oder Spalten gleichzeitig ausblenden, indem sie die aufrufen[**Zeilen ausblenden**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) und[**Spalten ausblenden**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) Methoden der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Sammlung bzw. Beide Methoden nehmen den Anfangszeilen- oder Spaltenindex und die Anzahl der Zeilen oder Spalten, die ausgeblendet werden sollen, als Parameter.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

 Es ist auch möglich, die zu verwenden[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Klasse'[**Zeilen einblenden**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) und[**Spalten einblenden**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns)Methoden, um mehrere Zeilen und Spalten sichtbar zu machen.

{{% /alert %}}
