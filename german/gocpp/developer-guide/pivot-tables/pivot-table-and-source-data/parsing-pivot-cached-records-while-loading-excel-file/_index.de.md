---
title: Pivot Cached Records beim Laden der Excel Datei mit Golang via C++ parsen
linktitle: Parsing von Pivot Cache Datensätzen
type: docs
weight: 70
url: /de/go-cpp/parsing-pivot-cached-records-while-loading-excel-file/
description: Erfahren Sie, wie Sie Pivot Cache Datensätze beim Laden von Excel Dateien mit Aspose.Cells for C++ analysieren.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie eine Pivot-Tabelle erstellen, erstellt Microsoft Excel eine Kopie der Quelldaten und speichert sie im Pivot-Cache. Der Pivot-Cache befindet sich im Speicher von Microsoft Excel. Sie können ihn nicht sehen, aber das sind die Daten, auf die die Pivot-Tabelle Bezug nimmt, wenn Sie Ihre Pivot-Tabelle erstellen oder eine Slicer-Auswahl ändern oder Zeilen/Spalten verschieben. Dies ermöglicht es Microsoft Excel, sehr schnell auf Änderungen in der Pivot-Tabelle zu reagieren, aber es kann auch die Größe Ihrer Datei verdoppeln. Immerhin ist der Pivot-Cache nur eine Kopie Ihrer Quelldaten, so dass es sinnvoll ist, dass die Dateigröße potenziell verdoppelt wird.

Wenn Sie Ihre Excel-Datei im Workbook-Objekt laden, können Sie entscheiden, ob Sie auch die Datensätze des Pivot-Cache laden möchten oder nicht, indem Sie die Eigenschaft [**LoadOptions.GetParsingPivotCachedRecords()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getparsingpivotcachedrecords/) verwenden. Der Standardwert dieser Eigenschaft ist **false**. Wenn der Pivot-Cache ziemlich groß ist, kann dies die Leistung verbessern. Wenn Sie jedoch auch die Datensätze des Pivot-Cache laden möchten, sollten Sie diese Eigenschaft auf **true** setzen.

## **Analysieren von Pivot-Cached-Datensätzen beim Laden der Excel-Datei**

Der folgende Beispielcode erläutert die Verwendung der Eigenschaft [**LoadOptions.GetParsingPivotCachedRecords()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getparsingpivotcachedrecords/). Er lädt die [Beispieldatei Excel](61767773.xlsx) beim Analysieren der Pivot-Cached-Datensätze. Anschließend aktualisiert er die Pivot-Tabelle und speichert sie als [Ausgabedatei Excel](61767774.xlsx).

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ParsingPivotCachedRecordsWhileLoadingExcelFile.go" >}}
