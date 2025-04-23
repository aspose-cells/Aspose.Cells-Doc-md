---
title: Добавьте текст WordArt с встроенными стилями с помощью C++
linktitle: Добавление словесного искусства текста с встроенными стилями
type: docs
weight: 270
url: /ru/cpp/add-word-art-text-with-built-in-styles/
description: Узнайте, как добавлять текст WordArt с встроенными стилями, используя Aspose.Cells for C++.
---

## **Возможные сценарии использования**
Вы можете добавить текст WordArt с встроенными стилями с помощью Aspose.Cells. Для этого используйте метод [ShapeCollection.AddWordArt()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addwordart/)

## **Добавление словесного искусства текста с встроенными стилями**
В следующем образце кода добавляются тексты Word Art с различными встроенными стилями. Пожалуйста, проверьте [выходной файл Excel](5115470.xlsx), созданный с помощью этого кода. Так выглядит [выходной файл Excel](5115470.xlsx) в Microsoft Excel.

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
