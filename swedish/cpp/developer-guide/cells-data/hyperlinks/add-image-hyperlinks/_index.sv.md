---
title: Lägg till bildhyperlänkar med C++
linktitle: Lägg till bildhyperlänkar
type: docs
weight: 140
url: /sv/cpp/add-image-hyperlinks/
description: Lär dig hur du lägger till bildhyperlänkar med API n Aspose.Cells for C++.
keywords: Lägg till bildhyperlänkar, Infoga bildhyperlänkar
---

{{% alert color="primary" %}} 

Hyperlänkar är användbara för att komma åt information på andra kalkylblad eller på webbplatser. Microsoft Excel låter användare lägga till hyperlänkar på text i celler och på bilder. Bildhyperlänkar kan göra navigering i ett kalkylblad enklare, till exempel som knappar för nästa och föregående, eller logotyper som länkar till särskilda platser. Detta dokument förklarar hur du infogar bildhyperlänkar i ett kalkylblad med hjälp av Aspose.Cells.

{{% /alert %}} 

Aspose.Cells möjliggör att du lägger till hyperlänkar till bilder i kalkylblad vid körning. Det är möjligt att ange och ändra länkens skärmtips och adress. Följande provkod illustrerar hur du lägger till en bildhyperlänk i ett kalkylblad.

```c++
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

    // Instantiate a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a string value to a cell
    worksheet.GetCells().Get(u"C2").PutValue(u"Image Hyperlink");

    // Set the 4th row height
    worksheet.GetCells().SetRowHeight(3, 100);

    // Set the C column width
    worksheet.GetCells().SetColumnWidth(2, 21);

    // Add a picture to the C4 cell
    int index = worksheet.GetPictures().Add(3, 2, 4, 3, srcDir + u"aspose-logo.jpg");

    // Get the picture object
    Picture pic = worksheet.GetPictures().Get(index);

    // Set the placement type
    pic.SetPlacement(PlacementType::FreeFloating);

    // Add an image hyperlink
    Hyperlink hlink = pic.AddHyperlink(u"http://www.aspose.com/");

    // Specify the screen tip
    hlink.SetScreenTip(u"Click to go to Aspose site");

    // Save the Excel file
    workbook.Save(outDir + u"ImageHyperlink_out.xls");

    std::cout << "Image hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
