---
title: 用C++设置形状或文本框的文本效果阴影
linktitle: 设置文本效果阴影
type: docs
weight: 250
url: /zh/cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: 学习如何使用编号Aspose.Cells for C++为形状或文本框设置文本效果的阴影。
---

{{% alert color="primary" %}}

你可以为任何形状或文本框的**文本效果**设置**阴影**。请使用[**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/)属性，它会展示形状文本的设置并返回[**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/)对象。在访问后，请通过[**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/)属性设置**阴影**。该属性类型为[**PresetShadowType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/presetshadowtype/)，具有几个值，部分如下：

- 偏移对角线底部右
- 偏移底部
- 偏移对角线顶部右
- 内部左
- 内部中心
- 透视对角线左上
- 透视对角线右下

{{% /alert %}}

以下代码片段演示了如何使用[**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/)属性为形状或文本框设置文本效果的阴影。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Add text box with these dimensions
    TextBox tb = ws.GetShapes().AddTextBox(2, 0, 2, 0, 100, 400);

    // Set the text of the textbox
    tb.SetText(u"This text has the following settings.\n\nText Effects > Shadow > Offset Bottom");

    // Set all the text runs shadow to preset offset bottom
    for (int i = 0; i < tb.GetTextBody().GetCount(); i++)
    {
        tb.GetTextBody().Get(i).GetTextOptions().GetShadow().SetPresetType(PresetShadowType::OffsetBottom);
    }

    // Set the font color and size of the textbox
    tb.GetFont().SetColor(Color::Red());
    tb.GetFont().SetSize(16);

    // Save the output file
    wb.Save(outDir + u"outputSettingTextEffectsShadowOfShapeOrTextbox.xlsx", SaveFormat::Xlsx);

    std::cout << "Text effects shadow of shape or textbox set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
