---
title: Sortieren Sie Daten in Spalten mit einer benutzerdefinierten Sortierliste
type: docs
weight: 290
url: /de/net/sort-data-in-column-with-custom-sort-list/
description: Erfahren Sie, wie Sie Daten in der Spalte mithilfe einer benutzerdefinierten Liste sortieren, indem Sie Aspose.Cells for .NET API verwenden.
keywords: Sort Data in Column with Custom Sort List, Sort data by custom list.
---
##  **Mögliche Nutzungsszenarien**

 Sie können die Daten in der Spalte mithilfe einer benutzerdefinierten Liste sortieren. Dies kann mit erfolgen[**DataSorter.AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2)Methode. Diese Methode funktioniert jedoch nur, wenn die Elemente in der benutzerdefinierten Liste keine Kommas enthalten. Wenn sie Kommas wie „USA,US“, „China,CN“ usw. haben, müssen Sie [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference) verwenden. aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) Methode. Hier ist der letzte Parameter kein String, sondern ein Array von Strings.

##  **Sortieren Sie Daten in Spalten mit einer benutzerdefinierten Sortierliste**

Der folgende Beispielcode erläutert die Verwendung der [**DataSorter.AddKey-Methode (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey /methods/3) Methode zum Sortieren von Daten mit einer benutzerdefinierten Sortierliste. Bitte sehen Sie sich ... an[Beispiel-Excel-Datei](50528327.xlsx) in diesem Code verwendet und[Excel-Datei ausgeben](50528328.xlsx) dadurch erzeugt. Der folgende Screenshot zeigt die Auswirkung des Codes auf die Beispiel-Excel-Datei bei der Ausführung.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

##  **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}
