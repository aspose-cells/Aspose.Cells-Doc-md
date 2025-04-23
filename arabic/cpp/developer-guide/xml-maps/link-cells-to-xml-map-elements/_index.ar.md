---
title: ربط الخلايا بعناصر خريطة XML باستخدام C++
linktitle: ربط الخلايا بعناصر خريطة XML
type: docs
weight: 50
url: /ar/cpp/link-cells-to-xml-map-elements/
description: تعلم كيفية ربط الخلايا بعناصر خريطة XML باستخدام Aspose.Cells مع C++.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك ربط خلاياك بعناصر خريطة XML باستخدام Aspose.Cells. يرجى استخدام الأسلوب [**Cells.LinkToXmlMap()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/linktoxmlmap/) لهذا الغرض.

## **ربط الخلايا بعناصر خريطة XML**

يقوم الكود العيني التالي بتحميل [ملف إكسل المصدري](5115471.xlsx) الذي يحتوي على خريطة XML ومن ثم يربط الخلايا A1، B2، C3، D4، E5، و F6 بعناصر خريطة XML FIELD1، FIELD2، FIELD4، FIELD5، FIELD7، و FIELD8 على التوالي ومن ثم يحفظ سجل العمل في [ملف إكسل المخرجات](5115467.xlsx).

إذا قمت بفتح [ملف إكسل المخرجات](5115467.xlsx) ونقرت على زر المطور > مصدر، سترى الخلايا مرتبطة بعناصر خريطة XML وسيتم إظهارها أيضًا من قبل Microsoft Excel كما هو موضح في هذه الصورة.

```cpp
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

    // Load sample workbook
    Workbook wb(srcDir + u"sample.xlsx");

    // Access the Xml Map inside it
    XmlMap map = wb.GetWorksheets().GetXmlMaps().Get(0);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Map FIELD1 and FIELD2 to cell A1 and B2
    ws.GetCells().LinkToXmlMap(map.GetName(), 0, 0, u"/root/row/FIELD1");
    ws.GetCells().LinkToXmlMap(map.GetName(), 1, 1, u"/root/row/FIELD2");

    // Map FIELD4 and FIELD5 to cell C3 and D4
    ws.GetCells().LinkToXmlMap(map.GetName(), 2, 2, u"/root/row/FIELD4");
    ws.GetCells().LinkToXmlMap(map.GetName(), 3, 3, u"/root/row/FIELD5");

    // Map FIELD7 and FIELD8 to cell E5 and F6
    ws.GetCells().LinkToXmlMap(map.GetName(), 4, 4, u"/root/row/FIELD7");
    ws.GetCells().LinkToXmlMap(map.GetName(), 5, 5, u"/root/row/FIELD8");

    // Save the workbook in xlsx format
    wb.Save(outDir + u"output.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
