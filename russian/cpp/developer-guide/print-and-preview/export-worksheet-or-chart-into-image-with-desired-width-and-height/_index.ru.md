---
title: Экспортировать рабочий лист или график в изображение с желаемой шириной и высотой с помощью C++
linktitle: Экспорт рабочего листа или диаграммы в изображение с желаемой шириной и высотой
type: docs
weight: 290
url: /ru/cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/
description: Используйте Aspose.Cells для экспорта рабочего листа или графика в изображение с желаемой шириной и высотой на C++.
---

{{% alert color="primary" %}}

Вы можете использовать Aspose.Cells для экспорта вашего листа или диаграммы в изображение с указанной шириной и высотой. Он предоставляет метод [**ImageOrPrintOptions.SetDesiredSize()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/setdesiredsize/) для установки желаемой ширины и высоты экспортированного изображения. Ширина и высота указываются в пикселях.

{{% /alert %}}

Приведенный ниже код экспортирует рабочий лист в изображение размером 400x400.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Source directory
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Create workbook object from source file
    Workbook workbook(sourceDir + u"sampleWorksheetToImageDesiredSize.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set image or print options
    ImageOrPrintOptions opts;
    opts.SetOnePagePerSheet(true);
    opts.SetImageType(Drawing::ImageType::Png);
    opts.SetDesiredSize(400, 400, false);

    // Render sheet into image
    SheetRender sr(worksheet, opts);
    sr.ToImage(0, outputDir + u"outputWorksheetToImageDesiredSize.png");

    std::cout << "Worksheet rendered to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{< app/cells/assistant language="cpp" >}}
