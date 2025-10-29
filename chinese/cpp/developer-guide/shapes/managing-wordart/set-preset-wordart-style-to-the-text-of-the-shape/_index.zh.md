---
title: 用 C++ 为形状的文字设置预设文字艺术样式
linktitle: 为形状的文字设置预设文字艺术样式
type: docs
weight: 280
url: /zh/cpp/set-preset-wordart-style-to-the-text-of-the-shape/
description: 学习如何用 Aspose.Cells for C++ 为形状的文本设置预设文字艺术样式。
---

## **可能的使用场景**
你可以用 Aspose.Cells 为形状的文本设置预设文字艺术样式。请使用 [FontSetting.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/setwordartstyle/) 或 [FontSettingCollection.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/fontsettingcollection/setwordartstyle/) 方法。

## **设置预设文字艺术样式到形状的文字**
以下示例代码创建一个带有文本的文本框，然后使用 [FontSetting.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/setwordartstyle/) 方法设置其文字的预设文字艺术样式。这也是 [输出Excel文件](5115445.xlsx) 在Microsoft Excel中的显示方式。

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
