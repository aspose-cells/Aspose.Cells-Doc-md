---
title: Экспортировать данные XML, связанные с XML картой внутри рабочей книги, с помощью C++
linktitle: Экспорт данных XML, связанных с XML схемой внутри книги
type: docs
weight: 20
url: /ru/cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/
description: Узнайте, как экспортировать XML данные, связанные с XML картами внутри вашей рабочей книги, используя Aspose.Cells for C++.
---

## **Экспорт XML-данных, связанных с XML-схемой, внутри книги**

Пожалуйста, используйте метод [**Workbook::ExportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/exportxml/) для экспорта XML-данных, связанных с вашими XML-картами внутри рабочей книги. Следующий пример кода экспортирует XML-данные всех XML-карт из рабочей книги по очереди. Пожалуйста, проверьте [пример файла Excel](5115497.xlsx), используемый в этом коде, и [экспортированные XML-данные первой XML-карты](5472487.xml).

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
