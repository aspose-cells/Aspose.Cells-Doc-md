---
title: Analysieren von zwischengespeicherten Pivot-Datensätzen beim Laden einer Excel-Datei
type: docs
weight: 70
url: /de/net/parsing-pivot-cached-records-while-loading-excel-file/
---
## **Mögliche Nutzungsszenarien**

Wenn Sie eine Pivot-Tabelle erstellen, nimmt Microsoft Excel eine Kopie der Quelldaten und speichert sie im Pivot-Cache. Der Pivot-Cache wird im Speicher von Microsoft Excel gespeichert. Sie können es nicht sehen, aber das sind die Daten, auf die die Pivot-Tabelle verweist, wenn Sie Ihre Pivot-Tabelle erstellen oder eine Slicer-Auswahl ändern oder Zeilen/Spalten verschieben. Dadurch kann Microsoft Excel sehr gut auf Änderungen in der Pivot-Tabelle reagieren, aber es kann auch die Größe Ihrer Datei verdoppeln. Schließlich ist der Pivot-Cache nur ein Duplikat Ihrer Quelldaten, sodass es sinnvoll ist, dass Ihre Dateigröße möglicherweise doppelt so groß ist.

Wenn Sie Ihre Excel-Datei in das Workbook-Objekt laden, können Sie mithilfe von entscheiden, ob Sie auch die Datensätze des Pivot-Cache laden möchten oder nicht[**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/parsingpivotcachedrecords) Eigentum. Der Standardwert dieser Eigenschaft ist**FALSCH** . Wenn der Pivot-Cache ziemlich groß ist, kann er die Leistung steigern. Wenn Sie aber auch die Datensätze von Pivot Cache laden möchten, sollten Sie diese Eigenschaft auf setzen**Stimmt**.

## **Analysieren von zwischengespeicherten Pivot-Datensätzen beim Laden einer Excel-Datei**

Der folgende Beispielcode erläutert die Verwendung von[**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/parsingpivotcachedrecords) Eigentum. Es lädt die[Beispiel-Excel-Datei](61767773.xlsx) beim Analysieren der zwischengespeicherten Pivot-Datensätze. Dann aktualisiert es die Pivot-Tabelle und speichert sie als[Excel-Datei ausgeben](61767774.xlsx).

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.cs" >}}
