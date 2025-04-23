---
title: Frys Översta Rad(r) i Excel Ark med C++
linktitle: Frys rader
type: docs
weight: 190
url: /sv/cpp/how-to-freeze-rows-of-excel-worksheet
description: I denna artikel kommer du att lära dig hur man fryser översta rader i Excel Ark programmässigt med C++ biblioteket och Aspose.Cells API.
keywords: Frysta översta rader, Frysta översta raden.
---

## **Introduktion**

I denna artikel kommer vi att lära oss hur man fryser översta rad(er). När du har en stor mängd data under en gemensam rubrik kan du inte se rubriken när du skrollar nedåt i arket. Du kan frysa översta rad(er) så att du kan se den frysta delen även när resten av datan skrollas. Du kan enkelt se rubriker i de översta raderna.

## **Frysa rader i Excel**

**![Frysa översta rad(er) i Excel](Freeze-Rows.png)**

1. Om du vill frysa översta rad(er), välj först raden under den rad som ska frysas.
2. Klicka på Visa > Frysa rader.
3. I rullgardinsmenyn, klicka på Frysa översta rad.
4. Om du skrollar nedåt, är den första raden alltid i översta vyn.

**![Frysen rad](Frozen-Row.png)**

Som du kan se är den första raden fryst, och den första raden förblir alltid överst i vyn när du skrollar nedåt.

Frys Rader låter dig se dina stora data utan att förlora radetiketten.

## **Frys Rader med Aspose.Cells for C++**
Det är enkelt att frysa rad(er) med Aspose.Cells for C++. 
Använd [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)-metoden för att frysa rad(er) vid den valda raden.
1. Skapa en arbetsbok för att öppna filen eller skapa en tom fil.
2. Frys den första raden med Worksheet.FreezePanes() metoden.
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

    // Freezing panes at the cell B2
    workbook.GetWorksheets().Get(0).FreezePanes(u"A2", 1, 0);

    // Saving the file
    workbook.Save(u"frozen.xlsx");

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Bifogad [provkäll-Excel-fil](../Freeze.xlsx).
