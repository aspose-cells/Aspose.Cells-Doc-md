---
title: Esporta dati XML collegati alla mappa XML all interno del Workbook con C++
linktitle: Esporta dati XML collegati alla mappa XML all interno del foglio di lavoro
type: docs
weight: 20
url: /it/cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/
description: Impara come esportare dati XML collegati alle Maps XML nel tuo workbook usando Aspose.Cells for C++.
---

## **Esporta dati XML collegati alla mappa XML all'interno del Workbook**

Per favore, utilizza il metodo [**Workbook::ExportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/exportxml/) per esportare dati XML collegati alle tue Maps XML nel workbook. Il seguente codice di esempio esporta i dati XML di tutte le Maps XML dal workbook una per una. Controlla il [file Excel di esempio](5115497.xlsx) usato in questo codice e i [dati XML esportati della prima Map XML](5472487.xml).

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
