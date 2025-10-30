---
title: Formatera intervall med C++
linktitle: Formatera områden
type: docs
weight: 105
url: /sv/cpp/how-to-format-a-range/
description: Lär dig hur man formaterar intervall i Excel med Aspose.Cells och C++. Tillämpa stilar, fonter och färger på cellområden programmässigt.
---

## **Möjliga användningsscenario**
När du behöver tillämpa en stil på ett område kan du använda områdesformatering.

## **Hur man formaterar ett område i Excel**

För att formatera ett område med celler i Excel kan du använda de inbyggda formateringsalternativen som tillhandahålls av Excel. Så här kan du formatera en område med celler direkt i Excel:

1. Öppna Excel och öppna arbetsboken som innehåller det område du vill formatera.

2. Välj det område med celler som du vill formatera. Du kan klicka och dra för att markera området, eller så kan du använda tangentbordsgenvägar som Skift + Piltangenter för att utöka markeringen.

3. När området är markerat högerklickar du på det markerade området och väljer "Formatera celler" från snabbmenyn. Alternativt kan du gå till fliken Start i Excel-ribbonen, klicka på rullgardinsmenyn "Format" i gruppen "Celler" och välja "Formatera celler".

4. Dialogrutan "Formatera celler" visas. Här kan du välja olika formateringsalternativ att tillämpa på det markerade området. Till exempel kan du ändra teckensnittsstil, teckenstorlek, teckenfärg, nummerformat, linjer, bakgrundsfärg, etc. Utforska de olika flikarna i dialogrutan för att komma åt olika formateringsalternativ.

5. Efter att ha gjort de önskade formateringsändringarna klickar du på "OK"-knappen för att tillämpa formateringen på det markerade området.

## **Hur man formaterar ett intervall med C++**

För att formatera ett intervall med Aspose.Cells kan du använda följande metoder:
1. [Range.ApplyStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/)
2. [Range.SetStyle(Style style)](https://reference.aspose.com/cells/cpp/aspose.cells/range/setstyle/)

## **Exempelkod**
I detta exempel skapar vi ett Excel-arbetsbok, lägger till några exempeldata, får tillgång till det första kalkylbladet och definierar två intervall ("A1:C3" och "A4:C5" ). Sedan skapar vi nya stilar, sätter olika formateringsalternativ (t.ex. fontfärg, fetstil) och tillämpar stilen på intervallet. Slutligen sparar vi arbetsboken till en ny fil.
<br>
![todo:image_alt_text](format-range.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
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

    Range range = worksheet.GetCells().CreateRange(u"A1:C3");
    Style style = workbook.CreateStyle();
    style.GetFont().SetColor(Color::Red());
    style.GetFont().SetIsBold(true);

    StyleFlag flag;
    flag.SetFont(true);
    range.ApplyStyle(style, flag);

    Range range2 = worksheet.GetCells().CreateRange(u"A4:C5");
    Style style2 = workbook.CreateStyle();
    style2.GetFont().SetColor(Color::Blue());
    style2.GetFont().SetIsItalic(true);
    range2.SetStyle(style2);

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
