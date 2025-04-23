---
title: Parsing von Pivot Cache Datensätzen beim Laden der Excel Datei mit C++
linktitle: Parsing von Pivot Cache Datensätzen
type: docs
weight: 70
url: /de/cpp/parsing-pivot-cached-records-while-loading-excel-file/
description: Erfahren Sie, wie Sie Pivot Cache Datensätze beim Laden von Excel Dateien mit Aspose.Cells for C++ analysieren.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie eine Pivot-Tabelle erstellen, erstellt Microsoft Excel eine Kopie der Quelldaten und speichert sie im Pivot-Cache. Der Pivot-Cache befindet sich im Speicher von Microsoft Excel. Sie können ihn nicht sehen, aber das sind die Daten, auf die die Pivot-Tabelle Bezug nimmt, wenn Sie Ihre Pivot-Tabelle erstellen oder eine Slicer-Auswahl ändern oder Zeilen/Spalten verschieben. Dies ermöglicht es Microsoft Excel, sehr schnell auf Änderungen in der Pivot-Tabelle zu reagieren, aber es kann auch die Größe Ihrer Datei verdoppeln. Immerhin ist der Pivot-Cache nur eine Kopie Ihrer Quelldaten, so dass es sinnvoll ist, dass die Dateigröße potenziell verdoppelt wird.

Wenn Sie Ihre Excel-Datei im Workbook-Objekt laden, können Sie entscheiden, ob Sie auch die Datensätze des Pivot-Cache laden möchten oder nicht, indem Sie die Eigenschaft [**LoadOptions.GetParsingPivotCachedRecords()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getparsingpivotcachedrecords/) verwenden. Der Standardwert dieser Eigenschaft ist **false**. Wenn der Pivot-Cache ziemlich groß ist, kann dies die Leistung verbessern. Wenn Sie jedoch auch die Datensätze des Pivot-Cache laden möchten, sollten Sie diese Eigenschaft auf **true** setzen.

## **Analysieren von Pivot-Cached-Datensätzen beim Laden der Excel-Datei**

Der folgende Beispielcode erläutert die Verwendung der Eigenschaft [**LoadOptions.GetParsingPivotCachedRecords()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getparsingpivotcachedrecords/). Er lädt die [Beispieldatei Excel](61767773.xlsx) beim Analysieren der Pivot-Cached-Datensätze. Anschließend aktualisiert er die Pivot-Tabelle und speichert sie als [Ausgabedatei Excel](61767774.xlsx).

## **Beispielcode**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create load options
    LoadOptions options;

    // Set ParsingPivotCachedRecords true, default value is false
    options.SetParsingPivotCachedRecords(true);

    // Load the sample Excel file containing pivot table cached records
    U16String inputFilePath = srcDir + u"sampleParsingPivotCachedRecordsWhileLoadingExcelFile.xlsx";
    Workbook wb(inputFilePath, options);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first pivot table
    PivotTable pt = ws.GetPivotTables().Get(0);

    // Set refresh data flag true
    pt.SetRefreshDataFlag(true);

    // Refresh and calculate pivot table
    pt.RefreshData();
    pt.CalculateData();

    // Set refresh data flag false
    pt.SetRefreshDataFlag(false);

    // Save the output Excel file
    U16String outputFilePath = outDir + u"outputParsingPivotCachedRecordsWhileLoadingExcelFile.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Pivot table cached records parsed and refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
