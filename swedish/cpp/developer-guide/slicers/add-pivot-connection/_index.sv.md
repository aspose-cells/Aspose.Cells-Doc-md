---
title: Lägg till pivottabellanslutning med C++
linktitle: Lägg till pivottabellanslutning
type: docs
weight: 30
url: /sv/cpp/add-pivot-connection/
description: Lär dig hur du lägger till pivottabellanslutning med Aspose.Cells biblioteket med hjälp av C++.
keywords: Lägg till pivottabellanslutning utan Office 2013, Office 2016, Office 2019 och Office 365.
---

## **Möjliga användningsscenario**

Om du vill associera slicer och pivottabell i Excel måste du högerklicka på slicern och välja alternativet "Rapportanslutningar...". I alternativlistan kan du använda kryssrutan. På liknande sätt, om du vill associera slicer och pivottabell med hjälp av Aspose.Cells API programmatiskt, använd [**Slicer.AddPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/addpivotconnection/) metoden. Den kommer att associera slicer och pivottabell.

## **Associera slicer och Pivottabell**

Följande exempelkod laddar in den [exempel-Excel-filen](add-pivot-connection.xlsx) som innehåller en befintlig slicer. Den får åtkomst till slicern och associerar sedan slicer och pivottabell. Slutligen sparar den arbetsboken som [utdata-Excel-fil](add-pivot-connection-out.xlsx). 

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"add-pivot-connection.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"add-pivot-connection-out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    // Access the first PivotTable inside the PivotTable collection
    PivotTableCollection pivotTables = worksheet.GetPivotTables();
    PivotTable pivotTable = pivotTables.Get(0);

    // Access the first slicer inside the slicer collection
    SlicerCollection slicers = worksheet.GetSlicers();
    Slicer slicer = slicers.Get(0);

    // Add PivotTable connection
    slicer.AddPivotConnection(pivotTable);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "PivotTable connection added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
