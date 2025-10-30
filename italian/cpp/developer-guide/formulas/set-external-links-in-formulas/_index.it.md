---
title: Impostare i collegamenti esterni nelle formule con C++
linktitle: Imposta collegamenti esterni nelle formule
type: docs
weight: 20
url: /it/cpp/set-external-links-in-formulas/
description: Impara come includere collegamenti a file esterni nelle formule usando Aspose.Cells con C++.
---

{{% alert color="primary" %}} 

A volte è necessario includere collegamenti a file esterni nelle formule, ad esempio, per valutare un valore di cella o intervallo contro di essi. Aspose.Cells fornisce questa funzionalità e questo documento spiega come utilizzarla.

{{% /alert %}} 

Il codice di esempio qui sotto mostra come includere file esterni nelle formule.

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
{{< app/cells/assistant language="cpp" >}}
