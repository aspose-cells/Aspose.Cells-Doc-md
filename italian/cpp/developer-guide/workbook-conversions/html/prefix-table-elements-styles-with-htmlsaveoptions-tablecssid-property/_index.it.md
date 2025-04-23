---
title: Prefissare gli stili degli elementi della tabella con la proprietà HtmlSaveOptions.TableCssId con C++
linktitle: Prefissare gli stili degli elementi della tabella con la proprietà HtmlSaveOptions.TableCssId
type: docs
weight: 110
url: /it/cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
description: Impara come prefissare gli stili degli elementi della tabella utilizzando Aspose.Cells for C++ con la proprietà HtmlSaveOptions.TableCssId.
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells ti consente di prefissare gli stili degli elementi della tabella con la proprietà [**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/). Supponi di impostare questa proprietà con un valore come **MyTest_TableCssId**, allora troverai gli stili degli elementi della tabella come mostrato di seguito

```cpp
table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.
```

La seguente schermata mostra l'effetto dell'utilizzo della proprietà [**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/) sull'HTML di output.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **Prefissare gli stili degli elementi della tabella con la proprietà HtmlSaveOptions.TableCssId**

Il codice di esempio seguente dimostra come utilizzare la proprietà [**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/). Si prega di controllare l'[output HTML](60489790.zip) generato dal codice per avere un riferimento.

## **Codice di Esempio**

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
