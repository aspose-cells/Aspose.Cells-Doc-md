---
title: Rendera gradientfyllning för WordArt vid konvertering av kalkylblad till HTML med C++
linktitle: Rendera Gradient Fill för WordArt vid konvertering av kalkylblad till HTML
type: docs
weight: 90
url: /sv/cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/
description: Lär dig att rendera gradientfyllning för WordArt vid konvertering av kalkylblad till HTML med C++.
---

## **Möjliga användningsscenario**
Innan Aspose.Cells 17.1, renderade inte Aspose.Cells gradientfyllningen av ordkonst när Excel-filen konverterades till HTML-format. Sedan version 17.1 av Aspose.Cells stöds gradientfyllning av ordkonst. Följande skärmbild jämför effekten på gradientfyllningen genom att konvertera excelfilen med hjälp av Aspose.Cells 17.1 och den äldre versionen.

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)
## **Rendera Gradient Fill för WordArt vid konvertering av kalkylblad till HTML**
Följande provkod konverterar [källa excelfil](22774111.xlsx) till [utmatnings-HTML-format](22774109.zip). Källa Excel-filen innehåller ett ordkonstobjekt med gradientfyllning som visas i ovanstående skärmbild.
## **Exempelkod**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sourceGradientFill.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save workbook to HTML format
    workbook.Save(outDir + u"out_sourceGradientFill.html");

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
