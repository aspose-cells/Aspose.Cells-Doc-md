---
title: İstenilen Genişlik ve Yükseklikte Çalışma Sayfası veya Grafik Dışa Aktarma (C++)
linktitle: İstenen Genişlik ve Yükseklikte Çalışma Sayfasını veya Şekli Görüntüye Dışa Aktar
type: docs
weight: 290
url: /tr/cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/
description: Aspose.Cells kullanarak çalışma sayfasını veya grafiği istenen genişlik ve yükseklikte dışa aktarın C++ ile.
---

{{% alert color="primary" %}}

Aspose.Cells'ı kullanarak çalışma sayfasını veya şekli istenen genişlik ve yükseklikte bir görüntüye dışa aktarabilirsiniz. Dışa aktarılan görüntünün istenen genişlik ve yüksekliğini ayarlamak için [**ImageOrPrintOptions.SetDesiredSize()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/setdesiredsize/) yöntemini sağlar. Genişlik ve yükseklik piksel biriminde belirtilir.

{{% /alert %}}

Aşağıdaki kod çalışma sayfasını 400x400 boyutunda bir görüntüye dışa aktarır.

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
