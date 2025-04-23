---
title: WordArt Text mit integrierten Stilen mit C++ hinzufügen
linktitle: Fügen Sie Word Art Text mit integrierten Stilen hinzu
type: docs
weight: 270
url: /de/cpp/add-word-art-text-with-built-in-styles/
description: Erfahre, wie man WordArt Text mit integrierten Stilen mit Aspose.Cells for C++ hinzufügt.
---

## **Mögliche Verwendungsszenarien**
 Du kannst WordArt-Text mit integrierten Stilen mithilfe von Aspose.Cells hinzufügen. Bitte verwende die Methode [ShapeCollection.AddWordArt()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addwordart/) dafür.

## **Fügen Sie Word-Art-Text mit integrierten Stilen hinzu**
Der folgende Beispielcode fügt Wortkunsttexte mit unterschiedlichen integrierten Stilen hinzu. Überprüfen Sie die mit diesem Code generierte [Ausgabedatei](5115470.xlsx) in Microsoft Excel. So sieht die [Ausgabedatei](5115470.xlsx) in Microsoft Excel aus.

![todo:image_alt_text](add-word-art-text-with-built-in-styles_1.png)

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

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Add Word Art Text with Built-in Styles
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle1, u"Aspose File Format APIs", 0, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle2, u"Aspose File Format APIs", 10, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle3, u"Aspose File Format APIs", 20, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle4, u"Aspose File Format APIs", 30, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle5, u"Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "WordArt added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
