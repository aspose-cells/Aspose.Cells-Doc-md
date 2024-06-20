---
title: Daten in Spalte mit benutzerdefinierter Sortierliste sortieren.
type: docs
weight: 290
url: /de/net/sort-data-in-column-with-custom-sort-list/
description: Erfahren Sie, wie Sie Daten in der Spalte mithilfe einer benutzerdefinierten Liste sortieren, indem Sie die Aspose.Cells for .NET API verwenden.
keywords: Daten in Spalte mit benutzerdefinierter Sortierliste sortieren, Daten nach benutzerdefinierter Liste sortieren.
---

## **Mögliche Verwendungsszenarien**

Sie können Daten in der Spalte mithilfe einer benutzerdefinierten Liste sortieren. Dies kann mit der Methode [**DataSorter.AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2) erfolgen. Diese Methode funktioniert jedoch nur, wenn die Elemente in der benutzerdefinierten Liste keine Kommas enthalten. Wenn sie Kommas enthalten wie "USA,US", "China,CN" usw., dann müssen Sie die [**DataSorter.AddKey-Methode (Int32, SortOrder, String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) verwenden. Hier ist der letzte Parameter kein String, sondern ein Array von Strings.

## **Daten in Spalte mit benutzerdefinierter Sortierliste sortieren**

Der folgende Beispielscode erläutert die Verwendung der [**DataSorter.AddKey-Methode (Int32, SortOrder, String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) zur Sortierung von Daten mit benutzerdefinierter Sortierliste. Bitte sehen Sie sich die in diesem Code verwendete [Beispieldatei Excel](50528327.xlsx) und die [Ausgabedatei Excel](50528328.xlsx) an, die davon generiert wird. Der folgende Screenshot zeigt die Auswirkung des Codes auf die Beispieldatei Excel bei der Ausführung.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}
