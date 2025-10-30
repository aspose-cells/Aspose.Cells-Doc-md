---
title: Ange författare vid skrivskydning av kalkylblad med C++
linktitle: Ange författare vid skrivskydd av arbetsbok
type: docs
weight: 40
url: /sv/cpp/specify-author-while-write-protecting-workbook/
description: Lär dig hur du anger ett författarnamn vid skrivskydd av ett kalkylblad med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Du kan ange författarnamnet när du skriver skyddar ditt kalkylblad med Aspose.Cells API. Använd [**Workbook.GetAuthor()**](https://reference.aspose.com/cells/cpp/aspose.cells/writeprotection/getauthor/)-egenskapen för detta ändamål.

## **Ange författare vid skrivskydd av arbetsbok**

Följande kodexempel förklarar användningen av egenskapen [**Workbook.GetAuthor()**](https://reference.aspose.com/cells/cpp/aspose.cells/writeprotection/getauthor/). Koden skapar en tom arbetsbok, skriver den skyddad med ett lösenord, specificerar författarnamnet och sparar den som en [utdata Excel-fil](67338582.xlsx). Följande skärmdump visar effekten av kodexemplet på utdata Excel-filen för din referens.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **Exempelkod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create empty workbook
    Workbook wb;

    // Write protect workbook with password
    wb.GetSettings().GetWriteProtection().SetPassword(u"1234");

    // Specify author while write protecting workbook
    wb.GetSettings().GetWriteProtection().SetAuthor(u"SimonAspose");

    // Save the workbook in XLSX format
    wb.Save(outDir + u"outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx");

    std::cout << "Workbook write protected with author specified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
