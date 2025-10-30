---
title: Zeilen und Spalten ausblenden und anzeigen
type: docs
weight: 60
url: /de/python-net/hiding-and-showing-rows-and-columns/
description: Dieser Artikel zeigt, wie man Zeilen und Spalten mit der Aspose.Cells for Python via .NET API ausblendet und anzeigt.
keywords: Python Excel Bibliothek, Aspose.Cells Python Zeilen ausblenden und anzeigen, Python Spalten ausblenden und anzeigen, Python Zeilen und Spalten ausblenden, Python Zeilen und Spalten anzeigen.
---

{{% alert color="primary" %}}

Manchmal ist es sinnvoll, bestimmte Zeilen oder Spalten in einem Arbeitsblatt auszublenden und später anzuzeigen. Microsoft Excel bietet diese Funktion und auch Aspose.Cells for Python via .NET.

{{% /alert %}}

## **Steuerung der Sichtbarkeit von Zeilen und Spalten**

Aspose.Cells for Python via .NET bietet eine Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält eine [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection), die es Entwicklern ermöglicht, auf jedes Arbeitsblatt in der Excel-Datei zuzugreifen. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) bietet eine [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung, die alle Zellen im Arbeitsblatt repräsentiert. Die Sammlung [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) bietet mehrere Methoden zum Verwalten von Zeilen oder Spalten in einem Arbeitsblatt. Einige davon werden im Folgenden erläutert.

## **Wie man Zeilen und Spalten ausblendet**

Entwickler können eine Zeile oder Spalte ausblenden, indem sie die [**hide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_row/)- und [**hide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_column/)-Methoden der [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung aufrufen. Beide Methoden nehmen den Zeilen- und Spaltenindex als Parameter an, um die spezifische Zeile oder Spalte auszublenden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-HidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

Es ist auch möglich, eine Zeile oder Spalte auszublenden, indem die Zeilenhöhe oder Spaltenbreite auf 0 gesetzt wird.

{{% /alert %}}

## **Wie man Zeilen und Spalten anzeigt**

Entwickler können eine versteckte Zeile oder Spalte anzeigen, indem sie die [**unhide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_row/)- und [**unhide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_column/)-Methoden der [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung aufrufen. Beide Methoden nehmen zwei Parameter an:

- **Zeilen- oder Spaltenindex** - der Index einer Zeile oder Spalte, der verwendet wird, um die spezifische Zeile oder Spalte anzuzeigen.
- **Zeilenhöhe oder Spaltenbreite** - die Zeilenhöhe oder Spaltenbreite, die der Zeile oder Spalte nach dem Ausblenden zugewiesen wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-UnhidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

Wenn Sie eine versteckte Spalte sichtbar machen, müssen Sie sie bei Bedarf auf die zuvor zugewiesene Breite oder ursprüngliche Breite wiederherstellen, indem Sie die Spalte mit einer negativen Breite ausblenden. Zum Beispiel: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

## **Wie man mehrere Zeilen und Spalten ausblendet**

Entwickler können mehrere Zeilen oder Spalten auf einmal ausblenden, indem sie die [**hide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_rows/)- und [**hide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_columns/)-Methoden der [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-Sammlung aufrufen. Beide Methoden nehmen den Startindex der Zeile oder Spalte und die Anzahl der auszublendenden Zeilen oder Spalten als Parameter an.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

Es ist auch möglich, die [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)- und [**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows/)-Methoden der Klasse [**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns/) zu verwenden, um mehrere Zeilen und Spalten sichtbar zu machen.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
