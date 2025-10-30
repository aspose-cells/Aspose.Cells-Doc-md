---
title: Beräkning av Excel 2016 MINIFS och MAXIFS funktioner med C++
description: Denna artikel introducerar hur man använder Aspose.Cells biblioteket för att beräkna MINIFS och MAXIFS funktioner i Microsoft Excel 2016 med C++.
keywords: Aspose.Cells, Excel, 2016, MINIFS funktion, MAXIFS funktion, beräkning
type: docs
weight: 300
url: /sv/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Möjliga användningsscenario**
Microsoft Excel 2016 stöder MINIFS och MAXIFS funktioner. Dessa funktioner stöds inte i Excel 2013 eller tidigare versioner. Aspose.Cells stöder också beräkning av dessa funktioner. Följande skärmdump illustrerar användningen av dessa funktioner. Läs de röda kommentarerna i skärmbilden för att förstå hur dessa funktioner fungerar.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Beräkning av Excel 2016 MINIFS och MAXIFS funktioner**
Följande exempelkod laddar [exempel excel filen](5115149.xlsx) och anropar [Workbook.CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) metoden för att utföra formelberäkningen via Aspose.Cells och sparar sedan resultaten i [utgångs PDF](5115154.pdf).

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
{{< app/cells/assistant language="cpp" >}}
