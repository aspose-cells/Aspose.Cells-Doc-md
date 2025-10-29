---
title: Добавление элементов ActiveX с помощью Aspose.Cells и C++
linktitle: Добавить элементы ActiveX
type: docs
weight: 260
url: /ru/cpp/add-activex-controls-using-aspose-cells/
description: Узнайте, как программно добавлять элементы ActiveX в листы Excel с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Вы можете добавлять элементы ActiveX с помощью Aspose.Cells с использованием метода [**ShapeCollection::AddActiveXControl()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addactivexcontrol/). Этот метод принимает параметр [**ControlType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/), который задаёт тип элемента ActiveX для вставки в лист. Значения следующего типа:

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

После добавления элемента ActiveX в коллекцию фигур, вы можете получить объект элемента ActiveX через метод [**Shape::get_ActiveXControl()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getactivexcontrol/) и установить его свойства.

{{% /alert %}}

Следующий пример кода добавляет переключатель (Toggle Button) ActiveX с помощью Aspose.Cells for C++.

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
