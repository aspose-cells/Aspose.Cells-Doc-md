---
title: Passwortschutz für das VBA Projekt der Excel Arbeitsmappe mit C++
linktitle: Schützen Sie das VBA Projekt der Excel Arbeitsmappe mit einem Passwort
type: docs
weight: 10
url: /de/cpp/password-protect-the-vba-project-of-excel-workbook/
description: Lernen Sie, wie man das VBA Projekt einer Excel Arbeitsmappe mit Aspose.Cells in C++ passwortschützt.
---

## **Passwortschutz für das VBA-Projekt der Excel-Arbeitsmappe in C++**

Sie können das VBA (Visual Basic for Applications) Projekt einer Arbeitsmappe mit Aspose.Cells mit der [**VbaProject.Protect()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/protect/)-Methode passwortschützen.

## **Beispielcode**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](43352067.xlsm), greift auf ihr VBA-Projekt zu und schützt es mit einem Passwort. Schließlich speichert er es als [Ausgabedatei](43352068.xlsm).

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
