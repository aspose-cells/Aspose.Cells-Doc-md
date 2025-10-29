---
title: 用 C++ 添加带内置样式的文字艺术（WordArt）文本
linktitle: 添加具有内置样式的艺术字文本
type: docs
weight: 270
url: /zh/cpp/add-word-art-text-with-built-in-styles/
description: 学习如何用 Aspose.Cells for C++ 添加带内置样式的文字艺术文本。
---

## **可能的使用场景**
你可以使用 Aspose.Cells 添加带内置样式的文字艺术文本。请使用 [ShapeCollection.AddWordArt()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addwordart/) 方法实现。

## **添加具有内置样式的艺术字文本**
以下示例代码使用不同的内置样式添加Word Art文本。请使用[code]output excel file[/code]检查使用此代码生成的[输出excel文件](5115470.xlsx)。这是[输出excel文件](5115470.xlsx)在Microsoft Excel中的外观。

![todo:image_alt_text](add-word-art-text-with-built-in-styles_1.png)

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Add Word Art Text with Built-in Styles
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle1, u"Aspose File Format APIs", 0, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle2, u"Aspose File Format APIs", 10, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle3, u"Aspose File Format APIs", 20, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle4, u"Aspose File Format APIs", 30, 0, 0, 0, 100, 800);
    ws.GetShapes().AddWordArt(PresetWordArtStyle::WordArtStyle5, u"Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "WordArt added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
