---
title: Esporta il foglio di lavoro o il grafico in immagine con larghezza e altezza desiderate con C++
linktitle: Esporta un foglio di lavoro o un grafico in un immagine con larghezza e altezza desiderate
type: docs
weight: 290
url: /it/cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/
description: Usa Aspose.Cells per esportare il foglio di lavoro o il grafico in immagine con larghezza e altezza desiderate in C++.
---

{{% alert color="primary" %}}

Puoi usare Aspose.Cells per esportare il tuo foglio di lavoro o grafico in un'immagine con la larghezza e l'altezza desiderate. Fornisce un metodo [**ImageOrPrintOptions.SetDesiredSize()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/setdesiredsize/) per impostare la larghezza e l'altezza desiderate dell'immagine esportata. La larghezza e l'altezza sono specificate in unità di pixel.

{{% /alert %}}

Il seguente codice esporta il foglio di lavoro in un'immagine delle dimensioni 400x400.

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
