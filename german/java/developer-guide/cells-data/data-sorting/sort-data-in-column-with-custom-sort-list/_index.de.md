---
title: Daten in Spalte mit benutzerdefinierter Sortierliste sortieren
type: docs
weight: 210
url: /de/java/sort-data-in-column-with-custom-sort-list/
---
## **Mögliche Nutzungsszenarien**

Sie können Daten in der Spalte mithilfe einer benutzerdefinierten Liste sortieren. Dies kann mit erfolgen[DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)) Methode. Diese Methode funktioniert jedoch nur, wenn die Elemente in der benutzerdefinierten Liste keine Kommas enthalten. Wenn sie Kommas wie "USA, US", "China, CN" usw. enthalten, müssen Sie verwenden[DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)) Methode. Hier ist der letzte Parameter kein String, sondern ein Array von Strings.

## **Daten in Spalte mit benutzerdefinierter Sortierliste sortieren**

Der folgende Beispielcode erläutert, wie die Methode DataSorter.AddKey(int key, SortOrder order, String[]customList) verwendet wird, um Daten mit einer benutzerdefinierten Sortierliste zu sortieren. Bitte sehen Sie sich ... an[Beispiel-Excel-Datei](50528359.xlsx)in diesem Code verwendet und[Excel-Datei ausgeben](50528358.xlsx)dadurch erzeugt. Der folgende Screenshot zeigt die Auswirkung des Codes auf die Beispiel-Excel-Datei bei der Ausführung.

![todo: Bild_alt_Text](sort-data-in-column-with-custom-sort-list_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SortDataInColumnWithCustomSortList.java" >}}
