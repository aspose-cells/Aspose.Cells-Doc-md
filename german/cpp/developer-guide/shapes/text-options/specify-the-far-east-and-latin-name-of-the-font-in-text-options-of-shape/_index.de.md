---
title: Far East und Latin Namen der Schriftart in den Textoptionen der Form mit C++ angeben
linktitle: Den Fernost und Lateinischen Namen der Schriftart in den Textoptionen der Form festlegen
type: docs
weight: 1600
url: /de/cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/
description: Lernen Sie, wie man die Far East und Latin Schriftartnamen in den Textoptionen einer Form mit Aspose.Cells for C++ angibt.
---

## **Mögliche Verwendungsszenarien**

Manchmal möchten Sie Text in einer Far East-Schriftsprache anzeigen, z.B. Japanisch, Chinesisch, Thai usw. Aspose.Cells bietet die [**TextOptions.GetFarEastName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getfareastname/)-Eigenschaft, mit der der Name der Far East-Schriftart festgelegt werden kann. Außerdem können Sie den Latin-Schriftartnamen mit der [**TextOptions.GetLatinName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getlatinname/)-Eigenschaft angeben.

## **Den Fernost- und Lateinischen Namen der Schriftart in den Textoptionen der Form festlegen**

Das folgende Beispiel erstellt eine Textbox und fügt some Japanischen Text darin ein. Es gibt dann die lateinischen und Fernost-Schriftartnamen des Textes an und speichert die Arbeitsmappe als [Ausgabe-Excel](67338274.xlsx). Der folgende Screenshot zeigt die lateinischen und Fernost-Schriftartnamen der Ausgabetextbox in Microsoft Excel.

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)

## **Beispielcode**

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
