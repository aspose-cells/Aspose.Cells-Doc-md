---
title: Dölja visningen av nollvärden i kalkylbladet med C++
linktitle: Döljning av visning av nollvärden i kalkylarket
type: docs
weight: 50
url: /sv/cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: Den här artikeln visar exempel på kod som förklarar hur man programmässigt döljer nollvärden i ett Excel kalkylblad med C++ biblioteket eller API et.
keywords: dölj nollvärden i Excel kalkylbladet med C++
---

{{% alert color="primary" %}} 

Ibland måste du dölja nollvärden i ett kalkylblad. Det kan vara en personlig preferens eller en formateringsstandard.

{{% /alert %}} 

För att dölja nollvärden i ett arbetsblad i Microsoft Excel (till exempel Microsoft Excel 2003):

1. Från menyn ** Verktyg ** väljer du ** Alternativ ** och väljer sedan fliken ** Visa **.
1. Avmarkera alternativet ** Nollvärden **.
1. Klicka på **OK**.

Se följande exempelkod som visar hur man döljer nollor med Aspose.Cells.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    //Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Create a new Workbook object
    Workbook workbook(inputFilePath);

    // Get First worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Hide the zero values in the sheet
    sheet.SetDisplayZeros(false);

    // Save the workbook
    workbook.Save(srcDir + u"outputfile.out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
