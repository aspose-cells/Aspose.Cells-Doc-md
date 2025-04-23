---
title: C++ ile Hücreden HTML5 Dizgisini alın
linktitle: Hücreden HTML5 Dizgisini alın
type: docs
weight: 90
url: /tr/cpp/get-html5-string-from-cell/
description: Aspose.Cells for C++ API kullanarak hücreden HTML5 dizgisini nasıl alınır öğrenin.
keywords: Hücreden HTML5 dizesi al, Hücreden HTML5 dizesi al, Hücrenin HTML5 dizesini yönet
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, boolean parametre alan [**GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) metodunu kullanarak hücrenin HTML dizgisini döndürür. Eğer parametre olarak **false** verirseniz, Normal HTML döner, eğer **true** verirseniz, HTML5 dizesi döner.

## **Hücreden HTML5 Dizgisini Al**

Aşağıdaki örnek kod, bir çalışma kitabı nesnesi oluşturur ve ilk çalışsayısının A1 hücresine bazı metinler ekler. Ardından, A1 hücresinden Normal HTML ve HTML5 dizelerini [**GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) yöntemini kullanarak alır ve bunları konsola yazdırır.

## **Örnek Kod**

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

## **Konsol Çıktısı**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
