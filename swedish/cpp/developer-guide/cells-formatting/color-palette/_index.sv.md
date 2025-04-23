---
title: Hur man använder färgpalett med C++
linktitle: Hur man använder färgpaletten
type: docs
weight: 80
url: /sv/cpp/excel-color-palette/
description: C++ kod för att lägga till anpassade färger till paletten och använda Excel färgpaletten med Aspose.Cells for C++ API.
keywords: c++ lägga till anpassade färger till paletten, c++ programmatisk användning av Excel färgpaletten, hur man använder färgpaletten i arbetsboken programmatisk, c++ hur man använder färgpaletten i Excel
---

## **Färger och Palett**

En palett är antalet färger som är tillgängliga för att skapa en bild. Användningen av en standardiserad palett i en presentation gör att användaren kan skapa en enhetlig look. Varje Microsoft Excel (97-2003) fil har en palett med 56 färger som kan tillämpas på celler, teckensnitt, rutnät, grafiska objekt, fyllningar och linjer i en graf.

Med Aspose.Cells är det möjligt att inte bara använda palettens befintliga färger utan också anpassade färger. Innan du använder en anpassad färg, lägg till den först i paletten.

Detta ämne diskuterar hur man lägger till anpassade färger i paletten.

## **Lägg till anpassade färger i paletten**

Aspose.Cells stöder Microsoft Excels 56-färgspalett. För att använda en anpassad färg som inte är definierad i paletten, lägg till färgen i paletten.

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) tillhandahåller en [**ChangePalette**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/changepalette/)-metod som tar följande parametrar för att lägga till en anpassad färg för att ändra paletten:

- Anpassad färg, den anpassade färgen som ska läggas till.
- Index, index för färgen i paletten som den anpassade färgen kommer att ersätta. Ska vara mellan 0-55.

Exemplet nedan lägger till en anpassad färg (Orchid) i paletten innan den tillämpas på en font.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Check if Orchid color is in the palette
    std::cout << "Is Orchid in palette? " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add Orchid color to the palette at index 55
    workbook.ChangePalette(Color::Orchid(), 55);

    // Verify if Orchid is now in the palette
    std::cout << "Is Orchid in palette now? " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add a new worksheet
    int i = workbook.GetWorksheets().Add();

    // Get the reference to the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in cell A1
    cell.PutValue(u"Hello Aspose!");

    // Create a new style
    Style styleObject = workbook.CreateStyle();

    // Set the custom color (Orchid) to the font
    styleObject.GetFont().SetColor(workbook.GetColors()[55]);

    // Apply the style to the cell
    cell.SetStyle(styleObject);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Paletten rymmer endast 56 färger. När du lägger till en anpassad färg i paletten ändras paletten och alla element i filen formaterade med den tidigare färgen ändras. Så, när du ändrar paletten, var mycket försiktig. Dessutom är detta begränsningen i XLS (Excel 97 - 2003) filformat endast då det inte finns någon sådan begränsning för XLSX eller andra avancerade MS Excel (2007/2010 eller 2013) filformat.

{{% /alert %}}
