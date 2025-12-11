---  
title: Output Blank Page when there is Nothing to Print with C++  
linktitle: Output Blank Page when there is Nothing to Print  
type: docs  
weight: 90  
url: /cpp/output-blank-page-when-there-is-nothing-to-print/  
description: Handle empty worksheets and print blank pages with Aspose.Cells using C++.  
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**  

If the sheet is empty, then Aspose.Cells will not print anything when you export the worksheet to an image. You can change this behavior by using [**ImageOrPrintOptions.GetOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getoutputblankpagewhennothingtoprint/) property. When you set it **to** true, it will print the blank page.  

## **Output Blank Page when there is Nothing to Print**  

The following sample code creates **an** empty workbook **that** has an empty worksheet and renders the empty worksheet to an image after setting the [**ImageOrPrintOptions.GetOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getoutputblankpagewhennothingtoprint/) property **to** true. Consequently, it generates **a** blank page, **as** there is nothing to print, which you can see in the image below.  

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)  

## **Sample Code**  

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
