---
title: Hantera intervall med C++
linktitle: Områden
type: docs
weight: 105
url: /sv/cpp/managing-ranges/
description: Lär dig hantera intervall i Excel filer med Aspose.Cells och C++. Skapa, ändra och formatera intervall programmatiskt.
---

## **Introduktion**

I Excel kan du markera flera celler med musen, det markerade celluppsättningen kallas "Område".

Till exempel kan du klicka med vänster musknapp i cellen "A1" i Excel och sedan dra till cellen "C4". Det rektangulära område du markerat kan också enkelt skapas som en objekt genom att använda Aspose.Cells.

Så här skapar du området, anger värde, ställer in stil och utför fler operationer på "Området" objektet.

## **Hantera områden med hjälp av Aspose.Cells**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)-klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-samling som möjliggör åtkomst till varje kalkylblad i en Excel-fil. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-klassen. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-klassen tillhandahåller en [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-samling.

### **Skapa område**

När du vill skapa ett rektangulärt område som sträcker sig över A1:C4 kan du använda följande kod:

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook;

    // Get Cells from the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Create a Range from A1 to C4
    Range range = cells.CreateRange(u"A1:C4");

    Aspose::Cells::Cleanup();
}
```

### **Sätt värde i cellerna i området**

Säg att du har ett område med celler som sträcker sig över A1:C4. Matrisen gör 4 * 3 = 12 celler. De individuella områdscellerna är arrangerade sekventiellt: Område[0,0], Område[0,1], Område[0,2], Område[1,0], Område[1,1], Område[1,2], Område[2,0], Område[2,1], Område[2,2], Område[3,0], Område[3,1], Område[3,2].

Följande exempel visar hur man anger värden i cellerna i området.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook;

    // Get Cells from the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Create a Range from A1 to C4
    Range range = cells.CreateRange(u"A1:C4");

    // Put values in specific cells
    range.Get(0, 0).PutValue(u"A1");
    range.Get(0, 1).PutValue(u"B1");
    range.Get(0, 2).PutValue(u"C1");
    range.Get(3, 0).PutValue(u"A4");
    range.Get(3, 1).PutValue(u"B4");
    range.Get(3, 2).PutValue(u"C4");

    // Save the Workbook
    workbook.Save(u"RangeValueTest.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Ställ in stil på cellerna i området**

Följande exempel visar hur man ställer in stil på cellerna i området.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook;

    // Get Cells
    WorksheetCollection sheets = workbook.GetWorksheets();
    Cells cells = sheets.Get(0).GetCells();

    // Create Range
    Range range = cells.CreateRange(u"A1:C4");

    // Put value
    range.Get(0, 0).PutValue(u"A1");
    range.Get(3, 2).PutValue(u"C4");

    // Set Style
    Style style00 = workbook.CreateStyle();
    style00.SetPattern(BackgroundType::Solid);
    style00.SetForegroundColor(Color::Red());
    range.Get(0, 0).SetStyle(style00);

    Style style32 = workbook.CreateStyle();
    style32.SetPattern(BackgroundType::HorizontalStripe);
    style32.SetForegroundColor(Color::Green());
    range.Get(3, 2).SetStyle(style32);

    // Save the Workbook
    workbook.Save(u"RangeStyleTest.xlsx");

    std::cout << "Workbook saved successfully with range styles applied!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Hämta aktuellt område av området**

CurrentRegion är en egenskap som returnerar ett områdesobjekt som representerar det aktuella området. 

Det aktuella området är ett område som begränsas av en kombination av tomma rader och tomma kolumner. Endast läsbar.

I Excel kan du få aktuellt område genom att:
1. Välj ett område (område1) med muslådan.
2. Klicka på "Hem - Redigering - Sök och markera - Gå till speciellt - Aktuellt område", eller använd "Ctrl+Skift+*", du kommer att se att Excel automatiskt hjälper dig att välja ett område (område2), nu har du gjort det, område2 är det aktuella området för område1.

Med Aspose.Cells kan du använda egenskapen "Range.CurrentRegion" för att utföra samma funktion.

Ladda ner följande testfil, öppna den i Excel, använd muslådan för att välja ett område "A1:D7", klicka sedan på "Ctrl+Skift+*", du kommer att se att område "A1:C3" är valt.

[current_region.xlsx](current_region.xlsx)

Kör nu följande exempel, se hur det fungerar i Aspose.Cells:

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook(u"current_region.xlsx");

    // Get Cells from the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Create a Range from A1 to D7
    Range src = cells.CreateRange(u"A1:D7");

    // Get the CurrentRegion of the created range
    Range A1C3 = src.GetCurrentRegion();

    Aspose::Cells::Cleanup();
}
```


## **Fortsatta ämnen**
- [Autofyllt område i Excel-fil](/cells/sv/cpp/autofill-ranges/)
- [Kopiera områden i Excel](/cells/sv/cpp/copy-ranges-of-Excel/)
- [Kopiera områdesdata endast](/cells/sv/cpp/copy-range-data-only/)
- [Kopiera områdesdata med stil](/cells/sv/cpp/copy-range-data-with-style/)
- [Kopiera områdesstil endast](/cells/sv/cpp/copy-range-style-only/)
- [Skapa unionsspann](/cells/sv/cpp/create-union-range/)
- [Klipp och klistra område](/cells/sv/cpp/cut-and-paste-cells/)
- [Radera områden](/cells/sv/cpp/delete-ranges-from-Excel/)
- [Få adresscellsantal offset hela kolumnen och hela raden för området](/cells/sv/cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Infoga områden](/cells/sv/cpp/insert-ranges-to-Excel/)
- [Sammanfoga eller dela upp cellområde](/cells/sv/cpp/merge-or-unmerge-range-of-cells/)
- [Flytta cellområde i ett kalkylblad](/cells/sv/cpp/move-range-of-cells-in-a-worksheet/)
- [Skapa arbetsbok och arbetsbladsspecifika namngivna områden](/cells/sv/cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [Sök och ersätt data i ett område](/cells/sv/cpp/search-and-replace-data-in-a-range/)
{{< app/cells/assistant language="cpp" >}}
