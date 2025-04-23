---
title: Daten in Spalte mit benutzerdefinierter Sortierliste sortieren.
type: docs
weight: 210
url: /de/java/sort-data-in-column-with-custom-sort-list/
---

## **Mögliche Verwendungsszenarien**

Sie können Daten in der Spalte mit einer benutzerdefinierten Liste sortieren. Dies kann mit [DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey-int-int-java.lang.String-) durchgeführt werden. Diese Methode funktioniert jedoch nur, wenn die Elemente in der benutzerdefinierten Liste keine Kommas enthalten. Wenn sie Kommas enthalten, wie "USA, US", "China, CN" usw., müssen Sie die Methode [DataSorter.AddKey](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey-int-int-java.lang.String-) verwenden. Der letzte Parameter ist hier kein String, sondern ein Array von Strings.

## **Daten in Spalte mit benutzerdefinierter Sortierliste sortieren**

Der folgende Beispielscode erläutert, wie die Methode DataSorter.AddKey(int key, SortOrder order, String[] customList) verwendet wird, um Daten mit einer benutzerdefinierten Sortierliste zu sortieren. Bitte beachten Sie die für diesen Code verwendete [Beispiel-Excel-Datei](50528359.xlsx) und die von ihm generierte [Ausgabe-Excel-Datei](50528358.xlsx). Der folgende Screenshot zeigt die Auswirkung des Codes auf die Beispiel-Excel-Datei bei der Ausführung.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SortDataInColumnWithCustomSortList.java" >}}
{{< app/cells/assistant language="java" >}}
