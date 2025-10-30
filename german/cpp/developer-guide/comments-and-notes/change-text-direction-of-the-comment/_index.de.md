---
title: Ändern Sie die Textausrichtung des Kommentars mit C++
linktitle: Ändern der Textausrichtung des Kommentars
type: docs
weight: 10
url: /de/cpp/change-text-direction-of-the-comment/
description: Lernen Sie, wie Sie die Textausrichtung von Kommentaren in Excel mit Aspose.Cells for C++ ändern.
---

{{% alert color="primary" %}}

Microsoft Excel ermöglicht es Benutzern, Kommentare zu Zellen hinzuzufügen, um zusätzliche Informationen bereitzustellen und Daten hervorzuheben. Entwickler müssen möglicherweise den Kommentar anpassen, um Ausrichtungseinstellungen und Textrichtung, Schriftfarbe usw. anzugeben. Aspose.Cells bietet APIs, um diese Aufgabe zu erledigen.

{{% /alert %}}

Aspose.Cells bietet eine [**Shape.GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextdirection/)-Eigenschaft, um die Textausrichtung eines Kommentars festzulegen. Der folgende Beispielcode demonstriert die Verwendung der [**Shape.GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextdirection/)-Eigenschaft, um die Textausrichtung eines Kommentars festzulegen.

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
