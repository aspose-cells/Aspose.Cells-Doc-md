---
title: Konvertera arbetsblad till bild  Ta bort vitt utrymme runt data med C++
linktitle: Konvertera arbetsblad till bild  Ta bort vitt utrymme runt data
type: docs
weight: 40
url: /sv/cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Lär dig hur du konverterar ett arbetsblad till en bild och tar bort vitt utrymme runt datan med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Ibland måste du presentera kalkylbladsbilder i applikationer eller webbsidor. Till exempel kan du behöva infoga bilder i ett Word-dokument, en PDF-fil, en PowerPoint-presentation eller något annat dokument. I huvudsak vill du rendera ett kalkylblad som en bild så att det kan klistras in i andra applikationer. Aspose.Cells gör det möjligt att konvertera Microsoft Excel-kalkylblad till bilder.

{{% /alert %}}

## **Ta bort mellanrum runt data**

[**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/)-API:en konverterar ett kalkylblad till en bildfil med vilka attribut som helst, till exempel bildformat, sidade kalkylblad, osv. Flera bildformat stöds, inklusive BMP, GIF, JPG, TIFF och EMF.

När du använder blad-till-bild-funktionen, har den genererade bilden som standard vitt utrymme, det vill säga en kant, runt den. Du kan ta bort detta genom att ställa in top, bottom, left och right sidmarginaler för källarbetsbladet till 0 och specificera [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) attribut därefter.

Följande kodsippa tar bort mellanrummet runt datan i den resulterande bilden.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open the template file
    Workbook book(srcDir + u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Define LoadOptions and set LoadFilter
    LoadOptions options;
    options.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All));

    // Specify your print area if you want
    // sheet.GetPageSetup().SetPrintArea(u"A1:H8");

    // To remove the white border around the image.
    sheet.GetPageSetup().SetLeftMargin(0);
    sheet.GetPageSetup().SetRightMargin(0);
    sheet.GetPageSetup().SetBottomMargin(0);
    sheet.GetPageSetup().SetTopMargin(0);

    // Define ImageOrPrintOptions
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(Aspose::Cells::Drawing::ImageType::Emf);

    // Set only one page would be rendered for the image
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetPrintingPage(PrintingPageType::IgnoreBlank);

    // Create the SheetRender object based on the sheet with its
    // ImageOrPrintOptions attributes
    SheetRender sr(sheet, imgOptions);

    // Convert the image
    sr.ToImage(0, outDir + u"outputRemoveWhitespaceAroundData.emf");

    std::cout << "Image converted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
