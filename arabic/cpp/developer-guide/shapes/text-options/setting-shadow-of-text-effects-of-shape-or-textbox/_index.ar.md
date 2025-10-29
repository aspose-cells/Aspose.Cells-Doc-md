---
title: تعيين ظل تأثيرات النص للشكل أو مربع النص باستخدام C++
linktitle: تعيين ظل تأثيرات النص
type: docs
weight: 250
url: /ar/cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: تعلم كيفية ضبط ظل تأثيرات النص للأشكال أو مربعات النص باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

 يمكنك تعيين **ظل** **تأثيرات النص** لأي شكل أو مربع نص. يرجى استخدام خاصية [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/). فهي تعرض إعداد نص الشكل وتعيد كائنات [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/). بعد الوصول إليها، يرجى تعيين **الظل** عبر خاصية [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/). هذه الخاصية من نوع [**PresetShadowType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/presetshadowtype/) الذي يحتوي على عدة قيم، منها:

- إزاحة قطرية لأسفل اليمين
- إزاحة لأسفل
- إزاحة قطرية لأعلى اليمين
- داخل اليسار
- داخل الوسط
- زاوية رؤية قطرية العلوي الأيسر
- زاوية رؤية قطرية السفلي الأيمن

{{% /alert %}}

يُظهر مقتطف الكود التالي استخدام خاصية [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/) لضبط ظل تأثيرات النص في الشكل أو مربع النص.

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
