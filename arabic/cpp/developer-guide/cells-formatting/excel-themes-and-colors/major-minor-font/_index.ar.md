---
title: ترويسات وخطوة السمة للنص مع C++
linktitle: سمات العناوين والنص الأساسي للسمات
description: تعد Aspose.Cells مكتبة C++ للعمل مع ملفات جداول البيانات، وتدعم تعيين خطوط السمة للترويسات والجسد في مستندات Excel، مما يمكّن المستخدمين من تخصيص مظهر ونمط المستند. سيتناول هذا المقال كيفية استخدام المكتبة للعمل مع خطوط السمة للترويسات والجسد في مستندات Excel.
keywords: Aspose.Cells, مستند Excel, عنوان, نص أساسي, خط سمة, مظهر, أسلوب
type: docs
weight: 120
url: /ar/cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

سيتم تغيير الخط الافتراضي تلقائيًا عند تغيير إعداد المنطقة.

إذا تم تغيير الخط الافتراضي، ستتم أيضًا تغيير ارتفاع الصف وعرض العمود، وقد يؤدي ذلك إلى تخريب تخطيط الصفحة.

ما الذي تسبب تغيير الخط الافتراضي؟

إذا تم ضبط خط السمة في Excel، فإن Excel سيقوم تلقائيًا بالتبديل بين خطوط مختلفة استنادًا إلى بيئة اللغة الحالية.

{{% /alert %}}

## **سمات العناوين والنص الأساسي للسمات في Excel**

في Excel، اختر تبويب الصفحة الرئيسية، وانقر على صندوق قائمة الخط، سترى "خطوط السمة" مع خطين من خطوط السمة: Calibri Light (عناوين) و Calibri (الجسد) على الأعلى مع إعداد المنطقة الإنجليزية.

**![سمات الخطوط](Theme-Fonts.png)**

إذا تم اختيار خط السمة، فسيعرض اسم الخط بشكل مختلف في مناطق مختلفة.
إذا كنت لا تريد أن يتغير الخط تلقائيًا في المناطق المختلفة، فلا تحدد خطي السمة.

## **تغيير خطوط العناوين والجسد برمجياً**
باستخدام Aspose.Cells for C++، يمكننا التحقق مما إذا كان الخط الافتراضي هو خط سمة أو تعيين خط السمة باستخدام خاصية [**Font.GetSchemeType()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getschemetype/).

يظهر الرمز البرمجي العيني التالي كيفية التلاعب بخط السمة.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object
    Workbook workbook(u"Book1.xlsx");

    // Get the default style
    Style defaultStyle = workbook.GetDefaultStyle();

    // Get the font scheme type
    FontSchemeType schemeType = defaultStyle.GetFont().GetSchemeType();

    // Check if the font is a theme font
    if (schemeType == FontSchemeType::Major || schemeType == FontSchemeType::Minor)
    {
        std::cout << "It's theme font" << std::endl;
    }

    // Change theme font to normal font
    defaultStyle.GetFont().SetSchemeType(FontSchemeType::None);

    // Set the modified default style back to the workbook
    workbook.SetDefaultStyle(defaultStyle);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **الحصول ديناميكيًا على خط السمة المحلي برمجياً**
في بعض الأحيان، يكون خوادمنا وأجهزة المستخدمين غير في نفس الإقليم. كيف يمكننا الحصول على نفس الخط الذي يرغب المستخدمون فيه لمعالجة الملف؟

علينا تعيين إعدادات المنطقة للنظام قبل تحميل الملف باستخدام الخاصية [**LoadOptions.GetRegion()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getregion/).

يُظهر نموذج الشفرة التالي كيفية الحصول على خط السمة المحلي.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new LoadOptions
    LoadOptions options;

    // Set the customer's region to Japan
    options.SetRegion(CountryCode::Japan);

    // Instantiate a new Workbook with the specified options
    Workbook workbook(u"Book1.xlsx", options);

    // Get the default style of the workbook
    Style defaultStyle = workbook.GetDefaultStyle();

    // Get the customer's local font name
    U16String localFontName = defaultStyle.GetFont().GetName();

    std::cout << "Local Font Name: " << localFontName.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
