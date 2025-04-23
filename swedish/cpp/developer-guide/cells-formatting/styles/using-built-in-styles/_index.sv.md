---
title: Använd inbyggda stilar med C++
linktitle: Användning av inbyggda stilar
type: docs
weight: 80
url: /sv/cpp/using-built-in-styles/
description: C++ kod för att använda Excels inbyggda stilar med Aspose.Cells for C++ API
keywords: c++ använd excel inbyggda stilar, c++ programmatiskt tillämpa stilar i arbetsbok, programmatiskt tillämpa stilar i arbetsbok, c++ tillämpa inbyggda stilar i excel, c++ tillämpa inbyggda stilar i arbetsbok, c++ kod tillämpa inbyggda stilar i arbetsbok, c++ kod tillämpa inbyggda stilar i excel arbetsbok
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller en stor samling återanvändbara stilar för att formatera en cell i ett kalkylblad. Vi kan använda inbyggda stilar i vår arbetsbok och även skapa anpassade stilar.

{{% /alert %}}

## **Hur man använder inbyggda stilar**

Metoden [**Workbook.CreateBuiltinStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/createbuiltinstyle/) och uppräkningen [**BuiltinStyleType**](https://reference.aspose.com/cells/cpp/aspose.cells/builtinstyletype/) gör det bekvämt att använda inbyggda stilar. Här är en lista över alla möjliga inbyggda stilar:

- Tjugo_procent_Accent_1
- Tjugo_procent_Accent_2
- Tjugo_procent_Accent_3
- Tjugo_procent_Accent_4
- Tjugo procent accent 5
- Tjugo procent accent 6
- Fyrtio procent accent 1
- Fyrtio procent accent 2
- Fyrtio procent accent 3
- Fyrtio procent accent 4
- Fyrtio procent accent 5
- Fyrtio procent accent 6
- Sextio procent accent 1
- Sextio procent accent 2
- Sextio procent accent 3
- Sextio procent accent 4
- Sextio procent accent 5
- Sextio procent accent 6
- Accent 1
- Accent 2
- Accent 3
- Accent 4
- Accent 5
- Accent 6
- Dåligt
- Beräkning
- Kontrollera cell
- Komma
- Komma 1
- Valuta
- Valuta 1
- Förklarande text
- Bra
- Rubrik 1
- RUBRIK_2
- RUBRIK_3
- RUBRIK_4
- HYPERLINK
- FÖLJD_HYPERLÄNK
- INMATNING
- LÄNKAD_CELL
- NEUTRAL
- NORMAL
- NOTIS
- UTGÅNG
- PROCENT
- TITEL
- TOTAL
- VARNINGSTEXT
- RADNIVÅ
- KOLUMNIVÅ

## C++ kod för att använda inbyggda stilar

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output file paths
    U16String output1Path = srcDir + u"Output.xlsx";
    U16String output2Path = srcDir + u"Output.out.ods";

    // Create a new workbook
    Workbook workbook;

    // Create a built-in style of type Title
    Style style = workbook.CreateBuiltinStyle(BuiltinStyleType::Title);

    // Get the first worksheet and its cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Access cell A1 and set its value and style
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Aspose");
    cell.SetStyle(style);

    // Auto-fit the first column and row
    worksheet.AutoFitColumn(0);
    worksheet.AutoFitRow(0);

    // Save the workbook to the first output path
    workbook.Save(output1Path);
    std::cout << "File saved " << output1Path.ToUtf8() << std::endl;

    // Save the workbook to the second output path
    workbook.Save(output2Path);
    std::cout << "File saved " << output2Path.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
