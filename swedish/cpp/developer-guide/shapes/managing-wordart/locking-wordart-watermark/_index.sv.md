---
title: Lås WordArt vattenmärke med C++
linktitle: Låsa WordArt vattenstämpel
type: docs
weight: 170
url: /sv/cpp/locking-wordart-watermark/
description: Lär dig hur man låser WordArt vattenmärken i Excel kalkblad med Aspose.Cells for C++. Förhindra redigering, flyttning och markering av vattenmärken programmatiskt.
---

{{% alert color="primary" %}}

Aspose.Cells API:erna tillåter att lägga till WordArt-vattenmärken på kalkbladet på ett sätt som gör att WordArt blir ett objekt som du kan flytta och positionera på kalkbladet. Det är också möjligt att låsa WordArt-objektet för alla interaktioner som redigering, flyttning och markering. Denna artikel förklarar användningen av [**Shape.SetLockedProperty**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setlockedproperty/) metod för att låsa vissa aspekter av vattenmärket.

{{% /alert %}}

Aspose.Cells API:erna tillåter att låsa vissa aspekter av vattenmärket så att användarinteraktionen kan begränsas eller helt blockeras. Följande kodexempel visar användningen av API Aspose.Cells for C++ för att låsa urval, flyttning, redigering och omstorlek av vattenmärket genom att skapa ett kalkblad från början.

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
