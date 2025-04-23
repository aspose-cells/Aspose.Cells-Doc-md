---
title: Infoga en länkad bild från webbadress med C++
linktitle: Infoga en länkad bild från webbadress
type: docs
weight: 450
url: /sv/cpp/insert-a-linked-picture-from-web-address/
description: Lär dig hur du infogar en länkad bild från en webbadress i ett arbetsblad med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Ibland behöver du infoga en bild från webben (http://) i ett kalkylblad. För att göra detta, ange bildens URL och bilden kommer att hämtas varje gång kalkylarket öppnas i Microsoft Excel. Bilden är inte fysiskt inbäddad i Excel-dokumentet, utan pekar på en webbresurs.

{{% /alert %}}

## **Använda Microsoft Excel**

I Microsoft Excel (till exempel 2007):

1. Klicka på **Infoga** i menyn och välj **Bild**.
1. Ange webbadressen för bilden i dialogrutan Infoga bild.

## **Använder Aspose.Cells for C++**

Aspose.Cells for C++ stöder att lägga till en länkad bild med hjälp av [**ShapeCollection::AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, System::String sourceFullName)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlinkedpicture/)-metoden. Metoden returnerar ett [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/)-objekt.

Följande exempel visar hur man lägger till en länkad bild från en webbadress till ett arbetsblad.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook workbook;

    // Insert a linked picture (from Web Address) to B2 Cell
    U16String imageUrl(u"http://www.aspose.com/Images/aspose-logo.jpg");
    Picture pic = workbook.GetWorksheets().Get(0).GetShapes().AddLinkedPicture(1, 1, 100, 100, imageUrl);

    // Set the height and width of the inserted image
    pic.SetHeightInch(1.04);
    pic.SetWidthInch(2.6);

    // Save the Excel file
    U16String outputPath = outDir + u"outLinkedPicture.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Linked picture inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
