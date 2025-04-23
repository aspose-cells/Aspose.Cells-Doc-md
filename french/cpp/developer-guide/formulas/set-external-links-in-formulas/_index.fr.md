---
title: Définir des liens externes dans les formules avec C++
linktitle: Définir des liens externes dans les formules
type: docs
weight: 20
url: /fr/cpp/set-external-links-in-formulas/
description: Apprenez comment inclure des liens vers des fichiers externes dans les formules en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}} 

Parfois, il est nécessaire d'inclure des liens vers des fichiers externes dans les formules, par exemple, pour évaluer une valeur de cellule ou de plage par rapport à eux. Aspose.Cells offre cette fonctionnalité et ce document explique comment l'utiliser.

{{% /alert %}} 

Le code d'exemple ci-dessous montre comment inclure des fichiers externes dans des formules.

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
