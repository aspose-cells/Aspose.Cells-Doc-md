---  
title: Create a Style object using the CellsFactory class with C++  
description: Aspose.Cells is a C++ library for working with spreadsheet files that provides a style object to style cells. This article introduces how to create a cell style object using the CellsFactory class in the Aspose.Cells library so that users can customize the appearance of the cells as needed.  
keywords: Aspose.Cells, C++ library, electronic spreadsheet, style object, cell style, customization  
type: docs  
weight: 70  
url: /cpp/create-style-object-using-cellsfactory-class/  
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Create Style object using CellsFactory class**  
The following sample code creates [Style](https://reference.aspose.com/cells/cpp/aspose.cells/style) object using [CellsFactory](https://reference.aspose.com/cells/cpp/aspose.cells/cellsfactory) class and then sets the default style of the workbook. Please download the [output Excel file](5115153.xlsx) to see the results of this code for your reference.  

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

    // Create a Style object using CellsFactory class
    CellsFactory cf;
    Style st = cf.CreateStyle();

    // Set the Style fill color to Yellow
    st.SetPattern(BackgroundType::Solid);
    st.SetForegroundColor(Color::Yellow());

    // Create a workbook and set its default style using the created Style object
    Workbook wb;
    wb.SetDefaultStyle(st);

    // Save the workbook
    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
