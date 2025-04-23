---
title: Lås rutor i Excel Arbetsblad med C++
linktitle: Frysa rader
type: docs
weight: 190
url: /sv/cpp/how-to-freeze-panes-of-excel-worksheet
description: I denna artikel lär du dig hur du låser rutor i Excel Arbetsblad programmässigt med C++ Bibliotek och Aspose.Cells API.
keywords: Frys paneor, Frys fönster.
---

## **Introduktion**

I den här artikeln lär vi oss Hur man fryser paneor. När du har en stor mängd data under en gemensam rubrik kan du inte se rubriken när du scrollar ner i kalkylbladet. Och varje post innehåller mycket data. Du kan frysa paneor så att du kan se den frysta delen även när resten av datan scrollas. Du kan enkelt se rubriker i de översta raderna eller första kolumnerna. Att frysa och avfrysa paneor ändrar bara vy av datan utan att ändra själva datan.

## **I Excel**

**![Frys rader i Excel](Frys-panor.png)**

1. Om du vill frysa paneor, frysa rader och kolumner, välj först en cell (som B2).
2. Klicka på Visa > Frysa rader.
3. I rullgardinsmenyn klickar du på Frysa rader.
4. Om du scrollar ner eller till höger, är den första raden och kolumnen frysta.

**![Frysade paneor](Frozen-Panes.png)**

Som du kan se är den första raden och kolumn A frysta, den andra raden är 32, och den andra synliga kolumnen är D.

Frys fönster gör att du kan visa dina stora data utan att hålla koll på rad- eller kolumnetiketter.

## **Frys fönster med Aspose.Cells for C++**
Det är enkelt att frysa fönster med Aspose.Cells for C++. Använd [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)-metoden för att frysa fönster vid den valda cellen.
1. Skapa en arbetsbok för att öppna filen eller skapa en tom fil.
2. Frys fönster med Worksheet.FreezePanes()-metoden.
3. Spara filen.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    U16String inputFilePath(u"Freeze.xlsx");
    Workbook workbook(inputFilePath);

    // Freeze panes at the cell B2
    WorksheetCollection sheets = workbook.GetWorksheets();
    sheets.Get(0).FreezePanes(u"B2", 1, 1);

    // Save the file
    U16String outputFilePath(u"frozen.xlsx");
    workbook.Save(outputFilePath);

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Bifogad [provkälla Excel-fil](Frys.xlsx).
