---
title: 使用 Aspose.Cells 与 C++ 添加 ActiveX 控件
linktitle: 添加 ActiveX 控件
type: docs
weight: 260
url: /zh/cpp/add-activex-controls-using-aspose-cells/
description: 学习如何使用 Aspose.Cells for C++ 编程方式向 Excel 工作表添加 ActiveX 控件。
---

{{% alert color="primary" %}}

您可以使用 [**ShapeCollection::AddActiveXControl()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addactivexcontrol/) 方法通过 Aspose.Cells 添加 ActiveX 控件。此方法接受一个参数 [**ControlType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/) ，指定要在工作表中添加的 ActiveX 控件类型。其值如下：

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

一旦在形状集合中添加了 ActiveX 控件，就可以通过 [**Shape::get_ActiveXControl()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getactivexcontrol/) 方法访问 ActiveX 控件对象，并设置其各种属性。

{{% /alert %}}

以下示例代码使用 Aspose.Cells for C++ 添加了一个切换按钮 ActiveX 控件。

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
