---
title: Dela skärm i Excel ark med C++
linktitle: Dela skärm
type: docs
weight: 190
url: /sv/cpp/how-to-split-screen-of-excel-worksheet
description: I denna artikel lär du dig hur du visar vissa rader och/eller kolumner i separata paneler genom att dela arket i två eller fyra delar programmatiskt med C++.
keywords: Frysta översta rader, Frysta översta raden.
---

## **Introduktion**

I denna artikel kommer vi att lära oss hur man visar vissa rader och/eller kolumner i separata paneler genom att dela arket i två eller fyra delar. När man arbetar med stora datamängder behöver vi se några delar av samma ark samtidigt för att jämföra olika underuppsättningar av data. Funktionerna för att dela skärmen kan möta dina behov.

## **Hur man delar skärmen i Excel**
För att dela upp ett arbetsblad i två eller fyra delar, gör följande:

1. Välj rad/kolumn/cell innan vilken du vill placera uppdelningen.
2. På fliken Visa, i gruppen Fönster, klicka på knappen Dela.

**![Dela skärm](Split-Screen.png)**

## **Dela arbetsblad vertikalt på kolumner**

För att separera två områden av kalkylarket vertikalt, välj kolumnen till höger om den kolumn där du vill att uppdelningen ska visas och klicka på Split-knappen i Excel.

Det är enkelt att dela arket vertikalt på kolumner programmatiskt med Aspose.Cells for C++, vi behöver bara välja en cell i den övre raden som aktiv cell, sedan
dela med [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/)-metoden.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet in the workbook.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Sets C1 cell in the top row as the active cell.
    sheet.SetActiveCell(u"C1");

    // Split worksheet vertically on columns.
    sheet.Split();

    std::cout << "Worksheet processed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Dela arbetsblad horisontellt på rader**
För att separera ditt Excel-fönster horisontellt, välj raden under den rad där du vill att uppdelningen ska ske i Excel.

Det är enkelt att dela arket horisontellt på rader programmatiskt med Aspose.Cells for C++, vi behöver bara välja en cell i den vänstra kolumnen som aktiv cell, sedan
dela med [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/)-metoden.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook and load an existing Excel file.
    Workbook workbook(u"Book1.xlsx");

    // Access the first worksheet in the workbook.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Set the A6 cell in the left column as the active cell.
    sheet.SetActiveCell(u"A6");

    // Split the worksheet horizontally on rows.
    sheet.Split();

    // Save the modified workbook to a new file.
    workbook.Save(u"dest.xlsx");

    std::cout << "Workbook processed and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Dela arbetsblad i fyra delar**
För att visa fyra olika sektioner av samma arbetsblad samtidigt, dela upp skärmen både vertikalt och horisontellt i Excel.

Det är enkelt att dela arket vertikalt på kolumner programmatiskt med Aspose.Cells for C++, vi behöver bara välja en cell som inte finns i den första raden och kolumnen som aktiv cell, sedan
dela med [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/)-metoden.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Set E6 cell as the active cell.
    sheet.SetActiveCell(u"E6");

    // Split worksheet into four parts.
    sheet.Split();

    Aspose::Cells::Cleanup();
}
```

## **Hur man tar bort uppdelning**
För att ta bort arbetsbladets uppdelning, klicka bara på Split-knappen igen.

Aspose.Cells for C++ tillhandahåller en [**Worksheet.RemoveSplit**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/) metod för att ta bort split-inställningen.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Remove split
    sheet.RemoveSplit();

    // Split worksheet into four parts
    sheet.Split();

    std::cout << "Worksheet split successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
