---
title: Unterstützung für deutsche Lokalisierung in Named Range Formeln mit C++
linktitle: Unterstützung für das deutsche Gebietsschema in benannten Bereichsformeln
type: docs
weight: 60
url: /de/cpp/support-for-german-locale-in-named-range-formulae/
description: Erfahren Sie, wie Sie Named Range Formeln in deutscher Lokalisierung mit Aspose.Cells und C++ verarbeiten.
---

Englische Formeln werden in benannte Bereiche geschrieben. Diese Excel-Datei kann in einer Umgebung geöffnet werden, in der das System auf Deutsch eingestellt ist; jedoch wird die englische Formel ins Deutsche übersetzt. Das folgende Beispiel zeigt diese Funktion, aber es erfordert, dass Excel auf Deutsch installiert ist und das System ebenfalls auf Deutsch eingestellt ist.

Eine Beispieldatei zum Testen dieses Features kann über folgenden Link heruntergeladen werden:

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
