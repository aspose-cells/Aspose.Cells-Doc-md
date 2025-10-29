---
title: Префиксировать стили элементов таблицы с помощью свойства HtmlSaveOptions.TableCssId в C++
linktitle: Префиксировать стили элементов таблицы с помощью свойства HtmlSaveOptions.TableCssId
type: docs
weight: 110
url: /ru/cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
description: Узнайте, как добавлять префикс к стилям элементов таблицы с помощью Aspose.Cells for C++ и свойства HtmlSaveOptions.TableCssId.
---

## **Возможные сценарии использования**

Aspose.Cells позволяет префиксить стили элементов таблиц с помощью [**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/). Предположим, вы установите это свойство с каким-либо значением, например **MyTest_TableCssId**, тогда вы увидите стили элементов таблиц, как показано ниже

```cpp
table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.
```

На следующем скриншоте показано влияние использования свойства [**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/) на выходной HTML.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **Префиксировать стили элементов таблицы с помощью свойства HtmlSaveOptions.TableCssId**

Следующий образец кода демонстрирует, как использовать свойство [**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/). Пожалуйста, проверьте [выходной HTML](60489790.zip), сгенерированный кодом, для справки.

## **Образец кода**

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
