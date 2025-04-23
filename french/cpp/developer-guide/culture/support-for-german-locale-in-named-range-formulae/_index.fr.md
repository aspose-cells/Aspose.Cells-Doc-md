---
title: Prise en charge de la localisation allemande dans les formules de plage nommée avec C++
linktitle: Prise en charge de l allemand dans les formules de plage nommée
type: docs
weight: 60
url: /fr/cpp/support-for-german-locale-in-named-range-formulae/
description: Apprenez comment gérer les formules de plages nommées en locale allemande en utilisant Aspose.Cells avec C++.
---

Les formules en anglais sont écrites dans des régions nommées. Ce fichier Excel peut être ouvert dans un environnement où le système est configuré en locale allemande ; cependant, la formule en anglais sera traduite en allemand. L'exemple suivant illustre cette fonctionnalité, mais il nécessite que Excel soit installé en allemand et que la locale du système soit également réglée en allemand.

Un fichier d'exemple pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant:

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
