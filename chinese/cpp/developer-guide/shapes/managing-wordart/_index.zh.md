---
title: 用C++向工作表添加WordArt水印
linktitle: 管理文字艺术
type: docs
weight: 180
url: /zh/cpp/add-wordart-watermark-to-worksheet/
description: 学习如何使用 Aspose.Cells for C++ 在Excel工作表中添加WordArt水印。
---

{{% alert color="primary" %}} 

使用WordArt为电子表格添加特殊文本效果，例如，将标题横跨文件顶部，装饰文本，并使文本适应预设形状，或将文本应用于Excel工作表作为背景水印。 WordArt成为您可以在电子表格中移动或定位以添加装饰的对象。

{{% /alert %}} 

以下示例显示如何添加文字艺术形状以设置工作表的背景水印。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first default sheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add Watermark
    Shape wordart = sheet.GetShapes().AddTextEffect(MsoPresetTextEffect::TextEffect1,
        u"CONFIDENTIAL", u"Arial Black", 50, false, true,
        18, 8, 1, 1, 130, 800);

    // Get the fill format of the word art
    FillFormat wordArtFormat = wordart.GetFill();

    // Set the transparency
    wordArtFormat.SetTransparency(0.9);

    // Make the line invisible
    LineFormat lineFormat = wordart.GetLine();

    // Save the file
    U16String outputPath = outDir + u"Watermark_Test.out.xls";
    workbook.Save(outputPath);

    std::cout << "Watermark added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高级主题**
- [添加具有内置样式的艺术字文本](/cells/zh/cpp/add-word-art-text-with-built-in-styles/)
- [锁定WordArt水印](/cells/zh/cpp/locking-wordart-watermark/)
- [将文本形状的文字设置为预设的WordArt样式](/cells/zh/cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
