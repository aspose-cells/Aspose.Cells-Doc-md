---  
title: Render Gradient Fill for the WordArt while Converting Spreadsheets to HTML with C++  
linktitle: Render Gradient Fill for the WordArt while Converting Spreadsheets to HTML  
type: docs  
weight: 90  
url: /cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/  
description: Learn to render gradient fill for WordArt while converting spreadsheets to HTML with C++.  
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**  
Before Aspose.Cells 17.1, Aspose.Cells did not render the gradient fill of WordArt when the Excel file was converted to HTML format. Since the release of Aspose.Cells 17.1, WordArt gradient fill is supported. The following screenshot compares the gradient‑fill effect by converting the Excel file using Aspose.Cells 17.1 and an older version.  

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)  

## **Render Gradient Fill for the WordArt while Converting Spreadsheets to HTML**  
The following sample code converts the [source Excel file](22774111.xlsx) into [output HTML format](22774109.zip). The source Excel file contains a WordArt object with gradient fill, as shown in the screenshot above.  

## **Sample Code**  
```cpp
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

    // Path of input Excel file
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
{{< app/cells/assistant language="cpp" >}}
