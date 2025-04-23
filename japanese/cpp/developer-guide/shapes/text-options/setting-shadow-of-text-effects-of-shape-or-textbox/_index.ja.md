---
title: 図形またはテキストボックスの文字効果の shadow を設定するC++
linktitle: 文字効果の shadow を設定する
type: docs
weight: 250
url: /ja/cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: Aspose.Cells for C++を使用して、図形やテキストボックスの文字効果の影を設定する方法を学びます。
---

{{% alert color="primary" %}}

任意の図形やテキストボックスのテキスト効果の**Shadow**を設定できます。[**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/)プロパティを使用してください。このプロパティは図形のテキスト設定を示し、[**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/)オブジェクトを返します。アクセス後、[**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/)プロパティを介して**Shadow**を設定してください。このプロパティは[**PresetShadowType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/presetshadowtype/)型で、いくつかの値を持ちます。例として：

- DiagonalBottomRightのOffset
- ボトムのオフセット
- DiagonalTopRightのOffset
- 左内部
- 中央内部
- PerspectiveDiagonalUpperLeft
- PerspectiveDiagonalLowerRight

{{% /alert %}}

以下のコードスニペットは、[**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/) プロパティを使用してShapeまたはTextBoxのテキスト効果のシャドウを設定する例です。

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
