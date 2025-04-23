---
title: Analysieren von Pivot Cached Datensätzen beim Laden der Excel Datei
type: docs
weight: 100
url: /de/java/parsing-pivot-cached-records-while-loading-excel-file/
---

## **Mögliche Verwendungsszenarien**

Wenn Sie eine Pivot-Tabelle erstellen, erstellt Microsoft Excel eine Kopie der Quelldaten und speichert sie im Pivot-Cache. Der Pivot-Cache befindet sich im Speicher von Microsoft Excel. Sie können ihn nicht sehen, aber das sind die Daten, auf die die Pivot-Tabelle Bezug nimmt, wenn Sie Ihre Pivot-Tabelle erstellen oder eine Slicer-Auswahl ändern oder Zeilen/Spalten verschieben. Dies ermöglicht es Microsoft Excel, sehr schnell auf Änderungen in der Pivot-Tabelle zu reagieren, aber es kann auch die Größe Ihrer Datei verdoppeln. Immerhin ist der Pivot-Cache nur eine Kopie Ihrer Quelldaten, so dass es sinnvoll ist, dass die Dateigröße potenziell verdoppelt wird.

Beim Laden Ihrer Excel-Datei im Workbook-Objekt können Sie entscheiden, ob Sie auch die Datensätze des Pivot-Cache laden möchten oder nicht, indem Sie die Eigenschaft [**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#ParsingPivotCachedRecords) verwenden. Der Standardwert dieser Eigenschaft ist **false**. Wenn der Pivot-Cache ziemlich groß ist, kann dies die Leistung steigern. Wenn Sie jedoch auch die Datensätze des Pivot-Cache laden möchten, sollten Sie diese Eigenschaft auf **true** setzen.

## **Analysieren von Pivot-Cached-Datensätzen beim Laden der Excel-Datei**

Der folgende Beispielcode erläutert die Verwendung der Eigenschaft [**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#ParsingPivotCachedRecords). Er lädt die [Beispiel-Excel-Datei](61767786.xlsx) und parst dabei die Pivot-Cached-Datensätze. Dann aktualisiert er die Pivot-Tabelle und speichert sie als die [Ausgabe-Excel-Datei](61767785.xlsx).

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.java" >}}
{{< app/cells/assistant language="java" >}}
