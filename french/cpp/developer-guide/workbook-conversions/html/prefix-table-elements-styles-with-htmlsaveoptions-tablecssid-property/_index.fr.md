---
title: Prefixer les styles des éléments du tableau avec la propriété HtmlSaveOptions.TableCssId avec C++
linktitle: Prefixer les styles des éléments du tableau avec la propriété HtmlSaveOptions.TableCssId
type: docs
weight: 110
url: /fr/cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
description: Apprenez comment préfixer les styles des éléments du tableau en utilisant Aspose.Cells for C++ avec la propriété HtmlSaveOptions.TableCssId.
---

## **Scénarios d'utilisation possibles**

Aspose.Cells vous permet de préfixer les styles des éléments de tableau avec la propriété [**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/). Supposons que vous définissiez cette propriété avec une valeur comme **MyTest_TableCssId**, alors vous trouverez les styles des éléments de tableau comme indiqué ci-dessous

```cpp
table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.
```

La capture d'écran suivante montre l'effet de l'utilisation de la propriété [**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/) sur le HTML de sortie.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **Prefixer les styles des éléments du tableau avec la propriété HtmlSaveOptions.TableCssId**

Le code d'exemple suivant montre comment utiliser la propriété [**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/). Veuillez vérifier le fichier HTML de sortie (60489790.zip) généré par le code pour une référence.

## **Code d'exemple**

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
