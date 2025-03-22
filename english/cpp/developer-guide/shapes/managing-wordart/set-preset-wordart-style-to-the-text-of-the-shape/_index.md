---
title: Set Preset WordArt Style to the Text of the Shape with C++
linktitle: Set Preset WordArt Style to the Text of the Shape
type: docs
weight: 280
url: /cpp/set-preset-wordart-style-to-the-text-of-the-shape/
description: Learn how to set preset WordArt style to the text of a shape using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**
You can set preset WordArt style to the text of the shape using Aspose.Cells. Please use [FontSetting.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/setwordartstyle/) or [FontSettingCollection.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/fontsettingcollection/setwordartstyle/) methods for this purpose.

## **Set Preset WordArt Style to the Text of the Shape**
The following sample code creates a text box with some text and then sets preset WordArt style of its text using [FontSetting.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/setwordartstyle/) method. This is how the [output excel file](5115445.xlsx) looks in Microsoft Excel.

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