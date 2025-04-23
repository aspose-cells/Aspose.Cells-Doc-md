---
title: Защитите паролем проект VBA книги Excel с помощью C++
linktitle: Защита паролем проекта VBA книги Excel
type: docs
weight: 10
url: /ru/cpp/password-protect-the-vba-project-of-excel-workbook/
description: Узнайте, как защитить проект VBA книги Excel паролем с помощью Aspose.Cells и C++.
---

## **Защитите паролем проект VBA книги Excel на C++**

Вы можете защитить проект VBA (Visual Basic for Applications) книги паролем с помощью Aspose.Cells, используя метод [**VbaProject.Protect()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/protect/).

## **Образец кода**

Следующий пример кода загружает [пример файла Excel](43352067.xlsm), получает доступ к его проекту VBA и защищает его паролем. В конце он сохраняет его как [выходной файл Excel](43352068.xlsm).

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
