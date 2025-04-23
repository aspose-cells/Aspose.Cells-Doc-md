---
title: Bloquear marca de agua WordArt con C++
linktitle: Bloqueo de marca de agua de WordArt
type: docs
weight: 170
url: /es/cpp/locking-wordart-watermark/
description: Aprenda cómo bloquear marcas de agua WordArt en hojas de cálculo de Excel usando Aspose.Cells for C++. Evite la edición, movimiento y selección de las marcas de agua programáticamente.
---

{{% alert color="primary" %}}

Las API de Aspose.Cells permiten agregar marcas de agua WordArt en la hoja de cálculo de tal manera que el WordArt se convierta en un objeto que puede mover y posicionar en la hoja de cálculo. También es posible bloquear el objeto WordArt para cualquier interacción como edición, movimiento y selección. Este artículo explica el uso del método [**Shape.SetLockedProperty**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setlockedproperty/) para bloquear algunos aspectos de la marca de agua.

{{% /alert %}}

Las API de Aspose.Cells permiten bloquear ciertos aspectos de la marca de agua para que la interacción del usuario pueda ser limitada o completamente bloqueada. El siguiente fragmento de código demuestra el uso de la API Aspose.Cells for C++ para bloquear la selección, movimiento, edición y cambio de tamaño de la marca de agua creando una hoja de cálculo desde cero.

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

    // Lock Shape Aspects
    wordart.SetIsLocked(true);
    wordart.SetLockedProperty(ShapeLockType::Selection, true);
    wordart.SetLockedProperty(ShapeLockType::ShapeType, true);
    wordart.SetLockedProperty(ShapeLockType::Move, true);
    wordart.SetLockedProperty(ShapeLockType::Resize, true);
    wordart.SetLockedProperty(ShapeLockType::Text, true);

    // Get the fill format of the word art
    FillFormat wordArtFormat = wordart.GetFill();

    // Set the color
    wordArtFormat.SetOneColorGradient(Color::Red(), 0.2, GradientStyleType::Horizontal, 2);

    // Set the transparency
    wordArtFormat.SetTransparency(0.9);

    // Make the line invisible
    wordart.SetHasLine(false);

    // Save the file
    workbook.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```
