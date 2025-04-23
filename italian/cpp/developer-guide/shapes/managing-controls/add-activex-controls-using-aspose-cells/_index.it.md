---
title: Aggiungi controlli ActiveX usando Aspose.Cells con C++
linktitle: Aggiungi controlli ActiveX
type: docs
weight: 260
url: /it/cpp/add-activex-controls-using-aspose-cells/
description: Impara come aggiungere controlli ActiveX ai fogli di lavoro Excel mediante programmazione usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Puoi aggiungere controlli ActiveX con Aspose.Cells usando il metodo [**ShapeCollection::AddActiveXControl()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addactivexcontrol/). Questo metodo accetta un parametro [**ControlType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/) che specifica il tipo di controllo ActiveX da aggiungere all'interno di un foglio di lavoro. Ha i seguenti valori:

- ControlType::CheckBox
- ControlType::ComboBox
- ControlType::CommandButton
- ControlType::Image
- ControlType::Label
- ControlType::ListBox
- ControlType::RadioButton
- ControlType::ScrollBar
- ControlType::SpinButton
- ControlType::TextBox
- ControlType::ToggleButton
- ControlType::Sconosciuto

Una volta aggiunto il controllo ActiveX all'interno della raccolta di forme, puoi accedere all'oggetto del controllo ActiveX tramite il metodo [**Shape::get_ActiveXControl()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getactivexcontrol/) e impostarne le varie proprietà.

{{% /alert %}}

Il codice di esempio seguente aggiunge un controllo ActiveX Toggle Button usando Aspose.Cells for C++.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Drawing::ActiveXControls;

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Add Toggle Button ActiveX Control inside the Shape Collection
    Shape s = sheet.GetShapes().AddActiveXControl(ControlType::ToggleButton, 4, 0, 4, 0, 100, 30);

    // Access the ActiveX control object and set its linked cell property
    ActiveXControl c = s.GetActiveXControl();
    c.SetLinkedCell(u"A1");

    // Save the workbook in xlsx format
    wb.Save(outDir + u"AddActiveXControls_out.xlsx", SaveFormat::Xlsx);

    std::cout << "ActiveX control added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
