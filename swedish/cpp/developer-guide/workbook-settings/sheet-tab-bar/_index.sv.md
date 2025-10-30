---
title: Hur man kontrollerar Sheet Tab Bar med C++
linktitle: Hur man kontrollerar flikfält för arkhuvuden
type: docs
weight: 600
url: /sv/cpp/how-to-control-sheet-tab-bar/
description: Lär dig hur du kontrollerar Sheet Tab Bar via API n Aspose.Cells for C++.
keywords: Hur man kontrollerar flikfält för arkhuvuden, Hantera flikfält för arkhuvuden, Ange flikfält för arkhuvuden, Kontrollera flikfält för arkhuvuden. 
---

## **Möjliga användningsscenario**
När du behöver justera visningen av Excel-bladlisten måste du veta hur du kontrollerar bladfliken, till exempel att dölja eller visa bladfliksfältet, ändra bladflikens bredd, ange den första synliga fliken och så vidare. Aspose.Cells stöder dessa funktioner. Aspose.Cells erbjuder följande egenskaper och metoder för att hjälpa dig att uppnå dina mål.

- [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/)
- [**WorkbookSettings.GetSheetTabBarWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getsheettabbarwidth/)
- [**WorkbookSettings.GetFirstVisibleTab()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getfirstvisibletab/)

## **Hur man kontrollerar Sheet Tab Bar med Aspose.Cells for C++**
Detta exempel visar hur man:

1. Skapa en arbetsbok.
1. Lägga till data till celler i den första arbetsboken.
1. Visa flikfältet och ange bredden på flikfältet.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook object
    Workbook workbook;

    // Obtain the reference to the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
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

    // Display the sheet tab and set the width of the tab bar
    workbook.GetSettings().SetShowTabs(true);
    workbook.GetSettings().SetSheetTabBarWidth(150);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Förhandsgranskning av resultatfil:
<br>
<image src="result.png" width="70%" />

{{< app/cells/assistant language="cpp" >}}
