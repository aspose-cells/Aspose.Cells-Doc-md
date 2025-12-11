---  
title: Export Print Area Range to HTML with C++  
linktitle: Export Print Area Range to HTML  
type: docs  
weight: 60  
url: /cpp/export-print-area-range-to/  
description: Learn how to export the print area range to HTML using Aspise.Cells for C++.  
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**  

This is a common scenario where we need to export only the print area, i.e., a selected range of cells, instead of the entire sheet to HTML. This feature is already available for PDF rendering; however, you can now perform this task for HTML as well. First, set the print area in the page‑setup object of the worksheet. Later, use the [**HtmlSaveOptions.GetExportPrintAreaOnly()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportprintareaonly/) flag to export the selected range only.  

## **Sample Code**  

The following sample code loads a workbook and then exports the print area to HTML. The sample file for testing this feature can be downloaded from the following link:  

[sampleInlineCharts.xlsx](79527946.xlsx)  

```cpp
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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleInlineCharts.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"outputInlineCharts.html";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the print area
    worksheet.GetPageSetup().SetPrintArea(u"D2:M20");

    // Initialize HtmlSaveOptions
    HtmlSaveOptions options;

    // Set flag to export print area only
    options.SetExportPrintAreaOnly(true);

    // Save to HTML format
    workbook.Save(outputFilePath, options);

    std::cout << "HTML file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
{{< app/cells/assistant language="cpp" >}}
