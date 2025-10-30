---
title: Daten in Spalte mit benutzerdefinierter Sortierliste mit Golang via C++ sortieren
linktitle: Daten in Spalte mit benutzerdefinierter Sortierliste sortieren.
type: docs
weight: 290
url: /de/go-cpp/sort-data-in-column-with-custom-sort-list/
description: Erfahren Sie, wie man Daten in der Spalte mithilfe einer benutzerdefinierten Liste durch die API Aspose.Cells for C++ sortiert.
keywords: Daten in Spalte mit benutzerdefinierter Sortierliste sortieren, Daten nach benutzerdefinierter Liste sortieren.
---

## **Mögliche Verwendungsszenarien**

Sie können Daten in der Spalte mit einer benutzerdefinierten Liste sortieren. Dies kann mit [**DataSorter::AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/) Methode durchgeführt werden. Diese Methode funktioniert jedoch nur, wenn die Elemente in der benutzerdefinierten Liste keine Kommata enthalten. Falls sie Kommata wie "USA,US", "China,CN" usw. enthalten, müssen Sie die [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/) Methode verwenden. Hier ist der letzte Parameter kein String, sondern ein Array von Strings.

## **Daten in Spalte mit benutzerdefinierter Sortierliste sortieren**

Der folgende Beispielcode erklärt, wie die [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/) Methode zum Sortieren von Daten mit einer benutzerdefinierten Sortierliste verwendet wird. Bitte sehen Sie die [Beispieldatei Excel](50528327.xlsx), die in diesem Code verwendet wird, und die [Ausgabedatei Excel](50528328.xlsx), die daraus generiert wurde. Das folgende Screenshot zeigt die Wirkung des Codes auf die Beispiel-Excel-Datei bei der Ausführung.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SortDataInColumnWithCustomSortList.go" >}}
