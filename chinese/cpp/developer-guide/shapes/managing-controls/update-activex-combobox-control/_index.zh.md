---
title: 使用 C++ 更新 ActiveX ComboBox 控件
linktitle: 更新ActiveX组合框控件
type: docs
weight: 170
url: /zh/cpp/update-activex-combobox-control/
description: 学习如何使用 Aspose.Cells 结合 C++ 读写 ActiveX ComboBox 控件的值。
---

## **可能的使用场景**
您可以使用 Aspose.Cells 读写 ActiveX ComboBox 控件的值。请通过 [Shape.ActiveXControl](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/activexcontrol/) 属性访问 ActiveX 控件，然后通过 [ActiveXControl.GetType()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/activexcontrolbase/gettype/) 属性检查其类型。它应返回 [ControlType.ComboBox](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/)，然后可以将其类型转换为 [ComboBoxActiveXControl](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol/) 对象以读写其各个属性。

请下载以下示例代码中使用的 [示例 Excel 文件](5115124.xlsx)。

## **更新ActiveX ComboBox控件**
以下截图显示了样本代码对 [样本excel文件](5115124.xlsx) 的效果。正如你所看到的，活动X组合框的值已更新为"This is combo box control"。

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |

## **示例代码**
以下样本代码更新了 [样本excel文件](5115124.xlsx) 中存在的活动X组合框控件的值。

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
