---
title: Verwalten der Cells HTML Zeichenfolge mit C++
linktitle: Zellen HTML String verwalten
type: docs
weight: 600
url: /de/cpp/manage-cells-html-string/
description: Lernen Sie, wie Sie die Cells HTML Zeichenfolge über die API Aspose.Cells for C++ verwalten.
keywords: Fügen Sie HTML String in die Zelle ein, setzen Sie HTML String in die Zelle, fügen Sie HTML String hinzu, erhalten Sie den HTML String der Zelle, verwalten Sie Zellen HTML String
---

## **Mögliche Verwendungsszenarien**
Wenn Sie gestylte Daten für eine bestimmte Zelle festlegen müssen, können Sie eine HTML-Zeichenfolge der Zelle zuweisen. Natürlich können Sie auch die HTML-Zeichenfolge der Zelle erhalten. Aspose.Cells bietet diese Funktion. Aspose.Cells stellt die folgenden Eigenschaften und Methoden bereit, um Ihre Ziele zu erreichen.
- [**Cell::GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/)
- [**Cell::SetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/sethtmlstring/)

## **Abrufen und festlegen des HTML-Strings mithilfe von Aspose.Cells**
Dieses Beispiel zeigt, wie Sie:

1. Erstellen Sie ein Arbeitsbuch und fügen Sie einige Daten hinzu.
1. Die spezifische Zelle im ersten Arbeitsblatt abrufen.
1. Setzen Sie den HTML-String in die Zelle.
1. Holen Sie den HTML-String der Zelle.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a Workbook object
    Workbook workbook;

    // Obtain the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");

    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");

    cell = cells.Get(u"C1");
    cell.PutValue(u"Price");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");

    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");

    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");

    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");

    Cell c3 = cells.Get(u"C3");
    // Set HTML string for C3 cell
    c3.SetHtmlString(u"<b>test bold</b>");

    Cell c4 = cells.Get(u"C4");
    // Set HTML string for C4 cell
    c4.SetHtmlString(u"<i>test italic</i>");

    // Get the HTML string of specific cell
    std::cout << c3.GetHtmlString().ToUtf8() << std::endl;
    std::cout << c4.GetHtmlString().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Ausgabe, die vom Beispielcode generiert wurde

Der folgende Screenshot zeigt die Ausgabe des obigen Beispielcodes.

![todo:image_alt_text](htmlstring.png)
{{< app/cells/assistant language="cpp" >}}
