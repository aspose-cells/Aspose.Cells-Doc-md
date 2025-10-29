---
title: Блокировка Watermark WordArt с помощью C++
linktitle: Блокировка водяного знака WordArt
type: docs
weight: 170
url: /ru/cpp/locking-wordart-watermark/
description: Узнайте, как блокировать водяные знаки WordArt в Excel с помощью Aspose.Cells for C++. Предотвращайте редактирование, перемещение и выбор водяных знаков программно.
---

{{% alert color="primary" %}}

APIs Aspose.Cells позволяют добавлять водяные знаки WordArt на лист так, что WordArt становится объектом, который можно перемещать и размещать на листе. Также возможно заблокировать объект WordArt для взаимодействий, таких как редактирование, перемещение и выбор. В этой статье объясняется использование метода [**Shape.SetLockedProperty**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setlockedproperty/) для блокировки некоторых аспектов водяного знака.

{{% /alert %}}

APIs Aspose.Cells позволяют блокировать определённые аспекты водяного знака, чтобы ограничить или полностью заблокировать взаимодействие пользователя. Следующий фрагмент кода демонстрирует использование API Aspose.Cells for C++ для блокировки выделения, перемещения, редактирования и изменения размера водяного знака, создавая таблицу с нуля.

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
{{< app/cells/assistant language="cpp" >}}
