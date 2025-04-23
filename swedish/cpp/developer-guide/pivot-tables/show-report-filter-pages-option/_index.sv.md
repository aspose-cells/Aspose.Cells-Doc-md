---
title: Visa rapportfilter sidor alternativ med C++
linktitle: Visa rapportfilter sida alternativ
type: docs
weight: 110
url: /sv/cpp/show-report-filter-pages-option/
description: Lär dig hur du aktiverar "Visa rapportfilter sidor" alternativet i pivottabeller med hjälp av Aspose.Cells for C++.
---

## **Visa rapportfilter-sideast alternativ**
Excel stöder att skapa pivottabeller, lägga till rapportfilter och aktivera "Visa rapportfilter-sidor"-alternativet. Aspose.Cells stöder också denna funktion för att aktivera "Visa rapportfilter-sidor"-alternativet på den skapade pivottabellen. Nedan visas en skärmdump som visar "Visa rapportfilter-sidor"-alternativet i Excel.

![todo:image_alt_text](show-report-filter-pages-option_1.png)

Provfil och utdatafiler kan laddas ner här för att testa provkoden:

` `[Käll-Excel-fil](81920786.xlsx) 

[Utdata Excel-fil](81920787.xlsx)

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

    // Load template file
    Workbook wb(srcDir + u"samplePivotTable.xlsx");

    // Get first pivot table in the worksheet
    PivotTable pt = wb.GetWorksheets().Get(1).GetPivotTables().Get(0);

    // Set pivot field
    pt.ShowReportFilterPage(pt.GetPageFields().Get(0));

    // Set position index for showing report filter pages
    pt.ShowReportFilterPageByIndex(pt.GetPageFields().Get(0).GetPosition());

    // Set the page field name
    pt.ShowReportFilterPageByName(pt.GetPageFields().Get(0).GetName());

    // Save the output file
    wb.Save(outDir + u"outputSamplePivotTable.xlsx");

    std::cout << "Pivot table report filter pages set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
