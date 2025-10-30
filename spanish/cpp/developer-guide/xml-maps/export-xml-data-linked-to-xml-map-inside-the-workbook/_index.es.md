---
title: Exportar datos XML vinculados al mapa XML dentro del libro de trabajo con C++
linktitle: Exportar datos XML vinculados al XML Map dentro del libro de trabajo
type: docs
weight: 20
url: /es/cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/
description: Aprenda cómo exportar datos XML vinculados a mapas XML dentro de su libro de trabajo usando Aspose.Cells for C++.
---

## **Exportar datos XML vinculados al mapa XML dentro del libro**

Por favor, usa el método [**Workbook::ExportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/exportxml/) para exportar datos XML vinculados a tus mapas XML dentro de tu libro de trabajo. El siguiente código de ejemplo exporta los datos XML de todos los mapas XML uno por uno. Revisa el [archivo de ejemplo de Excel](5115497.xlsx) usado en este código y los [datos XML exportados del primer mapa XML](5472487.xml).

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
