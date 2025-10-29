---
title: تجنب تدوين الأرقام الكبيرة في الصيغة الأسية أثناء الاستيراد من HTML باستخدام C++
linktitle: تجنب العلامة العلمية للأرقام الكبيرة أثناء الاستيراد من HTML
type: docs
weight: 10
url: /ar/cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: تعلم كيفية تجنب تدوين الأرقام الكبيرة في الصيغة الأسية أثناء الاستيراد من HTML باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

 أحيانًا يتضمن HTML الخاص بك أرقامًا طويلة مثل 1234567890123456 والتي تتجاوز 15 رقمًا، وعند استيراد HTML إلى ملف إكسل، تتغير هذه الأرقام إلى صيغة أُسية مثل 1.23457E+15. إذا كنت تريد استيراد الرقم كما هو وعدم تحويله إلى صيغة أُسية، يرجى استخدام خاصية [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/cpp/aspose.cells/abstracttextloadoptions/getkeepprecision/) وتعيينها إلى **true** أثناء تحميل HTML الخاص بك.

{{% /alert %}}

 يوضح الكود النموذجي التالي كيفية استخدام خاصية [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/cpp/aspose.cells/abstracttextloadoptions/getkeepprecision/). ستقوم الـ API باستيراد الرقم كما هو دون تحويله إلى صيغة أُسية.

```c++
#include <iostream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Startup();

    U16String html = u"<html><body><p>1234567890123456</p></body></html>";

    std::vector<uint8_t> byteArray;
    for (int32_t i = 0; i < html.GetLength(); ++i)
    {
        char16_t c = html[i];
        if (c <= 0x7F)
            byteArray.push_back(static_cast<uint8_t>(c));
    }

    HtmlLoadOptions loadOptions = HtmlLoadOptions(LoadFormat::Html);
    loadOptions.SetKeepPrecision(true);

    Vector<uint8_t> data(byteArray.data(), static_cast<int32_t>(byteArray.size()));
    Workbook workbook(data, loadOptions);

    Worksheet sheet = workbook.GetWorksheets().Get(0);
    sheet.AutoFitColumns();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(outDir + u"outputAvoidExponentialNotationWhileImportingFromHtml.xlsx", SaveFormat::Xlsx);

    std::cout << "File saved successfully." << std::endl;

    Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
