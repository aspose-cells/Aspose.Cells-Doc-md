---
title: Konvertieren Sie eine Excel-Tabelle in einen Datenbereich
type: docs
weight: 10
url: /de/python-java/convert-an-excel-table-to-a-range-of-data/
---
## **Konvertieren Sie eine Excel-Tabelle in einen Datenbereich**
Aspose.Cells for Python via Java bietet die Option, Excel-Tabellen in eine Reihe von Daten zu konvertieren. Dafür sorgt die API[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\) ) Methode. Das folgende Code-Snippet demonstriert die Verwendung von[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\))-Methode zum Konvertieren einer Excel-Tabelle in einen Datenbereich.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRange.py" >}}
## **Konvertieren Sie eine Excel-Tabelle in einen Bereich mit Optionen**
Sie können beim Konvertieren einer Tabelle in einen Bereich mit zusätzliche Optionen bereitstellen[TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) Klasse. Sie können eine Instanz von übergeben[TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions)Klasse zum[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(com.aspose.cells.TableToRangeOptions\))-Methode, um zusätzliche Optionen anzugeben. Das folgende Code-Snippet demonstriert die Verwendung von[TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions)Klasse, um den letzten Zeilenindex der Tabelle festzulegen. Die Tabellenformatierung wird bis zum angegebenen Zeilenindex beibehalten und die restliche Formatierung wird entfernt.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRangeWithOptions.py" >}}
