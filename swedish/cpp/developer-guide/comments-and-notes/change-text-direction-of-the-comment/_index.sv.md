---
title: Ändra textriktningen för kommentaren med C++
linktitle: Ändra textens riktning på kommentaren
type: docs
weight: 10
url: /sv/cpp/change-text-direction-of-the-comment/
description: Lär dig hur du ändrar textriktningen för kommentarer i Excel med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Microsoft Excel tillåter användare att lägga till kommentarer till celler för att lägga till ytterligare information och framhäva data. Utvecklare kan behöva anpassa kommentaren för att ange justeringsinställningar och textriktning. Aspose.Cells tillhandahåller API:er för att utföra uppgiften.

{{% /alert %}}

Aspose.Cells tillhandahåller en [**Shape.GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextdirection/) egenskap för att ange textriktning för en kommentar. Följande kodexempel visar hur man använder [**Shape.GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextdirection/) egenskapen för att ställa in textriktning för en kommentar.

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
