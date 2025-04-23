---
title: Hur man ändrar färgen på kommentarf_font med C++
linktitle: Hur man ändrar kommentarens teckensnittsfärg
type: docs
weight: 180
url: /sv/cpp/how-to-change-the-comment-font-color/
description: Lär dig hur du kan anpassa kommentarsfärgen i Excel med Aspose.Cells och C++.
---

{{% alert color="primary" %}} 

Microsoft Excel gör det möjligt för användare att lägga till kommentarer i celler för att lägga till ytterligare information och markera data. Utvecklare kan behöva anpassa kommentaren för att specificera inriktning, textinriktning, teckensnittsfärg osv. Aspose.Cells tillhandahåller API:er för att uppnå detta.

{{% /alert %}} 

Aspose.Cells tillhandahåller en [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/) egenskap för att ställa in teckensnittfärgen för en kommentar. Följande kodexempel visar användningen av [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/) egenskapen för att ställa in teckensnittfärgen.

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

Den [utdatafil](102662195.xlsx) som genererats av ovanstående kod bifogas för din referens.
