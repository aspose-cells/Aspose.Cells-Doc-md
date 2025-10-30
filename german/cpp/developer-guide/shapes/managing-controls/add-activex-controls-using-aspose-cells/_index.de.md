---
title: ActiveX Steuerelemente mit Aspose.Cells und C++ hinzufügen
linktitle: ActiveX Steuerelemente hinzufügen
type: docs
weight: 260
url: /de/cpp/add-activex-controls-using-aspose-cells/
description: Erfahren Sie, wie man ActiveX Steuerelemente programmgesteuert zu Excel Arbeitsblättern mit Aspose.Cells for C++ hinzufügt.
---

{{% alert color="primary" %}}

Sie können ActiveX-Steuerelemente mit Aspose.Cells mithilfe der [**ShapeCollection::AddActiveXControl()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addactivexcontrol/)-Methode hinzufügen. Diese Methode nimmt einen Parameter [**ControlType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/) entgegen, der den Typ des hinzuzufügenden ActiveX-Steuerelements innerhalb eines Arbeitsblatts angibt. Es hat die folgenden Werte:

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
- ControlType::Unbekannt

Nachdem Sie das ActiveX-Steuerelement in die Shapes-Sammlung eingefügt haben, können Sie das ActiveX-Steuerelement-Objekt mit der [**Shape::get_ActiveXControl()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getactivexcontrol/)-Methode zugreifen und verschiedene Eigenschaften davon setzen.

{{% /alert %}}

Der folgende Beispielcode fügt einen Umschaltknopf ActiveX-Control mit Aspose.Cells for C++ hinzu.

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
