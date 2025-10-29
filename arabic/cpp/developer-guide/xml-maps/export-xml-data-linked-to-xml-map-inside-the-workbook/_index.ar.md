---
title: تصدير بيانات XML المرتبطة بخريطة XML داخل ملف العمل باستخدام C++
linktitle: تصدير بيانات XML المرتبطة بخريطة XML داخل دفتر العمل
type: docs
weight: 20
url: /ar/cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/
description: تعلم كيفية تصدير بيانات XML المرتبطة بخريطات XML داخل مصنفك باستخدام Aspose.Cells for C++.
---

## **تصدير البيانات XML المرتبطة بخريطة XML داخل الكتيب**

يرجى استخدام طريقة [**Workbook::ExportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/exportxml/) لتصدير بيانات XML المرتبطة بخريطات XML داخل مصنفك. يوضح الكود النموذجي التالي تصدير بيانات XML لجميع خرائط XML من المصنف واحدة تلو الأخرى. يرجى مراجعة [ملف إكسل النموذجي](5115497.xlsx) المستخدم في هذا الكود و[بيانات XML المصدرة من أول خريطة XML](5472487.xml).

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
