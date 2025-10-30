---
title: Stöd för tysk lokal i namngivna omfångsformler med C++
linktitle: Stöd för tysk lokal i namnformler
type: docs
weight: 60
url: /sv/cpp/support-for-german-locale-in-named-range-formulae/
description: Lär dig att hantera namngivna omfångsformler i tysk lokal med Aspose.Cells och C++.
---

Engelska formeler skrivs in i namngivna regioner. Denna Excel-fil kan öppnas i en miljö där systemet är konfigurerat till tysk lokal; dock ska de engelska formel översättas till tyska. Följande exempel visar denna funktion, men det kräver att Excel är installerat på tyska och att systemlokalen är inställd på tyska.

En testfil för att testa den här funktionen kan laddas ner från följande länk:

[sampleNamedRangeTest.xlsm](73990165.xlsm)

```c++
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

    // Define the name and formula for the named range
    const U16String name(u"HasFormula");
    const U16String value(u"=GET.CELL(48, INDIRECT(\"ZS\",FALSE))");

    // Load the source workbook
    Workbook wbSource(srcDir + u"sampleNamedRangeTest.xlsm");

    // Get the worksheet collection
    WorksheetCollection wsCol = wbSource.GetWorksheets();

    // Add a new named range and get its index
    int32_t nameIndex = wsCol.GetNames().Add(name);

    // Get the named range by index
    Name namedRange = wsCol.GetNames().Get(nameIndex);

    // Set the formula for the named range
    namedRange.SetRefersTo(value);

    // Save the workbook with the new named range
    wbSource.Save(outDir + u"sampleOutputNamedRangeTest.xlsm");

    std::cout << "Named range added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
