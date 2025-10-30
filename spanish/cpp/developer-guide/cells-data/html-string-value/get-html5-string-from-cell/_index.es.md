---
title: Obtener cadena HTML5 de la Celda con C++
linktitle: Obtener cadena HTML5 de la Celda
type: docs
weight: 90
url: /es/cpp/get-html5-string-from-cell/
description: Aprende cómo obtener la cadena HTML5 de una celda usando la API Aspose.Cells for C++.
keywords: Obtener cadena HTML5 de la celda, obtener cadena HTML5 de la celda, administrar cadena HTML5 de la celda
---

## **Escenarios de uso posibles**

Aspose.Cells devuelve la cadena HTML de la celda usando el método [**GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) que acepta un parámetro booleano. Si pasas **false**, devolverá HTML normal, pero si pasas **true**, devolverá cadena HTML5.

## **Obtener cadena HTML5 de la Celda**

El siguiente código de ejemplo crea un objeto de libro de trabajo y agrega un texto en la celda A1 de la primera hoja de cálculo. Luego obtiene la cadena HTML normal y HTML5 de la celda A1 usando el método [**GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) e imprime en la consola.

## **Código de muestra**

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

## **Salida de la consola**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
