---
title: Thumbnail des Arbeitsblatts mit C++ erstellen
linktitle: Thumbnail des Arbeitsblatts generieren
type: docs
weight: 110
url: /de/cpp/generate-thumbnail-of-the-worksheet/
description: Erstellen Sie Thumbnails von Arbeitsblättern als Bilder mit Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Es kann nützlich sein, Miniaturansichten aus Arbeitsblättern zu generieren. Eine Miniaturansicht ist ein kleines Bild, das in ein Word-Dokument oder eine PowerPoint-Präsentation eingefügt werden kann, um eine Vorschau dessen zu geben, was sich auf dem Arbeitsblatt befindet. Sie kann einer Webseite mit einem Link zum Download des Originaldokuments hinzugefügt werden und hat viele weitere Verwendungsmöglichkeiten.

{{% /alert %}} 

Aspose.Cells for C++ ermöglicht es, Arbeitsblätter in Bilddateien auszugeben, was die Generierung von Thumbnails erleichtert. Der folgende Beispielcode zeigt, wie man Arbeitsblätter mit C++ in Bilddateien ausgibt.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load source workbook
    Workbook book(srcDir + u"sampleGenerateThumbnailOfWorksheet.xlsx");

    // Configure image rendering options
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(ImageType::Bmp);
    imgOptions.SetVerticalResolution(200);
    imgOptions.SetHorizontalResolution(200);
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetDesiredSize(600, 600, true); // Set thumbnail dimensions

    // Access first worksheet
    WorksheetCollection worksheets = book.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Render worksheet to image
    SheetRender sr(sheet, imgOptions);
    sr.ToImage(0, outDir + u"outputGenerateThumbnailOfWorksheet.bmp");

    std::cout << "Worksheet thumbnail generated successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
