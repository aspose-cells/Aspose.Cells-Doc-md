---
title: Ladda en Webb bild från en URL till ett Excel blad med C++
linktitle: Ladda en webbild från en URL till ett Excel kalkylblad
type: docs
weight: 30
url: /sv/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/
description: Lär dig hur man konverterar en bild från URL till inbäddad bild i Excel med C++ och Aspose.Cells for C++ API.
keywords: excel visa bild från url, excel url till bild, visa bild i excel från url, excel infoga bild från url, konvertera url till bild i excel, excel bild från url, ladda bild från url i excel, C++, Excel
---

## Ladda en bild från en URL till ett Excel-kalkylblad

Aspose.Cells for C++ API ger ett enkelt sätt att ladda bilder från URL:er till Excel-blad. Denna artikel förklarar hur man laddar ned bilddata till en minnesström och infogar den i bladet med Aspose.Cells. Bilderna blir inbäddade i Excel-filen och kräver inte externa nedladdningar när filen öppnas.

## Exempelkod

```c++
#include <iostream>
#include <Aspose.Cells.h>
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    try
    {
        // Create a new workbook
        Workbook wb;

        // Get the first worksheet
        WorksheetCollection worksheets = wb.GetWorksheets();
        Worksheet sheet = worksheets.Get(0);

        // Get the pictures collection
        PictureCollection pictures = sheet.GetPictures();

        // Insert the picture from local file to B2 cell (row 1, column 1)
        // Note: Image file should be pre-downloaded to source directory
        U16String imagePath = srcDir + u"aspose-logo.jpg";
        pictures.Add(1, 1, imagePath);

        // Save the Excel file
        wb.Save(outDir + u"webimagebook.out.xlsx");
        std::cout << "Image added successfully." << std::endl;
    }
    catch (const std::exception& ex)
    {
        std::cerr << "Error: " << ex.what() << std::endl;
        return 1;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

För scenarier som kräver alltid uppdaterade bilder från en URL, använd metoden beskriven i [Infoga en länkad bild från webbadress](/cells/sv/cpp/insert-a-linked-picture-from-web-address/). Den här metoden laddar ned bilden från URL varje gång bladet öppnas.

{{% /alert %}}
