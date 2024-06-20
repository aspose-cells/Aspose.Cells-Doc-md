---
title: Konvertieren einer Excel Tabelle in einen Datenbereich
type: docs
weight: 10
url: /de/python-java/convert-an-excel-table-to-a-range-of-data/
---

## **Konvertieren einer Excel-Tabelle in einen Datenbereich**
Aspose.Cells für Python via Java bietet die Möglichkeit, eine Excel-Tabelle in einen Datenbereich zu konvertieren. Dafür bietet die API die Methode [ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)). Der folgende Codeausschnitt zeigt die Verwendung der Methode [ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)) zur Konvertierung einer Excel-Tabelle in einen Datenbereich.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRange.py" >}}
## **Konvertieren einer Excel-Tabelle in einen Bereich mit Optionen**
Sie können zusätzliche Optionen angeben, während Sie eine Tabelle in einen Bereich mit der Klasse [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) konvertieren. Sie können eine Instanz der Klasse [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) an die Methode [ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(com.aspose.cells.TableToRangeOptions\)) übergeben, um zusätzliche Optionen anzugeben. Der folgende Codeausschnitt zeigt die Verwendung der Klasse [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) zum Festlegen des letzten Zeilenindexes der Tabelle. Die Tabellenformatierung bleibt bis zum angegebenen Zeilenindex erhalten und der Rest der Formatierung wird entfernt.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRangeWithOptions.py" >}}
