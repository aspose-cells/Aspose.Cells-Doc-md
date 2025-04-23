---
title: تحويل ورقة العمل إلى صورة وورقة العمل إلى صورة بواسطة الصفحة باستخدام C++
linktitle: تحويل ورقة العمل إلى صورة وورقة العمل إلى صورة بواسطة الصفحة
type: docs
weight: 80
url: /ar/cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/
description: تعلم كيفية تحويل ورقة العمل إلى ملف صورة وورقة عمل متعددة الصفحات إلى ملف صورة لكل صفحة باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

تم تصميم هذا الوثيقة لتزويد المطورين بفهم تفصيلي لكيفية تحويل ورقة العمل إلى ملف صورة وورقة عمل متعددة الصفحات إلى ملف صورة لكل صفحة.

في بعض الأحيان قد تحتاج إلى تقديم ورقات العمل على شكل صور، على سبيل المثال، لاستخدامها في التطبيقات أو صفحات الويب. قد تحتاج إلى إدراج الصور في مستند Word أو ملف PDF أو عرض PowerPoint، أو استخدامها في سيناريو آخر. ببساطة، ترغب في عرض ورقة العمل على شكل صورة. تدعم Aspose.Cells تحويل ورقات العمل في ملفات Microsoft Excel إلى صور. بالإضافة إلى ذلك، تدعم Aspose.Cells تحويل دفتر العمل إلى عدة ملفات صور، واحدة لكل صفحة.

قد تستخدم أتمتة Office لتحقيق ذلك، لكن للأتمتة عيوبها الخاصة. هناك العديد من الأسباب والمشكلات المطلوبة: على سبيل المثال، الأمان، الاستقرار، القابلية للتوسع/السرعة، السعر، والميزات. باختصار، هناك العديد من الأسباب، لكن السبب الرئيسي هو أن مايكروسوفت نفسها توصي بشدة بعدم الاعتماد على أتمتة Office.

{{% /alert %}}

## **استخدام Aspose.Cells لتحويل ورقة العمل إلى ملف صورة**

يوضح هذا المقال كيفية إنشاء تطبيق وحدة التحكم في فيجوال ستوديو، وتحويل ورقة العمل إلى صورة، وتحويل ورقة العمل إلى صورة واحدة لكل ورقة بمجرد وصف بسيط باستخدام واجهة برمجة التطبيقات Aspose.Cells.

تحتاج إلى تضمين مساحة أسماء [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) في برنامجك/مشروعك. لديها العديد من الفئات القيمة، مثل [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/)، [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)، [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/)، وهكذا. تمثل فئة [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) ورقة عمل لعرض الصور لورقة العمل ولديها طريقة [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/) محملة يمكن أن تحول ورقة العمل إلى ملفات صورة مباشرة مع أي سمات أو خيارات مضبوطة. يمكنها إرجاع كائن `System.Drawing.Bitmap`، ويمكنك حفظ ملف صورة على القرص/البث. تدعم العديد من تنسيقات الصور، على سبيل المثال، BMP، PNG، GIF، JPG، JPEG، TIFF، EMF، وغيرها.

يشرح هذا المقال كيفية:

- تحويل ورقة العمل إلى صورة
- تحويل كل صفحة في ورقة العمل إلى صورة

تظهر هذه المهمة كيفية استخدام Aspose.Cells لتحويل ورقة عمل من دفتر العمل القالب إلى ملف صورة.

### **إعداد المشروع**

1. أولاً، [قم بتحميل Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp).
1. قم بتثبيته على جهاز التطوير الخاص بك. تعمل جميع مكونات [Aspose](http://www.aspose.com/)، عند التثبيت، في وضع التقييم. لا يوجد حد زمني لوضع التقييم، ويقوم فقط بحقن علامات مائية في المستندات التي تم إنشاؤها. الآن، ابدأ Visual Studio وأنشئ تطبيق وحدة تحكم جديد. يستخدم هذا المثال تطبيق وحدة تحكم C++. أضف مرجعًا إلى Aspose.Cells في المشروع المُنشأ.

### **تحويل ورقة العمل إلى ملف صورة**

أنشأت دفتر عمل جديد في Microsoft Excel وأضفت بعض البيانات في ورقة العمل الأولى: **Testbook.xlsx** (ورقة عمل واحدة). ثم قم بتحويل ورقة العمل في الملف القالب Sheet1 إلى ملف صورة يُعرف باسم SheetImage.jpg.

التالي هو الكود الذي استخدمته العنصر لإنجاز المهمة. يحول Sheet1 في **Testbook.xlsx** إلى ملف صورة لشرح سهولة هذا التحويل.

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

std::string convert_u16_to_string(const U16String& u16str);

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheettoImageFile.xlsx");
    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions imgOptions;
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetImageType(ImageType::Jpeg);

    SheetRender sr(sheet, imgOptions);
    sr.ToImage(0, outDir + u"outputConvertWorksheettoImageFile.jpg");

    std::cout << "Worksheet converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **استخدام Aspose.Cells لتحويل ورقة العمل إلى ملف صورة بواسطة الصفحة**

يوضح هذا المثال كيفية استخدام Aspose.Cells لتحويل ورقة عمل من مصنف قوالب يحتوي على عدة صفحات إلى ملف صورة واحد لكل صفحة.

### **تحويل ورقة العمل إلى صورة حسب الصفحة**

لقد أنشأت ورق عمل جديد في Microsoft Excel وأضافت بعض البيانات في ورقة العمل الأولى: ملفTestbook2.xlsx (ورقة عمل واحدة).

الآن، قم بتحويل ورقة العمل Sheet1 في ملف القالب إلى ملفات صور (ملف واحد لكل صفحة). حيث أنني قمت بالفعل بإنشاء تطبيق الوحدة التحكم لأداء مهمة النسخ، سأتجاوز خطوات إنشاء تطبيق الوحدة التحكم تلك وأنتقل مباشرة إلى خطوات تحويل ورقة العمل.

وفيما يلي الكود الذي يستخدمه المكون لإنجاز المهمة. يقوم بتحويل الشريحة Sheet1 في Testbook2.xlsx إلى ملفات صورة حسب الصفحة.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

std::u16string intToU16String(int value) {
    std::u16string result;
    if (value == 0) {
        result.push_back(u'0');
        return result;
    }
    while (value > 0) {
        result.insert(result.begin(), static_cast<char16_t>(u'0' + (value % 10)));
        value /= 10;
    }
    return result;
}

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheetToImageByPage.xlsx");

    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);
    options.SetImageType(ImageType::Tiff);

    SheetRender sr(sheet, options);
    for (int j = 0; j < sr.GetPageCount(); j++)
    {
        std::u16string pageNum = intToU16String(j + 1);
        U16String fileName = outDir + U16String(u"outputConvertWorksheetToImageByPage_") + U16String(pageNum.c_str()) + U16String(u".tif");
        sr.ToImage(j, fileName);
    }

    std::cout << "Worksheet converted to images by page successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
