---
title: Ange Far East och Latin namn för teckensnittet i Textalternativ för form med C++
linktitle: Ange det fjärrösterländska och latinska namnet på teckensnittet i texternas alternativ för Shape
type: docs
weight: 1600
url: /sv/cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/
description: Lär dig hur man anger Far East och Latin teckensnittsnamn i textalternativen för en form med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Ibland vill du visa text i Far East-språk som japanska, kinesiska, thai, etc. Aspose.Cells tillhandahåller [**TextOptions.GetFarEastName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getfareastname/)-egenskapen som kan användas för att ange namnet på Far East-språket. Dessutom kan du också ange Latin-teckensnittsnamnet med [**TextOptions.GetLatinName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getlatinname/)-egenskapen.

## **Ange det fjärrösterländska och latinska namnet på teckensnittet i texternas alternativ för Shape**

Följande exempel skapar en textruta och lägger till japansk text inuti den. Den specificerar sedan Latin- och Far East-teckensnittsnamnen för texten och sparar arbetsboken som [utdata Excel-fil](67338274.xlsx). Nedan visas en skärmbild av Latin- och Far East-teckensnämnena för den utgående textrutan i Microsoft Excel.

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)

## **Exempelkod**

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
{{< app/cells/assistant language="cpp" >}}
