---
title: البحث عن خلايا ذات نمط معين باستخدام C++
linktitle: العثور على الخلايا ذات النمط المحدد
type: docs
weight: 190
url: /ar/cpp/find-cells-with-specific-style/
description: تعلم كيفية البحث أو إيجاد خلايا ذات نمط معين بواسطة واجهة برمجة التطبيقات Aspose.Cells for C++.
keywords: البحث عن الخلايا ذات النمط المحدد، البحث عن الخلايا ذات النمط المحدد
---

{{% alert color="primary" %}}

في بعض الأحيان، تحتاج إلى العثور على الخلايا ذات النمط المحدد. يمكنك استخدام Aspose.Cells للعثور على جميع الخلايا ذات النمط المشترك. توفر Aspose.Cells الخاصية [**FindOptions.GetStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/findoptions/getstyle/) التي يمكنك استخدامها لتحديد النمط الخاص للبحث عن الخلايا.

{{% /alert %}}

الشفرة في هذا المثال تجد جميع الخلايا التي لها نفس النمط مثل الخلية A1. بعد تنفيذ الشفرة، تحتوي جميع الخلايا التي لها نفس النمط كما في A1 على نص "تم العثور".

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String filePath = srcDir + u"TestBook.xlsx";

    Workbook workbook(filePath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Style style = worksheet.GetCells().Get(u"A1").GetStyle();

    FindOptions options;
    options.SetStyle(style);

    Cell nextCell;

    do
    {
        nextCell = worksheet.GetCells().Find(U16String(), nextCell, options);
        if (nextCell.GetRow() == -1)
            break;
        nextCell.PutValue(u"Found");
    } while (true);

    U16String outputPath = outDir + u"output.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
