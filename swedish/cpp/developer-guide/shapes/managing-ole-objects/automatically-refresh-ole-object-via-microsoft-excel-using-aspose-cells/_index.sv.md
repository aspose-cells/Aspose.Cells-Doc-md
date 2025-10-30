---
title: Automatiskt uppdatera OLE objekt via Microsoft Excel med C++
linktitle: Automatisk uppdatering av OLE objekt
type: docs
weight: 270
url: /sv/cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: Läs hur du automatiskt uppdaterar OLE objekt i Microsoft Excel med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller egenskapen [**OleObject.GetAutoLoad()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getautoload/) för att fräscha upp OLE-objektet när Excel-filen öppnas i Microsoft Excel. På grund av denna egenskap visas rätt OLE-bild genererad av Microsoft Excel.

{{% /alert %}}

Följande exempelprogram laddar den [exempel Excel-fil](5115231.xlsx) som har en icke-virtuell OLE-bild. OLE-objektet är egentligen ett Microsoft Word-dokument, men exempel-Excel-filen visar djurbilden istället för Microsoft Word-bilden. Men om du öppnar [utgångs-Excel-filen](5115225.xlsx), kommer du att se att Microsoft Excel visar rätt OLE-bild.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object from your sample excel file
    Workbook wb(srcDir + u"sample.xlsx");

    // Access first worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Set auto load property of first ole object to true
    sheet.GetOleObjects().Get(0).SetAutoLoad(true);

    // Save the workbook in xlsx format
    wb.Save(srcDir + u"RefreshOLEObjects_out.xlsx", SaveFormat::Xlsx);

    std::cout << "OLE object refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
