---
title: Cambiar el espaciado de caracteres del cuadro de texto o forma de Excel con C++
linktitle: Cambiar Espaciado de Caracteres de Cuadro de Texto o Forma de Excel
type: docs
weight: 280
url: /es/cpp/change-character-spacing-of-excel-textbox-or-shape/
description: Aprende cómo cambiar el espaciado de caracteres del cuadro de texto o forma de Excel usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Puedes cambiar el espaciado de caracteres del cuadro de texto o forma de Excel usando la propiedad [**TextOptions.GetSpacing()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getspacing/).

{{% /alert %}}

El siguiente código de ejemplo cambia el espaciado de caracteres del cuadro de texto en un archivo de Excel a 4 puntos y luego lo guarda en disco.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load your excel file inside a workbook object
    Workbook wb(srcDir + u"sampleChangeTextBoxOrShapeCharacterSpacing.xlsx");

    // Access your text box which is also a shape object from shapes collection
    Shape shape = wb.GetWorksheets().Get(0).GetShapes().Get(0);

    // Access the first font setting object via GetCharacters() method
    FontSetting fs = shape.GetRichFormattings()[0];

    // Set the character spacing to point 4
    fs.GetTextOptions().SetSpacing(4);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"outputChangeTextBoxOrShapeCharacterSpacing.xlsx", SaveFormat::Xlsx);

    std::cout << "Character spacing changed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
