---
title: Daten sortieren
type: docs
weight: 130
url: /de/python-net/sort-data-of-excel/
description: Lernen Sie, wie Sie Daten mithilfe der Aspose.Cells for for Python via .NET API sortieren.
keywords: Python Excel Bibliothek, Python Daten in aufsteigender oder absteigender Reihenfolge sortieren, Python Daten basierend auf der Hintergrundfarbe sortieren.
---

{{% alert color="primary" %}}

Das Sortieren von Daten ist eine der vielen nützlichen Funktionen von Microsoft Excel. Es ermöglicht Benutzern, Daten zu ordnen, um das Scannen zu erleichtern. Aspose.Cells für Python via .NET ermöglicht Entwicklern das Sortieren von Arbeitsblattdaten alphabetisch oder numerisch, was genauso funktioniert wie Microsoft Excel zum Sortieren von Daten.

{{% /alert %}}

## **Daten sortieren in Microsoft Excel**

Um Daten in Microsoft Excel zu sortieren:

1. Wählen Sie **Daten** im **Sortieren**-Menü aus. Der Sortieren-Dialog wird angezeigt.
1. Wählen Sie eine Sortieroption aus.

Im Allgemeinen wird das Sortieren auf einer Liste durchgeführt - definiert als eine zusammenhängende Gruppe von Daten, bei der die Daten in Spalten angezeigt werden.

## **Daten sortieren mit Aspose.Cells für Python Excel-Bibliothek**

Aspose.Cells für Python via .NET bietet die [**DataSorter**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter)-Klasse, die zum Sortieren von Daten in aufsteigender oder absteigender Reihenfolge verwendet wird. Die Klasse hat einige wichtige Elemente wie z.B. Eigenschaften wie Key1 ... Key3 und Order1 ... Order3. Diese Elemente werden verwendet, um sortierte Schlüssel zu definieren und die Schlüsselsortierreihenfolge festzulegen.

Sie müssen Schlüssel definieren und die Sortierreihenfolge festlegen, bevor Sie das Daten sortieren implementieren. Die Klasse bietet die [**sort**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort/#aspose.cells.Cells-aspose.cells.CellArea)-Methode, die verwendet wird, um Daten nach den Zelldaten in einem Arbeitsblatt zu sortieren.

Die [**sort**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort/#aspose.cells.Cells-aspose.cells.CellArea)-Methode akzeptiert die folgenden Parameter:

- [**aspose.cells.Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells), die Zellen für das zugrunde liegende Arbeitsblatt.
- [**aspose.cells.CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea), der Bereich von Zellen. Definieren Sie den Zellenbereich, bevor Sie das Daten sortieren anwenden.

In diesem Beispiel wird die Vorlagendatei "Buch1.xls" verwendet, die in Microsoft Excel erstellt wurde. Nach Ausführen des unten stehenden Codes wird die Daten entsprechend sortiert.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DataSorting-1.py" >}}

{{% alert color="primary" %}}

Wenn Sie *Von links nach rechts sortieren* möchten, verwenden Sie das [**DataSorter.sort_left_to_right**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort_left_to_right/)-Attribut.

{{% /alert %}}

### **Daten mit Hintergrundfarbe sortieren mit der Aspose.Cells für Python Excel-Bibliothek**

Excel bietet Funktionen zum Sortieren von Daten basierend auf der Hintergrundfarbe. Die gleiche Funktion wird mit Aspose.Cells für Python via .NET mittels DataSorter bereitgestellt, wobei [**SortOnType**](https://reference.aspose.com/cells/python-net/aspose.cells/sortontype/). CellColor in [**add_key()**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOnType-aspose.cells.SortOrder-any) verwendet werden kann, um Daten basierend auf der Hintergrundfarbe zu sortieren. Alle Zellen, die die angegebene Farbe in der [**add_key()**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOnType-aspose.cells.SortOrder-any)-Funktion enthalten, werden entsprechend den SortOrder-Einstellungen oben oder unten platziert, und die Reihenfolge der restlichen Zellen ändert sich überhaupt nicht.

Hier sind die Beispiel Dateien, die heruntergeladen werden können, um diese Funktion zu testen:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SortDataInColumnWithBackgroundColor-1.py" >}}

## **Erweiterte Themen**
- [Daten in Spalte mit benutzerdefinierter Sortierliste sortieren](/cells/de/python-net/sort-data-in-column-with-custom-sort-list/)
- [Spezifizieren von Sortierwarnungen beim Sortieren von Daten](/cells/de/python-net/specifying-sort-warning-while-sorting-data/)
{{< app/cells/assistant language="python-net" >}}
