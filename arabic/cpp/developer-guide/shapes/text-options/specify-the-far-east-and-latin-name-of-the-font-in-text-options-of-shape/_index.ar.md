---
title: تحديد اسم الخط الشرقي الأقصى واللاتيني في خيارات النص للشكل باستخدام C++
linktitle: تحديد اسم الشرق الأقصى واللاتيني للخط في خيارات النص للشكل
type: docs
weight: 1600
url: /ar/cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/
description: تعلم كيفية تحديد أسماء خطوط الشرق الأقصى واللاتينية في خيارات النص لشكل باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

 أحيانًا تريد عرض النص في خط لغة الشرق الأقصى مثل اليابانية أو الصينية أو التايلاندية، إلخ. توفر Aspose.Cells خاصية [**TextOptions.GetFarEastName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getfareastname/) التي يمكن استخدامها لتحديد اسم الخط للغة الشرق الأقصى. بالإضافة إلى ذلك، يمكنك أيضًا تحديد اسم خط اللاتينية باستخدام خاصية [**TextOptions.GetLatinName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getlatinname/).

## **تحديد اسم الشرق الأقصى واللاتيني للخط في خيارات النص للشكل**

يخلق الكود التالي مربع نص ويضيف فيه نصًا يابانيًا. ثم يحدد أسماء الخط اللاتيني وشرق آسيا للنص ويحفظ ملف العمل كملف إكسل الناتج. يظهر لقطة الشاشة أسماء الخطوط في مربع النص الناتج في إكسل.

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    Workbook wb;

    Worksheet ws = wb.GetWorksheets().Get(0);

    int idx = ws.GetTextBoxes().Add(5, 5, 50, 200);
    TextBox tb = ws.GetTextBoxes().Get(idx);

    tb.SetText(u"\u3053\u3093\u306B\u3061\u306F\u4E16\u754C");

    tb.GetTextOptions().SetLatinName(u"Comic Sans MS");
    tb.GetTextOptions().SetFarEastName(u"KaiTi");

    wb.Save(u"outputSpecifyFarEastAndLatinNameOfFontInTextOptionsOfShape.xlsx", SaveFormat::Xlsx);

    std::cout << "Textbox created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
