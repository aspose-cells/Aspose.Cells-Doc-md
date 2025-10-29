---
title: تعيين ماكرو إلى تحكم النموذج باستخدام C++
linktitle: تعيين ماكرو إلى عنصر تحكم النموذج
type: docs
weight: 60
url: /ar/cpp/assign-macro-to-form-control/
description: تعلم كيفية تعيين رمز الماكرو إلى تحكم النموذج مثل زر باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

تسمح Aspose.Cells لك بتعيين شيفر آلي إلى عنصر تحكم النموذج مثل زر. يرجى استخدام الخاصية [**Shape.GetMacroName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getmacroname/) لتعيين شيفر آلي جديد إلى عنصر تحكم النموذج داخل سجل العمل.

{{% /alert %}}

الكود النموذجي التالي ينشئ دفتر عمل جديد، يعين رمز الماكرو لزر النموذج، ويحفظ الناتج بتنسيق XLSM. عند فتح ملف XLSM الناتج في Microsoft Excel، ستشاهد رمز الماكرو التالي.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **تعيين ماكرو إلى تحكم النموذج في C++**

إليك الشيفرة الزمنية العينية لإنشاء ملف XLSM الناتج مع شيفر آلي.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Vba;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    int moduleIdx = workbook.GetVbaProject().GetModules().Add(sheet);
    VbaModule module = workbook.GetVbaProject().GetModules().Get(moduleIdx);
    module.SetCodes(
        u"Sub ShowMessage()\r\n"
        u"    MsgBox \"Welcome to Aspose!\"\r\n"
        u"End Sub"
    );

    Button button = sheet.GetShapes().AddButton(2, 0, 2, 0, 28, 80);
    button.SetPlacement(PlacementType::FreeFloating);
    button.GetFont().SetName(u"Tahoma");
    button.GetFont().SetIsBold(true);
    button.GetFont().SetColor(Color::Blue());
    button.SetText(u"Aspose");

    button.SetMacroName(sheet.GetName() + u".ShowMessage");

    U16String outputPath = outDir + u"Output.out.xlsm";
    workbook.Save(outputPath);

    std::cout << "VBA button added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
