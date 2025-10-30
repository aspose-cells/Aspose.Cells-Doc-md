---
title: Generera miniatyrbild av arbetsblad med C++
linktitle: Generera miniatyrbild av arbetsboken
type: docs
weight: 110
url: /sv/cpp/generate-thumbnail-of-the-worksheet/
description: Generera miniatyrbilder av arbetsblad som bilder med Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Det kan vara användbart att generera miniatyrbilder från arbetsböcker. En miniatyrbild är en liten bild som kan klistras in i ett Word-dokument eller en PowerPoint-presentation för att ge en förhandsgranskning av innehållet i arbetsboken. Den kan läggas till på en webbsida med en länk för att ladda ner den ursprungliga filen och har en mängd andra användningsområden.

{{% /alert %}} 

Aspose.Cells for C++ tillåter dig att exportera arbetsblad till bildfiler, vilket gör generering av miniatyrbilder enkelt. Följande exempel visar hur man exporterar arbetsblad till bildfiler med C++.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load source workbook
    Workbook book(srcDir + u"sampleGenerateThumbnailOfWorksheet.xlsx");

    // Configure image rendering options
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(ImageType::Bmp);
    imgOptions.SetVerticalResolution(200);
    imgOptions.SetHorizontalResolution(200);
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetDesiredSize(600, 600, true); // Set thumbnail dimensions

    // Access first worksheet
    WorksheetCollection worksheets = book.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Render worksheet to image
    SheetRender sr(sheet, imgOptions);
    sr.ToImage(0, outDir + u"outputGenerateThumbnailOfWorksheet.bmp");

    std::cout << "Worksheet thumbnail generated successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
