---
title: C++ kullanarak Şekil veya Metin Kutusu nun Metin Efektleri Gölgesini Ayarlama
linktitle: Metin Efektleri Gölgesini Ayarlama
type: docs
weight: 250
url: /tr/cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: Aspose.Cells for C++ kullanarak şekil veya metin kutularının metin efektleri gölgesini nasıl ayarlayacağınızı öğrenin.
---

{{% alert color="primary" %}}

Herhangi bir Şekil veya Metin Kutusu'nun **Metin Efektleri**nin **Gölgesi**ni ayarlayabilirsiniz. Lütfen [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/) özelliğini kullanın. Bu, şeklin metnini ayarlar ve [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/) nesnelerini döndürür. Erişim sağladıktan sonra, [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/) özelliği aracılığıyla **Gölge**yi ayarlayın. Bu özellik, birkaç değeri olan [**PresetShadowType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/presetshadowtype/) türündedir ve bazıları şunlardır:

- Dikey Sağa Ofset
- Alt Ofset
- OffsetDiagonalTopRight
- InsideLeft
- InsideCenter
- PerspectiveDiagonalUpperLeft
- PerspectiveDiagonalLowerRight

{{% /alert %}}

Aşağıdaki kod parçası, Shape veya TextBox'un metin efektleri gölgesini ayarlamak için [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/) özelliğinin kullanımını gösterir.

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
