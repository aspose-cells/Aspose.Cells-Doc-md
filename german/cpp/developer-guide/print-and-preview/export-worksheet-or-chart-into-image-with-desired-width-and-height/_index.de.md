---
title: Exportieren eines Arbeitsblatts oder Diagramms in ein Bild mit Wunschbreite und höhe mit C++
linktitle: Arbeitsblatt oder Diagramm in ein Bild mit gewünschter Breite und Höhe exportieren
type: docs
weight: 290
url: /de/cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/
description: Verwenden Sie Aspose.Cells, um Arbeitsblatt oder Diagramm in ein Bild mit gewünschter Breite und Höhe in C++ zu exportieren.
---

{{% alert color="primary" %}}

Sie können mit Aspose.Cells Ihr Arbeitsblatt oder Diagramm in ein Bild mit der gewünschten Breite und Höhe exportieren. Es bietet [**ImageOrPrintOptions.SetDesiredSize()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/setdesiredsize/) Methode, um die gewünschte Breite und Höhe des exportierten Bildes festzulegen. Die Breite und Höhe werden in Pixeln angegeben.

{{% /alert %}}

Der folgende Code exportiert das Arbeitsblatt in ein Bild mit der Größe 400x400.

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
