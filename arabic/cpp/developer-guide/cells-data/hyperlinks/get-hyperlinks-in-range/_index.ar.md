---
title: الحصول على الروابط التشعبية في النطاق باستخدام C++
linktitle: الحصول على الارتباطات التشعبية في النطاق
type: docs
weight: 100
url: /ar/cpp/get-hyperlinks-in-range/
description: تعلم كيفية الحصول على الروابط التشعبية في النطاق من خلال API Aspose.Cells for C++.
keywords: الحصول على الروابط الفائقة في النطاق، الحصول على كل الروابط الفائقة في النطاق المحدد، حذف الرابط الفائق في النطاق، حذف الروابط الفائقة في النطاق المحدد
---

## **الحصول على الارتباطات التشعبية في النطاق**

توفر فئة [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) خاصية [**GetHyperlinks()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/gethyperlinks/) التي تُرجع كل روابط الصفحة العمل المحددة. يمكنك أيضًا حذف الرابط الفائق عن طريق استدعاء الأسلوب [**Hyperlink.Delete**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/delete/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"HyperlinksSample.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Range range = worksheet.GetCells().CreateRange(u"A2", u"B3");
    Vector<Hyperlink> hyperlinks = range.GetHyperlinks();

    for (int i = 0; i < hyperlinks.GetLength(); ++i)
    {
        Hyperlink& link = hyperlinks[i];
        std::cout << link.GetArea().ToString().ToUtf8() << " : " << link.GetAddress().ToUtf8() << std::endl;
        link.Delete();
    }

    workbook.Save(outDir + u"HyperlinksSample_out.xlsx");
    std::cout << "Hyperlinks processed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
