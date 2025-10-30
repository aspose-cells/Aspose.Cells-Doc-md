---
title: ImageOrPrintOptions ile PageIndex ve PageCount Özellikleri Kullanarak Sayfa Dizisini Render Etme
linktitle: Sayfa Dizisini Render Et
type: docs
weight: 110
url: /tr/cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/
description: Aspose.Cells kullanarak Excel dosyasından sayfa dizisini resimlere dönüştürün.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells ile Excel dosyanızın sayısız sayfaları olsa da bunlardan sadece bazılarını oluşturmak istiyorsanız, ImageOrPrintOptions'ın [**ImageOrPrintOptions.GetPageIndex()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpageindex/) ve [**ImageOrPrintOptions.GetPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpagecount/) özelliklerini kullanarak sayısal bir dizi oluşturabilirsiniz. Bu özellikler, iş sayfanızda çok fazla örneğin binlerce sayfa olsa da sadece bazılarını oluşturmak istiyorsanız faydalıdır. Bu, sadece işleme süresini değil aynı zamanda oluşturma sürecinin bellek tüketimini de kaydedecektir.

## **Görüntü veya Yazdırma Seçenekleri Kullanılarak Sayfa Dizisi Oluşturma**

Aşağıdaki örnek kod, [**ImageOrPrintOptions.GetPageIndex()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpageindex/) ve [**ImageOrPrintOptions.GetPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpagecount/) özelliklerini kullanarak örnek Excel dosyasını yükler ve yalnızca 4, 5, 6 ve 7 sayfaları oluşturur. İşte kod tarafından oluşturulan sayfaların oluşturulmuş görüntüleri.

|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2)|
| :- | :- |
|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4)|

## **Örnek Kod**

```cpp
#include <iostream>
#include <string>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(srcDir + u"sampleImageOrPrintOptions_PageIndexPageCount.xlsx");

    Worksheet ws = wb.GetWorksheets().Get(0);

    ImageOrPrintOptions opts;
    opts.SetPageIndex(3);
    opts.SetPageCount(4);
    opts.SetImageType(ImageType::Png);

    SheetRender sr(ws, opts);

    for (int i = opts.GetPageIndex(); i < sr.GetPageCount(); i++)
    {
        std::wstring pageNum = std::to_wstring(i + 1);
        U16String filePath = outDir + U16String(u"outputImage-") + 
            U16String(reinterpret_cast<const char16_t*>(pageNum.c_str())) + 
            U16String(u".png");
        sr.ToImage(i, filePath);
    }

    std::cout << "Images generated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
