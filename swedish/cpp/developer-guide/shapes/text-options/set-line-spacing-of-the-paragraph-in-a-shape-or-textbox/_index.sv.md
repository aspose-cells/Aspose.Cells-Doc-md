---
title: Använd C++ för att ställa in radavstånd för stycket i en form eller textruta
linktitle: Ställ in radavstånd för stycket
type: docs
weight: 290
url: /sv/cpp/set-line-spacing-of-the-paragraph-in-a-shape-or-textbox/
description: Lär dig hur man ställer in radavstånd, innanrum och efterrum i ett stycke inom en form eller textruta med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Du kan ställa in radavståndet för stycket, dess utrymme före och efter med hjälp av egenskaperna [**TextParagraph.GetLineSpace()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textparagraph/getlinespace/), [**TextParagraph.GetSpaceBefore()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textparagraph/getspacebefore/) och [**TextParagraph.GetSpaceAfter()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textparagraph/getspaceafter/) i klassen [**TextParagraph**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textparagraph/).

{{% /alert %}}

Följande kodexempel förklarar användningen av de nämnda egenskaperna.

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

    // Create a workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Add text box inside the sheet
    ws.GetShapes().AddTextBox(2, 0, 2, 0, 100, 200);

    // Access first shape which is a text box and set its text
    Shape shape = ws.GetShapes().Get(0);
    shape.SetText(u"Sign up for your free phone number.\nCall and text online for free.");

    // Access the first paragraph
    TextParagraph p = shape.GetTextBody().GetTextParagraphs().Get(1);

    // Set the line space
    p.SetLineSpaceSizeType(LineSpaceSizeType::Points);
    p.SetLineSpace(20);

    // Set the space after
    p.SetSpaceAfterSizeType(LineSpaceSizeType::Points);
    p.SetSpaceAfter(10);

    // Set the space before
    p.SetSpaceBeforeSizeType(LineSpaceSizeType::Points);
    p.SetSpaceBefore(10);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"output_out.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
