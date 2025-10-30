---
title: Exportera XML data kopplat till XML karta i arbetsboken med C++
linktitle: Exportera XML data kopplad till XML karta i arbetsboken
type: docs
weight: 20
url: /sv/cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/
description: Lär dig hur man exporterar XML data kopplat till XML kartor i din arbetsbok med Aspose.Cells for C++.
---

## **Exportera XML-data som är länkad till XML-karta inuti arbetsboken**

Vänligen använd metoden [**Workbook::ExportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/exportxml/) för att exportera XML-data kopplad till dina XML-kartor i arbetsboken. Följande kodexempel exporterar XML-data för alla XML-kartor i arbetsboken en efter en. Kontrollera filen [exempel-Excelfil](5115497.xlsx) som används i detta kodexempel och [exporterad XML-data för första XML-kart](5472487.xml).

```c++
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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get XML maps from the workbook
    auto xmlMaps = workbook.GetWorksheets().GetXmlMaps();

    // Export all XML data from all XML Maps from the Workbook
    for (int i = 0; i < xmlMaps.GetCount(); i++)
    {
        // Access the XML Map
        XmlMap map = xmlMaps.Get(i);

        // Exports its XML Data to file
        workbook.ExportXml(map.GetName(), outDir + map.GetName() + u".xml");
    }

    std::cout << "XML data exported successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
