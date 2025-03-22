---
title: Change Text Direction of the Comment with C++
linktitle: Change Text Direction of the Comment
type: docs
weight: 10
url: /cpp/change-text-direction-of-the-comment/
description: Learn how to change the text direction of comments in Excel using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Microsoft Excel allows users to add comments to cells to add additional information and highlight data. Developers may need to customize the comment to specify alignment settings and text direction. Aspose.Cells provides APIs to accomplish the task.

{{% /alert %}}

Aspose.Cells provides a [**Shape.TextDirection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/textdirection/) property to set text direction for a comment. The following sample code demonstrates the use of [**Shape.TextDirection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/textdirection/) property to set text direction for a comment.

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