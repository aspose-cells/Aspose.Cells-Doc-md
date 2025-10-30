---
title: C++ ile Belge Dönüşüm Sürecini Takip Edin
linktitle: Belge Dönüşüm İlerlemesini İzle
type: docs
weight: 970
url: /tr/cpp/track-document-conversion-progress/
description: Aspose.Cells kullanarak C++ ta belge dönüşüm sürecini nasıl takip edeceğinizi öğrenin ve uygulama kullanılabilirliğini artırın.
---

## **Olası Kullanım Senaryoları**

Bazen büyük Excel dosyalarını dönüştürmek zaman alabilir. Bu süre boyunca, uygulamanızın kullanılabilirliğini artırmak için yalnızca yükleniyor ekranı yerine belge dönüşüm ilerlemesini göstermek isteyebilirsiniz. Aspose.Cells, [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/) arayüzü sağlayarak belge dönüşüm sürecini takip etmeyi destekler. [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/) arayüzü, uygulayacağınız [**PageStartSaving**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/pagestartsaving/) ve [**PageEndSaving**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/pageendsaving/) metodlarını sunar. Ayrıca, `TestPageSavingCallback` özel sınıfında gösterildiği gibi, hangi sayfaların gösterileceğini de kontrol edebilirsiniz.

## **Belge Dönüşüm İlerlemesini İzle**

Aşağıdaki kod örneği, [kaynak Excel dosyasını](94896151.xlsx) yükler ve `TestPageSavingCallback` özel sınıfını kullanarak dönüşüm ilerlemesini konsolda yazdırır ve [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/) arayüzünü uygular.

## **Örnek Kod**

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

Aşağıdaki, `TestPageSavingCallback` özel sınıfının kodudur.

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

## **Konsol Çıktısı**

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
