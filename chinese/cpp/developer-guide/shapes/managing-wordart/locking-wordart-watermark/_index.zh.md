---
title: 用 C++ 锁定文字艺术水印
linktitle: 锁定WordArt水印
type: docs
weight: 170
url: /zh/cpp/locking-wordart-watermark/
description: 学习如何用 Aspose.Cells for C++ 在 Excel 工作表中锁定文字艺术水印，防止编辑、移动和选择水印。
---

{{% alert color="primary" %}}

Aspose.Cells API 允许在工作表上添加文字艺术水印，使其成为可以移动和定位的对象。也可以将文字艺术对象锁定以阻止任何交互，例如编辑、移动和选择。本文介绍了[**Shape.SetLockedProperty**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setlockedproperty/)方法的用法，用于锁定水印的某些方面。

{{% /alert %}}

Aspose.Cells API 允许锁定水印的特定方面，从而限制或完全阻止用户交互。以下代码片段演示了如何使用 Aspose.Cells for C++ API 从头创建电子表格，锁定水印的选择、移动、编辑和调整大小。

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

    // Lock Shape Aspects
    wordart.SetIsLocked(true);
    wordart.SetLockedProperty(ShapeLockType::Selection, true);
    wordart.SetLockedProperty(ShapeLockType::ShapeType, true);
    wordart.SetLockedProperty(ShapeLockType::Move, true);
    wordart.SetLockedProperty(ShapeLockType::Resize, true);
    wordart.SetLockedProperty(ShapeLockType::Text, true);

    // Get the fill format of the word art
    FillFormat wordArtFormat = wordart.GetFill();

    // Set the color
    wordArtFormat.SetOneColorGradient(Color::Red(), 0.2, GradientStyleType::Horizontal, 2);

    // Set the transparency
    wordArtFormat.SetTransparency(0.9);

    // Make the line invisible
    wordart.SetHasLine(false);

    // Save the file
    workbook.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```
