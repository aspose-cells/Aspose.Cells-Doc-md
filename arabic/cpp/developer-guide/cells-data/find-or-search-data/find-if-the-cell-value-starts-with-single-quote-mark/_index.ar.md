---
title: البحث عما إذا كانت قيمة الخلية تبدأ بعلامة اقتباس مفردة باستخدام C++
linktitle: ابحث ما إذا كانت قيمة الخلية تبدأ بعلامة اقتباس واحدة.
type: docs
weight: 270
url: /ar/cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: تعلم كيفية البحث عما إذا كانت قيمة الخلية تبدأ بعلامة اقتباس مفردة عبر واجهة برمجة التطبيقات Aspose.Cells for C++.
keywords: العثور على قيمة الخلية التي تبدأ بعلامة اقتباس واحدة، البحث عن قيمة الخلية التي تبدأ بعلامة اقتباس واحدة
---

{{% alert color="primary" %}}

Aspose.Cells الآن يوفر خاصية [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) للعثور على ما إذا كانت قيمة الخلية تبدأ بعلامة اقتباس واحدة. قبل هذه الخاصية، لم يكن هناك طريقة للتمييز بين سلاسل مثل عينة و 'عينة وما إلى ذلك.

{{% /alert %}}

الشيفرة العينية التالية تشرح أن السلاسل مثل عينة و 'عينة لا يمكن تمييزها باستخدام الخاصية [**Cell::GetStringValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/). لذلك يجب علينا استخدام الخاصية [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) للتمييز بينهما.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Create worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Access cell A1 and A2
    Cell a1 = sheet.GetCells().Get(u"A1");
    Cell a2 = sheet.GetCells().Get(u"A2");

    // Add sample in A1 and sample with quote prefix in A2
    a1.PutValue(u"sample");
    a2.PutValue(u"'sample");

    // Print their string values, A1 and A2 both are same
    std::cout << "String value of A1: " << a1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "String value of A2: " << a2.GetStringValue().ToUtf8() << std::endl;

    // Access styles of A1 and A2
    Style s1 = a1.GetStyle();
    Style s2 = a2.GetStyle();

    std::cout << std::endl;

    // Check if A1 and A2 has a quote prefix
    std::cout << "A1 has a quote prefix: " << s1.GetQuotePrefix() << std::endl;
    std::cout << "A2 has a quote prefix: " << s2.GetQuotePrefix() << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
