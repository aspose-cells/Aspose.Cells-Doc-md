---
title: Imposta lo stile WordArt predefinito al testo della Forma con C++
linktitle: Imposta lo stile WordArt predefinito al testo della Forma
type: docs
weight: 280
url: /it/cpp/set-preset-wordart-style-to-the-text-of-the-shape/
description: Impara come impostare uno stile preset di WordArt al testo di una forma utilizzando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**
Puoi impostare uno stile preset di WordArt al testo di una forma utilizzando Aspose.Cells. Si prega di usare [FontSetting.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/setwordartstyle/) o [FontSettingCollection.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/fontsettingcollection/setwordartstyle/) metodi a questo scopo.

## **Imposta lo stile WordArt preset al testo della forma**
Il seguente esempio di codice crea una casella di testo con del testo e poi imposta lo stile WordArt preset del suo testo usando il metodo [FontSetting.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/setwordartstyle/). Questo è come appare il [file excel di output](5115445.xlsx) in Microsoft Excel.

![todo:image_alt_text](set-preset-wordart-style-to-the-text-of-the-shape_1.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create a textbox with some text
    TextBox textbox = worksheet.GetShapes().AddTextBox(0, 0, 0, 0, 100, 700);
    textbox.SetText(u"Aspose File Format APIs");
    textbox.GetFont().SetSize(44);

    // Sets preset WordArt style to the text of the shape.
    FontSetting fntSetting = textbox.GetRichFormattings()[0];
    fntSetting.SetWordArtStyle(PresetWordArtStyle::WordArtStyle3);

    // Save the workbook in xlsx format
    workbook.Save(u"..\\Data\\02_OutputDirectory\\outputSetPresetWordArtStyle.xlsx");

    std::cout << "Workbook saved successfully with preset WordArt style!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
