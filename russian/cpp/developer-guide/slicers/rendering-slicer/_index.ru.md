---
title: Отрисовка слайсера с помощью C++
type: docs
weight: 40
url: /ru/cpp/rendering-slicer/
description: Отрисуйте слайсеры в файлах Excel с помощью Aspose.Cells и C++.
---

## **Возможные сценарии использования**
Aspose.Cells поддерживает рендеринг формы срезки. Если вы конвертируете свой лист в изображение или сохраняете свою книгу в форматах PDF или HTML, вы увидите, что срезки правильно отрисованы.
## **Рендеринг срезки**
Следующий пример кода загружает [пример файла Excel](67338479.xlsx), содержащий существующий слайсер. Он преобразует лист в изображение, установив область печати, охватывающую только слайсер. На изображении показан [выходной файл изображения](67338480.png), демонстрирующий правильную отрисовку слайсера. Как видно, слайсер был отрисован правильно и выглядит так же, как в исходном файле Excel.

![todo:image_alt_text](rendering-slicer_1)
## **Образец кода**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing slicer.
    Workbook workbook(u"sampleRenderingSlicer.xlsx");

    // Access first worksheet.
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Set the print area because we want to render slicer only.
    ws.GetPageSetup().SetPrintArea(u"B15:E25");

    // Specify image or print options, set one page per sheet and only area to true.
    ImageOrPrintOptions imgOpts;
    imgOpts.SetHorizontalResolution(200);
    imgOpts.SetVerticalResolution(200);
    imgOpts.SetImageType(ImageType::Png);
    imgOpts.SetOnePagePerSheet(true);
    imgOpts.SetOnlyArea(true);

    // Create sheet render object and render worksheet to image.
    SheetRender sr(ws, imgOpts);
    sr.ToImage(0, u"outputRenderingSlicer.png");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
