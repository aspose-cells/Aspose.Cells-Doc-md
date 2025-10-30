---
title: Daten in Spalte mit benutzerdefinierter Sortierliste sortieren.
type: docs
weight: 290
url: /de/python-net/sort-data-in-column-with-custom-sort-list/
description: Erfahren Sie, wie Sie Daten in der Spalte mithilfe einer benutzerdefinierten Liste in der Aspose.Cells für Python via .NET API sortieren.
keywords: Python Excel Bibliothek, Python Daten in Spalte mit benutzerdefinierter Sortierliste sortieren, Python Daten nach benutzerdefinierter Liste sortieren
---

## **Mögliche Verwendungsszenarien**

Sie können Daten in der Spalte mit einer benutzerdefinierten Liste sortieren. Dies kann mit der Methode [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list) durchgeführt werden. Diese Methode funktioniert jedoch nur, wenn die Elemente in der benutzerdefinierten Liste keine Kommas enthalten. Wenn sie Kommas enthalten, wie z. B. "USA,US", "China,CN" usw., müssen Sie die Methode [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list) verwenden. Hier ist der letzte Parameter kein String, sondern ein Array von Zeichenfolgen.

## **Daten in Spalte mit benutzerdefinierter Sortierliste sortieren**

Der folgende Beispielcode erläutert, wie die Methode [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list) zur Sortierung von Daten mit einer benutzerdefinierten Sortierliste verwendet wird. Bitte beachten Sie die in diesem Code verwendete [Beispiel-Excel-Datei](50528327.xlsx) und die von ihm generierte [Ausgabe-Excel-Datei](50528328.xlsx). Der folgende Screenshot zeigt die Auswirkung des Codes auf die Beispiel-Excel-Datei bei der Ausführung.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SortDataInColumnWithCustomSortList.py" >}}
{{< app/cells/assistant language="python-net" >}}
