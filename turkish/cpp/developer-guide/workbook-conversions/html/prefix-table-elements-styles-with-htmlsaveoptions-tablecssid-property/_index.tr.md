---
title: C++ ile HtmlSaveOptions.TableCssId Özelliği ile Tablo Elemanları Stillerini Önekle
linktitle: HtmlSaveOptions.TableCssId Özelliği ile Tablo Elemanları Stillerini Önekle
type: docs
weight: 110
url: /tr/cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
description: HtmlSaveOptions.TableCssId özelliği kullanarak Aspose.Cells for C++ ile tablo öğesi stillerini ön ekleme yöntemini öğrenin.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, tablo öğeleri stillerini [**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/) özelliği ile ön eklemek için izin verir. Varsayalım ki, bu özelliği **MyTest_TableCssId** gibi bir değerle ayarlarsanız, aşağıdaki gibi tablo öğeleri stilleri bulacaksınız

```cpp
table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.
```

Aşağıdaki ekran görüntüsü, çıktı HTML'sine [**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/) özelliğinin kullanılmasının etkisini gösterir.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## ** HtmlSaveOptions.TableCssId Özelliği ile Tablo Elemanları Stillerini Önekle**

Aşağıdaki örnek kod, [**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/) özelliğinin kullanımını gösterir. Referans için kod tarafından oluşturulan [çıktı HTML'si](60489790.zip)'ni inceleyin.

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B5 and put value inside it
    Cell cell = ws.GetCells().Get(u"B5");
    cell.PutValue(u"This is some text.");

    // Set the style of the cell - font color is Red
    Style st = cell.GetStyle();
    st.GetFont().SetColor(Color::Red());
    cell.SetStyle(st);

    // Specify html save options - specify table css id
    HtmlSaveOptions opts;
    opts.SetTableCssId(u"MyTest_TableCssId");

    // Save the workbook in html
    wb.Save(u"outputTableCssId.html", opts);

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
