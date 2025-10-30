---
title: Använd Sheet.SheetId egenskapen av OpenXml med C++
linktitle: Använd Sheet.SheetId egenskapen av OpenXml
type: docs
weight: 200
url: /sv/cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: Denna artikel visar hur man använder Sheet.SheetId egenskapen av OpenXml med Excel manipulerings API eller bibliotek programmässigt.
keywords: blad id egenskap av openxml c++, blad id excel arbetsblad c++
---

## **Möjliga användningsscenario**

Egenskapen *Sheet.SheetId* finns inom *DocumentFormat.OpenXml.Spreadsheet*-namnrymden och ingår i OpenXml. Du kan se denna egenskap och dess värde i *workbook.xml* som visas på följande skärmdump. Aspose.Cells tillhandahåller motsvarande egenskap som [**Worksheet.GetTabId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettabid/).

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **Använd Sheet.SheetId-egenskapen i OpenXml med hjälp av Aspose.Cells**

Följande exempelkod laddar [provs-exelfilen](51740716.xlsx), läser av dess flik- eller flik-id, tilldelar det ett nytt flik-id och sparar det som [utdata-exelfil](51740717.xlsx). Se även konsolens utmatning för kodreferens.

## **Exempelkod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load source Excel file
    Workbook wb(u"sampleSheetId.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Print its Sheet or Tab Id on console
    std::cout << "Sheet or Tab Id: " << ws.GetTabId() << std::endl;

    // Change Sheet or Tab Id
    ws.SetTabId(358);

    // Save the workbook
    wb.Save(u"outputSheetId.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Konsoloutput**

{{< highlight java >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
