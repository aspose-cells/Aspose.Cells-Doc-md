---
title: Exportieren eines Zellbereichs eines Arbeitsblatts in ein Bild mit C++
linktitle: Exportieren eines Zellbereichs in ein Bild
type: docs
weight: 60
url: /de/cpp/export-range-of-cells-in-a-worksheet-to-image/
description: Erfahren Sie, wie man einen bestimmten Zellbereich in einem Arbeitsblatt mit Aspose.Cells und C++ in ein Bild exportiert.
---

## **Mögliche Verwendungsszenarien**

Sie können ein Bild eines Arbeitsblatts mit Aspose.Cells erstellen. Manchmal müssen Sie jedoch nur einen Bereich von Zellen in einem Arbeitsblatt in ein Bild exportieren. Dieser Artikel erläutert, wie dies erreicht werden kann.

## **Bereich von Zellen in einem Arbeitsblatt in ein Bild exportieren**

Um ein Bild eines Bereichs zu erstellen, setzen Sie den Druckbereich auf den gewünschten Bereich und setzen dann alle Ränder auf 0. setzen Sie außerdem [**ImageOrPrintOptions.GetOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getonepagepersheet/) auf **true**. Der folgende Code erstellt ein Bild des Bereichs D8:G16. Unten ist ein Screenshot der [Beispiel-Excel-Datei](47153160.xlsx) zu sehen, die im Code verwendet wird. Sie können den Code mit jeder Excel-Datei ausprobieren.

## **Screenshot der Beispiels-Excel-Datei und des exportierten Bilds**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

Die Ausführung des Codes erstellt lediglich ein Bild des Bereichs D8:G16.

**![todo:image_alt_text](Output-Image.png)**

## **Beispielcode**

```cpp
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

    // Create workbook from source file
    Workbook workbook(srcDir + u"sampleExportRangeOfCellsInWorksheetToImage.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the print area with the desired range
    worksheet.GetPageSetup().SetPrintArea(u"D8:G16");

    // Set all margins to 0
    worksheet.GetPageSetup().SetLeftMargin(0);
    worksheet.GetPageSetup().SetRightMargin(0);
    worksheet.GetPageSetup().SetTopMargin(0);
    worksheet.GetPageSetup().SetBottomMargin(0);

    // Set OnePagePerSheet option as true
    ImageOrPrintOptions options;
    options.SetOnePagePerSheet(true);
    options.SetImageType(Aspose::Cells::Drawing::ImageType::Jpeg);
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);

    // Take the image of the worksheet
    SheetRender sr(worksheet, options);
    sr.ToImage(0, outDir + u"outputExportRangeOfCellsInWorksheetToImage.jpg");

    std::cout << "Worksheet image exported successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
