---
title: Prefix Tabellenelemente mit HtmlSaveOptions.TableCssId Property mit C++
linktitle: Prefix Tabellenelemente mit HtmlSaveOptions.TableCssId Property
type: docs
weight: 110
url: /de/cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
description: Erfahren Sie, wie Sie Tabellenelement Stile mit Aspose.Cells for C++ und HtmlSaveOptions.TableCssId Property präfixieren.
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells ermöglicht es Ihnen, Tabellenelementstile mit der [**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/)-Eigenschaft zu versehen. Nehmen wir an, Sie setzen diese Eigenschaft mit einem Wert wie **MyTest_TableCssId**, dann finden Sie Tabellenelementstile wie unten gezeigt

```cpp
table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.
```

Der folgende Screenshot zeigt die Auswirkungen der Verwendung der [**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/)-Eigenschaft auf die Ausgabe von HTML.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **Prefix-Tabellenelemente mit HtmlSaveOptions.TableCssId-Property**

Der folgende Beispielcode zeigt, wie die [**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/)-Eigenschaft verwendet wird. Bitte überprüfen Sie das [Ausgabe-HTML](60489790.zip), das vom Code generiert wurde, als Referenz.

## **Beispielcode**

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
