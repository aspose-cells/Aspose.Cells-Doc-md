---
title: Anzeigen und Ausblenden von Zeilen, Spalten und Bildlaufleisten
type: docs
weight: 20
url: /de/net/show-and-hide-rows-columns-and-scroll-bars/
---
{{% alert color="primary" %}}

Aspose.Cells bietet Möglichkeiten, die Sichtbarkeit von Zeilen, Spalten und Bildlaufleisten eines Arbeitsblatts zu steuern.

{{% /alert %}}

## **Zeilen und Spalten ein- und ausblenden**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die es Entwicklern ermöglicht, auf jedes Arbeitsblatt in der Excel-Datei zuzugreifen. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Auflistung, die alle Zellen im Arbeitsblatt darstellt. Das[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-Sammlung bietet mehrere Methoden zum Verwalten von Zeilen oder Spalten in einem Arbeitsblatt. Einige davon werden unten besprochen.

### **Zeilen und Spalten anzeigen**

 Entwickler können jede ausgeblendete Zeile oder Spalte anzeigen, indem sie die aufrufen[**Zeile einblenden**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) und[**Spalte einblenden**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) Methoden der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Sammlung bzw. Beide Methoden nehmen zwei Parameter:

- **Zeilen- oder Spaltenindex** - der Index einer Zeile oder Spalte, der verwendet wird, um die bestimmte Zeile oder Spalte anzuzeigen.
- **Zeilenhöhe oder Spaltenbreite** - die Zeilenhöhe oder Spaltenbreite, die der Zeile oder Spalte nach dem Einblenden zugewiesen wurde.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Wenn Sie beim Sichtbarmachen einer ausgeblendeten Spalte die zuvor zugewiesene Breite oder die ursprüngliche Breite wiederherstellen müssen, blenden Sie die Spalte bitte mit einer negativen Breite ein. Beispiel: Arbeitsblatt.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Zeilen und Spalten ausblenden**

 Entwickler können eine Zeile oder Spalte ausblenden, indem sie die aufrufen[**Zeile ausblenden**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) und[**Spalte ausblenden**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) Methoden der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Sammlung bzw. Beide Methoden verwenden den Zeilen- und Spaltenindex als Parameter, um die bestimmte Zeile oder Spalte auszublenden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Es ist auch möglich, eine Zeile oder Spalte auszublenden, indem Sie die Zeilenhöhe bzw. Spaltenbreite auf 0 setzen.

{{% /alert %}}

### **Mehrere Zeilen und Spalten ausblenden**

 Entwickler können mehrere Zeilen oder Spalten gleichzeitig ausblenden, indem sie die aufrufen[**Zeilen ausblenden**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) und[**Spalten ausblenden**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) Methoden der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)Sammlung bzw. Beide Methoden nehmen den Anfangszeilen- oder Spaltenindex und die Anzahl der Zeilen oder Spalten, die ausgeblendet werden sollen, als Parameter.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

## **Bildlaufleisten ein- und ausblenden**

Bildlaufleisten werden verwendet, um durch den Inhalt einer beliebigen Datei zu navigieren. Normalerweise gibt es zwei Arten von Bildlaufleisten:

- Vertikale Bildlaufleisten
- Horizontale Bildlaufleisten

Microsoft Excel bietet auch horizontale und vertikale Bildlaufleisten, damit Benutzer durch Arbeitsblattinhalte blättern können. Mit Aspose.Cells können Entwickler die Sichtbarkeit beider Arten von Bildlaufleisten in Excel-Dateien steuern.

### **Steuern der Sichtbarkeit von Bildlaufleisten**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) die eine Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) -Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten einer Excel-Datei. Um die Sichtbarkeit von Bildlaufleisten zu steuern, verwenden Sie die[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) und[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible)Eigenschaften.[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) und[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) sind boolesche Eigenschaften, was bedeutet, dass diese Eigenschaften nur speichern können**Stimmt** oder**FALSCH** Werte.

#### **Bildlaufleisten sichtbar machen**

 Machen Sie Bildlaufleisten sichtbar, indem Sie die[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) oder[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) Eigentum zu**Stimmt**.

#### **Bildlaufleisten ausblenden**

 Blenden Sie Bildlaufleisten aus, indem Sie die[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) oder[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) Eigentum zu**FALSCH**.

**Beispielcode**

Unten ist ein vollständiger Code, der eine Excel-Datei, book1.xls, öffnet, beide Bildlaufleisten ausblendet und dann die geänderte Datei als output.xls speichert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideScrollBars-1.cs" >}}
