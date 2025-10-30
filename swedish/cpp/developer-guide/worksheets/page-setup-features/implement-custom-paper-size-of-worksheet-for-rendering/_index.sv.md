---
title: Implementera anpassad pappersstorlek för arbetsblad för rendering med C++
linktitle: Implementera Anpassad Papperstorlek på Arbetsbladet för Rendering
type: docs
weight: 70
url: /sv/cpp/implement-custom-paper-size-of-worksheet-for-rendering/
description: Denna artikel förklarar hur du använder C++ API för att ställa in anpassad papperstorlek på önskade arbetsblad när du renderar Excel fil till PDF format programmässigt.
keywords: sätt anpassad papperstorlek vid rendering av excel till pdf c++
---

## **Möjliga användningsscenario**

Det finns inget direkt alternativ för att skapa anpassade pappersstorlekar i MS Excel; dock kan du ställa in en anpassad pappersstorlek för dina önskade arbetsblad vid rendering av Excel-filer till PDF. Denna dokument förklarar hur du ställer in en anpassad pappersstorlek för ett arbetsblad med Aspose.Cells API.

## **Implementera anpassad pappersstorlek för arbetsblad för rendering**

Aspose.Cells låter dig implementera din önskade pappersstorlek för arbetsbladet. Du kan använda [**CustomPaperSize**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/custompapersize/)-metoden av [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)-klassen för att specificera en anpassad sidstorlek. Följande exempel kod visar hur man specificerar en anpassad pappersstorlek för det första arbetsbladet i arbetsboken. Se också den [utgångs PDF](45056028.pdf) som genererades med koden för referens.

## **Skärmdump**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **Exempelkod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Set custom paper size in unit of inches
    ws.GetPageSetup().CustomPaperSize(6, 4);

    // Access cell B4
    Cell b4 = ws.GetCells().Get("B4");

    // Add the message in cell B4
    b4.PutValue(u"Pdf Page Dimensions: 6.00 x 4.00 in");

    // Save the workbook in pdf format
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    wb.Save(outputDir + u"outputCustomPaperSize.pdf");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
