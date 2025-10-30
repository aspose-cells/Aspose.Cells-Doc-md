---
title: HTML5 Zeichenfolge aus Zelle mit C++ abrufen
linktitle: HTML5 Zeichenfolge aus Zelle abrufen
type: docs
weight: 90
url: /de/cpp/get-html5-string-from-cell/
description: Lernen Sie, wie man die HTML5 Zeichenfolge aus einer Zelle mit der API Aspose.Cells for C++ erhält.
keywords: Holen Sie den HTML5 String aus der Zelle, HTML5 String aus der Zelle erhalten, HTML5 String der Zelle verwalten
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells gibt die HTML-Zeichenfolge der Zelle mit der [**GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/)-Methode zurück, die einen booleschen Parameter akzeptiert. Wenn Sie **false** als Parameter übergeben, wird normales HTML zurückgegeben, aber wenn Sie **true** übergeben, wird HTML5-String zurückgegeben.

## **HTML5-Zeichenfolge aus Zelle erhält**

Der folgende Beispielcode erstellt ein Arbeitsmappenobjekt und fügt etwas Text in Zelle A1 des ersten Arbeitsblatts ein. Anschließend wird der Normal HTML- und HTML5-String aus Zelle A1 mit der Methode [**GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) geholt und auf der Konsole gedruckt.

## **Beispielcode**

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

## **Konsolenausgabe**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
