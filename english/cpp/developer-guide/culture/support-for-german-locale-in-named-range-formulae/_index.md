---
title: Support for German Locale in Named Range Formulae with C++
linktitle: Support for German Locale in Named Range Formulae
type: docs
weight: 60
url: /cpp/support-for-german-locale-in-named-range-formulae/
description: Learn how to handle named range formulae in German locale using Aspose.Cells with C++.
---

English formulae are written into named regions. This Excel file can be opened in an environment where the system is configured to German Locale; however, the English formula shall be translated to the German language. The following example demonstrates this feature, but it requires Excel to be installed in German and the system locale to be set to German as well.

A sample file for testing this feature can be downloaded from the following link:

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