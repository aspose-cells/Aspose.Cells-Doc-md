---
title: Frysa Första Kolumn(r) i Excel Ark med C++
linktitle: Frys kolumner
type: docs
weight: 190
url: /sv/cpp/how-to-freeze-columns-of-excel-worksheet
description: I denna artikel kommer du att lära dig hur man fryser vänstra kolumner i Excel Ark programmässigt med C++ biblioteket och Aspose.Cells API.
keywords: Frys vänstra kolumner, Frys första kolumner, Lås kolumnen(n)
---

## **Introduktion**

I denna artikel kommer vi att lära oss hur man fryser vänstra kolumn(er). När du har en stor mängd data i en rad kan du inte se de vänstra kolumnerna när du skrollar horisontellt ned över arket. Du kan frysa och låsa första kolumn(en) så att du kan se den frysta delen även när resten av datan skrollas. Du kan enkelt se rubriker i de vänstra kolumnerna.

## **Frys kolumner i Excel**

**![Frys vänster kolumn(er) i Excel](freeze-columns.png)**

1. Om du vill frysa vänstra kolumn(er), välj först kolumnen under den kolumn som ska frysas.
2. Klicka på Visa > Frysa rader.
3. Klicka på Frys Första Kolumn i rullgardinsmenyn.
4. Om du skrollar nedåt, är den första kolumnen alltid i vänster vy.

**![Frysen kolumn](frozen-columns.png)**

Som du kan se är den första kolumnen fryst, den första kolumnen är alltid låst överst i vyn när du skrollar horisontellt.

Frys Kolumner låter dig se din långa data utan att hålla koll på den första kolumnen.

## **Frys Kolumner med Aspose.Cells for C++**
Det är enkelt att frysa första kolumn(en) med Aspose.Cells for C++. 
Använd metod [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) för att frysa kolumn(er) vid den valda kolumnen.
1. Konstruera Arbetsbok för att öppna filen eller skapa en tom fil.
2. Frys den första kolumnen med Worksheet.FreezePanes() metoden.
3. Spara filen.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Freeze.xlsx");

    // Freezing panes at the second column
    workbook.GetWorksheets().Get(0).FreezePanes(u"B1", 0, 1);

    // Saving the file
    workbook.Save(u"frozen.xlsx");

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Bifogad [provkälla Excel-fil](Frys.xlsx).
