---
title: Daten sortieren
type: docs
weight: 130
url: /de/nodejs-cpp/sort-data-of-excel/
description: Lernen Sie, wie man Daten mit der Aspose.Cells for Node.js via C++ API sortiert.
keywords: Sortieren Sie Daten in aufsteigender oder absteigender Reihenfolge, sortieren Sie Daten basierend auf der Hintergrundfarbe
---

{{% alert color="primary" %}}

Datensortierung ist eine der nützlichen Funktionen von Microsoft Excel. Sie ermöglicht es Nutzern, Daten geordnet zu präsentieren, um die Übersicht zu erleichtern. Aspose.Cells for Node.js via C++ erlaubt Entwicklern, Arbeitsblattdaten alphabetisch oder numerisch zu sortieren, genau wie Microsoft Excel.

{{% /alert %}}

## **Daten sortieren in Microsoft Excel**

Um Daten in Microsoft Excel zu sortieren:

1. Wählen Sie **Daten** im **Sortieren**-Menü aus. Der Sortieren-Dialog wird angezeigt.
1. Wählen Sie eine Sortieroption aus.

Im Allgemeinen wird das Sortieren auf einer Liste durchgeführt - definiert als eine zusammenhängende Gruppe von Daten, bei der die Daten in Spalten angezeigt werden.

## **Daten mit Aspose.Cells sortieren**

Aspose.Cells for Node.js via C++ bietet die [**DataSorter**](https://reference.aspose.com/cells/nodejs-cpp/datasorter) Klasse, die zum Sortieren von Daten in aufsteigender oder absteigender Reihenfolge verwendet wird. Die Klasse verfügt über wichtige Mitglieder, z.B. Eigenschaften wie Key1 ... Key3 und Order1 ... Order3. Diese Mitglieder werden genutzt, um sortierte Schlüssel zu definieren und die Sortierreihenfolge zu bestimmen.

Sie müssen Schlüssel definieren und die Sortierreihenfolge festlegen, bevor Sie das Daten sortieren implementieren. Die Klasse bietet die [**DataSorter.sort**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#sort-cells-cellarea-)-Methode, die verwendet wird, um Daten nach den Zelldaten in einem Arbeitsblatt zu sortieren.

Die [**DataSorter.sort**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#sort-cells-cellarea-)-Methode akzeptiert die folgenden Parameter:

- [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells), die Zellen für das zugrunde liegende Arbeitsblatt.
- [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea), der Bereich von Zellen. Definieren Sie den Zellenbereich, bevor Sie das Daten sortieren anwenden.

In diesem Beispiel wird die Vorlagendatei "Buch1.xls" verwendet, die in Microsoft Excel erstellt wurde. Nach Ausführen des unten stehenden Codes wird die Daten entsprechend sortiert.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataSorting-1.js" >}}

{{% alert color="primary" %}}

Wenn Sie *Von links nach rechts sortieren* möchten, verwenden Sie das [**DataSorter.setSortLeftToRight**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#setSortLeftToRight-boolean-)-Attribut.

{{% /alert %}}

### **Daten mit Hintergrundfarbe sortieren**

Excel bietet Funktionen, um Daten basierend auf der Hintergrundfarbe zu sortieren. Diese Funktion ist in Aspose.Cells for Node.js via C++ mithilfe von DataSorter vorhanden, wobei [**SortOnType**](https://reference.aspose.com/cells/nodejs-cpp/sortontype/).CellColor in [**DataSorter.addKey**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-) genutzt werden kann, um Daten nach Hintergrundfarbe zu sortieren. Alle Zellen, die eine bestimmte Farbe in der Funktion enthalten, werden je nach SortOrder-Einstellung oben oder unten platziert, wobei die Reihenfolge der restlichen Zellen unverändert bleibt.

Hier sind die Beispiel Dateien, die heruntergeladen werden können, um diese Funktion zu testen:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SortDataInColumnWithBackgroundColor-1.js" >}}

## **Erweiterte Themen**
- [Daten in Spalte mit benutzerdefinierter Sortierliste sortieren](/cells/de/nodejs-cpp/sort-data-in-column-with-custom-sort-list/)
- [Spezifizieren von Sortierwarnungen beim Sortieren von Daten](/cells/de/nodejs-cpp/specifying-sort-warning-while-sorting-data/)

