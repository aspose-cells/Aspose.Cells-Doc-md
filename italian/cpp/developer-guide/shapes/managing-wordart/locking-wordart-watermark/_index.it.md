---
title: Blocca la filigrana WordArt con C++
linktitle: Bloccare WordArt Come Filigrana
type: docs
weight: 170
url: /it/cpp/locking-wordart-watermark/
description: Impara come bloccare le filigrane WordArt nei fogli di lavoro Excel usando Aspose.Cells for C++. Impedisci la modifica, il movimento e la selezione delle filigrane programmaticamente.
---

{{% alert color="primary" %}}

Le API di Aspose.Cells consentono di aggiungere filigrane WordArt sul foglio di lavoro in modo che il WordArt diventi un oggetto che puoi spostare e posizionare nel foglio. È anche possibile bloccare l'oggetto WordArt per qualsiasi interazione come modifica, spostamento e selezione. Questo articolo spiega come usare il metodo [**Shape.SetLockedProperty**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setlockedproperty/) per bloccare alcuni aspetti della filigrana.

{{% /alert %}}

Le API di Aspose.Cells consentono di bloccare alcuni aspetti della filigrana in modo che l'interazione dell'utente possa essere limitata o completamente bloccata. Il seguente esempio di codice dimostra l'uso dell'API Aspose.Cells for C++ per bloccare selezione, movimento, modifica e ridimensionamento della filigrana creando un foglio di calcolo da zero.

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
{{< app/cells/assistant language="cpp" >}}
