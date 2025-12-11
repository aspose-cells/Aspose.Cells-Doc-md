---  
title: Set Preset WordArt Style to the Text of the Shape with C++  
linktitle: Set Preset WordArt Style to the Text of the Shape  
type: docs  
weight: 280  
url: /cpp/set-preset-wordart-style-to-the-text-of-the-shape/  
description: Learn how to set a preset WordArt style to the text of a shape using Aspose.Cells for C++.  
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**  
You can set a preset WordArt style to the text of a shape using Aspose.Cells. Please use [FontSetting.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/setwordartstyle/) or [FontSettingCollection.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/fontsettingcollection/setwordartstyle/) methods for this purpose.  

## **Set Preset WordArt Style to the Text of the Shape**  
The following sample code creates a text box with some text and then sets a preset WordArt style for its text using the [FontSetting.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/setwordartstyle/) method. This is how the [output Excel file](5115445.xlsx) looks in Microsoft Excel.  

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

    // Create a text box with some text
    TextBox textbox = worksheet.GetShapes().AddTextBox(0, 0, 0, 0, 100, 700);
    textbox.SetText(u"Aspose File Format APIs");
    textbox.GetFont().SetSize(44);

    // Sets a preset WordArt style for the text of the shape.
    FontSetting fntSetting = textbox.GetRichFormattings()[0];
    fntSetting.SetWordArtStyle(PresetWordArtStyle::WordArtStyle3);

    // Save the workbook in xlsx format
    workbook.Save(u"..\\Data\\02_OutputDirectory\\outputSetPresetWordArtStyle.xlsx");

    std::cout << "Workbook saved successfully with preset WordArt style!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
