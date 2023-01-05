---
title: Daten in Spalte mit benutzerdefinierter Sortierliste sortieren
type: docs
weight: 290
url: /de/net/sort-data-in-column-with-custom-sort-list/
---
## **Mögliche Nutzungsszenarien**

 Sie können Daten in der Spalte mithilfe einer benutzerdefinierten Liste sortieren. Dies kann mit erfolgen[**DataSorter.AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2)Methode. Diese Methode funktioniert jedoch nur, wenn die Elemente in der benutzerdefinierten Liste keine Kommas enthalten. Wenn sie Kommas wie "USA,US", "China,CN" usw. enthalten, müssen Sie [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference. aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) Methode. Hier ist der letzte Parameter kein String, sondern ein Array von Strings.

## **Daten in Spalte mit benutzerdefinierter Sortierliste sortieren**

Der folgende Beispielcode erläutert die Verwendung von [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey /methods/3) Methode zum Sortieren von Daten mit benutzerdefinierter Sortierliste. Bitte sehen Sie sich die in diesem Code verwendete [Beispiel-Excel-Datei](50528327.xlsx) und die damit generierte [Excel-Ausgabedatei](50528328.xlsx) an. Der folgende Screenshot zeigt die Auswirkung des Codes auf die Beispiel-Excel-Datei bei der Ausführung.

![todo: Bild_alt_Text](sort-data-in-column-with-custom-sort-list_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}
