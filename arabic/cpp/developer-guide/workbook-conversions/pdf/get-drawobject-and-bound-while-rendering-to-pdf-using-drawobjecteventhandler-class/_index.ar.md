---
title: الحصول على رسم الكائن و Bound أثناء التصيير إلى PDF باستخدام C++ وفئة DrawObjectEventHandler
linktitle: الحصول على رسم الكائن و Bound أثناء التصيير إلى PDF
type: docs
weight: 70
url: /ar/cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
description: تعلم كيفية استخدام فئة DrawObjectEventHandler في C++ لالتقاط رسم الكائن و Bound أثناء تصيير ملفات Excel إلى PDF أو صور.
---

## **سيناريوهات الاستخدام المحتملة**

توفر Aspose.Cells فئة مجردة [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) التي تحتوي على طريقة [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/). يمكن للمستخدم تنفيذ [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) واستخدام الطريقة [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/) للحصول على [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) وBound أثناء تقديم Excel إلى PDF أو صورة. فيما يلي وصف موجز لمعلمات طريقة [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/).

- drawObject: سيتم تهيئة [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) وإرجاعه أثناء التقديم

- x: اليسار من [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

- y: الأعلى من [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

- width: عرض [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

- height: ارتفاع [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

إذا كنت تصيّر ملف Excel إلى PDF، فيمكنك استخدام فئة [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) مع [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/). بالمثل، إذا كنت تصيّر ملف Excel إلى صورة، يمكنك استخدام فئة [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) مع [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/).

## **الحصول على كائن الرسم وBound أثناء التقديم إلى Pdf باستخدام فئة DrawObjectEventHandler**

يرجى الاطلاع على الكود البرمجي التالي. يقوم بتحميل ملف Excel النموذجي ([sample Excel file](64716821.xlsx)) ويحفظه كملف PDF خارجي ([output PDF](64716822.pdf)). أثناء التصدير إلى PDF، يستخدم خاصية [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) ويقوم بالتقاط [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) و Bound للخلايا والأشياء الموجودة، مثل الصور، وما إلى ذلك. إذا كان نوع [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) هو Cell، فإنه يعرض Bound والقيمة النصية. وإذا كان نوع [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) هو صورة، فإنه يعرض Bound واسم الشكل. يرجى الاطلاع على مخرجات وحدة التحكم للرمز البرمجي أدناه للمزيد من المساعدة.

## **الكود المثالي**

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

class ClsDrawObjectEventHandler : public DrawObjectEventHandler
{
public:
    void Draw(DrawObject& drawObject, float x, float y, float width, float height) override
    {
        std::cout << std::endl;

        if (drawObject.GetType() == DrawObjectEnum::Cell)
        {
            std::cout << "[X]: " << x << " [Y]: " << y << " [Width]: " << width << " [Height]: " << height 
                      << " [Cell Value]: " << drawObject.GetCell().GetStringValue().ToUtf8() << std::endl;
        }

        if (drawObject.GetType() == DrawObjectEnum::Image)
        {
            std::cout << "[X]: " << x << " [Y]: " << y << " [Width]: " << width << " [Height]: " << height 
                      << " [Shape Name]: " << drawObject.GetShape().GetName().ToUtf8() << std::endl;
        }

        std::cout << "----------------------" << std::endl;
    }
};

void Run()
{
    Workbook wb(u"sampleGetDrawObjectAndBoundUsingDrawObjectEventHandler.xlsx");
    PdfSaveOptions opts;
    auto drawObjectEventHandler = std::make_shared<ClsDrawObjectEventHandler>();
    opts.SetDrawObjectEventHandler(drawObjectEventHandler.get());
    wb.Save(u"outputGetDrawObjectAndBoundUsingDrawObjectEventHandler.pdf", opts);
}

int main()
{
    Aspose::Cells::Startup();
    Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مخرجات الوحدة**

{{< highlight java >}}

[X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
