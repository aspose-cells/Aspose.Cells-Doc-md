---
title: Asignar Macro a Control de formulario con C++
linktitle: Asigna Macro a Control de Formulario
type: docs
weight: 60
url: /es/cpp/assign-macro-to-form-control/
description: Aprende cómo asignar un código Macro a un Control de formulario como un botón usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells te permite asignar un Código de Macro a un Control de Formulario como un Botón. Por favor utiliza la propiedad [**Shape.GetMacroName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getmacroname/) para asignar un nuevo Código de Macro a un Control de Formulario dentro del libro.

{{% /alert %}}

El siguiente ejemplo de código crea un nuevo libro de trabajo, asigna un Código Macro a un Botón de formulario y guarda el resultado en formato XLSM. Una vez que abres el archivo XLSM en Microsoft Excel, verás el siguiente código macro.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Asignar Macro a Control de formulario en C++**

Aquí está el código de muestra para generar el archivo de salida XLSM con Código de Macro.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Vba;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    int moduleIdx = workbook.GetVbaProject().GetModules().Add(sheet);
    VbaModule module = workbook.GetVbaProject().GetModules().Get(moduleIdx);
    module.SetCodes(
        u"Sub ShowMessage()\r\n"
        u"    MsgBox \"Welcome to Aspose!\"\r\n"
        u"End Sub"
    );

    Button button = sheet.GetShapes().AddButton(2, 0, 2, 0, 28, 80);
    button.SetPlacement(PlacementType::FreeFloating);
    button.GetFont().SetName(u"Tahoma");
    button.GetFont().SetIsBold(true);
    button.GetFont().SetColor(Color::Blue());
    button.SetText(u"Aspose");

    button.SetMacroName(sheet.GetName() + u".ShowMessage");

    U16String outputPath = outDir + u"Output.out.xlsm";
    workbook.Save(outputPath);

    std::cout << "VBA button added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
