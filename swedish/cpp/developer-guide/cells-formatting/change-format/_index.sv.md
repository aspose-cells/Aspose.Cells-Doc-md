---
title: Ändra formatet på en cell med C++
linktitle: Ändra formatet på en cell
description: Hur man använder Aspose.Cells biblioteket i C++ för att ändra formatering av celler, inklusive tecken, färg, ram osv. Genom att justera dessa egenskaper får du mer kontroll över hur cellerna ser ut och framhävs.
keywords: Aspose.Cells, cellformatering, C++, teckensnitt, färg, ram
type: docs
weight: 20
url: /sv/cpp/how-to-change-format-of-cell/
---

## **Möjliga användningsscenario**
När du vill markera viss data kan du ändra stilen på cellerna.

## **Hur man ändrar formatet på en cell i Excel**

För att ändra formatet på en enda cell i Excel, följ dessa steg:

1. Öppna Excel och öppna arbetsboken som innehåller den cell du vill formatera.

2. Leta reda på den cell du vill formatera.

3. Högerklicka på cellen och välj "Formatera celler" från snabbmenyn. Alternativt kan du markera cellen och gå till fliken Hem i Excel-ribbonen, klicka på rullgardinsmenyn "Formatera" i gruppen "Celler" och välj "Formatera celler".

4. Dialogrutan "Formatera celler" visas. Här kan du välja olika formateringsalternativ att tillämpa på den valda cellen. Till exempel kan du ändra typsnittsstil, typsnittstorlek, typsnittsfärg, nummerformat, kanter, bakgrundsfärg, etc. Utforska de olika flikarna i dialogrutan för att komma åt olika formateringsalternativ.

5. Efter att ha gjort önskade formateringsändringar klickar du på "OK"-knappen för att tillämpa formateringen på den valda cellen.

## **Hur man ändrar formatet på en cell med C++**

För att ändra formatet på en cell med Aspose.Cells kan du använda följande metoder:
1. [Cell.SetStyle(Style style)](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)
2. [Cell.SetStyle(Style style, bool explicitFlag)](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)
3. [Cell.SetStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)

## **Exempelkod**
I det här exemplet skapar vi en Exceldatabok, lägger till lite provdata, får åtkomst till det första kalkylarket och får två celler ("A2" och "B3"). Sedan får vi stilen på cellen, ställer in olika formateringsalternativ (t.ex. typsnittsfärg, fetstil) och ändrar formatet på cellen. Slutligen sparar vi arbetsboken till en ny fil.
![todo:image_alt_text](change-format.png)

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");
    cell = cells.Get(u"C1");
    cell.PutValue(u"Price");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);

    cell = cells.Get(u"C2");
    cell.PutValue(5);
    cell = cells.Get(u"C3");
    cell.PutValue(20);
    cell = cells.Get(u"C4");
    cell.PutValue(30);
    cell = cells.Get(u"C5");
    cell.PutValue(60);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cell a2 = worksheet.GetCells().Get(u"A2");
    Style style = a2.GetStyle();
    style.GetFont().SetColor(Color::Red());
    style.GetFont().SetIsBold(true);

    StyleFlag flag;
    flag.SetFontColor(true);
    a2.SetStyle(style, flag);

    Cell b3 = worksheet.GetCells().Get(u"B3");
    Style style2 = b3.GetStyle();
    style2.GetFont().SetColor(Color::Blue());
    style2.GetFont().SetIsItalic(true);
    b3.SetStyle(style2);

    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
