---
title: Especificar el nombre de fuente del Extremo Oriente y del Latín en Opciones de texto de forma con C++
linktitle: Especificar el nombre del Lejano Oriente y del Font en opciones de texto de forma
type: docs
weight: 1600
url: /es/cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/
description: Aprenda cómo especificar los nombres de fuentes de Extremo Oriente y Látin en las opciones de texto de una forma usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

A veces desea mostrar texto en fuentes de idiomas del Extremo Oriente, por ejemplo, japonés, chino, tailandés, etc. Aspose.Cells proporciona la propiedad [**TextOptions.GetFarEastName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getfareastname/) que se puede usar para especificar el nombre de la fuente del idioma del Extremo Oriente. Además, también puede especificar el nombre de la fuente del latín usando la propiedad [**TextOptions.GetLatinName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getlatinname/).

## **Especificar el nombre del Lejano Oriente y del Font en opciones de texto de forma**

El siguiente código de ejemplo crea un cuadro de texto y agrega algo de texto en japonés dentro de él. Luego especifica los nombres de fuente del latín y del Extremo Oriente del texto y guarda el libro de trabajo como [archivo de Excel de salida](67338274.xlsx). La siguiente captura de pantalla muestra los nombres de fuente del texto de salida en Microsoft Excel.

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)

## **Código de muestra**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    Workbook wb;

    Worksheet ws = wb.GetWorksheets().Get(0);

    int idx = ws.GetTextBoxes().Add(5, 5, 50, 200);
    TextBox tb = ws.GetTextBoxes().Get(idx);

    tb.SetText(u"\u3053\u3093\u306B\u3061\u306F\u4E16\u754C");

    tb.GetTextOptions().SetLatinName(u"Comic Sans MS");
    tb.GetTextOptions().SetFarEastName(u"KaiTi");

    wb.Save(u"outputSpecifyFarEastAndLatinNameOfFontInTextOptionsOfShape.xlsx", SaveFormat::Xlsx);

    std::cout << "Textbox created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
