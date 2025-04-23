---
title: Prefixa tabell elementstilar med HtmlSaveOptions.TableCssId egenskapen med C++
linktitle: Prefixa tabell elementstilar med HtmlSaveOptions.TableCssId egenskapen
type: docs
weight: 110
url: /sv/cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
description: Lär dig hur du prefixar tabell elementstilar med Aspose.Cells for C++ med HtmlSaveOptions.TableCssId egenskapen.
---

## **Möjliga användningsscenario**

Aspose.Cells låter dig prefixa tabelldatastilar med [**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/)-egenskapen. Anta att du anger denna egenskap med något värde som **MyTest_TableCssId**, kommer du att hitta tabelldatastilar som visas nedan

```cpp
table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.
```

Följande skärmbild visar effekten av att använda [**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/)egenskap på utdata-HTML.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **Prefixa tabell-elementstilar med HtmlSaveOptions.TableCssId-egenskapen**

Följande exempelkod visar hur man använder [**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/)-egenskapen. Vänligen kontrollera [utdata-HTML-filen](60489790.zip) som genererats av koden för referens.

## **Exempelkod**

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
