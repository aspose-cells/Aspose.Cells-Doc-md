---
title: Arbeitsblatt in Bild umwandeln  Entfernen von Leerraum um Daten mit C++
linktitle: Arbeitsblatt in Bild umwandeln  Entfernen von Leerraum um Daten
type: docs
weight: 40
url: /de/cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Lernen Sie, wie Sie ein Arbeitsblatt in ein Bild umwandeln und den Leerraum um die Daten mit Aspose.Cells for C++ entfernen.
---

{{% alert color="primary" %}}

Manchmal müssen Sie Arbeitsblattbilder in Anwendungen oder Webseiten präsentieren. Sie müssen beispielsweise Bilder in ein Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation oder ein anderes Dokument einfügen. Im Grunde genommen möchten Sie ein Arbeitsblatt als Bild rendern, damit es in andere Anwendungen eingefügt werden kann. Aspose.Cells ermöglicht es Ihnen, Microsoft Excel-Arbeitsblätter in Bilder umzuwandeln.

{{% /alert %}}

## **Leerraum um Daten entfernen**

Die [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) API wandelt ein Arbeitsblatt in eine Bilddatei mit beliebigen festgelegten Attributen um, z. B. Imageformat, nach Seiten paginierte Blätter usw. Verschiedene Bildformate werden unterstützt, einschließlich BMP, GIF, JPG, TIFF und EMF.

Wenn Sie die Sheet-to-Image-Funktion verwenden, enthält das Ausgabebild standardmäßig Leerraum, also einen Rahmen um es herum. Dies können Sie entfernen, indem Sie die oberen, unteren, linken und rechten Randeinstellungen für das Quellarbeitsblatt auf 0 setzen und die [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)-Attribute entsprechend angeben.

Der folgende Codeausschnitt entfernt den Leerraum um die Daten im Ausgabebild.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open the template file
    Workbook book(srcDir + u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Define LoadOptions and set LoadFilter
    LoadOptions options;
    options.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All));

    // Specify your print area if you want
    // sheet.GetPageSetup().SetPrintArea(u"A1:H8");

    // To remove the white border around the image.
    sheet.GetPageSetup().SetLeftMargin(0);
    sheet.GetPageSetup().SetRightMargin(0);
    sheet.GetPageSetup().SetBottomMargin(0);
    sheet.GetPageSetup().SetTopMargin(0);

    // Define ImageOrPrintOptions
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(Aspose::Cells::Drawing::ImageType::Emf);

    // Set only one page would be rendered for the image
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetPrintingPage(PrintingPageType::IgnoreBlank);

    // Create the SheetRender object based on the sheet with its
    // ImageOrPrintOptions attributes
    SheetRender sr(sheet, imgOptions);

    // Convert the image
    sr.ToImage(0, outDir + u"outputRemoveWhitespaceAroundData.emf");

    std::cout << "Image converted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
