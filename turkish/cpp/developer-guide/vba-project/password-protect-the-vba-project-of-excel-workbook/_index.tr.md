---
title: C++ kullanarak Excel Çalışma Kitabının VBA Projesini Parola ile Koruma
linktitle: Excel Çalışma Kitabının VBA Projesini Parola Koruması
type: docs
weight: 10
url: /tr/cpp/password-protect-the-vba-project-of-excel-workbook/
description: Aspose.Cells ile C++ kullanarak bir Excel çalışma kitabının VBA Projesini parola ile korumayı öğrenin.
---

## **Excel Çalışma Kitabının VBA Projesini C++ kullanarak parola ile koruyun**

Aspose.Cells kullanarak [**VbaProject.Protect()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/protect/) yöntemiyle çalışma kitabınızın VBA (Visual Basic for Applications) Projesini parola ile koruyabilirsiniz.

## **Örnek Kod**

Aşağıdaki örnek kod, [örnek Excel dosyasını](43352067.xlsm) yükler, VBA Projesine erişir ve parola ile korur. Son olarak, onu [çıktı Excel dosyası](43352068.xlsm) olarak kaydeder.

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
