---
title: Ställ in områdegräns med C++
type: docs
weight: 600
url: /sv/cpp/set-range-border/
description: Lär dig hur man sätter områdegränser med Aspose.Cells i C++.
---

## **Möjliga användningsscenario**
När du vill sätta gränsen för ett område behöver du inte ange varje cell individuellt. Du kan ställa in gränsen på hela området. Aspose.Cells erbjuder denna funktion. Denna artikel ger ett exempel på hur man använder Aspose.Cells för att sätta områdegräns.

## **Ange intervallsram i Excel**
För att ställa in gränsen för en serie i Excel kan du följa dessa steg:
1. Välj det cellområde där du vill tillämpa gränsen.
2. I fliken "Start" på menyfliksområdet, leta upp gruppen "Teckenformat".
3. Inom gruppen "Teckenformat", klicka på knappen "Gränser".
<br>
<img src="border.png" />
4. Välj den typ av gräns som du vill använda från alternativen i rullgardinsmenyn. Du kan välja mellan förinställda gränstyper eller anpassa din egen gräns.
5. När du har valt önskad gränstil kommer gränsen att appliceras på det valda cellområdet.

## **Ställ in gränslinje med hjälp av Aspose.Cells**
Detta exempel visar hur man:

1. Skapa en arbetsbok.
2. Lägg till data i celler i första kalkylbladet.
3. Skapa en [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range).
4. Sätt inre gräns för område.
5. Sätt yttergräns för område.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new Workbook object
    Workbook workbook;

    // Obtain the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
    Cell cell = cells.Get("A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get("B1");
    cell.PutValue(u"Count");
    cell = cells.Get("C1");
    cell.PutValue(u"Price");

    cell = cells.Get("A2");
    cell.PutValue(u"Apple");
    cell = cells.Get("A3");
    cell.PutValue(u"Mango");
    cell = cells.Get("A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get("A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get("B2");
    cell.PutValue(5);
    cell = cells.Get("B3");
    cell.PutValue(3);
    cell = cells.Get("B4");
    cell.PutValue(6);
    cell = cells.Get("B5");
    cell.PutValue(4);

    cell = cells.Get("C2");
    cell.PutValue(5);
    cell = cells.Get("C3");
    cell.PutValue(20);
    cell = cells.Get("C4");
    cell.PutValue(30);
    cell = cells.Get("C5");
    cell.PutValue(60);

    // Create a range (A1:C5)
    Range range = cells.CreateRange(u"A1", u"C5");

    // Set inner border of range
    CellsColor innerColor = workbook.CreateCellsColor();
    innerColor.SetColor(Color::Red());
    range.SetInsideBorders(BorderType::Vertical, CellBorderType::Thin, innerColor);
    innerColor.SetColor(Color::Green());
    range.SetInsideBorders(BorderType::Horizontal, CellBorderType::Thin, innerColor);

    // Set outer border of range
    CellsColor outerColor = workbook.CreateCellsColor();
    outerColor.SetColor(Color::Blue());
    range.SetOutlineBorders(CellBorderType::Thin, outerColor);

    // Save the Workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
