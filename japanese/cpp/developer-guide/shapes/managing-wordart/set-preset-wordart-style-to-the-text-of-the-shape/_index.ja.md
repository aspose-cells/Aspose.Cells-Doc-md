---
title: C++を使用してShapeのテキストにプリセットWordArtスタイルを設定します
linktitle: ShapeのテキストにプリセットWordArtスタイルを設定します
type: docs
weight: 280
url: /ja/cpp/set-preset-wordart-style-to-the-text-of-the-shape/
description: Aspose.Cells for C++を使用して、シェイプのテキストにプリセットWordArtスタイルを設定する方法を学びます。
---

## **可能な使用シナリオ**
Aspose.Cellsを使用してシェイプのテキストにプリセットWordArtスタイルを設定できます。この目的には、[FontSetting.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/setwordartstyle/)または[FontSettingCollection.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/fontsettingcollection/setwordartstyle/)メソッドを使用してください。

## **シェイプのテキストにプリセットWordArtスタイルを設定します**
次のサンプルコードは、テキストを含むテキストボックスを作成し、そのテキストに対して[FontSetting.SetWordArtStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/setwordartstyle/)を使用してプリセットWordArtスタイルを設定します。これは、[出力Excelファイル](5115445.xlsx)がMicrosoft Excelでどのように見えるかです。

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
