---
title: Wie man die Kommentarfarbe mit C++ ändert
linktitle: Wie ändere ich die Kommentarschriftfarbe
type: docs
weight: 180
url: /de/cpp/how-to-change-the-comment-font-color/
description: Lernen Sie, wie Sie die Kommentarfarbe in Excel mit Aspose.Cells und C++ anpassen.
---

{{% alert color="primary" %}} 

Microsoft Excel ermöglicht es Benutzern, Kommentare zu Zellen hinzuzufügen, um zusätzliche Informationen bereitzustellen und Daten hervorzuheben. Entwickler müssen möglicherweise den Kommentar anpassen, um Ausrichtungseinstellungen, Textausrichtung Schriftfarbe usw. anzugeben. Aspose.Cells bietet APIs, um diese Aufgabe zu erledigen.

{{% /alert %}} 

Aspose.Cells bietet eine [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/)-Eigenschaft, um die Schriftfarbe des Kommentars festzulegen. Der folgende Beispielcode demonstriert die Verwendung der [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/)-Eigenschaft, um die Textausrichtung eines Kommentars festzulegen.

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

Die [Ausgabedatei](102662195.xlsx), die vom obigen Code generiert wurde, ist als Referenz angehängt.
{{< app/cells/assistant language="cpp" >}}
