---
title: Externe Links in Formeln mit C++ setzen
linktitle: Externe Links in Formeln setzen
type: docs
weight: 20
url: /de/cpp/set-external-links-in-formulas/
description: Erfahren Sie, wie Sie mit Aspose.Cells in C++ Verweise auf externe Dateien in Formeln einschließen.
---

{{% alert color="primary" %}} 

Manchmal ist es notwendig, Links zu externen Dateien in Formeln einzuschließen, um zum Beispiel eine Zelle oder einen Bereichswert gegen sie auszuwerten. Aspose.Cells bietet diese Funktion und dieses Dokument erklärt, wie sie verwendet wird.

{{% /alert %}} 

Der nachfolgende Beispielcode zeigt, wie externe Dateien in Formeln eingebunden werden.

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
