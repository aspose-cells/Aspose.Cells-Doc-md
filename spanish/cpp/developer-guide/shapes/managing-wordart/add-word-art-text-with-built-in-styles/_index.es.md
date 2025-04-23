---
title: Agregar texto WordArt con estilos integrados con C++
linktitle: Añadir texto de Word Art con estilos integrados
type: docs
weight: 270
url: /es/cpp/add-word-art-text-with-built-in-styles/
description: Aprenda cómo agregar texto WordArt con estilos integrados usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**
Puede agregar texto WordArt con estilos integrados usando Aspose.Cells. Por favor, utilice el método [ShapeCollection.AddWordArt()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addwordart/) para este propósito.

## **Añadir texto de Word Art con estilos integrados**
El siguiente código de muestra añade textos de Word Art con diferentes estilos integrados. Por favor, revise el [archivo de excel de salida](5115470.xlsx) generado con este código. Así es como se ve el [archivo de excel de salida](5115470.xlsx) en Microsoft Excel

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
