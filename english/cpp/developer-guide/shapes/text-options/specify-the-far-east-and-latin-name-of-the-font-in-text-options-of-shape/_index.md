---
title: Specify the Far East and Latin Name of the Font in Text Options of Shape with C++
linktitle: Specify the Far East and Latin Name of the Font in Text Options of Shape
type: docs
weight: 1600
url: /cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/
description: Learn how to specify the Far East and Latin font names in text options of a shape using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**

Sometimes you want to display text in Far East language font e.g. Japanese, Chinese, Thai, etc. Aspose.Cells provides [**TextOptions.FarEastName**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/fareastname/) property that can be used to specify the font name of Far East language. Besides, you can also specify the Latin font name using [**TextOptions.LatinName**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/latinname/) property.

## **Specify the Far East and Latin Name of the Font in Text Options of Shape**

The following sample code creates a text box and adds some Japanese text inside it. It then specifies the Latin and Far East font names of the text and saves the workbook as [output Excel file](67338274.xlsx). The following screenshot shows the Latin and Far East font names of the output text box in Microsoft Excel.

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)

## **Sample Code**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    Workbook wb;

    Worksheet ws = wb.GetWorksheets().Get(0);

    int idx = ws.GetTextBoxes().Add(5, 5, 50, 200);
    TextBox tb = ws.GetTextBoxes().Get(idx);

    tb.SetText(u"\u3053\u3093\u306B\u3061\u306F\u4E16\u754C");

    tb.GetTextOptions().SetLatinName(u"Comic Sans MS");
    tb.GetTextOptions().SetFarEastName(u"KaiTi");

    wb.Save(u"outputSpecifyFarEastAndLatinNameOfFontInTextOptionsOfShape.xlsx", SaveFormat::Xlsx);

    std::cout << "Textbox created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```