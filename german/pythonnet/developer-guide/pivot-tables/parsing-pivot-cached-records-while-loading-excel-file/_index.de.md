---
title: Analysieren von zwischengespeicherten Pivot-Datensätzen beim Laden einer Excel-Datei
type: docs
weight: 70
url: /de/python-net/parsing-pivot-cached-records-while-loading-excel-file/
description: So analysieren Sie zwischengespeicherte Pivot-Datensätze beim Laden einer Excel-Datei mit Aspose.Cells for Python via .NET.
keywords: Parse Pivot Cached Records while loading Excel file.
---
##  **Mögliche Nutzungsszenarien**

Wenn Sie eine Pivot-Tabelle erstellen, erstellt Microsoft Excel eine Kopie der Quelldaten und speichert sie im Pivot-Cache. Der Pivot-Cache wird im Speicher von Microsoft Excel gespeichert. Sie können es nicht sehen, aber das sind die Daten, auf die die Pivot-Tabelle verweist, wenn Sie Ihre Pivot-Tabelle erstellen, eine Slicer-Auswahl ändern oder Zeilen/Spalten verschieben. Dadurch kann Excel sehr schnell auf Änderungen in der Pivot-Tabelle reagieren, kann aber auch die Größe Ihrer Datei verdoppeln. Schließlich ist der Pivot-Cache nur ein Duplikat Ihrer Quelldaten, sodass es sinnvoll ist, dass Ihre Dateigröße möglicherweise doppelt so groß ist.

Wenn Sie Ihre Excel-Datei in das Arbeitsmappenobjekt laden, können Sie mithilfe von entscheiden, ob Sie auch die Datensätze des Pivot-Cache laden möchten oder nicht[**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)Eigentum. Der Standardwert dieser Eigenschaft ist *false**. Wenn der Pivot-Cache recht groß ist, kann er die Leistung steigern. Wenn Sie aber auch die Datensätze des Pivot Cache laden möchten, sollten Sie diese Eigenschaft auf *true** setzen.

##  **Analysieren von zwischengespeicherten Pivot-Datensätzen beim Laden einer Excel-Datei**

Der folgende Beispielcode erläutert die Verwendung von[**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)Eigentum. Es lädt die[Beispiel-Excel-Datei](61767773.xlsx) beim Parsen der zwischengespeicherten Pivot-Datensätze. Dann aktualisiert es die Pivot-Tabelle und speichert sie als[Excel-Datei ausgeben](61767774.xlsx).

##  **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.py" >}}
