---
title: Изменение направления текста комментария с помощью C++
linktitle: Изменение направления текста комментария
type: docs
weight: 10
url: /ru/cpp/change-text-direction-of-the-comment/
description: Узнайте, как изменить направление текста комментариев в Excel, используя Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Microsoft Excel позволяет пользователям добавлять комментарии к ячейкам для добавления дополнительной информации и выделения данных. Разработчики могут потребоваться настроить комментарий, чтобы указать настройки выравнивания и направление текста. Aspose.Cells предоставляет API для выполнения этой задачи.

{{% /alert %}}

Aspose.Cells предоставляет свойство [**Shape.GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextdirection/) для установки направления текста комментария. Следующий пример показывает использование свойства [**Shape.GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextdirection/) для установки направления текста комментария.

```c++
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
    Workbook wb;

    // Get the first worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Add a comment to A1 cell
    int commentIndex = sheet.GetComments().Add(u"A1");
    Comment comment = sheet.GetComments().Get(commentIndex);

    // Set its vertical alignment setting
    comment.GetCommentShape().SetTextVerticalAlignment(TextAlignmentType::Center);

    // Set its horizontal alignment setting
    comment.GetCommentShape().SetTextHorizontalAlignment(TextAlignmentType::Right);

    // Set the Text Direction - Right-to-Left
    comment.GetCommentShape().SetTextDirection(TextDirectionType::RightToLeft);

    // Set the Comment note
    comment.SetNote(u"This is my Comment Text. This is test");

    // Save the Excel file
    U16String outputPath = outDir + u"OutCommentShape.out.xlsx";
    wb.Save(outputPath);

    std::cout << "Comment shape created and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
