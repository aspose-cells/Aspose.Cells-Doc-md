---
title: Voreingestellten WordArt Stil auf den Text der Form mit C++ setzen
linktitle: Voreingestellten WordArt Stil auf den Text der Form setzen
type: docs
weight: 280
url: /de/cpp/set-preset-wordart-style-to-the-text-of-the-shape/
description: Erfahre, wie man den voreingestellten WordArt Stil mithilfe von Aspose.Cells for C++ auf den Text einer Form anwendet.
---

## **Mögliche Verwendungsszenarien**
Den vorgegebenen WordArt-Stil auf den Text der Form mit Aspose.Cells setzen. Bitte nutze [FontSetting.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/setwordartstyle/) oder [FontSettingCollection.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/fontsettingcollection/setwordartstyle/) für diesen Zweck.

## **Voreingestellten WordArt-Stil auf den Text der Form setzen**
Das folgende Beispiel erstellt ein Textfeld mit einem Text und setzt dann den voreingestellten WordArt-Stil für dessen Text mithilfe der Methode [FontSetting.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/setwordartstyle/). So sieht die [Ausgabedatei im Excel-Format](5115445.xlsx) in Microsoft Excel aus.

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
