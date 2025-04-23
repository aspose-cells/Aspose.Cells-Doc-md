---
title: Shape un Metnini Ön Tanımlı WordArt Stili ile Ayarla (C++)
linktitle: Shape un Metnine Ön Tanımlı WordArt Stili Ayarla
type: docs
weight: 280
url: /tr/cpp/set-preset-wordart-style-to-the-text-of-the-shape/
description: Aspose.Cells for C++ kullanarak, şekil üzerindeki metne ön ayarlı WordArt stili ayarlamayı öğrenin.
---

## **Olası Kullanım Senaryoları**
 Shape'un Metnine Ön Tanımlı WordArt Stili Ayarla

## **Ön Ayarlı WordArt Stilini Şekil Metnine Ayarla**
 Aşağıdaki örnek kod, bir metin kutusu oluşturur ve ona bazı metinler ekler, ardından da metinlerinin ön tanımlı WordArt stilini [FontSetting.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/setwordartstyle/) yöntemiyle ayarlar. Bu şekilde [çıktı excel dosyası](5115445.xlsx) Microsoft Excel'de görünür.

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
