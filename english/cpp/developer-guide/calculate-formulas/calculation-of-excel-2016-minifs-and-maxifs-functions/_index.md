---
title: Calculation of Excel 2016 MINIFS and MAXIFS functions with C++
description: This article introduces how to use the Aspose.Cells library to calculate MINIFS and MAXIFS functions in Microsoft Excel 2016 using C++.
keywords: Aspose.Cells, Excel, 2016, MINIFS function, MAXIFS function, calculation
type: docs
weight: 300
url: /cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Possible Usage Scenarios**
Microsoft Excel 2016 supports MINIFS and MAXIFS functions. These functions are not supported in Excel 2013 or earlier versions. Aspose.Cells also supports the calculation of these functions. The following screenshot illustrates the usage of these functions. Please read the red comments inside the screenshot to know how these functions work.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Calculation of Excel 2016 MINIFS and MAXIFS functions**
The following sample code loads the [sample excel file](5115149.xlsx) and calls the [Workbook.CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) method to perform the formula calculation via Aspose.Cells and then saves the results in the [output PDF](5115154.pdf).

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    
    // Load your source workbook containing MINIFS and MAXIFS functions
    Workbook workbook(srcDir + u"sampleMINIFSAndMAXIFS.xlsx");
    
    // Perform Aspose.Cells formula calculation
    workbook.CalculateFormula();
    
    // Save the calculations result in pdf format
    PdfSaveOptions options;
    options.SetOnePagePerSheet(true);
    workbook.Save(outDir + u"outputMINIFSAndMAXIFS.pdf", options);

    std::cout << "PDF saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```