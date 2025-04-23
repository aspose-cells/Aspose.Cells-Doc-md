---
title: Proteja con contraseña el Proyecto VBA de un libro de Excel con C++
linktitle: Proteger con contraseña el proyecto VBA del libro de Excel
type: docs
weight: 10
url: /es/cpp/password-protect-the-vba-project-of-excel-workbook/
description: Aprenda cómo proteger con contraseña el Proyecto VBA de un libro de Excel usando Aspose.Cells con C++.
---

## **Proteja con contraseña el Proyecto VBA de un libro de Excel en C++**

Puede proteger con contraseña el Proyecto VBA (Visual Basic Applications) de un libro usando Aspose.Cells con el método [**VbaProject.Protect()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/protect/).

## **Código de muestra**

El siguiente código de ejemplo carga el [archivo de Excel de ejemplo](43352067.xlsm), accede a su Proyecto VBA y lo protege con una contraseña. Finalmente, lo guarda como el [archivo de Excel de salida](43352068.xlsm).

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
