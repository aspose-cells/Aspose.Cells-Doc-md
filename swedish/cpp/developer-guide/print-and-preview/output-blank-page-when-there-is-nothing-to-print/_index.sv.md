---  
title: Genererar tom sida när det inte finns något att skriva ut med C++  
linktitle: Utdata tom sida när det inte finns något att skriva ut  
type: docs  
weight: 90  
url: /sv/cpp/output-blank-page-when-there-is-nothing-to-print/  
description: Hantera tomma arbetsblad och skriv ut tomma sidor med Aspose.Cells i C++.  
---  

## **Möjliga användningsscenario**  

Om bladet är tomt, kommer Aspose.Cells inte att skriva ut något när du exporterar arbetsblad till bild. Du kan ändra denna beteende genom att använda [**ImageOrPrintOptions.GetOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getoutputblankpagewhennothingtoprint/) egenskapen. När du ställer in den på **true**, kommer den att skriva ut den tomma sidan.  

## **Utdata tom sida när det inte finns något att skriva ut**  

Följande kodexempel skapar arbetsboken som är tom med ett tomt kalkylblad och renderar det tomma kalkylbladet till en bild efter att ha satt egenskapen [**ImageOrPrintOptions.GetOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getoutputblankpagewhennothingtoprint/) till **true**. Följaktligen skapas en tom sida eftersom det inte finns något att skriva ut, vilket du kan se i bilden nedan.  

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)  

## **Exempelkod**  

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Output directory
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook wb;

    // Access first worksheet - it is an empty sheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Specify image or print options
    // Since the sheet is blank, we will set OutputBlankPageWhenNothingToPrint to true
    // So that an empty page gets printed
    ImageOrPrintOptions opts;
    opts.SetImageType(Drawing::ImageType::Png);
    opts.SetOutputBlankPageWhenNothingToPrint(true);

    // Render empty sheet to png image
    SheetRender sr(ws, opts);
    sr.ToImage(0, outputDir + u"OutputBlankPageWhenNothingToPrint.png");

    std::cout << "Blank page rendered to PNG successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```  
{{< app/cells/assistant language="cpp" >}}
