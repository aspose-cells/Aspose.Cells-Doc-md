---
title: Добавление WordArt Watermark в рабочий лист с помощью C++
linktitle: Управление WordArt
type: docs
weight: 180
url: /ru/cpp/add-wordart-watermark-to-worksheet/
description: Узнайте, как добавлять WordArt затенения в Excel рабочие листы с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Используйте WordArt для добавления специальных текстовых эффектов в электронные таблицы. Например, растяните заголовок сверху файла, украсьте текст или сделайте его соответствующим предварительно заданной форме или примените текст к листу Excel в качестве фонового водяного знака. WordArt становится объектом, который можно перемещать или позиционировать на листе, добавляя украшения.

{{% /alert %}} 

Приведенный ниже пример показывает, как добавить форму WordArt, чтобы установить водяной знак на фон для листа.

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

## **Продвинутые темы**
- [Добавление словесного искусства текста с встроенными стилями](/cells/ru/cpp/add-word-art-text-with-built-in-styles/)
- [Блокировка водяного знака WordArt](/cells/ru/cpp/locking-wordart-watermark/)
- [Установить предварительный стиль WordArt для текста формы](/cells/ru/cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
{{< app/cells/assistant language="cpp" >}}
