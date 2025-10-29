---
title: تتبع تقدم تحويل Excel إلى TIFF باستخدام C++
linktitle: تتبع تقدم التحويل من إكسيل إلى TIFF
type: docs
weight: 190
url: /ar/cpp/track-conversion-progress-of-excel-to-tiff/
description: تعلم كيفية تتبع تقدم تحويل ملفات Excel إلى تنسيق TIFF باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

أحيانًا قد يستغرق تحويل ملفات Excel الكبيرة بعض الوقت. خلال هذا الوقت، قد ترغب في عرض تقدم تحويل المستند بدلاً من شاشة التحميل فقط لتعزيز قابلية استخدام التطبيق الخاص بك. يدعم Aspose.Cells تتبع تقدم تحويل المستند من خلال توفير واجهة [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/). توفر واجهة [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/) طرق [**PageStartSaving**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/pagestartsaving/) و [**PageEndSaving**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/pageendsaving/) التي يمكنك تنفيذها في فئتك المخصصة. يمكنك أيضًا السيطرة على الصفحات التي يتم تصييرها كما هو موضح في فئة *TestPageSavingCallback* المخصصة.

## **تتبع تقدّم تحويل Excel إلى TIFF**

يعرض المثال البرمجي التالي تحميل ملف Excel المصدر (95584311.xlsx) وطباعة تقدم التحويل في وحدة التحكم باستخدام فئة *TestPageSavingCallback* التي تنفذ واجهة [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/). الملف الناتج المرفق هو مرجع لك.

[Output File](95584312.tiff)

## **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class TestTiffPageSavingCallback : public IPageSavingCallback {
public:
    void PageStartSaving(PageStartSavingArgs& args) override {
        // Implement page start saving logic here
    }

    void PageEndSaving(PageEndSavingArgs& args) override {
        // Implement page end saving logic here
    }
};

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"sampleUseWorkbookRenderForImageConversion.xlsx");

    ImageOrPrintOptions opts;
    opts.SetPageSavingCallback(new TestTiffPageSavingCallback());
    opts.SetImageType(Aspose::Cells::Drawing::ImageType::Tiff);

    WorkbookRender wr(workbook, opts);
    wr.ToImage(outDir + u"DocumentConversionProgressForTiff_out.tiff");

    std::cout << "Document converted to TIFF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

الكود التالي لصنف TestTiffPageSavingCallback المخصص.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

class TestTiffPageSavingCallback : public IPageSavingCallback
{
public:
    void PageStartSaving(PageStartSavingArgs& args) override
    {
        std::cout << "Start saving page index " << args.GetPageIndex() << " of pages " << args.GetPageCount() << std::endl;

        // Don't output pages before page index 2.
        if (args.GetPageIndex() < 2)
        {
            args.SetIsToOutput(false);
        }
    }

    void PageEndSaving(PageEndSavingArgs& args) override
    {
        std::cout << "End saving page index " << args.GetPageIndex() << " of pages " << args.GetPageCount() << std::endl;

        // Don't output pages after page index 8.
        if (args.GetPageIndex() >= 8)
        {
            args.SetHasMorePages(false);
        }
    }
};
```

## **مخرجات الوحدة**

{{< highlight java >}}

Start saving page index 0 of pages 10</br>
End saving page index 0 of pages 10</br>
Start saving page index 1 of pages 10</br>
End saving page index 1 of pages 10</br>
Start saving page index 2 of pages 10</br>
End saving page index 2 of pages 10</br>
Start saving page index 3 of pages 10</br>
End saving page index 3 of pages 10</br>
Start saving page index 4 of pages 10</br>
End saving page index 4 of pages 10</br>
Start saving page index 5 of pages 10</br>
End saving page index 5 of pages 10</br>
Start saving page index 6 of pages 10</br>
End saving page index 6 of pages 10</br>
Start saving page index 7 of pages 10</br>
End saving page index 7 of pages 10</br>
Start saving page index 8 of pages 10</br>
End saving page index 8 of pages 10</br>

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
