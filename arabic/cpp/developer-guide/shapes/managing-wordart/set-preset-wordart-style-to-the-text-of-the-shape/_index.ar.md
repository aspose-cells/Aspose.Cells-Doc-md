---
title: تعيين نمط كلمات فنية مسبق للنص في الشكل باستخدام C++
linktitle: تعيين نمط كلمات فنية مسبق لنص الشكل
type: docs
weight: 280
url: /ar/cpp/set-preset-wordart-style-to-the-text-of-the-shape/
description: تعلم كيفية تعيين نمط كلمات فنية مسبق لنص شكل باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**
 يمكنك تعيين نمط كلمات فنية مسبق لنص الشكل باستخدام Aspose.Cells. يرجى استخدام [FontSetting.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/setwordartstyle/) أو [FontSettingCollection.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/fontsettingcollection/setwordartstyle/) لهذا الغرض.

## **تعيين نمط كلمات فنية مسبق لنص الشكل**
يخلق رمز المثال التالي صندوق نص مع بعض النص ثم يعيّن نمط كلمات فنية مسبق لنصه باستخدام [FontSetting.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/setwordartstyle/). هكذا يظهر [ملف إكسل الناتج](5115445.xlsx) في Microsoft Excel.

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
