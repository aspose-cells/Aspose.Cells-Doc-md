---
title: Hämta eller ställ in Class Identifier för det inbäddade OLE objektet med C++
linktitle: Hämta eller ange klassidentifieraren för det inbäddade OLE objektet
type: docs
weight: 200
url: /sv/cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: Lär dig hur man hämtar eller ställer in klassidentifieraren för inbäddade OLE objekt med Aspose.Cells och C++.
---

## **Möjliga användningsscenario**
Aspose.Cells tillhandahåller egenskapen [OleObject.GetClassIdentifier()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getclassidentifier/), som du kan använda för att hämta eller ställa in klassidentifieraren för inbäddat OLE-objekt. OLE-objektklassidentifierare är faktiskt GUIDs, dvs. Globally Unique Identifiers. GUID är alltid 16 byte lång, därför är klassidentifierare också 16 byte långa. De finns ofta i Windows-registret och ger information till värdprogrammet om hur man öppnar inbäddade OLE-objekt som innehåller olika inbäddade resurser inne i klientapplikationen.

## **Hämta eller ange klassidentifieraren för det inbäddade OLE-objektet**
Följande skärmdump visar OLE-objektklassidentifieraren, dvs. GUID, som har lästs från [exempel Excel-fil](5115190.xls) med det inbäddade PowerPoint-OLE-objektet.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **Exempelkod**
Se följande exempelprogram som körs med den [exempel Excel-fil](5115190.xls) och dess konsolutmatning som skriver ut klassidentifieraren för OLE-objektet, dvs. GUID. Den utskrivna GUID är exakt densamma som visas i skärmbilden.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include <guiddef.h>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook wb(srcDir + u"sample.xls");
    Worksheet ws = wb.GetWorksheets().Get(0);
    OleObject oleObj = ws.GetOleObjects().Get(0);

    Vector<uint8_t> classIdentifier = oleObj.GetClassIdentifier();
    GUID guid;
    memcpy(&guid, classIdentifier.GetData(), sizeof(GUID));

    char guidStr[39];
    snprintf(guidStr, sizeof(guidStr), "{%08X-%04X-%04X-%02X%02X-%02X%02X%02X%02X}",
             guid.Data1, guid.Data2, guid.Data3,
             guid.Data4[0], guid.Data4[1], guid.Data4[2], guid.Data4[3],
             guid.Data4[4], guid.Data4[5], guid.Data4[6], guid.Data4[7]);

    std::cout << guidStr << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Konsoloutput**
Detta är konsoloutputen av ovanstående provkod när den kördes med [provexempelfilen](5115190.xls).

{{< highlight java >}}
DC020317-E6E2-4A62-B9FA-B3EFE16626F4
{{< /highlight >}}
