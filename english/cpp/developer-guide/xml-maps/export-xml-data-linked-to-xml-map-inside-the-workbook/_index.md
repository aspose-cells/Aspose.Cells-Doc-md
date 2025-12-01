---
title: Export XML Data linked to XML Map inside the Workbook with C++
linktitle: Export XML Data linked to XML Map inside the Workbook
type: docs
weight: 20
url: /cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/
description: Learn how to export XML data linked to XML Maps inside your workbook using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Export XML Data linked to XML Map inside the Workbook**

Please use the [**Workbook::ExportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/exportxml/) method to export XML data linked to your XML Maps inside your workbook. The following sample code exports XML data of all XML Maps from the workbook one by one. Please check the [sample excel file](5115497.xlsx) used in this code and the [exported XML data of the first XML Map](5472487.xml).

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
