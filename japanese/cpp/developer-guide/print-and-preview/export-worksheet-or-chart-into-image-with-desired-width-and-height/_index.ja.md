---
title: シートまたはチャートを desired な幅と高さの画像にエクスポート（C++）
linktitle: 所定の幅と高さでワークシートまたはグラフをイメージにエクスポート
type: docs
weight: 290
url: /ja/cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/
description: Aspose.Cells を使用し、希望の幅と高さでシートまたはチャートを画像にエクスポート（C++）
---

{{% alert color="primary" %}}

Aspose.Cellsを使用して、所定の幅と高さでワークシートまたはグラフをイメージにエクスポートできます。エクスポートされるイメージの幅と高さを指定するための[**ImageOrPrintOptions.SetDesiredSize()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/setdesiredsize/) メソッドを提供します。幅と高さはピクセル単位で指定されます。

{{% /alert %}}

次のコードは、400x400のサイズでワークシートをイメージにエクスポートします。

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
