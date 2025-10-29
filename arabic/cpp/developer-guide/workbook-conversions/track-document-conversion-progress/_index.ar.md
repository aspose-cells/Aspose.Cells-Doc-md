---
title: تتبع تقدم تحويل المستند باستخدام C++
linktitle: تتبع تقدم تحويل الوثائق
type: docs
weight: 970
url: /ar/cpp/track-document-conversion-progress/
description: تعلم كيف تتبع تقدم تحويل المستندات في C++ باستخدام Aspose.Cells لتعزيز قابلية استخدام التطبيق الخاص بك.
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان قد يستغرق تحويل ملفات Excel الكبيرة بعض الوقت. خلال هذا الوقت، قد ترغب في عرض تقدم تحويل المستند بدلًا من شاشة تحميل فقط لتعزيز قابلية استخدام تطبيقك. يدعم Aspose.Cells تتبع تقدم تحويل المستند عبر تقديم الواجهة [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/). توفر الواجهة [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/) طرق [**PageStartSaving**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/pagestartsaving/) و [**PageEndSaving**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/pageendsaving/) التي يمكنك تنفيذها في فئتك المخصصة. يمكنك أيضًا التحكم في الصفحات التي يتم تقديمها كما هو موضح في فئة `TestPageSavingCallback` المخصصة.

## **تتبع تقدم تحويل الوثائق**

يعتمد المثال التالي على تحميل ملف Excel المصدر [94896151.xlsx](94896151.xlsx) ويطبع تقدمه في لوحة التحكم باستخدام فئة `TestPageSavingCallback` التي تنفذ الواجهة [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/).

## **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class TestPageSavingCallback : public IPageSavingCallback
{
public:
    void PageStartSaving(PageStartSavingArgs& args) override
    {
        std::cout << "Page " << args.GetPageIndex() + 1 << " is starting to save." << std::endl;
    }

    void PageEndSaving(PageEndSavingArgs& args) override
    {
        std::cout << "Page " << args.GetPageIndex() + 1 << " has been saved." << std::endl;
    }
};

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String inputFilePath = srcDir + u"PagesBook1.xlsx";
    U16String outputFilePath = outDir + u"DocumentConversionProgress.pdf";

    Workbook workbook(inputFilePath);
    PdfSaveOptions pdfSaveOptions;

    TestPageSavingCallback callback;
    pdfSaveOptions.SetPageSavingCallback(&callback);

    workbook.Save(outputFilePath, pdfSaveOptions);

    std::cout << "Document conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

المثال التالي هو الكود الخاص بفئة `TestPageSavingCallback` المخصصة.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

class TestPageSavingCallback : public IPageSavingCallback
{
public:
    void PageStartSaving(PageStartSavingArgs& args) override
    {
        std::cout << "Start saving page index " << args.GetPageIndex() 
                  << " of pages " << args.GetPageCount() << std::endl;

        if (args.GetPageIndex() < 2)
        {
            args.SetIsToOutput(false);
        }
    }

    void PageEndSaving(PageEndSavingArgs& args) override
    {
        std::cout << "End saving page index " << args.GetPageIndex() 
                  << " of pages " << args.GetPageCount() << std::endl;

        if (args.GetPageIndex() >= 8)
        {
            args.SetHasMorePages(false);
        }
    }
};
```

## **مخرجات الوحدة**

{{< highlight java >}}

Start saving page index 0 of pages 11</br>
End saving page index 0 of pages 11</br>
Start saving page index 1 of pages 11</br>
End saving page index 1 of pages 11</br>
Start saving page index 2 of pages 11</br>
End saving page index 2 of pages 11</br>
Start saving page index 3 of pages 11</br>
End saving page index 3 of pages 11</br>
Start saving page index 4 of pages 11</br>
End saving page index 4 of pages 11</br>
Start saving page index 5 of pages 11</br>
End saving page index 5 of pages 11</br>
Start saving page index 6 of pages 11</br>
End saving page index 6 of pages 11</br>
Start saving page index 7 of pages 11</br>
End saving page index 7 of pages 11</br>
Start saving page index 8 of pages 11</br>
End saving page index 8 of pages 11

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
