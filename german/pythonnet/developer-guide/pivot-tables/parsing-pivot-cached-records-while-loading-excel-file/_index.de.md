---
title: Analysieren von Pivot Cached Datensätzen beim Laden der Excel Datei
type: docs
weight: 70
url: /de/python-net/parsing-pivot-cached-records-while-loading-excel-file/
description: Wie man zwischengespeicherte Pivot Datensätze beim Laden der Excel Datei mit Aspose.Cells für Python via .NET analysiert.
keywords: Aspose.Cells für Python Excel, Excel Python Bibliothek, Wie man zwischengespeicherte Pivot Datensätze beim Laden der Excel Datei mit Hilfe der Aspose.Cells für Python Excel Bibliothek analysiert.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie eine Pivot-Tabelle erstellen, erstellt Microsoft Excel eine Kopie der Quelldaten und speichert sie im Pivot-Cache. Der Pivot-Cache befindet sich im Speicher von Microsoft Excel. Sie können ihn nicht sehen, aber das sind die Daten, auf die die Pivot-Tabelle Bezug nimmt, wenn Sie Ihre Pivot-Tabelle erstellen oder eine Slicer-Auswahl ändern oder Zeilen/Spalten verschieben. Dies ermöglicht es Microsoft Excel, sehr schnell auf Änderungen in der Pivot-Tabelle zu reagieren, aber es kann auch die Größe Ihrer Datei verdoppeln. Immerhin ist der Pivot-Cache nur eine Kopie Ihrer Quelldaten, so dass es sinnvoll ist, dass die Dateigröße potenziell verdoppelt wird.

Wenn Sie Ihre Excel-Datei im Workbook-Objekt laden, können Sie entscheiden, ob Sie auch die Datensätze des Pivot-Cache laden möchten oder nicht, indem Sie die Eigenschaft [**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/) verwenden. Der Standardwert dieser Eigenschaft ist **false**. Wenn der Pivot-Cache ziemlich groß ist, kann dies die Leistung verbessern. Wenn Sie jedoch auch die Datensätze des Pivot-Cache laden möchten, sollten Sie diese Eigenschaft auf **true** setzen.

## **Wie man zwischengespeicherte Pivot-Datensätze beim Laden der Excel-Datei analysiert**

Der folgende Beispielcode erläutert die Verwendung der Eigenschaft [**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/). Er lädt die [Beispieldatei Excel](61767773.xlsx) beim Analysieren der Pivot-Cached-Datensätze. Anschließend aktualisiert er die Pivot-Tabelle und speichert sie als [Ausgabedatei Excel](61767774.xlsx).

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.py" >}}
{{< app/cells/assistant language="python-net" >}}
