---
title: حذف الفراغات الزائدة بعد فاصل السطر عند استيراد HTML باستخدام C++
linktitle: حذف المسافات الزائدة بعد فواصل الأسطر أثناء استيراد HTML
type: docs
weight: 20
url: /ar/cpp/delete-redundant-spaces-after-line-break-while-importing/
description: تعرف على كيفية حذف الفراغات الزائدة بعد فواصل السطور عند استيراد HTML باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

يرجى استخدام الخاصية [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getdeleteredundantspaces/) وتعيينها **true** لحذف جميع المسافات الزائدة التي تأتي بعد وسم فاصل الأسطر. بشكل افتراضي، تكون هذه الخاصية **false** ويتم الاحتفاظ بالمسافات الزائدة في ملفات Excel الناتجة.

{{% /alert %}}

## تأثير تعيين خاصية HTMLLoadOptions.DeleteRedundantSpaces بقيمة false و true

تُظهر اللقطة الشاشة التالية تأثير تعيين هذه الخاصية إلى **false** و **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## حذف المسافات الزائدة بعد فواصل الأسطر أثناء استيراد HTML

### مثال برمجي

الكود البرمجي التالي يُظهر استخدام خاصية [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getdeleteredundantspaces/). الرجاء تعيينها **true** أو **false** للحصول على الناتج كما هو موضح في اللقطة الشاشة أعلاه.

```c++
#include <iostream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String html = u8"<html> <body> <table> <tr> <td> <br>    This is sample data <br>    This is sample data<br>    This is sample data</td> </tr> </table> </body> </html>";

    std::vector<uint8_t> byteArray;
    for (int32_t i = 0; i < html.GetLength(); ++i)
    {
        char16_t c = html[i];
        if (c <= 0x7F)
            byteArray.push_back(static_cast<uint8_t>(c));
    }

    HtmlLoadOptions loadOptions(LoadFormat::Html);
    loadOptions.SetDeleteRedundantSpaces(true);

    Vector<uint8_t> data(byteArray.data(), static_cast<int32_t>(byteArray.size()));
    Workbook workbook(data, loadOptions);

    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);
    sheet.AutoFitColumns();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(outDir + u"outputDeleteRedundantSpacesWhileImportingFromHtml.xlsx", SaveFormat::Xlsx);

    std::cout << "File saved successfully." << std::endl;

    Cleanup();

    Aspose::Cells::Cleanup();
    return 0;
}
```
