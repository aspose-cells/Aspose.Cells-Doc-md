---
title: Получить HTML5 строку из ячейки с помощью C++
linktitle: Получить HTML5 строку из ячейки
type: docs
weight: 90
url: /ru/cpp/get-html5-string-from-cell/
description: Узнайте, как получить HTML5 строку из ячейки с помощью API Aspose.Cells for C++.
keywords: Получить строку HTML5 из ячейки, получить строку HTML5 из ячейки, управлять строкой HTML5 ячейки
---

## **Возможные сценарии использования**

Aspose.Cells возвращает HTML-строку ячейки с помощью метода [**GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/), который принимает булевский параметр. Если передать **false**, он вернет обычный HTML, а если **true**, — HTML5.

## **Получить HTML5 строку из ячейки**

В следующем образце кода создается объект книги и добавляется некоторый текст в ячейку A1 первого листа. Затем получается обычная HTML строка и HTML5 строка из ячейки A1, используя метод [**GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/), и выводится на консоль.

## **Образец кода**

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

## **Вывод в консоль**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
