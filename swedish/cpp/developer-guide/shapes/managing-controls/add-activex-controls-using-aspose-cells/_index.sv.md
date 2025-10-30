---
title: Lägg till ActiveX kontroller med Aspose.Cells med C++
linktitle: Lägg till ActiveX kontroller
type: docs
weight: 260
url: /sv/cpp/add-activex-controls-using-aspose-cells/
description: Läs hur du lägger till ActiveX kontroller till Excel blad programmässigt med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Du kan lägga till ActiveX-kontroller med Aspose.Cells med hjälp av [**ShapeCollection::AddActiveXControl()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addactivexcontrol/)-metoden. Denna metod tar en parameter [**ControlType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/) som specificerar vilken typ av ActiveX-kontroll som ska läggas till i ett blad. Den har följande värden:

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
- ControlType::Unknown

När du har lagt till ActiveX-kontrollen i formgruppen kan du komma åt ActiveX-kontrollobjektet via [**Shape::get_ActiveXControl()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getactivexcontrol/)-metoden och ställa in dess olika egenskaper.

{{% /alert %}}

Följande exempel kod lägger till en Toggle Button ActiveX-kontroll med Aspose.Cells for C++.

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
{{< app/cells/assistant language="cpp" >}}
