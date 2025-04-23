---
title: Sperren des WordArt Wasserzeichens mit C++
linktitle: Sperren des WordArt Wasserzeichens
type: docs
weight: 170
url: /de/cpp/locking-wordart-watermark/
description: Erfahre, wie man WordArt Wasserzeichen in Excel Arbeitsblättern mithilfe von Aspose.Cells for C++ sperrt. Verhindere das Bearbeiten, Verschieben und Auswählen von Wasserzeichen programmgesteuert.
---

{{% alert color="primary" %}}

Die APIs von Aspose.Cells ermöglichen es, WordArt-Wasserzeichen auf dem Arbeitsblatt hinzuzufügen, sodass das WordArt ein Objekt wird, das bewegt und positioniert werden kann. Es ist auch möglich, das WordArt-Objekt für jegliche Interaktion wie Bearbeiten, Verschieben und Auswählen zu sperren. Dieser Artikel erklärt die Verwendung der [**Shape.SetLockedProperty**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setlockedproperty/)-Methode, um einige Aspekte des Wasserzeichens zu sperren.

{{% /alert %}}

Die APIs von Aspose.Cells erlauben es, bestimmte Aspekte des Wasserzeichens zu sperren, sodass die Benutzerinteraktion eingeschränkt oder vollständig blockiert werden kann. Das folgende Code-Snippet demonstriert die Verwendung der API Aspose.Cells for C++, um die Auswahl, Bewegung, Bearbeitung und Größenänderung des Wasserzeichens zu sperren, indem eine Tabelle von Grund auf neu erstellt wird.

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
