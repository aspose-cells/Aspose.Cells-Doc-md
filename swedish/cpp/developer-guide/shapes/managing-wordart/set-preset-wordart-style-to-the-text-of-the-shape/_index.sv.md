---
title: Sätt förinställt WordArt stil till texten i formen med C++
linktitle: Sätt förinställt WordArt stil till texten i formen
type: docs
weight: 280
url: /sv/cpp/set-preset-wordart-style-to-the-text-of-the-shape/
description: Lär dig hur man ställer in förinställd WordArt stil till texten i en form med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**
 Du kan ställa in förinställd WordArt-stil till texten i formen med Aspose.Cells. Använd [FontSetting.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/setwordartstyle/) eller [FontSettingCollection.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/fontsettingcollection/setwordartstyle/) för detta ändamål.

## **Ställ in förinställd WordArt-stil till texten i formen**
Följande exempel kod skapar en textruta med lite text och ställer sedan in förinställd WordArt-stil för dess text med [FontSetting.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/setwordartstyle/) metod. Så här ser [utdataexcel-filen](5115445.xlsx) ut i Microsoft Excel.

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
