---
title: Как изменить цвет шрифта комментария с помощью C++
linktitle: Как изменить цвет шрифта комментария
type: docs
weight: 180
url: /ru/cpp/how-to-change-the-comment-font-color/
description: Узнайте, как настраивать цвет шрифта комментария в Excel с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}} 

Microsoft Excel позволяет пользователям добавлять комментарии к ячейкам для добавления дополнительной информации и выделения данных. Разработчики могут потребоваться настроить комментарий, чтобы указать настройки выравнивания, направление текста, цвет шрифта и т. д. Aspose.Cells предоставляют API для выполнения этой задачи.

{{% /alert %}} 

Aspose.Cells предоставляет свойство [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/), чтобы установить цвет шрифта комментария. Следующий пример демонстрирует использование свойства [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/) для установки направления текста комментария.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add some text in cell A1
    worksheet.GetCells().Get(u"A1").PutValue(u"Here");

    // Add a comment to A1 cell
    int commentIndex = worksheet.GetComments().Add(u"A1");
    Comment comment = worksheet.GetComments().Get(commentIndex);

    // Set its vertical alignment setting
    comment.GetCommentShape().SetTextVerticalAlignment(TextAlignmentType::Center);

    // Set the Comment note
    comment.SetNote(u"This is my Comment Text. This is Test.");

    // Get the comment shape
    Shape shape = comment.GetCommentShape();

    // Set the fill color of the shape to black
    shape.GetFill().GetSolidFill().SetColor(Color::Black());

    // Get the font of the shape
    Font font = shape.GetFont();

    // Set the font color to white
    font.SetColor(Color::White());

    // Create a StyleFlag to apply font color changes
    StyleFlag styleFlag;
    styleFlag.SetFontColor(true);

    // Apply the font color changes to the shape's text
    shape.GetTextBody().Format(0, shape.GetText().GetLength(), font, styleFlag);

    // Save the Excel file
    workbook.Save(outDir + u"outputChangeCommentFontColor.xlsx");

    Aspose::Cells::Cleanup();
}
```

[Выходной файл](102662195.xlsx), сгенерированный указанным выше кодом, приложен для вашего справки.
