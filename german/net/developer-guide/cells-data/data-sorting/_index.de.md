---
title: Datensortierung
type: docs
weight: 130
url: /de/net/sort-data-of-excel/
description: Erfahren Sie, wie Sie Daten mithilfe von Aspose.Cells for .NET API sortieren.
keywords: Sort data in ascending or descending order, Sort data based on the background color
---
{{% alert color="primary" %}}

Die Datensortierung ist eine der vielen nützlichen Funktionen von Excel. Es ermöglicht Benutzern, Daten anzuordnen, um das Scannen zu erleichtern. Mit Aspose.Cells können Entwickler Arbeitsblattdaten alphabetisch oder numerisch sortieren, was auf die gleiche Weise funktioniert wie Microsoft Excel zum Sortieren von Daten.

{{% /alert %}}

##  **Sortieren von Daten in Microsoft Excel**

So sortieren Sie Daten in Microsoft Excel:

1.  Wählen**Daten** von dem**Sortieren** Speisekarte. Der Sortierdialog wird angezeigt.
1. Wählen Sie eine Sortieroption.

Im Allgemeinen wird die Sortierung anhand einer Liste durchgeführt – definiert als eine zusammenhängende Datengruppe, in der die Daten in Spalten angezeigt werden.

##  **Sortieren von Daten mit Aspose.Cells**

 Aspose.Cells bietet die[**Datensortierer**](https://reference.aspose.com/cells/net/aspose.cells/datasorter)Klasse, die zum Sortieren von Daten in aufsteigender oder absteigender Reihenfolge verwendet wird. Die Klasse verfügt über einige wichtige Mitglieder, beispielsweise Eigenschaften wie Key1 ... Key3 und Order1 ... Order3. Diese Mitglieder werden verwendet, um sortierte Schlüssel zu definieren und die Sortierreihenfolge der Schlüssel anzugeben.

 Sie müssen Schlüssel definieren und die Sortierreihenfolge festlegen, bevor Sie die Datensortierung implementieren. Die Klasse bietet die[**Sortieren**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/sort/index)Methode zum Durchführen einer Datensortierung basierend auf den Zelldaten in einem Arbeitsblatt.

 Der[**Sortieren**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/sort/methods/1)Die Methode akzeptiert die folgenden Parameter:

- [**Aspose.Cells.Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), die Zellen für das zugrunde liegende Arbeitsblatt.
- [**Aspose.Cells.CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea), der Bereich der Zellen. Definieren Sie den Zellbereich, bevor Sie die Datensortierung anwenden.

In diesem Beispiel wird die in Microsoft Excel erstellte Vorlagendatei „Book1.xls“ verwendet. Nach der Ausführung des folgenden Codes werden die Daten entsprechend sortiert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-DataSorting-1.cs" >}}

{{% alert color="primary" %}}

 Wenn Sie *LeftToRight* sortieren möchten, verwenden Sie die[**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortlefttoright) Attribut.

{{% /alert %}}

###  **Sortieren von Daten mit Hintergrundfarbe**

Excel bietet Funktionen zum Sortieren von Daten basierend auf der Hintergrundfarbe. Die gleiche Funktion wird mit Aspose.Cells unter Verwendung von DataSorter bereitgestellt[**SortOnType**](https://reference.aspose.com/cells/net/aspose.cells/sortontype) .CellColor kann in verwendet werden[**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey) um Daten basierend auf der Hintergrundfarbe zu sortieren. Alle Zellen, die die angegebene Farbe enthalten[**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey), Funktion werden entsprechend der SortOrder-Einstellung oben oder unten platziert und die Reihenfolge der restlichen Zellen wird überhaupt nicht geändert.

Im Folgenden finden Sie Beispieldateien, die zum Testen dieser Funktion heruntergeladen werden können:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[AusgabesampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithBackgroundColor-1.cs" >}}

##  **Vorabthemen**
- [Sortieren Sie Daten in Spalten mit einer benutzerdefinierten Sortierliste](/cells/de/net/sort-data-in-column-with-custom-sort-list/)
- [Angeben einer Sortierwarnung beim Sortieren von Daten](/cells/de/net/specifying-sort-warning-while-sorting-data/)
