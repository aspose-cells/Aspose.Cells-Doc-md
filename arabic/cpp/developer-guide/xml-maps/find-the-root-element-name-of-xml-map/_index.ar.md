---
title: اعثر على اسم عنصر الجذر لخريطة XML باستخدام C++
linktitle: العثور على اسم العنصر الجذري لخريطة XML
type: docs
weight: 30
url: /ar/cpp/find-the-root-element-name-of-xml-map/
description: تعلم كيفية العثور على اسم عنصر الجذر لخريطة XML باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك العثور على *اسم العنصر الجذري لخريطة XML* باستخدام Aspose.Cells بخاصية [**XmlMap.GetRootElementName()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmap/getrootelementname/). اللقطة الشاشية التالية توضح اسم العنصر الجذري لخريطة XML في Microsoft Excel.

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **الكود المثالي**

يقوم الكود العيني التالي بتحميل [ملف إكسل عيني](55541789.xlsx) والوصول إلى أول خريطة XML وطباعة خاصيتها [**XmlMap.GetRootElementName()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmap/getrootelementname/). يرجى الاطلاع على مخرجات الوحدة للكود العيني المعطى أدناه.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleRootElementNameOfXmlMap.xlsx";

    // Load sample Excel file having Xml Map
    Workbook wb(inputFilePath);

    // Access first Xml Map inside the Workbook
    XmlMap xmap = wb.GetWorksheets().GetXmlMaps().Get(0);

    // Print Root Element Name of Xml Map on Console
    std::cout << "Root Element Name Of Xml Map: " << xmap.GetRootElementName().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مخرجات الوحدة**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
