---
title: Sätt arbetsbladets flikfärg med C++
linktitle: Ställ in färg på arbetsbladets flik
type: docs
weight: 120
url: /sv/cpp/set-worksheet-tab-color/
description: Denna artikel visar exempel kod som sätter Excel arbetsbladets flikfärg programatiskt med C++ API eller bibliotek.
keywords: Sätt färgen på Excel fliken med C++, kod för att sätta färgen på Excel fliken med C++
---

{{% alert color="primary" %}}

Aspose.Cells låter dig ändra färgen på individuella arbetsbladsflikar för att göra dem framträdande från resten. Till exempel kan du göra Utgifter röda, Försäljning gröna, Tillgångar blå, osv.

{{% /alert %}}

## **Ställa in färg på arbetsbladets flik i Microsoft Excel**
1. Högerklicka på en flik i flikarket längst ned på det aktuella arbetsbladet.
1. Välj **Flikfärg**.
1. Välj en färg från paletten.
1. Klicka på **OK**.

## **Ställa in färg på arbetsbladets flik med Aspose.Cells**
Exempelkoden nedan visar hur man ställer in flikfärg med Aspose.Cells.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"worksheettabcolor.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the book
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the tab color to red
    worksheet.SetTabColor(Color::Red());

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Worksheet tab color set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
