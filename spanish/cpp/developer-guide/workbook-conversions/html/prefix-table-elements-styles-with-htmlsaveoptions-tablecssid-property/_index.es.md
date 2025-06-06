---
title: Prefijo de estilos de elementos de tablas con la propiedad HtmlSaveOptions.TableCssId en C++
linktitle: Prefijo de estilos de elementos de tablas con la propiedad HtmlSaveOptions.TableCssId
type: docs
weight: 110
url: /es/cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
description: Aprende cómo prefijar estilos de elementos de tabla usando Aspose.Cells for C++ con la propiedad HtmlSaveOptions.TableCssId.
---

## **Escenarios de uso posibles**

Aspose.Cells le permite prefijar los estilos de los elementos de tabla con la propiedad [**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/). Supongamos que define esta propiedad con algún valor como **MyTest_TableCssId**, entonces encontrará estilos de elementos de tabla como se muestra a continuación

```cpp
table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.
```

La siguiente captura de pantalla muestra el efecto de usar la propiedad [**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/) en la salida de HTML.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **Prefijo de estilos de elementos de tablas con la propiedad HtmlSaveOptions.TableCssId**

El siguiente código de ejemplo demuestra cómo hacer uso de la propiedad [**HtmlSaveOptions.GetTableCssId()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gettablecssid/). Revise el [HTML de salida](60489790.zip) generado por el código como referencia.

## **Código de muestra**

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
