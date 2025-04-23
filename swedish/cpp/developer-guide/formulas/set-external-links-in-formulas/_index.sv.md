---
title: Ställ in externa länkar i formler med C++
linktitle: Ange externa länkar i formler
type: docs
weight: 20
url: /sv/cpp/set-external-links-in-formulas/
description: Lär dig hur du inkluderar länkar till externa filer i formler med Aspose.Cells och C++.
---

{{% alert color="primary" %}} 

Ibland är det nödvändigt att inkludera länkar till externa filer i formler, till exempel för att utvärdera en cell- eller områdesvärde mot dem. Aspose.Cells tillhandahåller denna funktion och detta dokument förklarar hur man använder den.

{{% /alert %}} 

Det exempelkod nedan visar hur du inkluderar externa filer i formler.

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

    // Instantiate a new Workbook
    Workbook workbook;

    // Get first Worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get Cells collection
    Cells cells = sheet.GetCells();

    // Set formula with external links
    cells.Get(u"A1").SetFormula(U16String(u"=SUM('[") + srcDir + u"book1.xlsx]Sheet1'!A2, '[" + srcDir + u"book1.xlsx]Sheet1'!A4)");

    // Set formula with external links
    cells.Get(u"A2").SetFormula(U16String(u"='[") + srcDir + u"book1.xlsx]Sheet1'!A8");

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully with external links!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
