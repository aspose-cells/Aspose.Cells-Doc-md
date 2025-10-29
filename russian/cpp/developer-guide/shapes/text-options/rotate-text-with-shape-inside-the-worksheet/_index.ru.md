---
title: Повернуть текст внутри формы на листе с помощью C++
linktitle: Повернуть текст
type: docs
weight: 1300
url: /ru/cpp/rotate-text-with-shape-inside-the-worksheet/
description: Узнайте, как управлять вращением текста в формах на листах Excel с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Вы можете добавлять текст внутри любой формы, используя Microsoft Excel. Если добавлять фигуру с помощью очень старой версии Microsoft Excel 2003, текст не будет вращаться вместе с формой. Однако при использовании новых версий Excel, таких как 2007, 2010, 2013 или 2016, текст будет вращаться вместе с формой. Вы можете управлять этим с помощью свойства [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrotatetextwithshape/). Значение по умолчанию этого свойства — **true**, что означает, что текст будет вращаться с формой. Если установить значение **false**, текст не будет вращаться вместе с формой.

## **Повернуть текст с фигурой внутри таблицы**

Следующий пример загружает [образец файла Excel](64716896.xlsx), который содержит треугольную фигуру, и вращение текста со всей фигурой. Если открыть пример файла в Microsoft Excel и повернуть треугольную фигуру, текст также повернётся с ней. Затем код устанавливает свойство [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrotatetextwithshape/) в значение **false** и сохраняет как [выходной файл Excel](64716897.xlsx). При открытии этого файла в Excel и вращении треугольной фигуры текст уже не будет вращаться. Ниже приведен скриншот, демонстрирующий эффект работы кода на примере файла.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Drawing::Texts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load sample Excel file
    Workbook wb(srcDir + u"sampleRotateTextWithShapeInsideWorksheet.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B4 and add message inside it
    Cell b4 = ws.GetCells().Get(u"B4");
    b4.PutValue(u"Text is not rotating with shape because RotateTextWithShape is false.");

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Access shape text alignment
    ShapeTextAlignment shapeTextAlignment = sh.GetTextBody().GetTextAlignment();

    // Do not rotate text with shape by setting RotateTextWithShape as false
    shapeTextAlignment.SetRotateTextWithShape(false);

    // Save the output Excel file
    wb.Save(outDir + u"outputRotateTextWithShapeInsideWorksheet.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
