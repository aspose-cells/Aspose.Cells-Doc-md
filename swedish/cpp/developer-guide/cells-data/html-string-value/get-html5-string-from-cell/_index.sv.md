---
title: Få HTML5 sträng från Cell med C++
linktitle: Få HTML5 sträng från Cell
type: docs
weight: 90
url: /sv/cpp/get-html5-string-from-cell/
description: Lär dig hur du får HTML5 strängen från en cell med API n Aspose.Cells for C++.
keywords: Få HTML5 sträng från cell, Hämta HTML5 sträng från cell, Hantera HTML5 sträng i cell
---

## **Möjliga användningsscenario**

Aspose.Cells returnerar HTML-strängen för cellen med metoden [**GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) som tar ett boolean-parameter. Om du skickar **false** som parameter, returnerar den Normal HTML, men om du skickar **true**, returnerar den HTML5-sträng.

## **Få HTML5-sträng från Cell**

Följande provkod skapar en arbetsbok och lägger till lite text i cell A1 på den första kalkylbladet. Den hämtar sedan normal HTML och HTML5-sträng från cell A1 med metoden [**GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) och skriver ut dem på konsolen.

## **Exempelkod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell A1 and put some text inside it
    Cell cell = ws.GetCells().Get(u"A1");
    cell.PutValue(u"This is some text.");

    // Get the Normal and Html5 strings
    U16String strNormal = cell.GetHtmlString(false);
    U16String strHtml5 = cell.GetHtmlString(true);

    // Print the Normal and Html5 strings on console
    std::cout << "Normal:\r\n" << strNormal.ToUtf8() << std::endl;
    std::cout << std::endl;
    std::cout << "Html5:\r\n" << strHtml5.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Konsoloutput**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
