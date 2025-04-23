---
title: Daten in Spalte mit benutzerdefinierter Sortierliste sortieren.
type: docs
weight: 290
url: /de/nodejs-cpp/sort-data-in-column-with-custom-sort-list/
description: Erfahren Sie, wie Sie Daten in der Spalte mithilfe einer benutzerdefinierten Liste sortieren, indem Sie die API Aspose.Cells for Node.js via C++ verwenden.
keywords: Daten in Spalte mit benutzerdefinierter Sortierliste sortieren, Daten nach benutzerdefinierter Liste sortieren.
---

## **Mögliche Verwendungsszenarien**

Sie können Daten in der Spalte mithilfe einer benutzerdefinierten Liste sortieren. Dies kann mit der Methode [**DataSorter.addKey**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-string-) erfolgen. Diese Methode funktioniert jedoch nur, wenn die Elemente in der benutzerdefinierten Liste keine Kommata enthalten. Wenn sie Kommata enthalten, z.B. "USA,US", "China,CN", müssen Sie die Methode [**DataSorter.addKey(Nummer, SortOrder, String[])**)](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-stringarray-) verwenden. Der letzte Parameter ist kein String, sondern ein Array von Strings.

## **Daten in Spalte mit benutzerdefinierter Sortierliste sortieren**

Der folgende Beispielcode erklärt, wie die Methode [**DataSorter.addKey(Nummer, SortOrder, String[])**)](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-stringarray-) verwendet wird, um Daten mit einer benutzerdefinierten Sortierung zu sortieren. Bitte sehen Sie sich die [Beispiel-Excel-Datei](50528327.xlsx) an, die in diesem Code verwendet wird, sowie die [Ausgabe-Excel-Datei](50528328.xlsx), die daraus generiert wird. Das folgende Bildschirmfoto zeigt die Auswirkung des Codes auf die Beispiel-Excel-Datei bei Ausführung.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SortDataInColumnWithCustomSortList.js" >}}

