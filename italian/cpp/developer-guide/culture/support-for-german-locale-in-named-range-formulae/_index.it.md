---
title: Supporto per il locale tedesco nelle formule dei range nominati con C++
linktitle: Supporto per la localizzazione in tedesco nelle formule dei nomi
type: docs
weight: 60
url: /it/cpp/support-for-german-locale-in-named-range-formulae/
description: Impara come gestire le formule di range nominati in locale tedesco usando Aspose.Cells con C++.
---

Le formule in inglese sono scritte nelle regioni nominate. Questo file Excel può essere aperto in un ambiente in cui il sistema è configurato in locale tedesco; tuttavia, la formula in inglese sarà tradotta in lingua tedesca. Il seguente esempio dimostra questa funzione, ma richiede che Excel sia installato in tedesco e il locale di sistema sia impostato su tedesco anch'esso.

Un file di esempio per testare questa funzionalità può essere scaricato dal seguente link:

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
