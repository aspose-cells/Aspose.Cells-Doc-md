---
title: Daten sortieren
type: docs
weight: 130
url: /de/net/sort-data-of-excel/
description: Erfahren Sie, wie Sie Daten mit der API Aspose.Cells for .NET sortieren.
keywords: Sortieren Sie Daten in aufsteigender oder absteigender Reihenfolge, sortieren Sie Daten basierend auf der Hintergrundfarbe
---

{{% alert color="primary" %}}

Die Datensortierung ist eine der vielen nützlichen Funktionen von Microsoft Excel. Benutzer können Daten zur einfacheren Überprüfung sortieren. Aspose.Cells ermöglicht Entwicklern, Tabellendaten alphabetisch oder numerisch zu sortieren, was genauso funktioniert wie Microsoft Excel, um Daten zu sortieren.

{{% /alert %}}

## **Daten sortieren in Microsoft Excel**

Um Daten in Microsoft Excel zu sortieren:

1. Wählen Sie **Daten** im **Sortieren**-Menü aus. Der Sortieren-Dialog wird angezeigt.
1. Wählen Sie eine Sortieroption aus.

Im Allgemeinen wird das Sortieren auf einer Liste durchgeführt - definiert als eine zusammenhängende Gruppe von Daten, bei der die Daten in Spalten angezeigt werden.

## **Daten mit Aspose.Cells sortieren**

Aspose.Cells bietet die [**DataSorter**](https://reference.aspose.com/cells/net/aspose.cells/datasorter)-Klasse zur Sortierung von Daten in aufsteigender oder absteigender Reihenfolge. Die Klasse hat einige wichtige Elemente, wie z.B. Eigenschaften wie Key1 ... Key3 und Order1 ... Order3. Diese Elemente werden verwendet, um sortierte Schlüssel zu definieren und die Sortierreihenfolge des Schlüssels anzugeben.

Sie müssen Schlüssel definieren und die Sortierreihenfolge festlegen, bevor Sie das Daten sortieren implementieren. Die Klasse bietet die [**Sort**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/sort/index)-Methode, die verwendet wird, um Daten nach den Zelldaten in einem Arbeitsblatt zu sortieren.

Die [**Sort**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/sort/methods/1)-Methode akzeptiert die folgenden Parameter:

- [**Aspose.Cells.Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), die Zellen für das zugrunde liegende Arbeitsblatt.
- [**Aspose.Cells.CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea), der Bereich von Zellen. Definieren Sie den Zellenbereich, bevor Sie das Daten sortieren anwenden.

In diesem Beispiel wird die Vorlagendatei "Buch1.xls" verwendet, die in Microsoft Excel erstellt wurde. Nach Ausführen des unten stehenden Codes wird die Daten entsprechend sortiert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-DataSorting-1.cs" >}}

{{% alert color="primary" %}}

Wenn Sie *Von links nach rechts sortieren* möchten, verwenden Sie das [**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortlefttoright)-Attribut.

{{% /alert %}}

### **Daten mit Hintergrundfarbe sortieren**

Excel bietet Funktionen zur Sortierung von Daten basierend auf der Hintergrundfarbe. Die gleiche Funktion wird mit Aspose.Cells über den DataSorter bereitgestellt, in dem [**SortOnType**](https://reference.aspose.com/cells/net/aspose.cells/sortontype).CellColor in [**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey) verwendet werden kann, um Daten basierend auf der Hintergrundfarbe zu sortieren. Alle Zellen, die die angegebene Farbe in der [**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey)-Funktion enthalten, werden oben oder unten platziert, je nach Einstellung von SortOrder, und die Reihenfolge der restlichen Zellen wird überhaupt nicht geändert.

Hier sind die Beispiel Dateien, die heruntergeladen werden können, um diese Funktion zu testen:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithBackgroundColor-1.cs" >}}

## **Erweiterte Themen**
- [Daten in Spalte mit benutzerdefinierter Sortierliste sortieren](/cells/de/net/sort-data-in-column-with-custom-sort-list/)
- [Spezifizieren von Sortierwarnungen beim Sortieren von Daten](/cells/de/net/specifying-sort-warning-while-sorting-data/)
