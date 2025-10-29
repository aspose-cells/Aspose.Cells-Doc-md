---
title: إضافة عناصر تحكم ActiveX باستخدام Aspose.Cells مع C++
linktitle: إضافة عناصر تحكم ActiveX
type: docs
weight: 260
url: /ar/cpp/add-activex-controls-using-aspose-cells/
description: تعلم كيف تضيف عناصر تحكم ActiveX إلى أوراق عمل إكسل برمجيًا باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

يمكنك إضافة عناصر تحكم ActiveX باستخدام Aspose.Cells باستخدام طريقة [**ShapeCollection::AddActiveXControl()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addactivexcontrol/). تأخذ هذه الطريقة معلمة [**ControlType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/) التي تحدد نوع عنصر تحكم ActiveX الذي سيتم إضافته داخل ورقة العمل. لها القيم التالية:

- نوع التحكم::مربع اختيار (CheckBox)
- نوع التحكم::مربع تحرير (ComboBox)
- نوع التحكم::زر أمر (CommandButton)
- نوع التحكم::صورة (Image)
- نوع التحكم::تسمية (Label)
- نوع التحكم::قائمة إطار (ListBox)
- نوع التحكم::زر اختيار (RadioButton)
- نوع التحكم::شريط تمرير (ScrollBar)
- نوع التحكم::زر تدوير (SpinButton)
- نوع التحكم::مربع النص (TextBox)
- نوع التحكم::زر تبديل (ToggleButton)
- نوع التحكم::غير معروف (Unknown)

بمجرد إضافة عنصر تحكم ActiveX داخل مجموعة الأشكال، يمكنك الوصول إلى كائن عنصر التحكم ActiveX عبر طريقة [**Shape::get_ActiveXControl()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getactivexcontrol/) وتعيين خصائصه المختلفة.

{{% /alert %}}

الكود النموذجي التالي يضيف عنصر تحكم Toggle Button باستخدام Aspose.Cells for C++.

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
