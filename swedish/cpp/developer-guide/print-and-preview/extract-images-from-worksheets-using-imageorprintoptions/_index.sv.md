---
title: Extrahera bilder från arbetsblad med hjälp av ImageOrPrintOptions i C++
linktitle: Extrahera bilder från arbetsblad
type: docs
weight: 140
url: /sv/cpp/extract-images-from-worksheets-using-imageorprintoptions/
description: Lär dig hur du extraherar bilder från Excel arbetsblad och sparar dem på en lokal enhet med Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Microsoft Excel-användare kan lägga till bilder i kalkylblad. Med Aspose.Cells är det möjligt att läsa bilder från Microsoft Excel-filer och spara dem på en lokal enhet. Den här artikeln visar hur du gör detta.

{{% /alert %}} 

Den exempelkod nedan visar hur man extraherar bilder från en Excel-fil och sparar dem.

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

    // Open a template Excel file
    Workbook workbook(srcDir + u"sampleExtractImagesFromWorksheets.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first Picture in the first worksheet
    Picture pic = worksheet.GetPictures().Get(0);

    // Define ImageOrPrintOptions
    ImageOrPrintOptions printoption;

    // Specify the image format
    printoption.SetImageType(ImageType::Jpeg);

    // Save the image
    pic.ToImage(outDir + u"outputExtractImagesFromWorksheets.jpg", printoption);

    std::cout << "Image extracted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
