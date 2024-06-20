---
title: Zeilen, Spalten und Bildlaufleisten anzeigen und ausblenden
type: docs
weight: 20
url: /de/net/show-and-hide-rows-columns-and-scroll-bars/
description: Dieser Artikel zeigt, wie man programmgesteuert Excel Arbeitsblattzeilen und spalten mithilfe der C# Sprache und des .NET API oder Bibliothek ein und ausblendet. Die Sichtbarkeit der Bildlaufleisten kann angepasst werden, und mehrere Zeilen und Spalten können ausgeblendet werden.
---

{{% alert color="primary" %}}

Aspose.Cells bietet Möglichkeiten, die Sichtbarkeit von Zeilen, Spalten und Bildlaufleisten eines Arbeitsblatts zu steuern.

{{% /alert %}}

## **Zeilen und Spalten anzeigen und ausblenden**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel-Datei darstellt. Die [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-Klasse enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-Sammlung, die es Entwicklern ermöglicht, auf jedes Arbeitsblatt in der Excel-Datei zuzugreifen. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Klasse bietet eine [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-Sammlung, die alle Zellen im Arbeitsblatt darstellt. Die [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-Sammlung bietet mehrere Methoden zum Verwalten von Zeilen oder Spalten in einem Arbeitsblatt. Einige davon werden unten besprochen.

### **Zeilen und Spalten anzeigen**

Entwickler können eine versteckte Zeile oder Spalte anzeigen, indem sie die [**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow)- und [**UnhideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn)-Methoden der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-Sammlung aufrufen. Beide Methoden nehmen zwei Parameter an:

- **Zeilen- oder Spaltenindex** - der Index einer Zeile oder Spalte, der verwendet wird, um die spezifische Zeile oder Spalte anzuzeigen.
- **Zeilenhöhe oder Spaltenbreite** - die Zeilenhöhe oder Spaltenbreite, die der Zeile oder Spalte nach dem Ausblenden zugewiesen wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Wenn Sie eine versteckte Spalte sichtbar machen, müssen Sie sie bei Bedarf auf die zuvor zugewiesene Breite oder ursprüngliche Breite wiederherstellen, indem Sie die Spalte mit einer negativen Breite ausblenden. Zum Beispiel: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Zeilen und Spalten ausblenden**

Entwickler können eine Zeile oder Spalte ausblenden, indem sie die [**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow)- und [**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn)-Methoden der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-Sammlung aufrufen. Beide Methoden nehmen den Zeilen- und Spaltenindex als Parameter an, um die spezifische Zeile oder Spalte auszublenden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Es ist auch möglich, eine Zeile oder Spalte auszublenden, indem die Zeilenhöhe oder Spaltenbreite auf 0 gesetzt wird.

{{% /alert %}}

### **Mehrere Zeilen und Spalten ausblenden**

Entwickler können mehrere Zeilen oder Spalten auf einmal ausblenden, indem sie die [**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows)- und [**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns)-Methoden der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-Sammlung aufrufen. Beide Methoden nehmen den Startindex der Zeile oder Spalte und die Anzahl der auszublendenden Zeilen oder Spalten als Parameter an.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

## **Bildlaufleisten einblenden und ausblenden**

Bildlaufleisten werden verwendet, um den Inhalt einer Datei zu durchsuchen. Normalerweise gibt es zwei Arten von Bildlaufleisten:

- Vertikale Scrollleisten
- Horizontale Scrollleisten

Microsoft Excel bietet auch horizontale und vertikale Scrollleisten an, damit Benutzer durch die Inhalte des Arbeitsblatts scrollen können. Mit Aspose.Cells können Entwickler die Sichtbarkeit beider Arten von Scrollleisten in Excel-Dateien steuern.

### **Steuerung der Sichtbarkeit von Bildlaufleisten**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält eine Vielzahl von Eigenschaften und Methoden zur Verwaltung einer Excel-Datei. Um die Sichtbarkeit von Bildlaufleisten zu steuern, verwenden Sie die Eigenschaften [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) und [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) der Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) und [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) sind Boolesche Eigenschaften, was bedeutet, dass diese Eigenschaften nur **true** oder **false** Werte speichern können.

#### **Sichtbarkeit von Bildlaufleisten herstellen**

Machen Sie die Bildlaufleisten sichtbar, indem Sie die Eigenschaften [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) oder [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) der Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) auf **true** setzen.

#### **Verbergen von Bildlaufleisten**

Blenden Sie die Bildlaufleisten aus, indem Sie die Eigenschaften [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) oder [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) der Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) auf **false** setzen.

**Beispielcode**

Im Folgenden finden Sie einen vollständigen Code, der eine Excel-Datei, book1.xls, öffnet, beide Bildlaufleisten ausblendet und dann die modifizierte Datei als output.xls speichert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideScrollBars-1.cs" >}}
