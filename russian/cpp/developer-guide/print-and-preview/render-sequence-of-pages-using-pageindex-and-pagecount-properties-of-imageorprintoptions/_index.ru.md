---
title: Рендер последовательности страниц с использованием свойств PageIndex и PageCount в ImageOrPrintOptions с C++
linktitle: Рендер последовательности страниц
type: docs
weight: 110
url: /ru/cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/
description: Рендер последовательности страниц из файла Excel в изображения с помощью Aspose.Cells с C++.
---

## **Возможные сценарии использования**

Вы можете воспроизвести последовательность страниц вашего Excel-файла на изображения с использованием Aspose.Cells с [**ImageOrPrintOptions.GetPageIndex()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpageindex/) и [**ImageOrPrintOptions.GetPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpagecount/) свойствами. Эти свойства полезны, когда имеется много, например, тысячи страниц в вашем рабочем листе, но вы хотите воспроизвести только некоторые из них. Это не только сэкономит время обработки, но и сэкономит потребление памяти процесса воспроизведения.

## **Отобразить последовательность страниц с использованием свойств PageIndex и PageCount класса ImageOrPrintOptions**

В следующем образцовом коде загружается [образец Excel-файла](55541781.xlsx) и воспроизводятся только страницы 4, 5, 6 и 7 с использованием [**ImageOrPrintOptions.GetPageIndex()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpageindex/) и [**ImageOrPrintOptions.GetPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpagecount/) свойств. Вот воспроизведенные страницы, созданные кодом.

|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2)|
| :- | :- |
|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4)|

## **Образец кода**

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
