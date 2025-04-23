---
title: Protéger par mot de passe le projet VBA d un classeur Excel avec C++
linktitle: Protégez le mot de passe du projet VBA de Classeur Excel
type: docs
weight: 10
url: /fr/cpp/password-protect-the-vba-project-of-excel-workbook/
description: Apprenez à protéger par mot de passe le projet VBA d un classeur Excel en utilisant Aspose.Cells avec C++.
---

## **Protéger par mot de passe le projet VBA d'un classeur Excel en C++**

Vous pouvez protéger par mot de passe le projet VBA (Visual Basic for Applications) d'un classeur avec Aspose.Cells en utilisant la méthode [**VbaProject.Protect()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/protect/).

## **Code d'exemple**

Le code exemple suivant charge le [fichier Excel d'exemple](43352067.xlsm), accède à son projet VBA, et le protège avec un mot de passe. Enfin, il l'enregistre en tant que [fichier Excel de sortie](43352068.xlsm).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Vba;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"samplePasswordProtectVBAProject.xlsm";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outputPasswordProtectVBAProject.xlsm";

    // Load the source Excel file
    Workbook wb(inputFilePath);

    // Access the VBA project of the workbook
    VbaProject vbaProject = wb.GetVbaProject();

    // Lock the VBA project for viewing with password
    vbaProject.Protect(true, u"11");

    // Save the output Excel file
    wb.Save(outputFilePath);

    std::cout << "VBA project password protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
