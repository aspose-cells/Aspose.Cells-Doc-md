---
title: Çizim Nesnesi ve Sınırlama Bilgisini (DrawObject ve Bound) PDF ye Dönüşüm Sırasında Alma (C++)
linktitle: PDF ye Dönüşüm Sırasında Çizim Nesnesi ve Sınırlama Bilgisini Alma
type: docs
weight: 70
url: /tr/cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
description: C++ dilinde DrawObject ve Bound bilgilerini yakalamak için DrawObjectEventHandler sınıfını kullanmayı öğrenin, Excel dosyalarını PDF veya resimlere dönüştürürken.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) isimli soyut bir sınıf sunar, kullanıcı [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/) metodunu uygulayabilir ve Excel dosyasını PDF veya görüntüye render ederken [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) metodunu kullanarak DrawObject ve Bound alabilir. Aşağıdaki, [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/) metodunun parametrelerinin kısa bir açıklaması yer almaktadır.

- drawObject: Render edilirken [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) başlatılır ve döndürülür

- x: [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)'nın solu

- y: [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)'nın üstü

- width:[**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)'nın genişliği

- height: [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)'nın yüksekliği

Eğer bir Excel dosyasını PDF'ye dönüştürüyorsanız, [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) sınıfını [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) ile kullanabilirsiniz. Benzer şekilde, Excel dosyasını Görüntüye dönüştürüyorsanız, [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) sınıfını ve [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) ile kullanabilirsiniz.

## **DrawObjectEventHandler sınıfını kullanarak PDF'ye render ederken DrawObject ve Bound almak**

Lütfen aşağıdaki örnek koda göz atın. Bu kod, [örnek Excel dosyasını](64716821.xlsx) yükler ve [çıktı PDF'sini](64716822.pdf) kaydeder. PDF'ye dönüştürürken, [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) özelliğini kullanır ve mevcut hücreler ile nesne (resim vb.) sınırlarını yakalar. Eğer türü Cell ise, sınırını ve StringValue'sunu yazdırır. Eğer türü Image ise, sınırını ve Shape adını gösterir. Daha fazla yardım için aşağıdaki örnek kodun konsol çıktılarına bakabilirsiniz.

## **Örnek Kod**

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

## **Konsol Çıktısı**

{{< highlight java >}}

[X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
