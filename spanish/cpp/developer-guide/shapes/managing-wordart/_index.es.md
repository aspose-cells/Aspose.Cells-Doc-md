---
title: Agrega una marca de agua WordArt a la hoja de cálculo con C++
linktitle: Gestionar WordArt
type: docs
weight: 180
url: /es/cpp/add-wordart-watermark-to-worksheet/
description: Aprende cómo agregar marcas de agua WordArt a hojas de cálculo de Excel usando Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Utilice WordArt para agregar efectos especiales de texto a las hojas de cálculo. Por ejemplo, estire un título en la parte superior del archivo, decore texto y ajuste texto a una forma predefinida, o aplique texto a una hoja de Excel como marca de agua de fondo. El WordArt se convierte en un objeto que puede mover o posicionar en las hojas de cálculo para agregar decoración.

{{% /alert %}} 

El siguiente ejemplo muestra cómo agregar una forma WordArt para establecer una marca de agua de fondo para una hoja de cálculo.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first default sheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add Watermark
    Shape wordart = sheet.GetShapes().AddTextEffect(MsoPresetTextEffect::TextEffect1,
        u"CONFIDENTIAL", u"Arial Black", 50, false, true,
        18, 8, 1, 1, 130, 800);

    // Get the fill format of the word art
    FillFormat wordArtFormat = wordart.GetFill();

    // Set the transparency
    wordArtFormat.SetTransparency(0.9);

    // Make the line invisible
    LineFormat lineFormat = wordart.GetLine();

    // Save the file
    U16String outputPath = outDir + u"Watermark_Test.out.xls";
    workbook.Save(outputPath);

    std::cout << "Watermark added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Temas avanzados**
- [Añadir texto de Word Art con estilos integrados](/cells/es/cpp/add-word-art-text-with-built-in-styles/)
- [Bloquear marca de agua WordArt](/cells/es/cpp/locking-wordart-watermark/)
- [Establecer un estilo de WordArt preestablecido al texto de la forma](/cells/es/cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
