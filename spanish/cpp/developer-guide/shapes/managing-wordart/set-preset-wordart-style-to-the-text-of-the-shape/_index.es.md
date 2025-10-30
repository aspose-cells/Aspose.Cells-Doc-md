---
title: Establecer estilo de WordArt predefinido en el texto de la forma con C++
linktitle: Establecer estilo de WordArt predefinido en el texto de la forma
type: docs
weight: 280
url: /es/cpp/set-preset-wordart-style-to-the-text-of-the-shape/
description: Aprenda cómo establecer un estilo de WordArt predefinido en el texto de una forma usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**
Puede establecer un estilo de WordArt predefinido en el texto de la forma usando Aspose.Cells. Por favor, utilice [FontSetting.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/setwordartstyle/) o [FontSettingCollection.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/fontsettingcollection/setwordartstyle/) para este propósito.

## **Establecer estilo de WordArt predefinido en el texto de la forma**
El siguiente código de ejemplo crea un cuadro de texto con algún texto y luego establece el estilo de WordArt predefinido de su texto usando el método [FontSetting.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/setwordartstyle/). Así es como se ve el [archivo de Excel de salida](5115445.xlsx) en Microsoft Excel.

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
{{< app/cells/assistant language="cpp" >}}
