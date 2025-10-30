---
title: Åtkomst och ändra visningsetiketten för den länkade Ole objektet med C++
linktitle: Åtkomst och ändring av visningsmärket för det länkade OLE objektet
type: docs
weight: 100
url: /sv/cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: Läs hur du får åtkomst till och ändrar visningsetiketten för länkade Ole objekt i Excel filer med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Microsoft Excel gör det möjligt att ändra displayetiketten för Ole-objektet, som visas i följande skärmbild. Du kan också komma åt eller ändra displayetiketten för Ole-objektet med Aspose.Cells API:er med [**GetLabel()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getlabel/) och [**SetLabel(const U16String\& value)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/setlabel/)-metoderna.

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **Åtkomst och ändring av visningsmärket för det länkade OLE-objektet**

Vänligen se följande provkod, den laddar [provexempel Excel-fil](64716810.xlsx) som innehåller Ole Object. Koden kommer åt Ole-objektet och ändrar dess etikett från prov API till Aspose API:er. Vänligen se konsolerna outputen nedan som visar effekten av provkoden på prov Excel-filen för referens.

## **Exempelkod**

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample Excel file
    U16String inputFilePath = u"sampleAccessAndModifyLabelOfOleObject.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first Ole Object
    OleObject oleObject = ws.GetOleObjects().Get(0);

    // Display the Label of the Ole Object
    std::cout << "Ole Object Label - Before: " << oleObject.GetLabel().ToUtf8() << std::endl;

    // Modify the Label of the Ole Object
    oleObject.SetLabel(u"Aspose APIs");

    // Save workbook to memory stream
    auto ms = wb.SaveToStream();

    // Set the workbook reference to null
    wb = Workbook();

    // Load workbook from memory stream
    wb = Workbook(ms);

    // Access first worksheet
    ws = wb.GetWorksheets().Get(0);

    // Access first Ole Object
    oleObject = ws.GetOleObjects().Get(0);

    // Display the Label of the Ole Object that has been modified earlier
    std::cout << "Ole Object Label - After: " << oleObject.GetLabel().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konsoloutput**

{{< highlight java >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
