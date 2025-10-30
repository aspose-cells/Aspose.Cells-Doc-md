---
title: Låsa VBA projektet med ett lösenord i Excel arbetsbok med C++
linktitle: Lösenordsskydda VBA projektet i Excel arbetsboken
type: docs
weight: 10
url: /sv/cpp/password-protect-the-vba-project-of-excel-workbook/
description: Lär dig hur du skyddar VBA projektet i en Excel arbetsbok med lösenord med Aspose.Cells och C++.
---

## **Lås VBA-projektet i Excel-arbetsboken med lösenord i C++**

Du kan låsa VBA (Visual Basic for Applications) projektet i en arbetsbok med Aspose.Cells med [**VbaProject.Protect()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/protect/)-metoden.

## **Exempelkod**

Följande exempel laddar den [exempel-Excel-filen](43352067.xlsm), får åtkomst till dess VBA-projekt och skyddar det med ett lösenord. Slutligen sparar den den som [utdata Excel-fil](43352068.xlsm).

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
{{< app/cells/assistant language="cpp" >}}
