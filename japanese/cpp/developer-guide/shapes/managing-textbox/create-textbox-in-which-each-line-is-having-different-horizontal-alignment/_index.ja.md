---
title: C++を使用して、各行が異なる水平配置のTextBoxを作成します。
linktitle: 異なる水平配置でTextBoxを作成します。
type: docs
weight: 310
url: /ja/cpp/create-textbox-in-which-each-line-is-having-different-horizontal-alignment/
description: C++を使って、各行に異なる水平配置を設定したTextBoxを作成する方法を学びます。
---

{{% alert color="primary" %}}

段落テキストの水平方向の配置を設定することができます。[**TextParagraph.GetAlignmentType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textparagraph/getalignmenttype/)プロパティを使用します。

{{% /alert %}}

以下のサンプルコードは、三つの行を作成し、それぞれの水平方向の配置を設定します。

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
