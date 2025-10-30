---
title: Hämta ikonsatser, datastavar eller färgskal objekt som används i villkorsformatering med C++
linktitle: Hämta ikonuppsättningar, datastavar eller färgskalobjekt
description: Aspose.Cells for C++ är ett bibliotek för att arbeta med kalkylbladsfiler. Det stöder användning av ikonuppsättningar, datastavar och färgskalobjekt i villkorsformatering för att visa data från kalkylblad. Denna artikel beskriver hur man använder Aspose.Cells biblioteket för att hämta data för dessa objekt.
keywords: Aspose.Cells, Betingad formatering, Ikonuppsättning, DataBar, Färgskala, Kalkylblad
type: docs
weight: 10
url: /sv/cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/
---

{{% alert color="primary" %}} 

Ibland behöver du hämta ikonuppsättningar som används i villkorsformatering av en cell eller ett cellområde och vill skapa en bildfil baserat på detta. Du kan behöva läsa datastavar eller färgskal som används i villkorsformateringen. Aspose.Cells for C++ stöder denna funktion.

{{% /alert %}} 

Följande kodexempel visar hur man läser ikonuppsättningar som används för villkorsstyrd formatering. Med Aspose.Cells enkla API sparas ikonuppsättningens bilddata som en bild.

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the A1 cell
    Cell cell = sheet.GetCells().Get(u"A1");

    // Get the conditional formatting result object
    ConditionalFormattingResult cfr = cell.GetConditionalFormattingResult();

    // Get the icon set
    ConditionalFormattingIcon icon = cfr.GetConditionalFormattingIcon();

    // Get the image data from the icon
    Vector<uint8_t> imageData = icon.GetImageData();

    // Create the image file based on the icon's image data
    ofstream outputFile((outDir + u"imgIcon.out.jpg").ToUtf8(), ios::binary);
    outputFile.write(reinterpret_cast<const char*>(imageData.GetData()), imageData.GetLength());
    outputFile.close();

    std::cout << "Icon image saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
