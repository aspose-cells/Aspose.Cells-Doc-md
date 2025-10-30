---
title: Erstellen eines Textfelds, bei dem jede Zeile eine andere horizontale Ausrichtung hat, mit C++
linktitle: Erstellen eines Textfelds mit unterschiedlicher horizontaler Ausrichtung
type: docs
weight: 310
url: /de/cpp/create-textbox-in-which-each-line-is-having-different-horizontal-alignment/
description: Erfahre, wie man ein Textfeld mit unterschiedlicher horizontaler Ausrichtung für jede Zeile unter Verwendung von Aspose.Cells mit C++ erstellt.
---

{{% alert color="primary" %}}

Sie können die horizontale Ausrichtung Ihres Absatztextes mit der Eigenschaft [**TextParagraph.GetAlignmentType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textparagraph/getalignmenttype/) festlegen.

{{% /alert %}}

Der folgende Beispielcode erstellt drei Linien und legt die horizontale Ausrichtung jeder von ihnen fest.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Add text box inside the sheet
    ws.GetShapes().AddTextBox(2, 0, 2, 0, 80, 400);

    // Access first shape which is a text box and set its text
    Shape shape = ws.GetShapes().Get(0);
    shape.SetText(u"Sign up for your free phone number.\nCall and text online for free.\nCall your friends and family.");

    // Access the first paragraph and set its horizontal alignment to left
    TextParagraph p = shape.GetTextBody().GetTextParagraphs().Get(0);
    p.SetAlignmentType(TextAlignmentType::Left);

    // Access the second paragraph and set its horizontal alignment to center
    p = shape.GetTextBody().GetTextParagraphs().Get(1);
    p.SetAlignmentType(TextAlignmentType::Center);

    // Access the third paragraph and set its horizontal alignment to right
    p = shape.GetTextBody().GetTextParagraphs().Get(2);
    p.SetAlignmentType(TextAlignmentType::Right);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"output_out.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
