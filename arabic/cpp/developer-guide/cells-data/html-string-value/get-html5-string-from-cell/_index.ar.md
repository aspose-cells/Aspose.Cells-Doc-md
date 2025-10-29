---
title: الحصول على سلسلة HTML5 من الخلية مع C++
linktitle: الحصول على سلسلة HTML5 من الخلية
type: docs
weight: 90
url: /ar/cpp/get-html5-string-from-cell/
description: تعلم كيفية الحصول على سلسلة HTML5 من خلية باستخدام API Aspose.Cells for C++.
keywords: الحصول على سلسلة HTML5 من الخلية، الحصول على سلسلة HTML5 من الخلية، إدارة سلسلة HTML5 للخلية
---

## **سيناريوهات الاستخدام المحتملة**

تُعيد Aspose.Cells سلسلة HTML للخلية باستخدام الطريقة [**GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) التي تقبل معلمة منطقية. إذا قمت بتمرير **false** كمعامل، فسيتم إرجاع HTML عادي، وإذا قمت بتمرير **true**، فسيتم إرجاع سلسلة HTML5.

## ** الحصول على سلسلة HTML5 من الخلية**

يقوم الكود النموذجي التالي بإنشاء كائن جدول بيانات ويضيف بعض النص في الخلية A1 للورقة العمل الأولى. يتم الحصول بعد ذلك على السلسلة العادية لـ HTML وسلسلة HTML5 من الخلية A1 باستخدام الأسلوب  [**GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) ويتم طباعتها على وحدة التحكم.

## **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell A1 and put some text inside it
    Cell cell = ws.GetCells().Get(u"A1");
    cell.PutValue(u"This is some text.");

    // Get the Normal and Html5 strings
    U16String strNormal = cell.GetHtmlString(false);
    U16String strHtml5 = cell.GetHtmlString(true);

    // Print the Normal and Html5 strings on console
    std::cout << "Normal:\r\n" << strNormal.ToUtf8() << std::endl;
    std::cout << std::endl;
    std::cout << "Html5:\r\n" << strHtml5.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مخرجات الوحدة**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
