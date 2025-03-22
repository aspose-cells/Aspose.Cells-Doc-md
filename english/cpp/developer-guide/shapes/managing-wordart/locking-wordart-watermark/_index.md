---
title: Locking WordArt Watermark with C++
linktitle: Locking WordArt Watermark
type: docs
weight: 170
url: /cpp/locking-wordart-watermark/
description: Learn how to lock WordArt watermarks in Excel worksheets using Aspose.Cells for C++. Prevent editing, movement, and selection of watermarks programmatically.
---

{{% alert color="primary" %}}

Aspose.Cells APIs allow adding WordArt watermarks on the worksheet in a way that the WordArt becomes an object that you can move and position on the worksheet. It is also possible to lock the WordArt object for any interaction such as editing, movement, and selection. This article explains the usage of [**Shape.SetLockedProperty**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setlockedproperty/) method to lock a few aspects of the watermark.

{{% /alert %}}

Aspose.Cells APIs allow locking certain aspects of the watermark so that the user interaction could be limited or completely blocked. The following code snippet demonstrates the usage of Aspose.Cells for C++ API to lock selection, movement, editing, and resizing of the watermark by creating a spreadsheet from scratch.

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