---
title: Zeilen, Spalten und Bildlaufleisten anzeigen und ausblenden
type: docs
weight: 20
url: /de/python-net/show-and-hide-rows-columns-and-scroll-bars/
description: Dieser Artikel zeigt, wie man Zeilen und Spalten in einem Excel Arbeitsblatt mit der Aspose.Cells für Python via .NET API programmgesteuert ein und ausblendet. Die Sichtbarkeit der Bildlaufleisten kann angepasst werden, und mehrere Zeilen und Spalten können ausgeblendet werden.
keywords: Python Excel Bibliothek, Zeilen und Spalten anzeigen, Zeilen und Spalten ausblenden, Vertikale Bildlaufleiste anzeigen, Horizontale Bildlaufleiste anzeigen, Vertikale Bildlaufleiste ausblenden, Horizontale Bildlaufleiste ausblenden, Zeilen, Spalten und Bildlaufleisten anzeigen und ausblenden.
---

{{% alert color="primary" %}}

Aspose.Cells für Python via .NET bietet Möglichkeiten, die Sichtbarkeit von Zeilen, Spalten und Bildlaufleisten eines Arbeitsblatts zu steuern.

{{% /alert %}}

## **Zeilen und Spalten anzeigen und ausblenden**

Aspose.Cells für Python via .NET stellt eine Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) bereit, die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält eine [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Eine Arbeitsblatt ist durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) dargestellt. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) bietet eine [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-Sammlung, die alle Zellen im Arbeitsblatt repräsentiert. Die Sammlung [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) bietet mehrere Methoden zur Verwaltung von Zeilen oder Spalten in einem Arbeitsblatt. Einige davon werden nachfolgend erläutert.

### **Zeilen und Spalten anzeigen**

Entwickler können eine versteckte Zeile oder Spalte anzeigen, indem sie die [**unhide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_row/)- und [**unhide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_column/)-Methoden der [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/)-Sammlung aufrufen. Beide Methoden nehmen zwei Parameter an:

- **Zeilen- oder Spaltenindex** - der Index einer Zeile oder Spalte, der verwendet wird, um die spezifische Zeile oder Spalte anzuzeigen.
- **Zeilenhöhe oder Spaltenbreite** - die Zeilenhöhe oder Spaltenbreite, die der Zeile oder Spalte nach dem Ausblenden zugewiesen wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-UnhidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

Wenn Sie eine versteckte Spalte sichtbar machen, müssen Sie sie bei Bedarf auf die zuvor zugewiesene Breite oder ursprüngliche Breite wiederherstellen, indem Sie die Spalte mit einer negativen Breite ausblenden. Zum Beispiel: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Zeilen und Spalten ausblenden**

Entwickler können eine Zeile oder Spalte ausblenden, indem sie die [**hide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_row/)- und [**hide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_column/)-Methoden der [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-Sammlung aufrufen. Beide Methoden nehmen den Zeilen- und Spaltenindex als Parameter an, um die spezifische Zeile oder Spalte auszublenden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-HidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

Es ist auch möglich, eine Zeile oder Spalte auszublenden, indem die Zeilenhöhe oder Spaltenbreite auf 0 gesetzt wird.

{{% /alert %}}

### **Mehrere Zeilen und Spalten ausblenden**

Entwickler können mehrere Zeilen oder Spalten auf einmal ausblenden, indem sie die [**hide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_rows/)- und [**hide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_columns)-Methoden der [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-Sammlung aufrufen. Beide Methoden nehmen den Startindex der Zeile oder Spalte und die Anzahl der auszublendenden Zeilen oder Spalten als Parameter an.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.py" >}}

## **Bildlaufleisten einblenden und ausblenden**

Bildlaufleisten werden verwendet, um den Inhalt einer Datei zu durchsuchen. Normalerweise gibt es zwei Arten von Bildlaufleisten:

- Vertikale Scrollleisten
- Horizontale Scrollleisten

Microsoft Excel bietet auch horizontale und vertikale Bildlaufleisten, damit Benutzer durch den Inhalt des Arbeitsblatts scrollen können. Mit Aspose.Cells für Python via .NET können Entwickler die Sichtbarkeit beider Arten von Bildlaufleisten in Excel-Dateien steuern.

### **Steuerung der Sichtbarkeit von Bildlaufleisten**

Aspose.Cells für Python via .NET stellt eine Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) bereit, die eine Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung einer Excel-Datei. Um die Sichtbarkeit der Bildlaufleisten zu steuern, verwenden Sie die Eigenschaften [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) und [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) der Klasse [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible). [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) und [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) sind Boolesche Eigenschaften, was bedeutet, dass diese Eigenschaften nur **true** oder **false** speichern können.

#### **Sichtbarkeit von Bildlaufleisten herstellen**

Machen Sie die Bildlaufleisten sichtbar, indem Sie die Eigenschaften [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) oder [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) der Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) auf **true** setzen.

#### **Verbergen von Bildlaufleisten**

Blenden Sie die Bildlaufleisten aus, indem Sie die Eigenschaften [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) oder [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) der Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) auf **false** setzen.

**Beispielcode**

Im Folgenden finden Sie einen vollständigen Code, der eine Excel-Datei, book1.xls, öffnet, beide Bildlaufleisten ausblendet und dann die modifizierte Datei als output.xls speichert.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Worksheets-Display-DisplayHideScrollBars-1.py" >}}
