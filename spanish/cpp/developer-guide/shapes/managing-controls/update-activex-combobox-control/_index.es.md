---
title: Actualizar control ComboBox ActiveX con C++
linktitle: Actualizar el control de cuadro combinado ActiveX
type: docs
weight: 170
url: /es/cpp/update-activex-combobox-control/
description: Aprenda cómo leer o escribir valores del control ComboBox ActiveX usando Aspose.Cells con C++.
---

## **Escenarios de uso posibles**
Puede leer o escribir los valores del control ComboBox ActiveX usando Aspose.Cells. Acceda al control ActiveX mediante la propiedad [Shape.ActiveXControl](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/activexcontrol/) y verifique su tipo mediante la propiedad [ActiveXControl.GetType()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/activexcontrolbase/gettype/). Debe devolver el valor [ControlType.ComboBox](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/), y luego convertirlo al tipo [ComboBoxActiveXControl](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol/) para leer o modificar sus diversas propiedades.

Descargue el [archivo de Excel de ejemplo](5115124.xlsx) utilizado en el siguiente código de ejemplo.

## **Actualizar control ActiveX ComboBox**
La siguiente captura de pantalla muestra el efecto del código de ejemplo en el [archivo de Excel de ejemplo](5115124.xlsx). Como puede ver, el valor del Control Combo Box ActiveX se ha actualizado a "Este es un control de combo box".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |

## **Código de muestra**
El siguiente código de ejemplo actualiza el valor del Control Combo Box ActiveX presente dentro del [archivo de Excel de ejemplo](5115124.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Drawing::ActiveXControls;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(srcDir + u"SourceFile.xlsx");

    Shape shape = wb.GetWorksheets().Get(0).GetShapes().Get(0);

    ActiveXControl c = shape.GetActiveXControl();

    if (c.GetType() == ControlType::ComboBox)
    {
        ComboBoxActiveXControl comboBoxActiveX = static_cast<ComboBoxActiveXControl>(c);
        comboBoxActiveX.SetValue(u"This is combo box control with updated value.");
    }

    wb.Save(outDir + u"OutputFile_out.xlsx");

    std::cout << "Workbook saved successfully with updated ComboBox value!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
