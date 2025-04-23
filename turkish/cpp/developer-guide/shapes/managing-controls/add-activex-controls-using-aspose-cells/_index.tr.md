---
title: Aspose.Cells ile ActiveX Kontrolleri C++ kullanarak Ekleme
linktitle: AktifX Kontrolleri Ekle
type: docs
weight: 260
url: /tr/cpp/add-activex-controls-using-aspose-cells/
description: Aspose.Cells for C++ kullanarak ActiveX kontrollerini Excel çalışma sayfalarına programatik olarak nasıl ekleyeceğinizi öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells ile ActiveX kontrollerini [**ShapeCollection::AddActiveXControl()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addactivexcontrol/) yöntemiyle ekleyebilirsiniz. Bu yöntem, bir parametre [**ControlType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/) alır ve bu parametre, bir çalışma sayfasına eklenecek ActiveX kontrol türünü belirtir. Aşağıdaki değerleri alır:

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
- ControlType::Bilinmeyen

ActiveX kontrolünü şekil koleksiyonu içine ekledikten sonra, [**Shape::get_ActiveXControl()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getactivexcontrol/) yöntemiyle ActiveX kontrol nesnesine erişebilir ve çeşitli özelliklerini ayarlayabilirsiniz.

{{% /alert %}}

Aşağıdaki örnek kod, Aspose.Cells for C++ kullanarak bir Toggle Button ActiveX Kontrolü ekler.

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
