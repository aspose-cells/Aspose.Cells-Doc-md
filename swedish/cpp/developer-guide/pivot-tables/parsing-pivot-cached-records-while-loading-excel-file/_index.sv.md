---
title: Parsning av Pivot Cached Records vid laddning av Excel fil med C++
linktitle: Parsning av Pivot Cached Records
type: docs
weight: 70
url: /sv/cpp/parsing-pivot-cached-records-while-loading-excel-file/
description: Lär dig hur du parsar pivot cacheade poster vid laddning av Excel filer med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

När du skapar en pivottabell tar Microsoft Excel en kopia av källdata och lagrar den i Pivot Cache. Pivot Cache hålls i minnet i Microsoft Excel. Du kan inte se den, men det är datan som pivottabellen hänvisar till när du bygger din pivottabell eller ändrar en Slicer-val eller flyttar rader/kolumner. Detta gör att Microsoft Excel kan vara mycket reaktivt på förändringar i pivottabellen, men det kan också dubbla storleken på din fil. Trots allt är Pivot Cache bara en kopia av din källdata så det är logiskt att din filstorlek kommer att vara potentiellt dubblerad.

När du laddar din Excel-fil i Workbook-objektet kan du bestämma om du också vill ladda Pivot Cache-poster eller inte med hjälp av [**LoadOptions.GetParsingPivotCachedRecords()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getparsingpivotcachedrecords/)-egenskapen. Standardvärdet för denna egenskap är **false**. Om Pivot Cache är ganska stor kan det öka prestandan. Men om du också vill ladda Pivot Cache-poster bör du ställa in denna egenskap som **true**.

## **Dekodning Pivot Cache-poster vid inläsning av Excel-fil**

Följande exempelkod förklarar användningen av [**LoadOptions.GetParsingPivotCachedRecords()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getparsingpivotcachedrecords/)-egenskapen. Den laddar den [provpå Excel-filen](61767773.xlsx) samtidigt som den dekoderar de pivot-cache-posterna. Därefter uppdaterar den pivotabell och sparar den som [utdata Excel-fil](61767774.xlsx).

## **Exempelkod**

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
