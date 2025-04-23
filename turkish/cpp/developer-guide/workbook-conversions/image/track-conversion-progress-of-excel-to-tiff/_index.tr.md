---
title: Excel den TIFF e Dönüşüm İlerleme Takibi (C++)
linktitle: Excel den TIFF e Dönüşüm İlerlemesini İzle
type: docs
weight: 190
url: /tr/cpp/track-conversion-progress-of-excel-to-tiff/
description: Aspose.Cells for C++ kullanarak Excel dosyalarının TIFF formatına dönüşüm ilerlemesini nasıl takip edeceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**

 Bazen büyük Excel dosyalarını dönüştürmek zaman alabilir. Bu süre boyunca, uygulamanızın kullanılabilirliğini artırmak için yalnızca yükleme ekranı yerine döküman dönüştürme ilerlemesini göstermek isteyebilirsiniz. Aspose.Cells, [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/) arayüzünü sağlayarak belge dönüşüm ilerlemesini takip etmeyi destekler. [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/) arayüzü, sizin özelleştirilmiş sınıfınızda uygulayabileceğiniz [**PageStartSaving**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/pagestartsaving/) ve [**PageEndSaving**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/pageendsaving/) metodlarını sağlar. Ayrıca, hangi sayfaların render edileceğini kontrol edebilirsiniz, bu da *TestPageSavingCallback* özel sınıfında gösterilmiştir.

## **Excel'den TIFF'e Dönüşüm İlerlemesini İzle**

 Aşağıdaki kod örneği, [**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/) arayüzünü uygulayan *TestPageSavingCallback* özel sınıfını kullanarak kaydettiğiniz kaynak Excel dosyasını (95584311.xlsx) yükler ve konsolda dönüşüm ilerlemesini gösterir. Oluşturulan çıktı dosyası örneğinize eklenmiştir.

[Output File](95584312.tiff)

## **Örnek Kod**

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

Aşağıdaki kod *TestTiffPageSavingCallback* özel sınıf için olan kodu içerir.

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

## **Konsol Çıktısı**

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
