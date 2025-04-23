---  
title: Leere Seite beim Drucken ausgeben, wenn nichts zu drucken ist, mit C++  
linktitle: Leeres Blatt ausgeben, wenn nichts gedruckt werden muss  
type: docs  
weight: 90  
url: /de/cpp/output-blank-page-when-there-is-nothing-to-print/  
description: Leere Arbeitsblätter behandeln und leere Seiten mit Aspose.Cells in C++ drucken.  
---  

## **Mögliche Verwendungsszenarien**  

Wenn das Blatt leer ist, druckt Aspose.Cells beim Exportieren des Arbeitsblatts in ein Bild nichts. Sie können dieses Verhalten ändern, indem Sie die Eigenschaft [**ImageOrPrintOptions.GetOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getoutputblankpagewhennothingtoprint/) verwenden. Wenn Sie sie auf **true** setzen, wird die leere Seite gedruckt.  

## **Leeres Blatt ausgeben, wenn nichts gedruckt werden muss**  

Der folgende Beispielcode erstellt die leere Arbeitsmappe, die ein leeres Arbeitsblatt enthält, und rendert dieses leere Arbeitsblatt in eine Bilddatei, nachdem die Eigenschaft [**ImageOrPrintOptions.GetOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getoutputblankpagewhennothingtoprint/) auf **true** gesetzt wurde. Folglich wird die leere Seite erzeugt, da nichts zum Drucken vorhanden ist, was im untenstehenden Bild sichtbar ist.  

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)  

## **Beispielcode**  

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Output directory
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook wb;

    // Access first worksheet - it is an empty sheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Specify image or print options
    // Since the sheet is blank, we will set OutputBlankPageWhenNothingToPrint to true
    // So that an empty page gets printed
    ImageOrPrintOptions opts;
    opts.SetImageType(Drawing::ImageType::Png);
    opts.SetOutputBlankPageWhenNothingToPrint(true);

    // Render empty sheet to png image
    SheetRender sr(ws, opts);
    sr.ToImage(0, outputDir + u"OutputBlankPageWhenNothingToPrint.png");

    std::cout << "Blank page rendered to PNG successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```  
