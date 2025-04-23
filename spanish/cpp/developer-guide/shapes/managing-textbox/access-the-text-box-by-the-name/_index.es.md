---
title: Acceder al cuadro de texto por el nombre con C++
linktitle: Acceda al cuadro de texto por el nombre
type: docs
weight: 230
url: /es/cpp/access-the-text-box-by-the-name/
description: Aprenda cómo acceder a un cuadro de texto por su nombre usando Aspose.Cells for C++.
---

## Acceda al cuadro de texto por el nombre

Anteriormente, los cuadros de texto se accedían por índice desde la colección [**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettextboxes/), pero ahora también puede acceder al cuadro de texto por su nombre en esta colección. Esto es una forma conveniente y rápida de acceder a su cuadro de texto si ya conoce su nombre.

El siguiente código de ejemplo primero crea un cuadro de texto y le asigna un texto y un nombre. Luego, en las siguientes líneas, accedemos al mismo cuadro de texto por su nombre y imprimimos su texto.

### Código C++ para acceder al cuadro de texto por nombre

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Create an object of the Workbook class
    Workbook workbook;

    // Access first worksheet from the collection
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add the TextBox to the worksheet
    int idx = sheet.GetTextBoxes().Add(10, 10, 10, 10);

    // Access newly created TextBox using its index & name it
    TextBox tb1 = sheet.GetTextBoxes().Get(idx);
    tb1.SetName(u"MyTextBox");

    // Set text for the TextBox
    tb1.SetText(u"This is MyTextBox");

    // Access the same TextBox via its name
    TextBox tb2 = sheet.GetTextBoxes().Get(u"MyTextBox");

    // Display the text of the TextBox accessed via name
    std::cout << tb2.GetText().ToUtf8() << std::endl;

    std::cout << "Press any key to continue..." << std::endl;
    std::cin.get();

    Aspose::Cells::Cleanup();
}
```

### Salida de consola generada por el código de ejemplo

Aquí está la salida en consola del código de muestra anterior.

{{< highlight java >}}

This is MyTextBox

{{< /highlight >}}
