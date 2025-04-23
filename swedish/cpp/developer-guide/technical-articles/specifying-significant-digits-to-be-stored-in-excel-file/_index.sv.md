---
title: Angivande av signifikanta siffror som ska lagras i Excel fil med C++
linktitle: Angivande av signifikanta siffror
type: docs
weight: 30
url: /sv/cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: Lär dig hur du specificerar signifikanta siffror som ska lagras i Excel filer med Aspose.Cells och C++.
---

## **Möjliga användningsscenario**

Som standard lagrar Aspose.Cells 17 signifikanta siffror av dubbelvärden inuti Excel-filen, till skillnad från MS-Excel som bara lagrar 15 signifikanta siffror. Du kan ändra Aspose.Cells standardbeteende från 17 till 15 signifikanta siffror med hjälp av [**GetSignificantDigits()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/getsignificantdigits/) egenskapen.

## **Ange signifikanta siffror som ska lagras i Excel-fil**

Följande kodsnutt tvingar Aspose.Cells att använda 15 signifikanta siffror när du lagrar dubbelvärden i Excel-filen. Kontrollera [utdata Excelfilen](22774105.xlsx). Byt ut dess extension till .zip och extrahera den, du kommer att se att endast 15 signifikanta siffror lagras i Excel-filen. Följande skärmbild förklarar effekten av [**GetSignificantDigits()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/getsignificantdigits/)-egenskapen på utdata Excel-filen.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Exempelkod**

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

    // By default, Aspose.Cells stores 17 significant digits unlike
    // MS-Excel which stores only 15 significant digits
    CellsHelper::SetSignificantDigits(15);

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell c = worksheet.GetCells().Get(u"A1");

    // Put double value, only 15 significant digits as specified by
    // CellsHelper.SignificantDigits above will be stored in excel file just like MS-Excel does
    c.PutValue(1234567890.123451711);

    // Save the workbook
    workbook.Save(outDir + u"out_SignificantDigits.xlsx");

    std::cout << "Workbook saved successfully with significant digits set to 15!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
