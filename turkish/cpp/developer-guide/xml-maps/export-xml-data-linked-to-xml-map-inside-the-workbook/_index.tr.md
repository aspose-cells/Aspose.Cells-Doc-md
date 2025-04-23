---
title: Çalışma kitabı içinde bağlı olan XML Verileri XML Haritası ile dışa aktarın (C++)
linktitle: Çalışma Kitabının İçine Bağlı XML Haritasından XML Verilerini Dışa Aktar
type: docs
weight: 20
url: /tr/cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/
description: Çalışma kitabınızdaki XML Haritalarıyla bağlı XML verilerini Dışa Aktarmayı öğrenin (Aspose.Cells for C++ ile)
---

## **Çalışma Kitabı içinde XML Haritasına bağlı XML Verilerini Dışa Aktar**

Lütfen çalışma kitabınızdaki XML Haritalarınıza bağlı XML verisini ihraç etmek için [**Workbook::ExportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/exportxml/) yöntemini kullanın. Aşağıdaki örnek kod, çalışma kitabındaki tüm XML Haritalarını tek tek ihraç eder. Bu kodda kullanılan [örnek excel dosyasını](5115497.xlsx) ve [birinci XML Haritasının ihraç edilen XML verisini](5472487.xml) kontrol edin.

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
