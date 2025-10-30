---
title: Lägg till anpassade XML delar och välj dem efter ID med C++
linktitle: Lägg till anpassade XML delar och välj dem efter ID
type: docs
weight: 70
url: /sv/cpp/add-custom-xml-parts-and-select-them-by-id/
description: Lär dig hur du lägger till och väljer anpassade XML delar i Excel filer med Aspose.Cells och C++.
---

## **Möjliga användningsscenario**

Anpassade XML-delar är XML-data som lagras inuti Microsoft Excel-dokument och används av applikationer som interagerar med dem. Det finns för närvarande ingen direkt metod att lägga till dem via Microsoft Excel UI. Du kan dock lägga till dem programmatiskt på olika sätt, exempelvis med VSTO eller Aspose.Cells. Använd [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/add/)-metoden för att lägga till en anpassad XML-del med Aspose.Cells API. Du kan även ställa in dess ID med [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/)-egenskapen. På samma sätt, om du vill välja en anpassad XML-del efter ID, kan du använda [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/)-metoden.

## **Lägg till anpassade XML-delar och välj dem efter ID**

Följande exempel lägger först till fyra anpassade XML-delar med [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/add/)-metoden. Den ställer sedan in deras ID med [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/)-egenskapen. Slutligen hittar eller väljer den en av de tillagda XML-delarna med [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/)-metoden. Se också kodens konsolutdata nedan för referens.

## **Exempelkod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Markup;

int main()
{
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Some data in the form of byte array
    // Please use correct XML and Schema instead
    Vector<uint8_t> btsData = { 1, 2, 3 };
    Vector<uint8_t> btsSchema = { 1, 2, 3 };

    // Create four custom xml parts
    wb.GetCustomXmlParts().Add(btsData, btsSchema);
    wb.GetCustomXmlParts().Add(btsData, btsSchema);
    wb.GetCustomXmlParts().Add(btsData, btsSchema);
    wb.GetCustomXmlParts().Add(btsData, btsSchema);

    // Assign ids to custom xml parts
    wb.GetCustomXmlParts().Get(0).SetID(u"Fruit");
    wb.GetCustomXmlParts().Get(1).SetID(u"Color");
    wb.GetCustomXmlParts().Get(2).SetID(u"Sport");
    wb.GetCustomXmlParts().Get(3).SetID(u"Shape");

    // Specify search custom xml part id
    U16String srchID = u"Fruit";
    srchID = u"Color";
    srchID = u"Sport";

    // Search custom xml part by the search id
    CustomXmlPart cxp = wb.GetCustomXmlParts().SelectByID(srchID);

    // Print the found or not found message on console
    if (cxp.IsNull())
    {
        std::cout << "Not Found: CustomXmlPart ID " << srchID.ToUtf8() << std::endl;
    }
    else
    {
        std::cout << "Found: CustomXmlPart ID " << srchID.ToUtf8() << std::endl;
    }

    std::cout << "AddCustomXMLPartsAndSelectThemByID executed successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Konsoloutput**

{{< highlight java >}}
Found: CustomXmlPart ID Sport
{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
