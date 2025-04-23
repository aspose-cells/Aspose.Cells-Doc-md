---
title: 如何用 C++ 改变批注的字体颜色
linktitle: 如何更改评论字体颜色
type: docs
weight: 180
url: /zh/cpp/how-to-change-the-comment-font-color/
description: 学习如何使用 Aspose.Cells 和 C++ 自定义批注的字体颜色。
---

{{% alert color="primary" %}} 

Microsoft Excel允许用户向单元格添加评论以补充信息并突出显示数据。开发人员可能需要自定义评论以指定对齐设置、文本方向、字体颜色等。Aspose.Cells提供了API以完成此任务。

{{% /alert %}} 

Aspose.Cells 提供了 [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/) 属性用于设置批注字体颜色。以下示例代码演示了如何使用 [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/) 属性设置批注的字体颜色。

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

上述代码生成的[输出文件](102662195.xlsx)附在此供您参考。
